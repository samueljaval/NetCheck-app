import os
import pync
import rumps
from single_test import truncate

def test_results(results):
    resdown = "Download Speed : " + results[0] + " Mbits/s"
    resup = "Upload Speed : " + results[1] + " Mbits/s"
    #explain = "\nIf you do not understand the units, click the Help/About button for a little crash course"
    if results[0] != "0":
        show = resdown + "\n" + " 1GB of data will be downloaded in " + truncate( (8000/float(results[0])) / 60 , 2) + " minutes"
    if results[1] != "0":
        try:
            show += "\n" + resup + "\n" + " 1GB of data will be uploaded in " + truncate( (8000/float(results[1])) / 60 , 2) + " minutes"
        except:
            show = resup + "\n" + " 1GB of data will be uploaded in " + truncate( (8000/float(results[1])) / 60 , 2) + " minutes" + "\n"
    os.system("""osascript -e 'display dialog  " """+ show + """ " buttons {"OK"} default button "OK" with title "SpeedTest Results"
    '""")

def started_test():
    pync.notify("Started Test", title="Speedtest")

def no_internet():
    pync.notify("You are not connected to the internet", title="Speedtest")

def get_overall():
    result = os.popen("""osascript -e 'display dialog "How long?" default answer "Enter the number your want (in minutes)" with title "Set Overtime Analysis"' """).readlines()
    return result

def get_interval():
    result = os.popen("""osascript -e 'display dialog "Intervals" default answer "Enter the number your want (in minutes)" with title "Set Overtime Analysis"' """).readlines()
    return result

def start_analysis():
    pync.notify("The speed analysis has started", title="Speedtest")

def show_time(remaining):
    pync.notify("The remaining time is " + str(remaining) + " min", title="Speedtest")

def not_started():
    pync.notify("You have not started the overtime test", title="Speedtest")
