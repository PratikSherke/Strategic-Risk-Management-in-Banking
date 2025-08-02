import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('Clean_data.csv')

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df[['Bank Deposits', 'Checking Accounts', 'Saving Accounts', 
                'Foreign Currency Account', 'Bank Loans', 'Credit Card Balance']].corr(), 
            annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Financial Metrics')
plt.savefig('visualizations/correlation_heatmap.png')
plt.close()

# Distribution of Estimated Income
plt.figure(figsize=(8, 6))
sns.histplot(df['Estimated Income'], bins=30, kde=True)
plt.title('Distribution of Estimated Income')
plt.savefig('visualizations/income_distribution.png')
plt.close()

# Boxplot for Credit Card Balance by Loyalty Classification
plt.figure(figsize=(8, 6))
sns.boxplot(x='Loyalty Classification', y='Credit Card Balance', data=df)
plt.title('Credit Card Balance by Loyalty Classification')
plt.savefig('visualizations/credit_card_boxplot.png')
plt.close()

print("EDA visualizations saved in 'visualizations' folder")
