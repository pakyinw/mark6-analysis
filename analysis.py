import pandas as pd

df = pd.read_csv (r'result.csv', usecols=[0,1,2,3,4,5,6,7], names=['Date', '1st','2nd','3rd','4th','5th','6th','7th'])
print (df['1st'].append(df['2nd']).append(df['3rd']).append(df['4th']).append(df['5th']).append(df['6th']).value_counts())

