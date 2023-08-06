<<<<<<< HEAD
import plotly.express as px

# data
dataFrame = px.data.iris()

# bar plot
setosa = dataFrame[dataFrame['species'] == 'setosa']
bar = px.scatter(data_frame=setosa, y='species', x='sepal_length', color='sepal_length', size='sepal_length', color_continuous_scale='Viridis')

bar.update_layout(plot_bgcolor='white')
bar.show()
=======
"""
Developer: Dhanush H V
"""

import numpy as np
import pandas as pd
import plotly.express as px

x = np.arange(0, 200)
y = np.random.randint(0, 100, 200)

df = pd.DataFrame(dict(x=x, y=y))
fig = px.line(df, x='x', y='y')
fig.show()
>>>>>>> c5eefd43d7380afbb98a3f2d75b402618492c9ae
