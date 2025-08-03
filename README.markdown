# Banking Risk Analytics: With Python, SQL, and Power BI for Enhanced Decision-Making

## Project Overview
This project develops a comprehensive data analytics pipeline to assess and minimize financial risks in banking, focusing on loan repayment likelihood. By leveraging **Python**, **SQL**, **Excel**, and **Power BI**, the project provides actionable insights through exploratory data analysis (EDA) and interactive dashboards, enabling data-driven decisions for loan approvals.

### Problem Statement
The goal is to understand risk analytics in banking and financial services, using data to evaluate client profiles and minimize the risk of financial loss from lending. The solution involves creating dashboards to identify clients likely to repay loans, thus optimizing lending decisions.

### Objectives
- **Data Collection**: Source banking dataset from Kaggle, containing client details, financial metrics, and banking relationships.
- **Data Cleaning**: Preprocess data using SQL, Python (Pandas, NumPy), and Excel to ensure quality and consistency.
- **Exploratory Data Analysis (EDA)**: Analyze data distributions, correlations, and trends to uncover risk patterns.
- **Visualization & Reporting**: Build interactive Power BI dashboards to present key performance indicators (KPIs) and insights.
- **Risk Assessment**: Provide insights to support loan approval decisions based on client financial profiles.

## Dataset
The dataset, sourced from Kaggle, includes multiple tables:
- **Clients - Banking**: Contains client details (e.g., Client ID, Name, Age, Nationality, Bank Deposits, Loans, Credit Card Balance).
- **Gender**: Maps GenderId to gender categories.
- **Banking Relationship**: Maps BRId to relationship types (e.g., Retail, Private Bank).
- **Investment Advisor**: Maps IAId to advisor names.
- **Period**: (Assumed to be part of the dataset for temporal analysis, if applicable).

**Key Columns**:
- Financial metrics: Bank Deposits, Checking Accounts, Saving Accounts, Foreign Currency Account, Bank Loans, Business Lending, Credit Card Balance.
- Demographic data: Age, Nationality, Occupation, Gender.
- Banking details: Fee Structure, Loyalty Classification, Risk Weighting, Engagement Days.

## Methodology
### 1. Data Collection
- Downloaded the dataset from Kaggle (`Banking.xlsx`).
- Loaded into Python using Pandas for initial exploration and into SQL for structured querying.

### 2. Data Cleaning
Performed in **SQL**, **Python**, and **Excel**:
- **Engagement Timeframe**: Created a column to categorize client tenure based on `Joined Bank`.
- **Engagement Days**: Calculated days since joining using `DATEDIFF` in Power BI or Python.
- **Income Band**: Binned `Estimated Income` into Low (<100,000) and Mid (<300,000) categories.
- **Processing Fees**: Assigned fees (e.g., 0.05 for High Fee Structure) for cost calculations.
- Handled missing values, duplicates, and outliers using Pandas and Excel.
- Normalized financial columns for consistency.

### 3. Exploratory Data Analysis (EDA)
- **Tools**: Python (Pandas, NumPy, Matplotlib, Seaborn).
- **Analyses**:
  - Identified strong positive correlations between Bank Deposits, Checking Accounts, Saving Accounts, and Foreign Currency Account, indicating clients with high balances maintain substantial funds across accounts.
  - Analyzed distributions of Age, Estimated Income, and Credit Card Balance using histograms and boxplots.
  - Explored risk patterns by Nationality, Gender, and Banking Relationship.
- **Visualizations**:
  - Heatmaps for correlation analysis.
  - Boxplots for detecting outliers in financial metrics.
  - Bar plots for categorical analysis (e.g., Loyalty Classification, Fee Structure).

