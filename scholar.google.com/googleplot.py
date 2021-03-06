#!/usr/bin/env python
import os
import sys
import json
import csv
import traceback
import matplotlib.pylab as plt

print('Google scholar plotting')

# directories which store json output data
directiories = [
    # 'data-backups[2018-02-17]',
    # 'data-backups[2018-02-23]',
    # 'data-backups[2018-02-27]',
    # 'data-backups[all]'
]

try:

    #define plot size in inches (width, height) & resolution(DPI)
    fig = plt.figure(figsize=(18, 8), dpi=100)

    years = list(range(1920, 2018))
    handles = []
    for directory in directiories:
        for fn in os.listdir(directory):
            json_data = json.load(open(directory + '/' + fn))
            result_data = []
            for year in years:
                result_data.append(json_data['results'][str(year)])

            # naming lines in legends
            basename = fn.split('.')[0]
            datetime = '[' + json_data['datetime'] + ']'
            label =  datetime + '  ' + basename

            line, = plt.plot(years, result_data, label=label)
            handles.append(line)

    plt.legend(handles=handles) # comment out if you don't want legends

    ticks = list(range(min(years), max(years)+1, 5))
    print('Ticks', ticks)
    plt.xticks(ticks)

    # set plotting limit of x and y axis
    # set one value in tuple for only limiting min-x or min-y value
    # plt.xlim( (2010, 2016) )
    # plt.ylim( (2000000) )

    plt.tight_layout()
    # plt.savefig('googlescholar_plot.png')
    plt.show()

except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Unexpected error:", exc_type)
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
