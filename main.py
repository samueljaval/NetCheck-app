import multiprocessing as mp
import threading
import rumps
import dialogs
import time
from single_test import get_speeds, truncate
from overtime_test import overtime_test

# This is the class defining the Mac MenuBar item which is the main user
# interface and center of the app

class MenuBar(rumps.App):

    overtime_started = 0
    started = 0
    overall = 0

    def time_to_hour(self,t):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))[11:]


    @rumps.clicked("More","Help/About")
    def help_about(self, _):
        # dialogs.help_dialog()
        pass

    @rumps.clicked("SpeedTest")
    def speedtest(self, _):
        dialogs.started_test()
        results = get_speeds()
        if results != ["0","0"]:
            dialogs.test_results(results)
        else :
            dialogs.no_internet()

    @rumps.clicked("Overtime Test")
    def big_test(self,sender):
        if self.overtime_started == 0 or not(self.thread.isAlive()):
            overall = dialogs.get_overall()
            intervals = dialogs.get_interval()
            print(overall, intervals)
            overallnb = ""
            intervalsnb = ""
            for x in overall[0]:
                if x.isdigit():
                    overallnb += x
            for x in intervals[0]:
                if x.isdigit():
                    intervalsnb += x
            self.overall = overallnb
            print(float(overallnb), float(intervalsnb))
            self.thread = threading.Thread(target = overtime_test, args=(int(overallnb), int(intervalsnb)))
            self.thread.daemon = True #thread killed when program exit, i.e app quit
            self.thread.start()
            self.started = time.time()
            dialogs.start_analysis()
            self.overtime_started = 1
        else :
            remaining = float(self.started) + float(self.overall)*60 - time.time()
            dialogs.show_time(truncate(remaining/60,2))


    @rumps.clicked("Quit App")
    def quit_app(self, _):
        rumps.quit_application()

# Startup of Anti-virus File App
if __name__ == "__main__":
    app = MenuBar("SpeedTest", quit_button=None)
    app.run()
