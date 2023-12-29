import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Chennai_dataset.csv')

df['N_BEDROOM'].fillna(df['N_BEDROOM'].median(), inplace=True)
df['QS_OVERALL'].fillna(df['QS_OVERALL'].median(), inplace=True)
df['N_BATHROOM'].fillna(df['N_BATHROOM'].median(), inplace=True)

for col in df.columns:
    if df[col].dtypes == 'float64':
        df[col] = df[col].astype('int64')

df = df.apply(lambda x: x.replace({'Ann Nagar': 'Anna Nagar', 'Ana Nagar': 'Anna Nagar', 'Adyr': 'Adyar', 'Chrompt': 'Chrompet', 'Chrmpet': 'Chrompet', 'Chormpet': 'Chrompet', 'KKNagar': 'KK Nagar', 'Velchery': 'Velachery', 'Karapakam': 'Karapakkam',
              'TNagar': 'T Nagar', 'Noo': 'No', 'Other': 'Others', 'Comercial': 'Commercial', 'Adj Land': 'AdjLand', 'Ab Normal': 'AbNormal', 'Partiall': 'Partial', 'PartiaLl': 'Partial', 'All Pub': 'AllPub', 'Pavd': 'Paved', 'NoAccess': 'No Access'}))

df['DATE_SALE'] = pd.to_datetime(df['DATE_SALE'], format='%d-%m-%Y')
df['DATE_BUILD'] = pd.to_datetime(df['DATE_BUILD'], format='%d-%m-%Y')
df['PROP_AGE'] = (pd.DatetimeIndex(df['DATE_SALE']).year -
                  pd.DatetimeIndex(df['DATE_BUILD']).year).astype('int64')

df = df.drop(columns='PRT_ID')
cat_df = df.select_dtypes(exclude=['int64'])
num_df = df.select_dtypes(include=['int64'])

cat_df = cat_df.drop(columns=['DATE_SALE', 'DATE_BUILD'])
num_df = num_df.drop(
    columns=['DIST_MAINROAD', 'QS_ROOMS', 'QS_BATHROOM', 'QS_BEDROOM', 'QS_OVERALL'])

le = LabelEncoder()
for i in cat_df:
    cat_df[i] = le.fit_transform(cat_df[i])

main_df = pd.concat([cat_df, num_df], axis=1)

X = main_df.drop(['SALES_PRICE'], axis=1).values
Y = main_df['SALES_PRICE'].values

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = RandomForestRegressor().fit(x_train, y_train)

pred_val = model.predict(x_test)
acc = round(r2_score(y_test, pred_val), 4)*100


def pred_chennai(area, sale_cond, park_facil, buildtype, utility_avail, street, mzzone, sqft, bedroom, bathroom, n_room, reg_fee, commition, age):

    area_pair = dict(zip(df['AREA'], main_df['AREA']))
    park_pair = dict(zip(df['PARK_FACIL'], main_df['PARK_FACIL']))
    build_pair = dict(zip(df['BUILDTYPE'], main_df['BUILDTYPE']))
    utility_pair = dict(zip(df['UTILITY_AVAIL'], main_df['UTILITY_AVAIL']))
    street_pair = dict(zip(df['STREET'], main_df['STREET']))
    mzone_pair = dict(zip(df['MZZONE'], main_df['MZZONE']))
    cond_pair = dict(zip(df['SALE_COND'], main_df['SALE_COND']))

    area = area_pair[area]
    sale_cond = cond_pair[sale_cond]
    park_facil = park_pair[park_facil]
    buildtype = build_pair[buildtype]
    utility_avail = utility_pair[utility_avail]
    street = street_pair[street]
    mzzone = mzone_pair[mzzone]

    price = model.predict([[area, sale_cond, park_facil, buildtype, utility_avail,
                          street, mzzone, sqft, bedroom, bathroom, n_room, reg_fee, commition, age]])[0]
    return round(price, 2)
