import nltk
import json
import plotly
import pandas as pd
import plotly.graph_objects as go

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download(['punkt','wordnet'])

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar, Histogram
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('messages', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # Viz 1
    genre = df.groupby('genre').count()['id'].sort_values()
    
    # Viz 2
    df['text length'] = df['message'].apply(lambda x: len(x.split()))
    histogram = df[df['text length'] < 100].groupby('text length').count()['id']

    # Viz 3
    total_category = df.drop(columns=['id','message','original','genre', 'text length']).sum().sort_values(ascending=False).head(5)

    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre.values,
                    y=genre.index,
                    orientation='h'
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Genre"
                },
                'xaxis': {
                    'title': "Counts"
                }
            }
        },

        {
            'data': [
                Bar(
                    x=histogram.index,
                    y=histogram.values
                )
            ],

            'layout': {
                'title': 'Distribution of Messages Length',
                'yaxis': {
                    'title': "Total Messages"
                },
                'xaxis': {
                    'title': "Total Words"
                }
            }
        },

        {
            'data': [
                Bar(
                    x=total_category.index,
                    y=total_category.values
                )
            ],

            'layout': {
                'title': 'Total Messages per Category (Top 5)',
                'yaxis': {
                    'title': "Total"
                },
                'xaxis': {
                    'title': "Category"
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
