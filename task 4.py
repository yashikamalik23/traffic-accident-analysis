import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:\\Users\\Yashika malik\\Downloads\\cleaned.csv")
print(df)
print("Data loaded. Shape:", df.shape)
print(df.head())
df1=df.columns
print(df1)
# 1. Accidents by Type of Collision
plt.figure(figsize=(12, 6))
sns.countplot(
    y='Type_of_collision', data=df,
    hue='Type_of_collision', palette='Set2', legend=False,
    order=df['Type_of_collision'].value_counts().index
)
plt.title("Accidents by Type of Collision")
plt.xlabel("Number of Accidents")
plt.ylabel("Type of Collision")
plt.tight_layout()
plt.show()

#2.Accidents by Severity Level
plt.figure(figsize=(10, 6))
sns.countplot(
    x='Accident_severity', data=df,
    hue='Accident_severity', palette='Set1', legend=False,
    order=df['Accident_severity'].value_counts().index
)
plt.title("Accidents by Severity Level")
plt.xlabel("Accident Severity")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

#3.Accidents by Weather Conditions
plt.figure(figsize=(10, 6))
sns.countplot(
    y='Weather_conditions', data=df,
    hue='Weather_conditions', palette='magma', legend=False,
    order=df['Weather_conditions'].value_counts().index
)
plt.title("Accidents by Weather Conditions")
plt.xlabel("Number of Accidents")
plt.ylabel("Weather Condition")
plt.tight_layout()
plt.show()

# 4.Accidents by Road Surface Type
plt.figure(figsize=(10, 6))
sns.countplot(
    y='Road_surface_type', data=df,
    hue='Road_surface_type', palette='viridis', legend=False,
    order=df['Road_surface_type'].value_counts().index
)
plt.title("Accidents by Road Surface Type")
plt.xlabel("Number of Accidents")
plt.ylabel("Road Surface Type")
plt.tight_layout()
plt.show()

# 5.Accidents by Light Conditions
plt.figure(figsize=(10, 6))
sns.countplot(
    x='Light_conditions', data=df,
    hue='Light_conditions', palette='coolwarm', legend=False,
    order=df['Light_conditions'].value_counts().index
)
plt.title("Accidents by Light Conditions")
plt.xlabel("Light Condition")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()




