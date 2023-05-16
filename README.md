# Zillow_project


Telco churn rate - individual project

# Objectives:

This project aims to explore the telco_churn database and determine predictive factors relating to churn. The database contains quite a bit of data collected on their customers. 

# Project Goal:

- Discover drivers of churn at Telco
- Use drivers to develop a machine learning model to predict whether someone will churn based on analyzed features.
- Churn is defined as a customer that leaves the company, for whatever reason.
- Predicting churn could be used to understand where to make changes in business practices. Ultimately, increasing retention... and thus, revenue.

# Initial questions:

I am curious to see how monthly charges, tenure, tech support and whether or not someone is a senior citizen affects churn rate at telco churn.

# The Plan:

Aquire data from codeup.com

Prepare data

Create encoded columns from existing data

Explore data in search of drivers of churn

Answer the following initial questions:
- Do monthly charges affect churn rate?
- Does tenure affect churn rate?
- Does whether or not someone has tech support affect churn?
- Does being a senior citizen or not affect churn?

Develop a Model to predict if a customer will churn

- Use drivers identified in explore to build predictive models
- Evaluate models on train and validate data
- Select the best model based on highest accuracy
- Evaluate the best model on test data
- Draw conclusions

# Steps to Reproduce:

- Clone this repo.
- Acquire the data from codeup.com
- Put the data in the file containing the cloned repo.
- Run notebook.
### Additional Requirements:
- to have an env.py file with applicable username and password for the codeup.com database
- download the pro_acquire, pro_prep, pro_model, and knear .py files as well
- import the following
  - import pandas as pd
  - import numpy as np
  - import scipy.stats as stats

  - import matplotlib.pyplot as plt
  - import seaborn as sns

  - from sklearn.tree import DecisionTreeClassifier
  - from sklearn.tree import plot_tree
  - from sklearn.metrics import classification_report, confusion_matrix
  - from sklearn.linear_model import LogisticRegression
  - from sklearn.ensemble import RandomForestClassifier
  - from sklearn.neighbors import KNeighborsClassifier

  - import pro_acquire as acq
  - import pro_prepare as prep
  - import pro_model as pm
  - import knear as k

# Data Dictionary:

| Feature | Definition |
|:--------|:-----------|
|customer_id | unique customer identifier (obj|
|tenure| how long someone has been a customer in months (int)|
|monthly_charges| how much a customer is charged monthly (float)|
|tech_support_Yes| whether or not a customer has tech support (1 for yes)|
|churn_encoded| whether or not a customer has churned (1 for yes)|
|senior_citizen_Yes| whether or not a customer is a senior citizen (1 for yes)|

# Takeaways:

- Customers that Churn pay more monthly charges on average than those who do not. Mean = ~$65.00
- Customers with higher tenure churn less than customers with < ~32 months of tenure.
- Customers with tech support churned ~11% less than those without tech support.
- The customer base is only ~19% senior, however, ~68% of the senior population churns.
- All 4 independent variables are statistically significant to churn. I will use all 4 in modeling.

- *** If I had more time, I would like to move beyond this rudimentary analysis and analyze more in depth the relationships between these variables and explore more features.

- the models predict better than baseline with selected features

# Recommendations:
- All of the selected features contribute to the churn rate of Telco. I would contact my senior citizen population to question which of their needs are not being met. 
    - Having tech support seems to alleviate churn in this population. 
    - When plans are opened/renewed, we should stress the importance of tech support. 
- Monthly charges are also a driver of churn and should be further explored to ensure our customers are getting what they feel they pay for i.e.. service, reliability, availability of signal. 

# Next steps:
- With more time, further statistical analysis of the remaining features would be in the best interest of the company.
    
    - Analyzing the relationships between multiple features in relation to churn, for example.. senior citizen, no tech support and has fiber internet. Even though the selected features affect churn, their relationships to other factors may direct where we want to focus efforts.

```python

```
