import numpy as np
import pandas as pd              
import matplotlib.pyplot as plt  
import seaborn as sns  

file_path="C:/Users/HP/Downloads/aquaattributes.xlsx"      
df = pd.read_excel(file_path, sheet_name="Sheet1")    

print(df.shape)         
print(df.columns)
print(df.info())        
print(df.head())  

     
print(df.isnull().sum())
df = df.fillna(df.median(numeric_only=True))
print(df.isnull().sum())
df['class'] = df['class'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)


for col in df.columns:
    print(col, df[col].isin(['-']).sum())
    
df.replace('-', np.nan, inplace=True)
    
numeric_cols = ['Conductivity', 'Nitrate', 'Fecalcaliform']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')



df['Conductivity'] = df['Conductivity'].fillna(df['Conductivity'].median())
df['Nitrate'] = df['Nitrate'].fillna(df['Nitrate'].median())
df['Fecalcaliform'] = df['Fecalcaliform'].fillna(df['Fecalcaliform'].median())
df['State'] = df['State'].fillna(df['State'].mode()[0])
print(df.isnull().sum())

print(df.describe())

plt.figure(figsize=(10, 6))
numeric_df = df.select_dtypes(include=['number'])  
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Water Quality Parameters")
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(df['pH'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of pH Levels in Water Samples")
plt.xlabel("pH Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Conductivity', y='B.O.D', data=df, hue='class', palette='coolwarm')
plt.title("Scatter Plot: Conductivity vs. B.O.D")
plt.xlabel("Conductivity")
plt.ylabel("Biological Oxygen Demand (B.O.D)")
plt.grid(True)
plt.show()


print("Missing Values in Each Column:")
print(df.isnull().sum())

# Grouping by class and taking average B.O.D
bod_by_class = df.groupby('class')['B.O.D'].mean()
plt.figure(figsize=(6, 5))
sns.barplot(x=bod_by_class.index, y=bod_by_class.values, palette='viridis')
plt.title("Average B.O.D by Water Quality Class")
plt.xlabel("Water Quality Class (0 = Not Acceptable, 1 = Acceptable)")
plt.ylabel("Average B.O.D (mg/L)")
plt.ylim(0, max(bod_by_class.values) + 5)
plt.grid(axis='y')
plt.show()








