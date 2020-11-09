import numpy as np
import plotly.graph_objects as go
from matplotlib import cm
import matplotlib

categories = 10 
theta = [i * 360 / categories for i in range(categories)]
theta = [theta[i] + 36 for i in range(categories)]
print(theta)
width = [360 / categories for _ in range(categories)]

num_scales = 5 
color_scale = np.linspace(0,1,num_scales, endpoint=True)
print(color_scale)
r = [1, 2, 3, 1, 3, 2, 2, 3, 3, 3]
r = np.asarray(r)
color_scale = r / num_scales
viridis = cm.get_cmap('plasma', 12)
marker_color = [matplotlib.colors.to_hex(viridis(color_scale[i])) for i in range(categories)]

title = dict(text="Wheel of Life")

# radial_axis = dict(range=(0,5), showticklabels=False, ticks='')
# angular_axis = dict(showticklabels=False, ticks='')
labels = ['Contribution', 'Growth', 'Love & Romance',
          'Fun & Joy', 'Family & Friends', 'Money',
          'Career', 'Mental Health', 'Environment',
          'Physical Health']

tickfont = dict(
      family = 'Old Standard TT, serif',
      size = 16,
      color = 'black'
      )

fig = go.Figure(go.Barpolar(
    r=r,
    theta=theta,
    width=width,
    hovertext=labels,
    marker_color=marker_color,
    marker_line_color="black",
    marker_line_width=2,
    opacity=1
))

fig.update_layout(
    template=None,
    title=title,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks='', showgrid=True, showline=False),
        angularaxis = dict(showticklabels=True, dtick = 36, ticks='', tickvals=theta, 
                           ticktext=labels, showgrid=True, tickfont=tickfont, showline=False)
    )
)

fig.show()