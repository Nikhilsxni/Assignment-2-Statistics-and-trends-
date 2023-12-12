"""
Created on Tue Dec 12 01:01:14 2023

@author: NIKHIL SONI
Student id: 22045846
"""
import pandas as pd
import matplotlib.pyplot as plt

# import DataFrame
df = pd.read_csv(r"C:\assignment 2 ads\electricity_prod\electricity_prod.csv")

# plotting a histogram
plt.figure(figsize=(10, 6))
for index, row in df.iterrows():
    plt.hist(row['2015'], bins=10, alpha=0.7, label=row['Country Name'])

plt.title('Electricity production from oil, gas and coal sources(2015)')
plt.xlabel('% of electricity production')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Print statistical information using pandas
stats = df['2015'].describe()
skewness = df['2015'].skew()
kurt = df['2015'].kurtosis()

print("Descriptive Statistics:")
print(stats)
print("\nSkewness:", skewness)
print("Kurtosis:", kurt)

# Add legend
plt.legend()

#show plot
plt.show()
