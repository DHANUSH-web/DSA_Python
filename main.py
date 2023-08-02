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
