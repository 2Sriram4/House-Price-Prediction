from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Mumbai_dataset.csv')

df = df.drop('locality', axis=1)


def crore_to_lakhs(row):
    if row['price_unit'] == 'L':
        return row['price']
    else:
        return row['price'] * 100


df['price'] = df.apply(crore_to_lakhs, axis=1)
df = df.drop(columns='price_unit')

df['price'] = np.log(df['price'])

cat_df = df.select_dtypes(include=['object'])
num_df = df.select_dtypes(exclude=['object'])

le = LabelEncoder()
for i in cat_df.columns:
    cat_df[i] = le.fit_transform(cat_df[i])

main_df = pd.concat((cat_df, num_df), axis=1)

X = main_df.drop(columns=['price']).values
Y = main_df['price'].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = RandomForestRegressor()
model.fit(x_train, y_train)

pred_val = model.predict(x_test)

type_pair = dict(zip(df['type'], main_df['type']))
region_pair = dict(zip(df['region'], main_df['region']))
status_pair = dict(zip(df['status'], main_df['status']))
age_pair = dict(zip(df['age'], main_df['age']))


def pred_mumbai(type, region, status, age, bhk, area):

    type = type_pair[type]
    region = region_pair[region]
    status = status_pair[status]
    age = age_pair[age]

    price = model.predict([[type, region, status, age, bhk, area]])[0]
    price = np.exp(price)
    return round(price,2)
