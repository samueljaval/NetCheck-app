import os
import pync
import rumps
from single_test import truncate

def test_results(results):
    # pync.notify("Donwload Speed : " + results[0] + " Mbits/s \nUpload Speed : " + results[1] + " Mbits/s", title="Speedtest Results")
    res = "Download Speed : " + results[0] + " Mbits/s\n Upload Speed : " + results[1] + " Mbits/s"
    down = "\n 1GB of data will be downloaded in " + truncate( (8000/float(results[0])) / 60 , 2) + " minutes"
    ups = "\n 1GB of data will be uploaded in " + truncate( (8000/float(results[1])) / 60 , 2) + " minutes"
    explain = "\n Check out the Help section if you do not understand the units"
    os.system("""osascript -e 'display dialog  " """+res + "\n" + down + ups + "\n" + explain + """ " buttons {"OK"} default button "OK" with title "SpeedTest Results"
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
