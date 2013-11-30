import sqlite3
from time import gmtime, strftime

class GamezServerDao(object):

    def InitializeDB(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = '''CREATE TABLE GAMES(GameID INTEGER PRIMARY KEY NOT NULL, MasterGameID INT NOT NULL, Status TEXT Not Null, Location TEXT NULL, IsDeleted INT Not Null Default 0);'''
        conn.execute(comm)
        comm = '''CREATE TABLE MASTER_GAMES(MasterGameID INTEGER PRIMARY KEY NOT NULL, GameDevID TEXT NOT NULL UNIQUE, GameTitle TEXT Not Null, GameDescription TEXT NULL, ConsoleID INT NOT NULL, ReleaseDate DATETIME NULL, CoverArtUri TEXT NULL, IsDeleted INT Not Null Default 0);'''
        conn.execute(comm)
        comm = '''CREATE TABLE CONSOLES(ConsoleID INTEGER PRIMARY KEY NOT NULL, ConsoleName TEXT Not Null UNIQUE, IsDeleted INT Not Null Default 0);'''
        conn.execute(comm)
        comm = '''CREATE TABLE LOG(LogID INTEGER PRIMARY KEY NOT NULL, Message TEXT Not Null, MessageTimeStamp DATETIME NOT NULL, IsDeleted INT Not Null Default 0);'''
        conn.execute(comm)
        conn.close()

    def GetGames(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "select CoverArtUri,GameTitle,GameDevID,GameDescription,ConsoleName,ReleaseDate,Status,Location,GameID from games inner join MASTER_GAMES INNER JOIN CONSOLES ON GAMES.MasterGameID=MASTER_GAMES.MasterGameID AND MASTER_GAMES.ConsoleID = CONSOLES.ConsoleID WHERE GAMES.IsDeleted=0 AND MASTER_GAMES.IsDeleted=0 AND CONSOLES.IsDeleted=0"
        result = conn.execute(comm).fetchall()
        conn.close()
        return result

    def GetWantedGames(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "select CoverArtUri,GameTitle,GameDevID,GameDescription,ConsoleName,ReleaseDate,Status,Location,GameID from games inner join MASTER_GAMES INNER JOIN CONSOLES ON GAMES.MasterGameID=MASTER_GAMES.MasterGameID AND MASTER_GAMES.ConsoleID = CONSOLES.ConsoleID WHERE GAMES.IsDeleted=0 AND MASTER_GAMES.IsDeleted=0 AND CONSOLES.IsDeleted=0 AND GAMES.Status='Wanted'"
        result = conn.execute(comm).fetchall()
        conn.close()
        return result

    def UpdateGameStatus(self, dbFile, gameId,status):
        conn = sqlite3.connect(dbFile)
        comm = "UPDATE GAMES SET Status='" + str(status) + "' WHERE GameID=" + str(gameId) + " AND IsDeleted=0"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return

    def DeleteGame(self, dbFile, gameId):
        conn = sqlite3.connect(dbFile)
        comm = "UPDATE GAMES SET IsDeleted=1 WHERE GameID=" + str(gameId) + " AND IsDeleted=0"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return

    def UpdateGameLocation(self, dbFile, gameId,location):
        conn = sqlite3.connect(dbFile)
        comm = "UPDATE GAMES SET Location='" + str(location) + "' WHERE GameID=" + str(gameId) + " AND IsDeleted=0"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return

    def GetMasterGames(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "SELECT GameDevID,GameTitle,GameDescription,ConsoleName,ReleaseDate,CoverArtUri FROM MASTER_GAMES INNER JOIN CONSOLES ON (MASTER_GAMES.ConsoleID = CONSOLES.ConsoleID) AND MASTER_GAMES.IsDeleted=0 AND CONSOLES.IsDeleted=0 ORDER BY GameTitle ASC"
        result = conn.execute(comm).fetchall()
        conn.close()
        return result

    def Log(self, dbFile, message):
        conn = sqlite3.connect(dbFile)
        comm = "INSERT OR IGNORE INTO LOG(Message,MessageTimeStamp) VALUES(?,?)"
        try:
            conn.execute(comm, (message,strftime("%Y-%m-%d %H:%M:%S", gmtime())))
            conn.commit()
        except:
            print('Error Logging Message to DB. Most likely due to a bad string value')
        conn.close()

    def GetLogMessages(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "SELECT Message,MessageTimeStamp FROM LOG WHERE IsDeleted=0 ORDER BY LogID DESC"
        result = conn.execute(comm).fetchall()
        conn.close()
        return result

    def ClearLog(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "UPDATE LOG SET IsDeleted=1 WHERE IsDeleted=0"
        conn.execute(comm)
        conn.commit()
        conn.close()

    def AddConsole(self, dbFile, console):
        conn = sqlite3.connect(dbFile)
        comm = "INSERT OR IGNORE INTO CONSOLES(ConsoleName) VALUES('" + console.replace("'","''") + "');"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return

    def AddGame(self, dbFile, gameId = None, gameTitle=None, gameDescription=None, releaseDate=None, coverArtUri=None, console=None):
        conn = sqlite3.connect(dbFile)
        comm = "INSERT OR IGNORE INTO MASTER_GAMES(GameDevID,GameTitle,GameDescription,ConsoleID,ReleaseDate,CoverArtUri) VALUES('" + gameId + "','" + gameTitle.replace("'","''") + "','" + gameDescription.replace("'","''") + "',(SELECT ConsoleID FROM CONSOLES WHERE ConsoleName='" + console.replace("'","''") + "' AND IsDeleted=0),'" + releaseDate + "','" + coverArtUri + "');"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return

    def GetConsoles(self, dbFile):
        conn = sqlite3.connect(dbFile)
        comm = "SELECT ConsoleName FROM CONSOLES WHERE IsDeleted=0"
        result = conn.execute(comm).fetchall()
        conn.close()
        return result

    def AddWantedGame(self, dbFile, console, gameTitle):
        conn = sqlite3.connect(dbFile)
        comm = "INSERT INTO GAMES (MasterGameID,Status) VALUES((SELECT MasterGameID FROM MASTER_GAMES WHERE GameTitle='" + str(gameTitle) + "' AND ConsoleID=(SELECT ConsoleID FROM CONSOLES WHERE ConsoleName='" + str(console) + "' AND IsDeleted=0) AND IsDeleted=0),'Wanted')"
        conn.execute(comm)
        conn.commit()
        conn.close()
        return