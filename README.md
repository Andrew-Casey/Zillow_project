# Zillow_project

<!-- #region -->

# Objectives:

- This project aims to explore the Zillow database and determine predictive factors relating to house tax value. The database contains an extensive collection of data on houses in the LA, Ventura and Orange County area. 

# Project Goal:

- Discover drivers of Tax_Value
- Use drivers to develop a machine learning model to predict future tax value for homes in the area of study.
- Predicting house values could be used to understand where to make changes in business practices. Ultimately, increasing homes sold... and thus, more revenue.

# Initial questions:

- I am curious to see how square feet, location, number of bedrooms and bathrooms affect tax value.

# The Plan:

- Aquire data from codeup.com

- Prepare data

- Create encoded columns from existing data

- Explore data in search of drivers of tax value

- Answer the following initial questions:
    - How does Sqft affect Tax_Value?
    - How does Bedrooms affect Tax_Value?
    - How does Bathrooms affect Tax_Value?
    - How does Lot_Size affect Tax_Value?
    - How does Year_Built affect Tax_Value?
    - How does having a Pool affect Tax_Value?
    - Does location affect Tax_Value? Which location is the most expensive? The cheapest?

- Develop a Model to predict house value:
    - Use drivers identified in explore to build predictive models
    - Evaluate models on train and validate data
    - Select the best model based on lowest RMSE and highest R^2 values
    - Evaluate the best model on test data
- Draw conclusions

# Steps to Reproduce:

- Clone this repo.
- Acquire the data from codeup.com using an env.py file with requisite credentials.
- Put the data in the file containing the cloned repo.
- Run notebook.

### Additional Requirements:

- to have an env.py file with applicable username and password for the codeup.com database
- download the acquire, evaluate, explore, prepare, and wrangle .py files

- import the following:
    - import pandas as pd
    - import itertools
    - import numpy as np
    - import scipy.stats as stats
    - from scipy.stats import pearsonr
    - from scipy.stats import spearmanr
    - import matplotlib.pyplot as plt
    - import seaborn as sns

    - from sklearn.linear_model import LinearRegression
    - from sklearn.preprocessing import MinMaxScaler
    - from sklearn.preprocessing import StandardScaler
    - from sklearn.preprocessing import RobustScaler
    - from sklearn.preprocessing import QuantileTransformer
    - from sklearn.model_selection import train_test_split
    - from sklearn.metrics import mean_squared_error
    - from sklearn.metrics import r2_score
    - from sklearn.feature_selection import RFE
    - from sklearn.linear_model import LassoLars
    - from sklearn.preprocessing import PolynomialFeatures
    - from sklearn.linear_model import TweedieRegressor
    - from sklearn.metrics import r2_score

    - import env
    - import acquire as a
    - import wrangle as w
    - import explore as e
    - import prepare as p
    - import evaluate as eva

    - import warnings
        - warnings.filterwarnings("ignore")


# Data Dictionary:

| Feature | Definition |
|:--------|:-----------|
|Tax_Value | The appraised tax value of the house(int)|
|Sqft| Sqft of living space (int)|
|Bedrooms| Number of Bedroom in a house (int)|
|Bathrooms| Number of Bathrooms in a house (float)|
|Pool| Whether or not there is a pool (int, bool)|
|Zip_Code| What Zip Code the house is in (int)|
|City| The city a house is located in (int)|
|LA| House located in LA County (obj)|
|Orange| House located in Orange County (obj)|
|Ventura| House located in Ventura County (obj)|



# Takeaways:
- The best performing model was Polynomial Regression
- the R^2 value is .30 and has RMSE of 270503.78
- I ran many iterations of the data, and found that using Sqft, Bedrooms, Bathrooms, Year_Built and pool produced the best predictive model. It does perform better than the baseline of 414380.33. 


# Recommendations:
- All of the selected features contribute to the assessed tax value of a home. I recommend better data collecting, to avoid massive amounts of null values in various categories (garage, story). I believe a better predictive model can be achieved with the ability to add additional features to the model. 

- Location always plays a large part in buying a home. LA, according to the data is the least desirable place to live. - I believe this is due to homes being older on average in LA (1956) as compared to Orange and Ventura (1973, 1975 respectively). To further explore location, delineating City and Zip Code as well as building materials in these areas may shed light on what residents of these areas desire or not. 


# Next steps:
- There has to be a better way to identify Zip Codes, City and other location metrics. With more time I would like to further investigate location metrics between the three counties.  
- Also, I want to continue my research and analyze the relationships between multiple features in relation to tax value, for example.. building materials, pool, Ventura, 2 Car Garage, 1 Story, Big yard and how they interact with each other. Even though the selected features affect tax value, their relationships to other factors may direct where we want to focus our marketing efforts.
<!-- #endregion -->
