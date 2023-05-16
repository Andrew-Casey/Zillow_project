import pandas as pd
import numpy as np


import seaborn as sns
import matplotlib.pyplot as plt

import env
import os
import wrangle as w

def check_file_exists(fn, query, url):
    """
    check if file exists in my local directory, if not, pull from sql db
    return dataframe
    """
    if os.path.isfile(fn):
        print('csv file found and loaded')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df 


def get_zillow():
    url = env.get_db_url('zillow')

    query = """ select taxvaluedollarcnt as Tax_Value, calculatedfinishedsquarefeet as Sqft, fips as County, roomcnt as Bedrooms, fullbathcnt as Bathrooms
from properties_2017
join predictions_2017 using (parcelid)
join propertylandusetype using (propertylandusetypeid)
where propertylandusedesc Like 'Single Family Residential'
	and transactiondate Like '2017%%'
             """
    filename = 'zillow.csv'
    df = check_file_exists(filename, query, url)

    return df

def get_zillow2():
    url = env.get_db_url('zillow')

    query = """ select taxvaluedollarcnt as Tax_Value, calculatedfinishedsquarefeet as Sqft, fips as County, bedroomcnt as Bedrooms, bathroomcnt as Bathrooms, lotsizesquarefeet as Lot_Size, yearbuilt as Year_Built, poolcnt as Pool, regionidzip as Zip_Code, regionidcity as City
from properties_2017
join predictions_2017 using (parcelid)
join propertylandusetype using (propertylandusetypeid)
left join storytype using (storytypeid)
left join typeconstructiontype using (typeconstructiontypeid)
where propertylandusedesc Like 'Single Family Residential'
	and transactiondate Like '2017%%'
             """
    filename = 'zillow2.csv'
    df = check_file_exists(filename, query, url)

    return df 


def wrangle_zillow():
    
    #load zillow database
    df = w.get_zillow()
    
    # change fips codes to county name
    df['County'] = df['County'].replace([6037.0, 6059.0, 6111.0],['LA','Orange','Ventura']).astype(str)

     # Create dummy variables for the species column
    dummy_df = pd.get_dummies(df['County'], drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    #drop all nulls
    df = df.dropna()
    
    #handle outliers
    df = df[df.Tax_Value <= 2000000]  
    df = df[df.Sqft <= 6000]
    df = df[df.Bedrooms <= 8]
    df = df[df.Bathrooms <= 5]

    return df

def wrangle_zillow2():
    
    #load zillow database
    df = w.get_zillow2()
    
    # change fips codes to county name
    df['County'] = df['County'].replace([6037.0, 6059.0, 6111.0],['LA','Orange','Ventura']).astype(str)

     # Create dummy variables for the species column
    dummy_df = pd.get_dummies(df['County'], drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)

    # fill pool null values to 0
    df.Pool = df.Pool.fillna(0)
    
    #drop all remaining nulls
    df = df.dropna()
    
    #handle outliers
    df = df[df.Tax_Value <= 2000000]  
    df = df[df.Sqft <= 6000]
    df = df[df.Bedrooms <= 8]
    df = df[df.Bathrooms <= 5]
    df = df[df.Lot_Size <= 12000]
    df = df[df.Year_Built >= 1920]

    return df