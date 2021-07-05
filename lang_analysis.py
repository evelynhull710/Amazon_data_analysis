import pandas as pd
import langdetect

def country(textstring):
    lang=langdetect.detect(textstring)
    print(lang)
    return lang

df = pd.read_csv("amazon_review_full_csv/test.csv")
df["Detected Language"] = df["review"].apply(country)
df.to_csv("articles_lang.csv", index=False)
print(df.to_string())