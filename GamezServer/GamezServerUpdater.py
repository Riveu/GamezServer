import Constants
import GamezServer.Logger
import urllib
import json
from distutils.version import LooseVersion
import tarfile
import shutil
import os
import urllib2

class GamezServerUpdater(object):
    """description of class"""

    def __init__(self,logFile):
        self.logfile = logFile

    def CheckForNewVersion(self):
        logger = GamezServer.Logger.Logger(self.logfile)
        logger.Log("Checking for an updated version")
        currentVersion = Constants.VersionNumber()
        logger.Log("Current Version: " + str(currentVersion))
        mostRecentVersion = self.GetLatestVersion()
        logger.Log("Most Recent Version: " + str(mostRecentVersion))
        newVersionAvailable = False
        if(LooseVersion(mostRecentVersion) > LooseVersion(currentVersion)):
            logger.Log("New Version Available")
            newVersionAvailable = True
        return newVersionAvailable

    def GetLatestVersion(self):
        mostRecentVersion = "0.0.0.0"
        url = "https://api.github.com/repos/Riveu/GamezServer/tags"
        opener = urllib.FancyURLopener({})
        responseObject = opener.open(url)
        response = responseObject.read()
        responseObject.close()
        jsonObject = json.loads(response)
        for val in jsonObject:
            name = val['name']
            tagVersion = name.replace("v","").replace("'","")
            tagVersion = str(tagVersion)
            try:
                if(LooseVersion(tagVersion) > LooseVersion(mostRecentVersion)):
                    mostRecentVersion = tagVersion
            except:
                continue
        return mostRecentVersion

    def Update(self,appPath):
        logger = GamezServer.Logger.Logger(self.logfile)
        logger.Log("Updating to latest version")
        filesToIgnore = ["Gamez.ini","Gamez.db"]
        filesToIgnoreSet     = set(filesToIgnore)
        updatePath = os.path.join(appPath,"update")
        if not os.path.exists(updatePath):     
            os.makedirs(updatePath)
        latestVersion = self.GetLatestVersion()
        tagUrl = "https://github.com/Riveu/GamezServer/tarball/v" + latestVersion
        logger.Log("Downloading from GitHub")
        data = urllib2.urlopen(tagUrl)
        downloadPath = os.path.join(appPath,data.geturl().split('/')[-1])
        downloadedFile = open(downloadPath,'wb')
        downloadedFile.write(data.read())
        downloadedFile.close()
        logger.Log("Extracting Files")
        tarredFile = tarfile.open(downloadPath)
        tarredFile.extractall(updatePath)
        tarredFile.close()
        os.remove(downloadPath)
        logger.Log("Upgrading Files")
        contentsDir = [x for x in os.listdir(updatePath) if os.path.isdir(os.path.join(updatePath, x))]
        updatedFilesPath = os.path.join(updatePath,contentsDir[0])
        for dirname, dirnames, filenames in os.walk(updatedFilesPath):
            dirname = dirname[len(updatedFilesPath)+1:]
            for file in filenames:
                src = os.path.join(updatedFilesPath,dirname,file)
                dest = os.path.join(appPath,dirname,file)
                if((file in filesToIgnoreSet) == True):
                    continue
                if(os.path.isfile(dest)):
                    os.remove(dest)
                os.renames(src,dest)
        logger.Log("Upgrading Complete")
        return "Successfully Upgraded to Version " + latestVersion