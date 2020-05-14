import os
import sys
import time
import csv

# checking if packages are installed

import single_test  # will check if speedtest is installed
try:
    from halo import Halo
except:
    print("\n\n\nPlease download the loading spinner package : pip install halo")
    print("or go to https://github.com/manrajgrover/halo \n\n\n")
    print("THE PROGRAM WON'T RUN WITHOUT THIS PACKAGE!")
try:
    import matplotlib.pyplot as plt
except:
    print("\n\n\nPlease download the matplotlib package : pip install matplotlib")
    print("or go to https://matplotlib.org/downloads.html \n\n\n")

# csv files containing raw data
def make_csv(d, u, t, unit):
    if not(os.path.isdir("raw-data")):
        os.mkdir("raw-data")
    units = ["Mbit/s" for i in range(len(t))]
    with open('raw-data/download_speeds.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(t, d, units))
    with open('raw-data/upload_speeds.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(t, u, units))

# making plots with matplotlib
def make_plots(d, u, t):
        if not(os.path.isdir("result-graphs")):
            os.mkdir("result-graphs")
        if d != [] :
            plt.figure()
            plt.plot(t,d)
            plt.title("Results of Download speed analysis (in Mbit/s)",loc='center')
            plt.xticks(rotation='vertical')
            plt.ylabel('download speed in Mbit/s')
            plt.tight_layout()
            plt.savefig('result-graphs/download_speeds.png')
        if u != []:
            plt.figure()
            plt.plot(t,u)
            plt.title("Results of Upload speed analysis (in Mbit/s)",loc='center')
            plt.xticks(rotation='vertical')
            plt.ylabel('upload speed in Mbit/s')
            plt.tight_layout()
            plt.savefig('result-graphs/upload_speeds.png')

# this function is defined just to have the Halo spinner as a decorator
@Halo(text='waiting until next test', spinner='dots')
def wait(t):
    time.sleep(t)

# main function
def overtime_test(overall, intervals):
    start = time.time()       # immutable
    get_time = time.time()    # mutable
    datetimes = []
    downloads_lst = []
    uploads_lst = []
    i = 0                     # just to count number of tests
    while get_time - start < overall*60:
        before = time.time()
        # chosen timestamp for a single test is right before the test rather than right after
        # just a matter of preference
        datetimes.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(before)))[5:])
        print(datetimes[-1], " --- starting speedtest n°", i)
        # the GetSpeed class is defined in the single_test.py file
        # GetSpeed uses the speedtest-cli package
        get_speed = single_test.GetSpeeds()
        st = [get_speed.get_down(), get_speed.get_up()]
        print("Results of test n°", i, " : Download = ", st[0], "Mbits/s ---- Upload = ", st[1], "Mbits/s\n")
        downloads_lst.append(float(st[0]))
        uploads_lst.append(float(st[1]))
        after = time.time()
        wait(intervals*60 - (after - before))
        get_time = time.time()
        i += 1
    try:
        make_plots(downloads_lst, uploads_lst, datetimes)
    except:
        print("\n\nCould not make the plots because the matplotlib package is not installed\n\n")
    try:
        make_csv(downloads_lst, uploads_lst, datetimes, "Mbit/s")
    except:
        print("\n\nCould not create the csv files\n\n")

    print("\n\n\n\n\nYou now have the graphs of your analysis in the result-graphs directory\n")
    print("You also have raw data in the csv files in the raw-data directory\n\n\n")


if __name__ == "__main__":
    overall = input("For how long do you want to run this overtime speedtest? (answer in minutes) :  ")
    interval = input("Give a time interval (in minutes) to run a speedtest :  ")
    try :
        if float(overall) > float(interval) and float(interval) >= 1:
            overtime_test(float(overall), float(interval))
        else :
            print("your interval has to be greater than 1 minute and overall time has to be greater than interval")
    except :
        print("something went wrong")
