import GamezServer.RiveuServer
import GamezServer.Logger
import GamezServer.GamezServerDao
import ConfigParser
import os
import shutil

class PostProcessor(object):
    def __init__(self,conffile, gameId,dbfile):
        self.conffile = conffile
        self.gameId = gameId
        self.dbfile = dbfile
        self.logger = GamezServer.Logger.Logger(dbfile)

    def start(self,sourceFile):
        result = False
        self.RiveuNotifications()
        dao = GamezServer.GamezServerDao.GamezServerDao()
        self.logger.Log("Running Post Processing")
        dest = ""
        if(str(dao.GetGameTitle(self.dbfile, self.gameId)[1]) == 'Nintendo Wii'):
            config = ConfigParser.RawConfigParser()
            config.read(self.conffile)
            enableWiiPostProcessing = config.get('PostProcessing','EnableWiiPostProcessing').replace("'","")
            wiiPostProcessingPath = config.get('PostProcessing','WiiDestinationPath').replace("'","").replace("\\\\","\\")
            if(enableWiiPostProcessing == "1" and wiiPostProcessingPath <> ""):
                self.logger.Log("Wii Game Detected. Getting Wii Destination Path")
                dest = wiiPostProcessingPath
                dest = os.path.join(dest, str(dao.GetGameTitle(self.dbfile, self.gameId)[0]))
            else:
                return sourceFile
        if(dest <> ""):
            self.logger.Log("Moving file(s) (" + sourceFile + ") => (" + dest + ")")
            result = self.MoveFile(sourceFile, dest)
        
        if(result):    
            return dest
        else:
            return ''

    def RiveuNotifications(self):
        config = ConfigParser.RawConfigParser()
        config.read(self.conffile)
        enableRiveu = config.get('RiveuNotifications','EnableRiveuNotifications').replace("'","")
        if(str(enableRiveu) == "1"):
            riveuServer = GamezServer.RiveuServer.RiveuServer(self.dbfile)
            dao = GamezServer.GamezServerDao.GamezServerDao()
            message = dao.GetGameTitle(self.dbfile, self.gameId)
            message = str(message[0]) + " - " + str(message[1]) + " Downloaded"
            username = config.get('RiveuNotifications','Username').replace("'","")
            password = config.get('RiveuNotifications','Password').replace("'","")
            self.logger.Log('Sending Riveu Notification')
            riveuServer.SendNotification(message, username, password)

    def MoveFile(self,source,destination):
        fileCount = 0
        if not os.path.exists(destination):
            os.makedirs(destination)
        for root, dirs, filenames in os.walk(source):
            for f in filenames:
                if(str(f).endswith(".wad") or str(f).endswith(".iso") or str(f).endswith(".wbfs")):
                    self.logger.Log("File Found: " + str(f))
                    shutil.move(os.path.join(root,f), os.path.join(destination, f))
                    fileCount = fileCount + 1
        self.logger.Log("Cleaning Up Folders")
        shutil.rmtree(root)
        if(fileCount == 0):
            shutil.rmtree(destination)
            return False
        else:
            return True