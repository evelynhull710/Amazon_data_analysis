# Importing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
%matplotlib inline 
sns.set(color_codes=True)
df = pd.read_csv("Downloads/articles_prods - articles_prods (3).csv")
# Dropping irrelevant columns
df = df.drop(['label'], axis=1)
df = df.rename(columns={"generalrating":"average_rating","commentrating":"comments"})
df.head(5)
sns.boxplot(x=df['stars'])
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df = df[~((df < (Q1-1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape
# Plotting a Histogram
df.stars.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of stars by article')
plt.ylabel('count')
plt.xlabel('stars');
# Finding the relations between the variables. doesnt work
# plt.figure(figsize=(20,10))
# c= df.corr()
# sns.heatmap(c,cmap="BrB",annot=True)
# c

# Plotting a scatter plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['comments'], df['stars'])
ax.set_xlabel('comments')
ax.set_ylabel('stars')
plt.show()