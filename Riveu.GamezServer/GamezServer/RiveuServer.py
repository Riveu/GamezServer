import urllib2
import GamezServerDao
import Logger

class RiveuServer(object):


    def __init__(self, dbFile):
        self.dbfile = dbFile

    def UpdateConsoles(self):
        logger = Logger.Logger(self.dbfile)
        logger.Log('Downloading Console List')
        url = 'http://www.riveu.com/GamezServer/consoles.txt'
        webFile = urllib2.urlopen(url).read()
        dao = GamezServerDao.GamezServerDao()
        for console in webFile.split('\n'):
            if(len(console) > 0):
                logger.Log('Adding Console: ' + console)
                dao.AddConsole(self.dbfile, console.replace("\r",""))
        return

    def UpdateGames(self):
        logger = Logger.Logger(self.dbfile)
        logger.Log('Downloading Games List')
        url = 'http://www.riveu.com/GamezServer/games.txt'
        webFile = urllib2.urlopen(url).read()
        dao = GamezServerDao.GamezServerDao()
        for game in webFile.split('\n'):
            if(len(game) > 0):
                gameAttributes = game.split('::||::')
                gameId = gameAttributes[0]
                gameTitle = gameAttributes[1]
                gameDescription = gameAttributes[2]
                releaseDate = gameAttributes[3]
                coverArt = gameAttributes[4]
                console = gameAttributes[5]
                logger.Log('Adding Game: ' + gameTitle + " - " + console)
                dao.AddGame(self.dbfile, gameId, gameTitle, gameDescription, releaseDate, coverArt, console.replace("\r",""))
        return