from lib.html_writer import HTMLstring
from lib.input import csv_read_countries_pop
import top5
import random5
import polish5

if __name__ == "__main__":
    df, country_codes = csv_read_countries_pop('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv')
    top5.create_plots(df, country_codes, 'output/graphgif_top5.gif')
    top5.create_plots(df, country_codes, 'output/graphgif_top5_col.gif', codes=True, color="col")
    top5.create_plots(df, country_codes, 'output/graphgif_top5_gs.gif', codes=True, color="gs")

    random5.create_plots(df, country_codes, 'output/graphgif_random5.gif')
    random5.create_plots(df, country_codes, 'output/graphgif_random5_col.gif', codes=True, color="col")
    random5.create_plots(df, country_codes, 'output/graphgif_random5_gs.gif', codes=True, color="gs")

    polish5.create_plots(df, country_codes, 'output/graphgif_polish5.gif')
    polish5.create_plots(df, country_codes, 'output/graphgif_polish5_col.gif', codes=True, color="col")
    polish5.create_plots(df, country_codes, 'output/graphgif_polish5_gs.gif', codes=True, color="gs")

    html_report = HTMLstring()
    html_report.add_text("Hello there", 1)
    html_report.add_text("Nice to meet you")
    html_report.add_text("More graphs incoming", 2)
    html_report.add_image(filepath="./graphgif_top5.gif", alt="graph", start=True)
    html_report.add_image(filepath="./graphgif_top5_col.gif", alt="graph", end=True)
    html_report.add_image(filepath="./graphgif_top5_gs.gif", alt="graph", start=True, end=True)
    html_report.add_text("It can be seen that while China maintains the largest population, "
                         "India has recently experienced the largest population growth. "
                         "Representation is now available in color as well as greyscale.")

    html_report.add_image(filepath="./graphgif_random5.gif", alt="graph", start=True)
    html_report.add_image(filepath="./graphgif_random5_col.gif", alt="graph", end=True)
    html_report.add_image(filepath="./graphgif_random5_gs.gif", alt="graph", start=True, end=True)
    html_report.add_text("These graphs are generated randomly, so there isn't much I can say about it :) "
                         "The size has been tweaked to avoid country names overlap, but due to randomness "
                         "such behaviour might still be possible.")

    html_report.add_image(filepath="./graphgif_polish5.gif", alt="graph", start=True)
    html_report.add_image(filepath="./graphgif_polish5_col.gif", alt="graph", end=True)
    html_report.add_image(filepath="./graphgif_polish5_gs.gif", alt="graph", start=True, end=True)
    html_report.add_text("These graphs still have some randomness to them, but we can see that Poland "
                         "has initially maintained a steady growth rate, which in the 21st century "
                         "reduced into a slow decline")

    html_report.save("output/report.html")
