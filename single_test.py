import speedtest
try:
    from halo import Halo
except:
    print("\n\nPlease download the loading spinner package : pip install halo")
    print("or go to https://github.com/manrajgrover/halo \n\n")

#fix speedtest library
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class GetSpeeds:

    def __init__(self):
        try:
            self.s = speedtest.Speedtest()
            self.s.get_servers()
            self.s.get_best_server()
        except:
            print("No detected connection")

    def truncate(self,f,decimals):
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

    @Halo(text='getting download speed', spinner='dots')
    def get_down(self):
        try:
            return self.truncate(self.s.download()/1000/1000,2) # Mbit/s
        except:
            return "0"

    @Halo(text='getting upload speed', spinner='dots')
    def get_up(self):
        try:
            return self.truncate(self.s.upload()/1000/1000,2) # Mbit/s
        except:
            return "0"


if __name__ == "__main__":
    print("starting speedtest...\n")
    gs = GetSpeeds()
    print("Donwload : ",gs.get_down(), "Mbits/s\n")
    print("Upload : ",gs.get_up(), "Mbits/s\n")
