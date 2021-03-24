import os
import sys
import time
import csv
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

# checking if packages are installed

try:  
    from halo import Halo
except:
    str1 = "Please download the loading spinner package : pip install halo\n\n"
    str2 = "or go to https://github.com/manrajgrover/halo \n\n"
    messagebox.showerror("Error", str1 + str2)
    quit()
try: 
    import speedtest
except:
    str1 = "Please download the speedtest-cli package : pip install speedtest-cli\n\n"
    str2 = "or go to https://github.com/sivel/speedtest-cli \n\n"
    messagebox.showerror("Error", str1 + str2)
    quit()
try:
    import matplotlib.pyplot as plt
except:
    str1 = "Please download the matplotlib package : pip install matplotlib\n\n"
    str2 = "or go to https://matplotlib.org/downloads.html \n\n"
    messagebox.showerror("Error", str1 + str2)
    quit()

import single_test  # will check if speedtest is installed

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
        print("\n\nCould not make the plots.\n\n")
    try:
        make_csv(downloads_lst, uploads_lst, datetimes, "Mbit/s")
    except:
        print("\n\nCould not create the csv files.\n\n")

    print("\n\n\n\n\nYou now have the graphs of your analysis in the result-graphs directory\n")
    print("You also have raw data in the csv files in the raw-data directory\n\n\n")


if __name__ == "__main__":
    overall = simpledialog.askinteger("value in minutes!", "For how long do you want to run this overtime speedtest? (answer in minutes)",
                                 parent=root,
                                 minvalue=1)
    interval = simpledialog.askinteger("value in minutes!", "Give a time interval (in minutes) to run a speedtest :  ",
                                 parent=root,
                                 maxvalue=overall, minvalue=1)
    if type(overall) == int and type(interval) == int:
        messagebox.showinfo(
        "Overtime SpeedTest just started!",
        "Check your terminal to see how it's going.\n\nWhen it's finished, you can look at the results with the .csv and .png files that we created in the project directory."
        )
        overtime_test(float(overall), float(interval))
        messagebox.showinfo(
        "Overtime SpeedTest just finished!",
        "Done!\n\nYou now have the graphs of your analysis in the result-graphs directory.\nYou also have raw data in the csv files in the raw-data directory"
        )
    else :
        messagebox.showerror("Error", "Oops, something went wrong")
        quit()

