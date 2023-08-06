import plotly.express as px

# data
dataFrame = px.data.iris()

# bar plot
setosa = dataFrame[dataFrame['species'] == 'setosa']
bar = px.scatter(data_frame=setosa, y='species', x='sepal_length', color='sepal_length', size='sepal_length', color_continuous_scale='Viridis')

bar.update_layout(plot_bgcolor='white')
bar.show()
