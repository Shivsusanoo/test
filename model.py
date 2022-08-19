# Importing Libraries
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

# Loading dataset
df = pd.read_csv(r'Customer_credit_default.csv')
df.drop(columns=['Unnamed: 0'],inplace=True)
# print(df.head())

X = df[['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE', 'PAY_1','PAY_2', 'PAY_3','TOTAL_BILL_AMT','TOTAL_PAY_AMT']]
y = df['DEFAULT_PAYMENT_NEXT_MONTH']

print(X.head())
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=99)

# Feature Scaling
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# Building model
rf = RandomForestClassifier(criterion='gini',n_estimators=350,max_depth=10,min_samples_split = 5,random_state=0)
rf.fit(X_train_s,y_train)
y_pred_rf = rf.predict(X_test_s)
print(f'accuracy: {accuracy_score(y_test,y_pred_rf)}')

# Saving model
joblib.dump(rf,'model.pkl')