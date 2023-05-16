#imports
import numpy as np
import pandas as pd
from pydataset import data
import os
import env



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

    query = """ select taxvaluedollarcnt as Tax_Value, calculatedfinishedsquarefeet as Sqft, fips as County, bedroomcnt as Bedrooms, bathroomcnt as Bathrooms, lotsizesquarefeet as Lot_Size, yearbuilt as Year_Built, poolcnt as Pool
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