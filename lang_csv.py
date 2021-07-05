# Importing required libraries.
import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
import langdetect
%matplotlib inline 
sns.set(color_codes=True)

def country(textstring):
    lang=''
    try:
        lang=langdetect.detect(textstring)
        return lang
    except:
        print("not valid string: "+textstring)
    finally:
        if not lang:
            return ""
    

df = pd.read_csv("amazon_review_full_csv/train.csv")
df["Detected Language"] = df["review"].apply(country)
df.to_csv("articles_lang_train.csv", index=False)
df = pd.read_csv("articles_lang_train.csv")
# Dropping irrelevant columns
df = df.drop(['index','title'], axis=1)
df.head(5)