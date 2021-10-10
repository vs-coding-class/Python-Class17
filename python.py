import pandas as pd
import seaborn as sb

df = pd.read_csv("savings_data_final.csv")
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)

#df = df["quant_saved"].to_list()
iqr = q3 - q1
lowerWhisker = q1 - 1.5*iqr
upperWhisker = q3 + 1.5*iqr
print(lowerWhisker, upperWhisker)

newDataFrame = [i for i in df['quant_saved'] if int(i) < upperWhisker]
