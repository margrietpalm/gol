import time
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation
import streamlit.components.v1 as components

from gol.core.game import Grid

# Set up model

def simulate(num, grid, grid_plot):  # update the y values (every 1000ms)
    grid.update()
    grid_plot.set_data(grid.grid)
    return grid_plot,


# Set up plot
fig, ax = plt.subplots()
cmap = colors.ListedColormap(['white', 'black'])
bounds = [0, .5, 1]
norm = colors.BoundaryNorm(bounds, cmap.N)
ax.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False, labeltop=False,
               labelright=False, labelbottom=False)
grid_plot = ax.imshow(grid.grid, interpolation='nearest', origin='lower', cmap=cmap, norm=norm)


grid_ani = animation.FuncAnimation(fig, simulate, 25, fargs=(grid, grid_plot),
                                    interval=50, blit=True)

# Set up UI

# w = st.sidebar.number_input(width, min_value=10, max_value=200, value=100)
# h = st.sidebar.number_input(height, min_value=10, max_value=200, value=100)
grid = Grid(nrow=100, ncol=100)
grid.seed(500)

st.title("Conway's game of life")
components.html(grid_ani.to_jshtml(), height=1000)
# st_plot = st.pyplot(plt)

# def init():  # give a clean slate to start
#     grid_plot.set_data(grid.grid)
#
# def simulate(i):  # update the y values (every 1000ms)
#     grid.update()
#     grid_plot.set_data(grid.grid)
#     st_plot.pyplot(plt)
#
# init()
#
# start_button = st.button('start/stop')
# started = False
#
# if start_button:
#     print(started)
#     if not started:
#         started = True
#         i = 0
#         while True:
#             simulate(i)
#             i += 1
#     else:
#         started = False


# run_button = st.button('▶')
# if run_button:
#     run()
# # st.button('⏯', on_click=update_grid)
# # st.button('⏹', on_click=st.stop)