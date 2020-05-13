import os
import sys
import speedtest
import time
import single_test
try:
    from halo import Halo
except:
    print("\n\nPlease download the loading spinner package : pip install halo")
    print("or go to https://github.com/manrajgrover/halo \n\n")
try:
    import matplotlib.pyplot as plt
except:
    print("\n\nPlease download the matplotlib package : pip install matplotlib")
    print("or go to https://matplotlib.org/downloads.html \n\n")


def make_plots(d, u, t):
    try:
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
    except :
        print("could not create graphs because the matplotlib package is not installed")

@Halo(text='waiting until next test', spinner='dots')
def wait(t):
    time.sleep(t)

def overtime_test(overall, intervals):
    start = time.time()
    get_time = time.time()
    datetimes = []
    downloads_lst = []
    uploads_lst = []
    i = 0
    while get_time - start < overall*60:
        before = time.time()
        # chosen timestamp for a single test is right before the test rather than right after
        datetimes.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(before)))[5:])
        print(datetimes[-1], " --- starting speedtest n°", i)
        get_speed = single_test.GetSpeeds()
        st = [get_speed.get_down(), get_speed.get_up()]
        print("Results of test n°", i, " : Download = ", st[0], "Mbits/s ---- Upload = ", st[1], "Mbits/s\n")
        downloads_lst.append(float(st[0]))
        uploads_lst.append(float(st[1]))
        after = time.time()
        wait(intervals*60 - (after - before))
        get_time = time.time()
        i += 1
    make_plots(downloads_lst, uploads_lst, datetimes)
    try:
        os.system("open result-graphs/download_speeds.png result-graphs/upload_speeds.png")
    except:
        print("could not open graphs")

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
