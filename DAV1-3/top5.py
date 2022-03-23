from lib.input import csv_read_countries_pop
from lib.animaplot import plot_countries_bar, plot_countries_line, show_plot, save_gif


def create_plots(df, country_codes, output_path: str, show=False, codes=False,
                 color: str = "def", plot_type="bar"):
    df.sort_values(df.columns[-1], ascending=False, inplace=True)
    df1 = df.head(5)
    suptitle = f"Population in years {df.columns[0]}-{df.columns[-1]}"
    title = f"5 countries with the largest population in year 2020"
    country_codes = country_codes if codes else None
    if plot_type == "bar":
        anim = plot_countries_bar(df1, suptitle=suptitle, title=title, unit="B", codes=country_codes, color=color)
    else:
        anim = plot_countries_line(df1, suptitle=suptitle, title=title, unit="B", codes=country_codes, color=color)
    save_gif(anim, output_path)
    if show:
        show_plot()
    return anim


if __name__ == '__main__':
    df, country_codes = csv_read_countries_pop('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv')
    anim_plot = create_plots(df, country_codes, 'output/graphgif_top5.gif', show=True, codes=False, plot_type="line")
    anim_plot2 = create_plots(df, country_codes, 'output/graphgif_top5_col.gif', show=True, codes=True, color="col")
    anim_plot3 = create_plots(df, country_codes, 'output/graphgif_top5_gs.gif', show=True, codes=True, color="gs")
