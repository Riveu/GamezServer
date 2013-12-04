import urllib2
import urllib
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
                dao.AddConsole(self.dbfile, console.replace("\r",""))
        return

    def UpdateGames(self):
        logger = Logger.Logger(self.dbfile)
        logger.Log('Downloading Games List')
        url = 'http://www.riveu.com/GamezServer/devgames.txt'
        webFile = urllib2.urlopen(url).read()
        dao = GamezServerDao.GamezServerDao()
        for game in webFile.split('\n'):
            if(len(game) > 0):
                gameAttributes = game.split('::||::')
                gameId = gameAttributes[0].decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                gameTitle = str(gameAttributes[1]).decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                gameDescription = str(gameAttributes[2]).decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                releaseDate = str(gameAttributes[3]).decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                coverArt = str(gameAttributes[4]).decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                console = str(gameAttributes[5]).decode("utf-8").replace(u'\ufeff','').replace(u'\xa0',' ').replace(u'\xb7','').replace(u'\xb2','').replace(u'\u2161','').replace(u'\u2164','')
                dao.AddGame(self.dbfile, gameId, gameTitle, gameDescription, releaseDate, coverArt, console.replace("\r",""))
        return

    def SendNotification(self, message, username, password):
        data = "CMD=SEND_NOTIFICATION&Username=" + username + "&Password=" + password + "&Message=" + urllib.quote_plus(message)
        url = 'http://riveu.com/API.aspx?' + data
        responseObject = urllib.FancyURLopener({}).open(url)
        responseObject.read()
        responseObject.close()