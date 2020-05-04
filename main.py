import multiprocessing as mp
import threading
import rumps
import dialogs
from single_test import get_speeds
from overtime_test import overtime_test

# This is the class defining the Mac MenuBar item which is the main user
# interface and center of the app
class MenuBar(rumps.App):

    overtime_started = 0

    @rumps.clicked("More","Help/About")
    def help_about(self, _):
        # dialogs.help_dialog()
        pass

    @rumps.clicked("SpeedTest")
    def speedtest(self, _):
        dialogs.started_test()
        results = get_speeds()
        if results != []:
            dialogs.test_results(results)
        else :
            dialogs.no_internet()

    @rumps.clicked("Overtime Test")
    def big_test(self,_):
        overall = dialogs.get_overall()
        intervals = dialogs.get_interval()
        print(overall, intervals)
        if self.overtime_started == 0:
            overallnb = ""
            intervalsnb = ""
            for x in overall[0]:
                if x.isdigit():
                    overallnb += x
            for x in intervals[0]:
                if x.isdigit():
                    intervalsnb += x
            print(float(overallnb), float(intervalsnb))
            self.thread = threading.Thread(target = overtime_test, args=(int(overallnb), int(intervalsnb)))
            self.thread.daemon = True #thread killed when program exit, i.e app quit
            self.thread.start()
            dialogs.start_analysis()
            self.overtime_started = 1

    @rumps.clicked("Quit App")
    def quit_app(self, _):
        rumps.quit_application()

# Startup of Anti-virus File App
if __name__ == "__main__":
    app = MenuBar("SpeedTest", quit_button=None)
    app.run()
