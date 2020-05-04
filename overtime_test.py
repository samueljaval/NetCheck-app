from single_test import get_speeds
import time
import os
import matplotlib.pyplot as plt

def get_input():
    return 10, 1

def make_plots(d, u, t):
    if d != [] :
        plt.figure()
        plt.plot(t,d)
        plt.title("Results of Download speed analysis (in Mbit/s)",loc='center')
        plt.xticks(rotation='vertical')
        plt.ylabel('download speed in Mbit/s')
        plt.tight_layout()
        plt.savefig('download_speeds.png')
    if u != []:
        plt.figure()
        plt.plot(t,u)
        plt.title("Results of Upload speed analysis (in Mbit/s)",loc='center')
        plt.xticks(rotation='vertical')
        plt.ylabel('upload speed in Mbit/s')
        plt.tight_layout()
        plt.savefig('upload_speeds.png')

def overtime_test(overall, intervals):
    start = time.time()
    get_time = time.time()
    datetimes = []
    downloads_lst = []
    uploads_lst = []
    try :
        while get_time - start < overall*60:
            before = time.time()
            # chosen timestamp for a single test is right before the test rather than right after
            datetimes.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(before)))[5:])
            print("ee")
            print(datetimes[-1])
            st = get_speeds()
            downloads_lst.append(float(st[0]))
            uploads_lst.append(float(st[1]))
            after = time.time()
            time.sleep(intervals*60 - (after - before))
            get_time = time.time()
            make_plots(downloads_lst, uploads_lst, datetimes)
            os.system("open download_speeds.png upload_speeds.png")
    except :
        print("not a number")
