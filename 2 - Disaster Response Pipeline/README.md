# Disaster Response Pipeline Project

### Libraries
To be able to run this project, you need to install the required libraries in the `requirements.txt`. Run the command below.
```
pip install -r requirements.txt
```

### Introduction
In this project, we are going to built a web app to do Machine Learning task, which is classifying a message. If we breakdown, there are three major steps in this project.

#### 1. ETL Process
We merge the dataset in the `data` folder (`disaster_messages.csv` and `disaster_categories.csv`), then do some preprocessing to get the clean data. We store the clean data in sqlite database `DisasterResponse.db`.

#### 2. Training Model
Using scikit-learn, then we train the classifier to be able to get a model which can classify a message, save the model in the `models` folder with the name `classifier.pkl`.

#### 3. Run the Web App
Using flask, we can run our model and deploy in the website so that people can manually type the message and see its category. 

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
