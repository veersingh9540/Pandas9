import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
  res = {}
  max= 0
  result = []
  for i in range(len(orders)):
    c_number = orders['customer_number'][i]
    if c_number not in res:
      res[c_number] = 0
    res[c_number] +=1
    if res[c_number] > max:
      max = res[c_number]

  for key, value in res.items():
    if value == max:
      result.append([key])

  print(result)

  return pd.DataFrame(result, columns= ['customer_number'])


#   DF= orders.groupby(['customer_number']).size().reset_index(name = "count")
#   DF.sort_values(['count'], ascending = False, inplace= True)

#   return pd.DataFrame(DF['customer_number'][0:1])