import os
import sys
import speedtest
import time
try:
    import urllib.request
except:
    print("You need the urllib package")
try:
    import matplotlib.pyplot as plt
except:
    print("You need the matplotlib package")


# fix speedtest library
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def truncate(f,decimals):
    s = str(f)
    res = ""
    decimals_bool = 0
    i = 0
    while i < len(s):
        if decimals_bool == 1:
            return s[:i+decimals]
        if s[i] == ".":
            decimals_bool = 1
        i+=1

# the arguments are boolans
# returns a type list
def get_speeds():
    try:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        results = []
        results.append(truncate(s.download()/1000/1000,2)) # Mbit/s
        results.append(truncate(s.upload()/1000/1000,2)) # Mbit/s
        return results
    except:
        return ["0","0"]


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
    i = 0
    try:
        while get_time - start < overall*60:
            before = time.time()
            # chosen timestamp for a single test is right before the test rather than right after
            datetimes.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(before)))[5:])
            print(datetimes[-1], " --- starting speedtest n°", i)
            st = get_speeds()
            print("Results of test n°", counter, " : Download = ", st[0], "Mbits/s ---- Upload = ", st[1], "Mbits/s")
            downloads_lst.append(float(st[0]))
            uploads_lst.append(float(st[1]))
            after = time.time()
            time.sleep(intervals*60 - (after - before))
            get_time = time.time()
            i += 1
        make_plots(downloads_lst, uploads_lst, datetimes)
        os.system("open download_speeds.png upload_speeds.png")
    except :
         print("not a number")

if __name__ == "__main__":
    overall = input("For how long do you want to run this overtime speedtest? (answer in minutes) :  ")
    interval = input("Give a time interval (in minutes) to run a speedtest :  ")
    overtime_test(float(overall), float(interval))
