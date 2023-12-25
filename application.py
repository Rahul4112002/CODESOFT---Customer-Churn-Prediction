from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app=application
model = pickle.load(open('Customer_Churn_Prediction.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')
@app.route('/home.html', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about.html', methods=['GET'])
def About():
    return render_template('about.html')

@app.route('/features.html', methods=['GET'])
def Features():
    return render_template('features.html')


standard_to = StandardScaler()
@app.route('/predict.html',methods=['GET' , 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        Geography_Germany = request.form['Geography_Germany']
        if(Geography_Germany == 'Germany'):
            Geography_Germany = 1
            Geography_Spain= 0
            Geography_France = 0
                
        elif(Geography_Germany == 'Spain'):
            Geography_Germany = 0
            Geography_Spain= 1
            Geography_France = 0
        
        else:
            Geography_Germany = 0
            Geography_Spain= 0
            Geography_France = 1
        Gender_Male = request.form['Gender_Male']
        if(Gender_Male == 'Male'):
            Gender_Male = 1
            Gender_Female = 0
        else:
            Gender_Male = 0
            Gender_Female = 1
        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography_Germany,Geography_Spain,Gender_Male]])
        if prediction==1:
             return render_template('predict.html',prediction_text="The Member will leave the bank")
        else:
             return render_template('predict.html',prediction_text="The Member will not leave the bank")
    return render_template('predict.html')        
if __name__=="__main__":
    app.run(debug=True)