import time
import psutil

def monitor():
    old_value = 0
    i = 0
    lst = []
    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        print(new_value/1000/1000/1000)
        if old_value: #anything but 0
            lst.append(new_value - old_value)
            if i == 1:
                send_stat(new_value - old_value, "the last 30 min")
            if i == 2:
                send_stat(new_value - old_value, "the last hour")
            if i == 4:
                send_stat(new_value - old_value, "the last 2hours")
            if i == 48:
                send_stat(new_value - old_value, "the last 25 hours")

        old_value = new_value


        time.sleep(1)

def convert_to_gbit(value):
    return value/1024./1024./1024.*8

def send_stat(value,s):
    print (s + "%0.3f" % convert_to_gbit(value))

if __name__ == "__main__":
    monitor()
