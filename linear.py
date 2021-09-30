import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv("data.csv")

height=df["Height"].tolist()
weight=df["Weight"].tolist()

m = 0.95
c = -93
y = []

for x in height:
  y_value = m*x + c
  y.append(y_value)

x=250

y=m*x +c
print(f"Weight of someone with height {x} is {y}")

height_array = np.array(height)
weight_array = np.array(weight)

m, c = np.polyfit(height_array, weight_array, 1)

y = []
for x in height_array:
  y_value = m*x + c
  y.append(y_value)

fig = px.scatter(x=height_array, y=weight_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(height_array), x1= max(height_array)
    )
])
fig.show()