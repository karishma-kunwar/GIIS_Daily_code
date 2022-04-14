import plotly
fig = go.Figure()
for column in df_col:
   
    fig.add_trace(
        go.Pie(
            values=df_col[column],
            labels= df1['Age_distribution'],
            domain=dict(x=[0.1, 1.0]),
            
            name=column
        )
    )
    

fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [
             dict(label = 'sindhupalanchowk',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,False,False,False,False,False,True]},
                          {'title': '',
                           'showlegend':True}]),
             dict(label = 'Sindhuli',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,False,False,False,False,True,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Rasuwa',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,False,False,False,True,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Ramechhap',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,False,False,True,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Nuwakot',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,False,True,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Makwanpur',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,False,True,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
              dict(label = 'Lalitpur',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,False,True,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Kavrepalanchowk',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,False,True,False,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
              dict(label = 'Kathmandu',
                  method = 'update',
                  args = [{'visible': [False, False, False,False,True,False,False,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Dolakha',
                  method = 'update',
                  args = [{'visible': [False, False, False,True,False,False,False,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Dhading',
                  method = 'update',
                  args = [{'visible': [False, False, True,False,False,False,False,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             dict(label = 'Chitwan',
                  method = 'update',
                  args = [{'visible': [False, True, False,False,False,False,False,False,False,False,False,False,False]},
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
      
             dict(label = 'Bhaktapur',
                  method = 'update',
                  args = [{'visible': [True, False, False,False,False,False,False,False,False,False,False,False,False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Age Distribution',
                           'showlegend':True}]),
             
             
             
             
             
            ]),

            direction="down",
            pad={"t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"

            
         
         
         
            )
    ])

fig.show()
plotly.offline.plot(fig,"newfile.html")

################################################################################3

# Another optimized code

fig = go.Figure()
addAll = True
for column in df_11.columns.to_list():
      fig.add_trace(
                go.Pie(
                values=df_11[column],
                labels= df_12['Age_distribution'],
                domain=dict(x=[0.1, 1.0]),
                
                name=column
                )
            )
button_all = dict(label = 'All',
                        method = 'update',                  
                        args = [{'visible': df_11.columns.isin(df_11.columns),
                                 'title': 'All',
                                  'showlegend':True}])
def create_layout_button(column):
  return dict(label = column,
              method = 'update',
              args = [{'visible': df_11.isin([column]),
                       'title': column,
                       'showlegend': True}])
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active = 0,
        buttons = ([button_all] * addAll) + list(df_11.columns.map(lambda column: create_layout_button(column)))
                )
            ])
#fig.show()
