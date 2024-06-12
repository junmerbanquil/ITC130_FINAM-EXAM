import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the web app
st.title('Maternal Health Risk Analysis')

# Load the dataset
@st.cache_data
def load_data():
    # Provide the correct path to the dataset
    url = 'Maternal Health Risk Data Set.csv'  # Replace with your data path or URL
    return pd.read_csv(url)

data = load_data()

# Sidebar header
st.sidebar.markdown("""
## ITC130 Final Exam
## Streamlit Project by:
## Junmer Banquil & Kristine Notarion
## https://github.com/junmerbanquil/ITC130_FINAM-EXAM.git
""")


# Sidebar header
st.sidebar.markdown("""
## Maternal Health Risk Analysis
""")

# Sidebar menu for navigation
menu = st.sidebar.selectbox(
    'Select an option',
    ('Dataset', 'Risk Level Distribution', 'Health Indicators Distribution', 'Age vs. Blood Pressure', 'Correlation Heatmap', 'Box Plots', 'Pairplot', 'Violin Plot')
)

if menu == 'Dataset':
    # Display the dataset as a table
    st.write('## Dataset')
    st.write(data)

elif menu == 'Risk Level Distribution':
    # Visualizing risk level distribution using a pie chart
    st.write('### Risk Level Distribution')
    st.write("This pie chart shows the proportion of each risk level in the dataset. It helps us understand the distribution of different risk levels among the patients.")
    fig, ax = plt.subplots()
    risk_counts = data['RiskLevel'].value_counts()
    ax.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Proportion of Each Risk Level')
    st.pyplot(fig)

elif menu == 'Health Indicators Distribution':
    # Health Indicators Distribution
    st.write('### Distribution of Health Indicators')
    st.write("These histograms show the distribution of Age, SystolicBP, DiastolicBP, Blood Sugar (BS), Body Temperature, and Heart Rate levels. Understanding these distributions can help in determining the health profile of the patients.")
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))
    sns.histplot(data['Age'], bins=20, kde=True, ax=ax[0, 0], color='blue')
    ax[0, 0].set_title('Age Distribution')
    sns.histplot(data['SystolicBP'], bins=20, kde=True, ax=ax[0, 1], color='green')
    ax[0, 1].set_title('Systolic BP Distribution')
    sns.histplot(data['DiastolicBP'], bins=20, kde=True, ax=ax[0, 2], color='red')
    ax[0, 2].set_title('Diastolic BP Distribution')
    sns.histplot(data['BS'], bins=20, kde=True, ax=ax[1, 0], color='orange')
    ax[1, 0].set_title('Blood Sugar Distribution')
    sns.histplot(data['BodyTemp'], bins=20, kde=True, ax=ax[1, 1], color='purple')
    ax[1, 1].set_title('Body Temperature Distribution')
    sns.histplot(data['HeartRate'], bins=20, kde=True, ax=ax[1, 2], color='brown')
    ax[1, 2].set_title('Heart Rate Distribution')
    st.pyplot(fig)

elif menu == 'Age vs. Blood Pressure':
    # Scatter plot of Age vs. SystolicBP
    st.write('### Age vs. Blood Pressure')
    st.write("This scatter plot shows the relationship between age and systolic blood pressure for different risk levels. It helps in identifying how age and blood pressure vary among patients with different risk levels.")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x='Age', y='SystolicBP', hue='RiskLevel', ax=ax)
    ax.set_title('Scatter plot of Age vs. Systolic BP')
    st.pyplot(fig)

elif menu == 'Correlation Heatmap':
    # Correlation heatmap
    st.write('### Correlation Heatmap')
    st.write("This heatmap shows the correlation between different health indicators in the dataset. High correlation values (positive or negative) indicate a strong relationship between the indicators, which can be important for understanding how different factors influence each other.")
    fig, ax = plt.subplots(figsize=(10, 8))
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation between Health Indicators')
    st.pyplot(fig)

elif menu == 'Box Plots':
    # Box plots of health indicators by risk level
    st.write('### Box Plots of Health Indicators by Risk Level')
    st.write("These box plots show the distribution of each health indicator across different risk levels.")
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))
    sns.boxplot(x='RiskLevel', y='Age', data=data, ax=ax[0, 0])
    ax[0, 0].set_title('Age by Risk Level')
    sns.boxplot(x='RiskLevel', y='SystolicBP', data=data, ax=ax[0, 1])
    ax[0, 1].set_title('Systolic BP by Risk Level')
    sns.boxplot(x='RiskLevel', y='DiastolicBP', data=data, ax=ax[0, 2])
    ax[0, 2].set_title('Diastolic BP by Risk Level')
    sns.boxplot(x='RiskLevel', y='BS', data=data, ax=ax[1, 0])
    ax[1, 0].set_title('Blood Sugar by Risk Level')
    sns.boxplot(x='RiskLevel', y='BodyTemp', data=data, ax=ax[1, 1])
    ax[1, 1].set_title('Body Temperature by Risk Level')
    sns.boxplot(x='RiskLevel', y='HeartRate', data=data, ax=ax[1, 2])
    ax[1, 2].set_title('Heart Rate by Risk Level')
    st.pyplot(fig)

elif menu == 'Pairplot':
    # Pairplot of health indicators
    st.write('### Pairplot of Health Indicators')
    st.write("This pairplot shows pairwise relationships in the dataset.")
    fig = sns.pairplot(data, hue='RiskLevel')
    st.pyplot(fig)

elif menu == 'Violin Plot':
    # Violin plot of health indicators by risk level
    st.write('### Violin Plot of Health Indicators by Risk Level')
    st.write("These violin plots show the distribution of each health indicator across different risk levels.")
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))
    sns.violinplot(x='RiskLevel', y='Age', data=data, ax=ax[0, 0])
    ax[0, 0].set_title('Age by Risk Level')
    sns.violinplot(x='RiskLevel', y='SystolicBP', data=data, ax=ax[0, 1])
    ax[0, 1].set_title('Systolic BP by Risk Level')
    sns.violinplot(x='RiskLevel', y='DiastolicBP', data=data, ax=ax[0, 2])
    ax[0, 2].set_title('Diastolic BP by Risk Level')
    sns.violinplot(x='RiskLevel', y='BS', data=data, ax=ax[1, 0])
    ax[1, 0].set_title('Blood Sugar by Risk Level')
    sns.violinplot(x='RiskLevel', y='BodyTemp', data=data, ax=ax[1, 1])
    ax[1, 1].set_title('Body Temperature by Risk Level')
    sns.violinplot(x='RiskLevel', y='HeartRate', data=data, ax=ax[1, 2])
    ax[1, 2].set_title('Heart Rate by Risk Level')
    st.pyplot(fig)

# Narrative explaining the context of the data
st.sidebar.write("""
### Context and Usage of the Data
This dataset contains various health indicators of pregnant women such as Age, Systolic Blood Pressure, Diastolic Blood Pressure, Blood Sugar, Body Temperature, and Heart Rate. These indicators are critical for determining the risk levels during pregnancy. The goal of this application is to provide insights into how different health indicators influence the risk levels.

### Metadata
- **Age**: Age of the patient
- **SystolicBP**: Systolic blood pressure
- **DiastolicBP**: Diastolic blood pressure
- **BS**: Blood sugar
- **BodyTemp**: Body temperature
- **HeartRate**: Heart rate
- **RiskLevel**: Risk level during pregnancy (Low, Mid, High)

### Insights
The following visualizations provide insights into the distribution and relationships of these health indicators.
""")
