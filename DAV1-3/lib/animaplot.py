import csv
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
from typing import Union

FIGURE_COUNTER = 1


def scale_df(df: pd.DataFrame, scale: int):
    df = df/(10**scale)
    return df


def df_closest_entries(df: pd.DataFrame, entry: Union[int, str], column: str, number: int):
    value = df[column][entry]
    dfc = df.copy()
    dfc["diff"] = abs(df[column] - value)
    entries_df = dfc.sort_values("diff", ascending=True).head(number)
    return entries_df.index


def plot_setup(df: pd.DataFrame, suptitle: str, title: str, unit: str, color):
    max_value = df.max().max()
    plt.ylim(top=max_value * 1.15)
    plt.suptitle(suptitle)
    plt.title(title)
    plt.xlabel("Countries")
    plt.ylabel(f"Population ({unit})")
    colors = list()
    if color == "def":
        colors = [(0, 0.2, 0.6, 0.8)] * 5
    if color == "col":
        colors = [(0.2 * x, 0.2, 1 - 0.2 * x, 0.8) for x in range(len(df.columns))]
    if color == "gs":
        colors = [(0.1 * x, 0.1 * x, 0.1 * x, 0.8) for x in range(len(df.columns))]
    return colors, max_value


def plot_countries_bar(df: pd.DataFrame, suptitle: str = None, title: str = None, unit="B",
                       codes: dict = None, color: str = "def"):
    if unit == "B":
        df = scale_df(df, 9)
    elif unit == "M":
        df = scale_df(df, 6)

    figsize = (5, 8)

    global FIGURE_COUNTER
    fig = plt.figure(FIGURE_COUNTER, figsize=figsize)
    FIGURE_COUNTER += 1

    colors, max_value = plot_setup(df, suptitle, title, unit, color)
    barcollection = plt.bar(df.index, df[df.columns[0]], color=colors)

    text_list = list()

    def autoyear(i, text):
        text.set_text(df.columns[i])
        return text

    def autolabels():
        nonlocal text_list
        for text in text_list:
            text.remove()
        text_list = list()
        i = 0
        for rect in barcollection:
            code = codes[df.index[i]]
            i += 1
            text = plt.text(rect.get_x() + rect.get_width() / 2., 1.05 * rect.get_height(),
                            code, ha='center', va='bottom')
            text_list.append(text)

    year_text = plt.text(4, max_value*1.05, df.columns[0], ha='center', va='bottom')

    def animate(i):
        y = df[df.columns[i]]
        nonlocal year_text
        year_text = autoyear(i, year_text)
        for j, b in enumerate(barcollection):
            b.set_height(y[j])
        if codes:
            autolabels()

    n = len(df.columns)
    anim = animation.FuncAnimation(fig, animate, repeat=True, blit=False, frames=n, interval=100)
    return anim


def plot_countries_line(df: pd.DataFrame, suptitle: str = None, title: str = None, unit="B",
                        codes: dict = None, color: str = "def"):
    if unit == "B":
        df = scale_df(df, 9)
    elif unit == "M":
        df = scale_df(df, 6)

    figsize = (5, 8)

    global FIGURE_COUNTER
    fig = plt.figure(FIGURE_COUNTER, figsize=figsize)
    FIGURE_COUNTER += 1

    colors, max_value = plot_setup(df, suptitle, title, unit, color)
    linecollection = plt.plot(df.index, df[df.columns[0]], color=colors)

    plt.show()
    # return anim


def show_plot():
    plt.show()


def save_gif(anim: animation.FuncAnimation, name: str):
    anim.save(name, writer=animation.PillowWriter(fps=8))
