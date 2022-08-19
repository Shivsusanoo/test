import numpy as np
import joblib
from flask import Flask, render_template, request
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    LIMIT_BAL = request.form.get('LIMIT_BAL')
    SEX = request.form.get('SEX')
    EDUCATION = request.form.get('EDUCATION')
    MARRIAGE = request.form.get('MARRIAGE')
    AGE = request.form.get('AGE')
    PAY_1 = request.form.get('PAY_1')
    PAY_2 = request.form.get('PAY_2')
    PAY_3 = request.form.get('PAY_3')
    TOTAL_BILL_AMT = request.form.get('TOTAL_BILL_AMT')
    TOTAL_PAY_AMT = request.form.get('TOTAL_PAY_AMT')


    if SEX.lower() == "male":
        SEX = 1
    else:
        SEX = 2
    

    if MARRIAGE.lower() == 'married':
        MARRIAGE = 1
    else:
        MARRIAGE = 2

    if EDUCATION.lower() == "graduate school":
        EDUCATION = 1
    elif EDUCATION.lower() == "university":
        EDUCATION = 2
    elif EDUCATION.lower() == "high school":
        EDUCATION = 3
    else:
        EDUCATION = 5

    def pay_value(p):
        if p.lower() == "pay duly":
            p = -1
        elif p.lower() == "payment delay for one month":
            p = 1
        elif p.lower() == "payment delay for two months":
            p = 2
        elif p.lower() == "payment delay for three month":
            p = 3
        elif p.lower() == "payment delay for four months":
            p = 4
        elif p.lower() == "payment delay for five month":
            p = 5
        elif p.lower() == "payment delay for six months":
            p = 6
        elif p.lower() == "payment delay for seven month":
            p = 7
        elif p.lower() == "payment delay for eight months":
            p = 8
        else:
            p = 9
        return p
    
    PAY_1 = pay_value(PAY_1)
    PAY_2 = pay_value(PAY_2)
    PAY_3 = pay_value(PAY_3)


    prediction = model.predict([[LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_1,PAY_2,PAY_3,TOTAL_BILL_AMT,TOTAL_PAY_AMT]])


    output = round(prediction[0],1)
    print(output)
    if output == 1:
        output = "Defaulter"
    else:
        output = "Non Defaulter"

    return render_template('home.html',data = 'Customer is: {}'.format(output))


if __name__ =="__main__":
    app.run(debug=True)