### 4. Visualization & Reporting
- **Tool**: Power BI.
- **KPIs Calculated**:
  - **Total Clients**: `DISTINCTCOUNT('Clients - Banking'[Client ID])`.
  - **Total Loan**: Sum of Bank Loans, Business Lending, and Credit Card Balance.
  - **Bank Deposit**: `SUM('Clients - Banking'[Bank Deposits])`.
  - **Total Fees**: `SUMX('Clients - Banking', [Total Loan] * [Processing Fees])`.
  - **Engagement Days**: `DATEDIFF('Clients - Banking'[Joined Bank], TODAY(), DAY)`.
  - Other KPIs: Checking Accounts, Saving Accounts, Foreign Currency Account, Credit Card Balance.
- **Dashboards**:
  - **Home**: Overview of KPIs (Total Clients, Total Loan, Total Deposit).
  - **Loan Analysis**: Visualizes loan amounts by client segments (e.g., Gender, Nationality).
  - **Deposit Analysis**: Displays deposit trends across account types.
  - **Summary Dashboard**: Aggregates key metrics for decision-making.

### 5. Key Findings
- **Correlation Insights**: Strong positive correlations among deposit accounts suggest that high-balance clients are diversified across account types, indicating lower risk profiles.
- **Risk Patterns**: Clients with higher Risk Weighting tend to have larger loans, requiring closer scrutiny.
- **Demographic Trends**: Certain nationalities and age groups show higher loan repayment reliability.
- **Loyalty Impact**: Jade and Platinum clients contribute significantly to deposits but also hold substantial loans.

## Tools & Technologies
- **Python**: Pandas, NumPy, Matplotlib, Seaborn for data cleaning and EDA.
- **SQL**: Data preprocessing and querying.
- **Excel**: Initial data exploration and cleaning.
- **Power BI**: Dashboard creation and KPI visualization.
- **Jupyter Notebook**: Documented EDA and preprocessing steps (`Banking_data_preprocessing.ipynb`).

## Repository Structure
```
├── data/
│   ├── Raw data.csv                # Raw dataset
│   ├── Clean_data.xlsx    # Cleaned dataset
├── scripts/
│   ├── data_cleaning.py           # Python script for data cleaning
│   ├── eda.py                     # Python script for EDA
│   ├── sql_queries.sql            # SQL queries for preprocessing
├── notebooks/
│   ├── Banking_data_analysis_main.ipynb  # Jupyter Notebook for EDA
├── dashboards/
│   ├── Banking_dashboard.pbix     # Power BI dashboard file (placeholder)
├── README.md                      # Project overview
```

## Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/banking-risk-analytics.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. **Run Python Scripts**:
   - Execute `data_cleaning.py` for preprocessing.
   - Run `eda.py` for exploratory analysis.
4. **SQL Setup**:
   - Import `Raw data.xlsx` into your SQL database (e.g., MySQL, SQLite).
   - Run queries in `sql_queries.sql`.
5. **Power BI**:
   - Open `Banking_dashboard.pbix` in Power BI Desktop to view dashboards.

## Usage
- **Data Cleaning**: Run `data_cleaning.py` to preprocess the dataset and generate `cleaned_banking_data.csv`.
- **EDA**: Use `eda.py` or `Banking_data_preprocessing.ipynb` to explore data and visualize trends.
- **Dashboards**: Load `Banking_dashboard.pbix` in Power BI to interact with KPIs and visualizations.
- **SQL Queries**: Execute `sql_queries.sql` for data extraction and preprocessing.

## Future Work
- **Predictive Modeling**: Incorporate machine learning (e.g., logistic regression, random forests) to predict loan repayment likelihood.
- **Automation**: Develop automated ETL pipelines for real-time data updates.
- **Segment Analysis**: Deepen analysis of client segments by occupation or loyalty classification.
- **Scalability**: Extend dashboards to include real-time risk monitoring and alerts.

## Conclusion
This project demonstrates a robust data analytics pipeline for banking risk assessment, combining data cleaning, EDA, and visualization to support informed lending decisions. The Power BI dashboards provide actionable insights, enabling banks to minimize financial risks and optimize loan approvals.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Your Name**: [Your GitHub Profile](https://github.com/your-username)
- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)
