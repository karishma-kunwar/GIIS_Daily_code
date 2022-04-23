import plotly.graph_objects as go

fig = go.Figure()

for column in new_file1.columns.to_list():
  fig.add_trace(go.Bar(
      y=read_new_file['Year'],
      x=new_file1[column],
    
      text = new_file1[column],
      
          name=column,
          orientation='h',
          width = 0.2
          
      ))
  
  fig.update_layout(barmode='stack',margin=dict(l=20, r=20, t=10, b=20),xaxis={'categoryorder':'total descending'}, title={ 'text': "Gender Wise distribution of Nepalgunj registered voters",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},paper_bgcolor='rgba(255,255,255,255)',
      plot_bgcolor='rgba(255,255,255,255)')
  
  fig.update_layout(legend=dict(
    yanchor="bottom",
    y=0.0,
    xanchor="right",
    x=1.0
))

  

  fig.update_xaxes(showticklabels=False,showgrid = False)


  fig.update_yaxes(tickvals = read_new_file['Year'] ,showgrid= False)


fig.show()