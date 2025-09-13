from flask import Flask,request,jsonify,render_template
import pandas as pd
import pickle

app= Flask(__name__)

def get_cleaned_data(form_data):
    gestation=float(form_data['gestation'])
    parity=int(form_data['parity'])
    age=float(form_data['age'])
    height=float(form_data['height'])
    weight=float(form_data['weight'])
    smoke=float(form_data['smoke'])
    
    cleaned_data ={
        "gestation":[gestation],
        "parity":[parity],
        "age":[age],
        "height":[height],
        "weight":[weight],
        "smoke":[smoke]
    }
    return cleaned_data

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def get_prediction():
    baby_data_form=request.form
    baby_data=get_cleaned_data(baby_data_form)
    baby_df=pd.DataFrame(baby_data)

    with open("model/model.pkl",'rb') as obj:
        model =pickle.load(obj)

    predictions=model.predict(baby_df)
    predictions=round(float(predictions),2)

    response={"Prediction":predictions}
    return render_template("index.html",predictions=predictions)


if __name__=='__main__':
    app.run(debug=True)