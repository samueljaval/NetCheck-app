import speedtest
import time
import urllib.request
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
def get_speeds(hidedownload, hideupload):
    try:
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        results = []
        if hidedownload == 0:
            results.append(truncate(s.download()/1000/1000,2)) # Mbit/s
        else :
            results.append("0")
        if hideupload == 0:
            results.append(truncate(s.upload()/1000/1000,2)) # Mbit/s
        else :
            results.append("0")
        return results
    except:
        return ["0","0"]


if __name__ == "__main__":
    print(get_speeds(0,1))
