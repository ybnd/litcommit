# Python Windows services: adapted from
#       http://www.chrisumbel.com/article/windows_services_in_python

import win32service
import win32serviceutil
import win32event
import win32process


def log(text):
    with open("D:\\Box Sync\\Literature\\_mgmt\\litcommit.log", 'a+') as f:
        f.write(text)

class litcommit(win32serviceutil.ServiceFramework):
    # you can NET START/STOP the service by the following name
    _svc_name_ = "litcommit"
    # this text shows up as the service name in the Service
    # Control Manager (SCM)
    _svc_display_name_ = "litcommit"
    # this text shows up as the description in the SCM
    _svc_description_ = "Periodically commits changes to the literature repository"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # create an event to listen for stop requests on
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        """
        Core logic of the service
        :return:
        """
        import servicemanager
        import subprocess
        from datetime import datetime, timedelta
        import copy
        import yaml

        rc = None
        log('\n\n>>>>')
        _committed_ = []

        now = datetime.now()

        # if the stop event hasn't been fired keep looping
        while rc != win32event.WAIT_OBJECT_0:
            with open('D:\Box Sync\Literature\_mgmt\config.yaml', 'r') as f:
                _cfg_ = yaml.load(f.read())

                _ltime_ = [
					datetime.strptime(t, '%H:%M') - timedelta(minutes = _cfg_['time-delta']) for t in _cfg_['time']
				]
                _utime_ = [
					datetime.strptime(t, '%H:%M') + timedelta(minutes=_cfg_['time-delta']) for t in _cfg_['time']
				]

            then = copy.copy(now)
            now = datetime.now()
            _ts_ = now.strftime('%Y/%m/%d %H:%M')

            log('\n\t' + _ts_)

            if any([lt.time() < now.time() < ut.time() for lt,ut in zip(_ltime_, _utime_)]) and \
                    len(_committed_) < len(_cfg_):
                subprocess.call(['py', 'D:\\Box Sync\\Literature\\_mgmt\\commit_changes.py'])

            if now.day != then.day:
                _committed_ = []

            # block for 20 minutes and listen for a stop event
            rc = win32event.WaitForSingleObject(self.hWaitStop, 60*1000*_cfg_['interval'])

        # called when we're being shut down
    def SvcStop(self):
        """
        Called when we're being shut down
        :return:
        """
        # tell the SCM we're shutting down
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # fire the stop event
        win32event.SetEvent(self.hWaitStop)
        log('\n<<<<\n')

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(litcommit)