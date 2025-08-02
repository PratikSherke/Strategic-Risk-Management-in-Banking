import pandas as pd
import numpy as np
from datetime import datetime

# Load dataset
df = pd.read_excel('Raw data.xlsx', sheet_name='Clients - Banking')

# Data Cleaning
# Handle missing values
df = df.fillna({
    'Estimated Income': df['Estimated Income'].median(),
    'Credit Card Balance': 0,
    'Bank Deposits': 0
})

# Create Engagement Days
df['Joined Bank'] = pd.to_datetime(df['Joined Bank'], format='%d-%m-%Y')
df['Engagement Days'] = (datetime.now() - df['Joined Bank']).dt.days

# Create Income Band
df['Income Band'] = pd.cut(df['Estimated Income'], 
                          bins=[0, 100000, 300000, float('inf')], 
                          labels=['Low', 'Mid', 'High'])

# Create Processing Fees
df['Processing Fees'] = df['Fee Structure'].map({
    'High': 0.05,
    'Mid': 0.03,
    'Low': 0.01
})

# Save cleaned dataset
df.to_csv('data/cleaned_banking_data.csv', index=False)
print("Data cleaning completed. Saved to 'cleaned_banking_data.csv'")
