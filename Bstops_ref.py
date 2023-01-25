import pandas as pd

df = pd.read_csv("Bstop.csv")
new_ref_id = []
counter = 1
for ref_id in range(len(df)):
    new_ref_id.append(counter)
    counter+=1

df['ref_id'] = range(1, len(df) + 1)

  

df.to_csv("Bstop_ref_id.csv", index=False)
  
print(df)