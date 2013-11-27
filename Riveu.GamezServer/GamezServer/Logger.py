import GamezServerDao

class Logger(object):
    logFile = ""

    def __init__(self, _logFile):
        self.logFile = _logFile

    def Log(self, message):
        print(message)
        dao = GamezServerDao.GamezServerDao()
        dao.Log(self.logFile,message)

    def ClearLog(self):
        dao = GamezServerDao.GamezServerDao()
        dao.ClearLog(self.logFile)