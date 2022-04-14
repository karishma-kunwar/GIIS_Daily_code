import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots 
import plotly
from plotly.offline import plot

fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

fig.add_trace(go.Pie(
    values=df_age['Male Count'],
    labels=df_age['District'],
    domain=dict(x=[0.3, 0.5]),
    name=''),
    row=1, col=1)

fig.add_trace(go.Pie(
    values=df_age['Female Count'],
    labels= df_age['District'],
    domain=dict(x=[0.8, 1.0]),
    name=''),
    row=1, col=2)
  


fig.layout.update(
   updatemenus = [
      go.layout.Updatemenu(
         type = "buttons", direction = "left", buttons=list(
            [
               dict(args = ["type", "pie"], label = "Pie", method = "restyle"),
               dict(args = ["type", "bar"], label = "Bar", method = "restyle")
            ]
         ),
         pad = {"r": 1, "t": 2},
         showactive = True,
         x = 0,
         xanchor = "left",
         y = 1.1,
         yanchor = "top"
      ), 
   ]
)

fig.show()
# fig = px.pie(df, values="21-40", names="District")
plotly.offline.plot(fig,"new_3.html")