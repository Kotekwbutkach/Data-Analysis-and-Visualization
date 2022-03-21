import csv
import numpy as np
import pandas as pd


def empty_string(string):
    values_to_check = {"", ".."}
    return True if string in values_to_check else False


def csv_read_countries_pop(filename: str, skip=0, cut_ends=0, lines: int = None):

    def read_line():
        row = next(reader, None)
        if row is None:
            return False
        name = row[2]
        if empty_string(name):
            return False
        names.append(name)
        codes[name] = row[3]
        value = [row[n]for n in range(4, len(row)-cut_ends)]
        value = [int(value[n]) if not empty_string(value[n]) else np.NaN for n in range(len(value))]
        values.append(value)
        return True

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        columns = list()
        values = list()
        names = list()
        codes = dict()
        for i in range(skip):
            next(reader, None)
        row = next(reader, None)
        for j in range(4, len(row)-cut_ends):
            columns.append(row[j][:4])
        if lines is None:
            while read_line():
                pass
        else:
            for i in range(lines):
                read_line()
        df = pd.DataFrame(values, columns=columns, index=names)
    return df, codes
# the default setup for unfiltered data for is skip=4, namepos=0, cutends=1
