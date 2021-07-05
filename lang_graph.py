# Importing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
%matplotlib inline 
sns.set(color_codes=True)
# df = pd.read_csv("articles_lang_train.csv")
df = pd.read_csv("articles_lang_prods.csv")
df['Detected Language'].value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of languages by review')
plt.ylabel('review')
plt.xlabel('Detected Language');