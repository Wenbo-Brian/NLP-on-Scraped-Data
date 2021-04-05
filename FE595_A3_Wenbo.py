import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_excel('/Users/yuwenbo/Desktop/3rd semester/FE595/Assignment/Assignment3/company_Daniel.xlsx')
with open('/Users/yuwenbo/Desktop/3rd semester/FE595/Assignment/Assignment3/company_Lantian.txt', "r") as f:
    data1 = f.read()
with open('/Users/yuwenbo/Desktop/3rd semester/FE595/Assignment/Assignment3/company_Wenbo.txt', 'r') as f:
    data2 = f.read()

columns = ['Name', 'Purpose']
df1 = pd.DataFrame(columns = [columns[0]])
df2 = pd.DataFrame(columns = [columns[1]])
    
df.columns = ['Name', 'Purpose']
data2 = re.sub("Purpose:", "\nPurpose:", data2)
pattern = re.compile(r"Name:\s*(.*?)\s*\n+Purpose:\s*(.*?)\s*\n")
result1 = pattern.findall(data1)
result2 = pattern.findall(data2)
    
for i in range(0,50):
    df1 = df1.append({'Name': list(result1[i])[0]}, ignore_index=True).append({'Name': list(result2[i])[0]}, ignore_index=True)
    df2 = df2.append({'Purpose': list(result1[i])[1]}, ignore_index=True).append({'Purpose': list(result2[i])[1]}, ignore_index=True)

df_temp = pd.concat([df1, df2], axis=1)
df = pd.concat([df, df_temp], axis=0, ignore_index=True)

nlp_lg = spacy.load("en_core_web_lg")
analyser = SentimentIntensityAnalyzer()

df['neg'] = df['Purpose'].apply(lambda x:analyser.polarity_scores(x)['neg'])
df['neu'] = df['Purpose'].apply(lambda x:analyser.polarity_scores(x)['neu'])
df['pos'] = df['Purpose'].apply(lambda x:analyser.polarity_scores(x)['pos'])
df['compound'] = df['Purpose'].apply(lambda x:analyser.polarity_scores(x)['compound'])

df.to_csv('/Users/yuwenbo/Desktop/3rd semester/FE595/Assignment/Assignment3/data_Wenbo.csv')
