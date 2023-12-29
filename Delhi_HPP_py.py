import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Delhi_dataset.csv')

df.drop(df.index[(df['Parking'] == 39)], axis=0, inplace=True)
df.drop(df.index[(df['Parking'] == 114)], axis=0, inplace=True)


def grp_loc(locality):
    locality = locality.lower()
    if 'rohini' in locality:
        return 'Rohini Sector'
    elif 'dwarka' in locality:
        return 'Dwarka Sector'
    elif 'shahdara' in locality:
        return 'Shahdara'
    elif 'vasant' in locality:
        return 'Vasant Kunj'
    elif 'paschim' in locality:
        return 'Paschim Vihar'
    elif 'alaknanda' in locality:
        return 'Alaknanda'
    elif 'vasundhara' in locality:
        return 'Vasundhara Enclave'
    elif 'punjabi' in locality:
        return 'Punjabi Bagh'
    elif 'kalkaji' in locality:
        return 'Kalkaji'
    elif 'lajpat' in locality:
        return 'Lajpat Nagar'
    elif 'laxmi' in locality:
        return 'Laxmi Nagar'
    elif 'patel' in locality:
        return 'Patel Nagar'
    else:
        return 'Other'


df['Locality'] = df['Locality'].apply(grp_loc)

df['Per_Sqft'].fillna(round((df['Price']/df['Area']), 0), inplace=True)
df['Furnishing'].fillna('Semi-Furnished', inplace=True)
df['Bathroom'].fillna(df['Bathroom'].mode()[0], inplace=True)
df['Type'].fillna(df['Type'].mode()[0], inplace=True)
df['Parking'].fillna(0, inplace=True)

df['Furnishing'] = df['Furnishing'].str.replace('-', ' ')
df['Status'] = df['Status'].str.replace('_', ' ')
df['Transaction'] = df['Transaction'].str.replace('_', ' ')
df['Type'] = df['Type'].str.replace('_', ' ')

for i in df.columns:
    if df[i].dtypes == 'float64':
        df[i] = df[i].astype('int64')

cat_df = df.select_dtypes(exclude=['int64'])
num_df = df.select_dtypes(include=['int64'])

num_df = num_df.drop('Per_Sqft', axis=1)


le = LabelEncoder()
for i in cat_df.columns:
    cat_df[i] = le.fit_transform(cat_df[i])

main_df = pd.concat([cat_df, num_df], axis=1)

X = main_df.drop('Price', axis=1).values
Y = main_df['Price'].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = RandomForestRegressor()
model.fit(x_train, y_train)


def pred_delhi(furnishing, locality, status, transaction, type, area, bhk, bathroom, parking):

    locality_pair = dict(zip(df['Locality'], main_df['Locality']))
    furnishing_pair = dict(zip(df['Furnishing'], main_df['Furnishing']))
    status_pair = dict(zip(df['Status'], main_df['Status']))
    type_pair = dict(zip(df['Type'], main_df['Type']))
    transaction_pair = dict(zip(df['Transaction'], main_df['Transaction']))

    furnishing = furnishing_pair[furnishing]
    locality = locality_pair[locality]
    status = status_pair[status]
    transaction = transaction_pair[transaction]
    type = type_pair[type]

    price = model.predict([[furnishing, locality, status,
                          transaction, type, area, bhk, bathroom, parking]])[0]
    return round(price, 2)
