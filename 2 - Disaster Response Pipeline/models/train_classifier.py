from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine

import pandas as pd
import numpy as np
import pickle
import nltk
import sys
nltk.download(['punkt','wordnet'])


def load_data(database_filepath):
    """load data from the sqlite database"""

    # Read the table as pandas dataframe
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('messages', con=engine)

    # Split the dataframe into x and y
    X = df['message']
    Y = df.drop(columns=['id','message','original','genre'])

    # Get the label names
    category_names = Y.columns

    return X, Y, category_names

def tokenize(text):
    """Tokenize and lemmatize each word in a given text"""

    # Tokenize the string text and initiate the lemmatizer
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    # Lemmatize each word in tokens
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """Create a machine learning pipeline"""

    # Create a pipeline consists of count vectorizer -> KneighborsClassifier()
    pipeline = Pipeline([
        
        ('text_pipeline', Pipeline([
            ('vect', CountVectorizer(tokenizer=tokenize)),
            ('tfidf', TfidfTransformer())
        ])),

        ('clf', MultiOutputClassifier(KNeighborsClassifier()))
    ])

    ## Find the optimal model using GridSearchCV
    parameters = {
        'text_pipeline__tfidf__use_idf': (True, False),
        'clf__estimator__weights': ['uniform', 'distance']
    }

    pipeline = GridSearchCV(pipeline, param_grid=parameters, verbose=5, cv=2, n_jobs=2)

    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    """Display the classification report for the given model"""

    # Predict the given X_test and create the report based on the Y_pred
    Y_pred = model.predict(X_test)
    print(classification_report(Y_test, Y_pred, target_names=category_names))


def save_model(model, model_filepath):
    """Save the given model into pickle object"""

    # Save the model based on model_filepath given
    pkl_filename = '{}'.format(model_filepath)
    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
