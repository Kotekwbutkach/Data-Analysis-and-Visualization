import random
from lib.input import csv_read_countries_pop
from lib.animaplot import df_closest_entries, plot_countries_bar, show_plot, save_gif


def create_plots(data_path: str, output_path: str, show=False, codes=False, color: str = "def"):
    df, country_codes = csv_read_countries_pop(data_path)
    df.sort_values(df.columns[-1], ascending=False, inplace=True)
    rcol = random.randrange(0, len(df.columns))
    df1 = df.loc[df_closest_entries(df, "Poland", df.columns[rcol], 5)]
    suptitle = f"Population in years {df.columns[0]}-{df.columns[-1]}"
    title = f"5 countries with Poland as centroid for year {df.columns[rcol]}"

    country_codes = country_codes if codes else None
    anim = plot_countries_bar(df1, suptitle=suptitle, title=title, unit="M", codes=country_codes,
                              color=color)
    save_gif(anim, output_path)
    if show:
        show_plot()
    return anim


if __name__ == '__main__':
    anim_plot = create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                            'output/graphgif_polish5.gif', show=True)
