import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()

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


class GetSpeeds:

    def __init__(self):
        try:
            self.s = speedtest.Speedtest()
            self.s.get_servers()
            self.s.get_best_server()
        except:
            print("No detected connection!\n\n")
            print("If you are connected to the internet, this could be a SLL certificate error!\n")
            print("Please make sure you run the 'Install Certificates.command' file located in your python directory\n")
            print("check this link for more details :")
            print("https://stackoverflow.com/questions/56326644/python-speedtest-facing-problems-with-certification-ssl-c1056\n\n")

    def truncate(self,f,decimals):
        s = str(f)
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

# used for testing
if __name__ == "__main__":
    print("starting speedtest...\n")
    gs = GetSpeeds()
    print("Donwload : ",gs.get_down(), "Mbits/s\n")
    print("Upload : ",gs.get_up(), "Mbits/s\n")
