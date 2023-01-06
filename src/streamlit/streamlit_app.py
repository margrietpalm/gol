import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from gol.game import Grid


import pyautogui


class Game:

    def __init__(self):
        self.init_ui()
        self.init_game()

    def init_ui(self):
        self.w = st.sidebar.slider('width', min_value=10, max_value=200, value=100)
        self.h = st.sidebar.slider('height', min_value=10, max_value=200, value=100)
        self.frac_alive = st.sidebar.slider('% alive', min_value=0, max_value=100,
                                            value=5)
        st.title("Conway's game of life")
        self.st_plot = st.pyplot(plt)

    def init_plot(self):
        fig, self.ax = plt.subplots()
        cmap = colors.ListedColormap(['white', 'black'])
        bounds = [0, .5, 1]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        self.ax.tick_params(axis='both', left=False, top=False, right=False, bottom=False, labelleft=False,
                            labeltop=False,
                            labelright=False, labelbottom=False)
        self.grid_plot = self.ax.imshow(np.zeros((self.grid.nrow, self.grid.ncol)), interpolation='nearest',
                                        origin='lower', cmap=cmap, norm=norm)
        self.st_plot.pyplot(plt)

    def init_game(self):
        self.grid = Grid(nrow=self.h, ncol=self.w)
        self.grid.seed(int(self.w * self.h * self.frac_alive / 100))

    def step(self, i):  # update the y values (every 1000ms)
        if i == 0:
            self.grid.reset()
        else:
            self.grid.update()
        self.grid_plot.set_data(self.grid.grid)
        self.st_plot.pyplot(plt)


if st.sidebar.button("⟳", help='restart simulation'):
    pyautogui.hotkey("ctrl", "F5")

game = Game()
game.init_plot()
i = 0

while True:
    game.step(i)
    i += 1
