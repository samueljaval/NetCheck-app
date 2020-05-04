import speedtest
import time

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
        return []
