from lib.html_writer import HTMLstring
import top5
import random5
import polish5

if __name__ == "__main__":
    top5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv', 'output/graphgif_top5.gif')
    top5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                      'output/graphgif_top5_col.gif', codes=True, color="col")
    top5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                      'output/graphgif_top5_gs.gif', codes=True, color="gs")

    random5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv', 'output/graphgif_random5.gif')
    random5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                         'output/graphgif_random5_col.gif', codes=True, color="col")
    random5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                         'output/graphgif_random5_gs.gif', codes=True, color="gs")

    polish5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv', 'output/graphgif_polish5.gif')
    polish5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                         'output/graphgif_polish5_col.gif', codes=True, color="col")
    polish5.create_plots('data/43dcc335-3110-4fcb-9b9f-94e318719e3c_Data.csv',
                         'output/graphgif_polish5_gs.gif', codes=True, color="gs")

    html_report = HTMLstring()
    html_report.add_text("Hello there", 1)
    html_report.add_text("Nice to meet you")
    html_report.add_text("Here, have some graphs", 2)
    html_report.add_image(filepath="./graphgif_top5.gif", alt="graph")
    html_report.add_text("It can be seen that while China maintains the largest population, "
                         "India has recently experienced the largest population growth")
    html_report.add_image(filepath="./graphgif_random5.gif", alt="graph")
    html_report.add_text("This graph is generated randomly, so there isn't much I can say about it :) "
                         "It is also possible for the country names to overlap, didn't yet find a way to "
                         "fix this behaviour.")
    html_report.add_image(filepath="./graphgif_polish5.gif", alt="graph")
    html_report.add_text("This graph still has some randomness to it, but we can see that Poland "
                         "has initially maintained a steady growth rate, which in the 21st century "
                         "reduced into a slow decline")
    html_report.save("output/report.html")
