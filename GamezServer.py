import cherrypy
import os
import ConfigParser
import GamezServer.GamezServerDao
import GamezServer.RiveuServer
import GamezServer.PostProcessor
import GamezServer.Logger
import GamezServer.GameSearcher
import sys
from GamezServer import Constants
from cherrypy.process.plugins import Monitor
from GamezServer import GamezServerUpdater
import thread

class RunWebServer(object):

    def __init__(self):
        cherrypy.engine.subscribe('start', self.start)
        cherrypy.engine.subscribe('stop', self.stop)

    @cherrypy.expose
    def index(self,redirect=None):
        updater = GamezServerUpdater.GamezServerUpdater(dbfile)
        gamesList = dao.GetGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Home</title>"
        content = content + "       <link rel=\"shortcut icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link rel=\"icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/demo_table_jui.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery.dataTables.js\" type=\"text/javascript\"></script>"
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form method=\"post\" action=\"https://www.paypal.com/cgi-bin/webscr\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr width=\"100%\"><td width=\"100%\"><table width=\"100%\"><tr width=\"100%\"><td width=\"80px\"><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td><td><div style=\"float:right;\"><input type=\"hidden\" name=\"cmd\" value=\"_s-xclick\"><input type=\"hidden\" name=\"hosted_button_id\" value=\"SPK7EYG47DHZ4\"><input type=\"image\" src=\"https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif\" border=\"0\" name=\"submit\" alt=\"Donate\"><img alt=\"\" border=\"0\" src=\"https://www.paypalobjects.com/en_US/i/scr/pixel.gif\" width=\"1\" height=\"1\"></div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li><li class='last'><a href='http://www.riveu.com/support.aspx' target='_blank'><span>Support</span></a></li><div style=\"text-align:right;padding: 15px 20px;color: #ffffff;text-shadow: 0 -1px 1px #5c2800;font-size: 14px;font-family: Helvetica;\">Version: " + str(version) + "</div></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <table id=\"logGrid\" width=\"100%\" class=\"display\"><thead><tr><th>Cover</th><th>Game Title</th><th>Game ID</th><th>Game Description</th><th>Console</th><th>Release Date</th><th>Status</th><th>Location</th><th>Commands</th></tr></thead><tbody>"
        for row in gamesList:
            try:
                gameId = str(row[8])
                statusValue = str(row[6])
                statusDropDown = "<select onchange=\"window.location = '/updatestatus?game_id=" + gameId + "&filePath=&status=' + this.value;\"><option value=\"Downloaded\">Downloaded</option><option value=\"Snatched\">Snatched</option><option value=\"Wanted\" selected>Wanted</option></select>"
                if(statusValue == 'Snatched'):
                    statusDropDown = "<select onchange=\"window.location = '/updatestatus?game_id=" + gameId + "&filePath=&status=' + this.value;\"><option value=\"Downloaded\">Downloaded</option><option value=\"Snatched\" selected>Snatched</option><option value=\"Wanted\">Wanted</option></select>"
                if(statusValue == 'Downloaded'):
                    statusDropDown = "<select onchange=\"window.location = '/updatestatus?game_id=" + gameId + "&filePath=&status=' + this.value;\"><option value=\"Downloaded\" selected>Downloaded</option><option value=\"Snatched\">Snatched</option><option value=\"Wanted\">Wanted</option></select>"
                content = content + "                       <tr><td><image  onError=\"this.onerror=null;this.src='images/noCoverArt.gif';\" style=\"width:125px;height:200px\" src=\"" + str(row[0]) + "\" alt=\"Cover Image\" /></td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5]) + "</td><td>" + statusDropDown + "</td><td>" + str(row[7]) + "</td><td><a href=\"/deletegame?game_id=" + gameId + "\">Delete</a></td></tr>"
            except:
                logger.Log("Unable to show game because there is unicode error in description: " + str(row[1]))
        content = content + "                       </tbody></table>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {$('#logGrid').dataTable({\"bJQueryUI\": true, \"sPaginationType\": \"full_numbers\"});});</script>"
        content = content + "       <div id=\"statusmessage\" style=\"position:fixed;bottom:0;padding:0 5px;line-height:25px;background-color:#eeee99;margin-bottom:-25px;font-weight:bold;left:0;right:0;\"></div>"
        content = content + "       <div id=\"versionstatusmessage\" style=\"position:fixed;bottom:0;padding:0 5px;line-height:25px;background-color:#eeee99;margin-bottom:-25px;font-weight:bold;left:0;right:0;\"><label>A new version of GamezServer is available</label>&nbsp;&nbsp;&nbsp;<button onclick=\"window.location='/updategamezserver';return false;\">Upgrade Now</button></div>"
        if(updater.CheckForNewVersion()):
             content = content + "<script>$('#versionstatusmessage').animate({'margin-bottom':0},200);setTimeout( function(){$('#versionstatusmessage').animate({'margin-bottom':-25},200);}, 500*1000);</script>"
        if(redirect=='gameadded'):
            content = content + "<script>$('#statusmessage').text('Game Added to Wanted List...').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        if(redirect=='gamedeleted'):
            content = content + "<script>$('#statusmessage').text('Game Deleted From Wanted List...').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        if(redirect=='statusupdated'):
            content = content + "<script>$('#statusmessage').text('Gamed Status Updated...').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        if(str(redirect).find("Successfully Upgraded to Version") <> -1):
           content = content + "<script>$('#statusmessage').text('" + str(redirect) + "').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def updategamezserver(self):
        updater = GamezServerUpdater.GamezServerUpdater(dbfile)
        updateResult = updater.Update(app_path)
        raise cherrypy.HTTPRedirect("/?redirect=" + updateResult)
        return

    @cherrypy.expose
    def mastergames(self):
        gamesList = dao.GetMasterGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Master Games</title>"
        content = content + "       <link rel=\"shortcut icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link rel=\"icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/demo_table_jui.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery.dataTables.js\" type=\"text/javascript\"></script>"
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form action=\"/clearlog\" method=\"post\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr><td><table><tr><td><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li><li class='last'><a href='http://www.riveu.com/support.aspx' target='_blank'><span>Support</span></a></li><div style=\"text-align:right;padding: 15px 20px;color: #ffffff;text-shadow: 0 -1px 1px #5c2800;font-size: 14px;font-family: Helvetica;\">Version: " + str(version) + "</div></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <table id=\"gamesGrid\" width=\"100%\" class=\"display\"><thead><tr><th>Cover</th><th>Game Title</th><th>Game ID</th><th>Game Description</th><th>Release Date</th><th>Console</th></tr></thead><tbody>"
        for row in gamesList:
            try:
                dateValue = str(row[4])
                if(dateValue == '//'):
                    dateValue = 'Unkown'
                content = content + "                       <tr><td><img src=\"" + str(row[5]) + "\" onError=\"this.onerror=null;this.src='images/noCoverArt.gif';\" style=\"width:125px;height:200px\" /></td><td>" + str(row[1]) + "</td><td>" + str(row[0]) + "</td><td>" + str(row[2]) + "</td><td>" + dateValue + "</td><td>" + str(row[3]) + "</td></tr>"
            except:
                logger.Log("Unable to show game because there is unicode error in description: " + str(row[1]))
        content = content + "                       </tbody></table>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {$('#gamesGrid').dataTable({\"bJQueryUI\": true, \"sPaginationType\": \"full_numbers\"});});</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def addgame(self):
        gamelist = dao.GetMasterGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Add Game</title>"
        content = content + "       <link rel=\"shortcut icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link rel=\"icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/modernizr-2.0.6.min.js\" type=\"text/javascript\"></script> "
        content = content + "       <script src=\"js/jquery.horizontalNav.js\" type=\"text/javascript\"></script> "
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form action=\"processAddGame\" method=\"post\" onsubmit=\"return CheckValidation();\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr><td><table><tr><td><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li><li class='last'><a href='http://www.riveu.com/support.aspx' target='_blank'><span>Support</span></a></li><div style=\"text-align:right;padding: 15px 20px;color: #ffffff;text-shadow: 0 -1px 1px #5c2800;font-size: 14px;font-family: Helvetica;\">Version: " + str(version) + "</div></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <div id=\"addgame-tabs\"><ul><li><a href=\"#addgame-tab\">Add Game</a></li></ul>"
        content = content + "                           <div id=\"addgame-tab\">"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Game Information</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <div class=\"ui-widget\"><table style=\"width:100%\"><tr style=\"width:100%\"><td style=\"width:100px\"><label for=\"game\">Game: </label></td><td style=\"width:95%\"><input name=\"game\" id=\"game\" style=\"width:60%;margin-left:20px\"></td></tr>"
        content = content + "                                       <tr><td style=\"width:100%;text-align:right;padding:15px\" colspan=\"2\"><button id=\"saveSettingsButton\" type=\"submit\">Add Game</button></td></tr></table></div>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                       </div>"    
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "<script>"
        content = content + "var availableGames = ["
        for row in gamelist:
            content = content + '"' + str(row[1]).replace("\r","") + " - " + str(row[3]) + '",'
        content = content + "];"

        content = content + "function CheckValidation(){var gameVal = availableGames.indexOf(document.getElementById('game').value);if(gameVal == -1){alert('Please Enter A Valid Game');return false;}else{return true;}}</script>"
        content = content + "       <script>$(function() {"
        content = content + "       $( \"#addgame-tabs\" ).tabs();$(\"#saveSettingsButton\").button();$(\"#game\").autocomplete({source: availableGames});});</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def processAddGame(self,game=None):
        consolelist = dao.GetConsoles(dbfile)
        console = ""
        for row in consolelist:
            if(str(game).find(str(row[0])) <> -1):
                console = str(row[0])
        if(console <> ""):
            game = str(game).replace(" - " + console, "")
            dao.AddWantedGame(dbfile,console,game)
            thread.start_new_thread(RunGameSearch, ())
        raise cherrypy.HTTPRedirect("/?redirect=gameadded")

    def stop(self):
        logger.Log("Shutting Down Web Server")

    def start(self):
        logger.Log("Web Server Started")

    @cherrypy.expose
    def log(self,redirect=None):
        logResult = dao.GetLogMessages(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Log</title>"
        content = content + "       <link rel=\"shortcut icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link rel=\"icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/demo_table_jui.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery.dataTables.js\" type=\"text/javascript\"></script>"
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form action=\"/clearlog\" method=\"post\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr><td><table><tr><td><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li><li class='last'><a href='http://www.riveu.com/support.aspx' target='_blank'><span>Support</span></a></li><div style=\"text-align:right;padding: 15px 20px;color: #ffffff;text-shadow: 0 -1px 1px #5c2800;font-size: 14px;font-family: Helvetica;\">Version: " + str(version) + "</div></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <table id=\"logGrid\" width=\"100%\" class=\"display\"><thead><tr><th>Date/Time</th><th>Message</th></tr></thead><tbody>"
        for row in logResult:
            content = content + "                       <tr><td width=\"250px\">" + str(row[1]) + "</td><td>" + str(row[0]) + "</td></tr>"
        content = content + "                       </tbody></table>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "               <tr>"
        content = content + "                   </td>"
        content = content + "                   <td colspan=\"2\" style=\"text-align:right;padding:15px\">"
        content = content + "                       <button id=\"clearLogButton\" type=\"submit\">Clear Log</button>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {$(\"#clearLogButton\").button();$('#logGrid').dataTable({\"bJQueryUI\": true, \"sPaginationType\": \"full_numbers\"});});</script>"
        content = content + "       <div id=\"statusmessage\" style=\"position:fixed;bottom:0;padding:0 5px;line-height:25px;background-color:#eeee99;margin-bottom:-25px;font-weight:bold;left:0;right:0;\"></div>"
        if(redirect=='logcleared'):
            content = content + "<script>$('#statusmessage').text('Log Cleared..').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def settings(self,redirect=None):
        config = ConfigParser.RawConfigParser()
        config.read(conffile)
        enableAuthChecked = ""
        enableUsenetCrawlerChecked = ""
        enableSabnzbdChecked = ""
        enableRiveuNotificationsChecked = ""
        enableWiiPostProcessingChecked = ""
        enablePS3PostProcessingChecked = ""
        enableXBOX360PostProcessingChecked = ""

        if(config.get('GamezServer','EnableAuth') == "1"):
            enableAuthChecked = "checked"
        if(config.get('UsenetCrawler','EnableUsenetCrawler') == "1"):
            enableUsenetCrawlerChecked = "checked"
        if(config.get('Sabnzbd','EnableSabnzbd') == "1"):
            enableSabnzbdChecked = "checked"
        if(config.get('RiveuNotifications','EnableRiveuNotifications') == "1"):
            enableRiveuNotificationsChecked = "checked"
        if(config.get('PostProcessing','EnableWiiPostProcessing') == "1"):
            enableWiiPostProcessingChecked = "checked"
        if(config.get('PostProcessing','EnablePS3PostProcessing') == "1"):
            enablePS3PostProcessingChecked = "checked"
        if(config.get('PostProcessing','EnableXBOX360PostProcessing') == "1"):
            enableXBOX360PostProcessingChecked = "checked"

        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Settings</title>"
        content = content + "       <link rel=\"shortcut icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link rel=\"icon\" href=\"/images/favicon.ico\" type=\"image/x-icon\">"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/modernizr-2.0.6.min.js\" type=\"text/javascript\"></script> "
        content = content + "       <script src=\"js/jquery.horizontalNav.js\" type=\"text/javascript\"></script> "
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form action=\"saveSettings\" method=\"post\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr><td><table><tr><td><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li><li class='last'><a href='http://www.riveu.com/support.aspx' target='_blank'><span>Support</span></a></li><div style=\"text-align:right;padding: 15px 20px;color: #ffffff;text-shadow: 0 -1px 1px #5c2800;font-size: 14px;font-family: Helvetica;\">Version: " + str(version) + "</div></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <div id=\"settings-tabs\"><ul><li><a href=\"#general-tab\">General</a></li><li><a href=\"#downloaders-tab\">Downloaders</a></li><li><a href=\"#searchers-tab\">Search Providers</a></li><li><a href=\"#notifications-tab\">Notifications</a></li><li><a href=\"#postprocessing-tab\">Post Processing</a></li></ul>"
        content = content + "                           <div id=\"general-tab\">"
        content = content + "                               <h4>General Settings</h4>"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Gamez Web Server</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr style=\"width:100%\"><td style=\"width:1o%\"><label>Host:</label></td><td style=\"width:90%\"><input name=\"host\" value=\"" + config.get('global','server.socket_host').replace("'","") + "\" type=\"text\" style=\"width:75%\"></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Port:</label></td><td><input name=\"port\" value=\"" + config.get('global','server.socket_port') + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Enable Authentication:</label></td><td><input name=\"enableAuth\" " + enableAuthChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Username:</label></td><td><input name=\"authUsername\" value=\"" + config.get('GamezServer','AuthUsername').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Password:</label></td><td><input name=\"authPassword\" value=\"" + config.get('GamezServer','AuthPassword').replace("'","") + "\" type=\"password\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                           <div id=\"downloaders-tab\">"
        content = content + "                               <h4>Downloaders</h4>"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Sabnzbd+</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enableSabnzbd\" " + enableSabnzbdChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Sabnzbd+ URL:</label></td><td><input name=\"sabnzbdUrl\" value=\"" + config.get('Sabnzbd','SabnzbdHostUrl').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>API Key:</label></td><td><input name=\"sabnzbdApiKey\" value=\"" + config.get('Sabnzbd','SabnzbdApiKey').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Category</label></td><td><input name=\"sabnzbdCategory\" value=\"" + config.get('Sabnzbd','SabnzbdCategory').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                           <div id=\"searchers-tab\">"
        content = content + "                               <h4>Search Providers</h4>"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Usenet-Crawler</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enableUsenetCrawler\" " + enableUsenetCrawlerChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>API Key:</label></td><td><input name=\"usenetCrawlerApi\" value=\"" + config.get('UsenetCrawler','UsenetCrawlerApiKey').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                           <div id=\"notifications-tab\">" 
        content = content + "                               <h4>Notifications</h4>"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Riveu</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enableRiveuNotifications\" " + enableRiveuNotificationsChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Username:</label></td><td><input name=\"riveuNotificationsUsername\" value=\"" + config.get('RiveuNotifications','Username').replace("'","") + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Password:</label></td><td><input name=\"riveuNotificationsPassword\" value=\"" + config.get('RiveuNotifications','Password').replace("'","") + "\" type=\"password\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                           <div id=\"postprocessing-tab\">" 
        content = content + "                               <h4>Post Processing</h4>"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Microsoft XBOX 360</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enableXBOX360PostProcessing\" " + enableXBOX360PostProcessingChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Destination Path:</label></td><td><input name=\"xbox360DestinationPath\" value=\"" + config.get('PostProcessing','XBOX360DestinationPath').replace("'","").replace('\\\\','\\') + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                               <br />"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Nintendo Wii</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enableWiiPostProcessing\" " + enableWiiPostProcessingChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Destination Path:</label></td><td><input name=\"wiiDestinationPath\" value=\"" + config.get('PostProcessing','WiiDestinationPath').replace("'","").replace('\\\\','\\') + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                               <br />"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Sony Playstation 3</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <table style=\"width:100%\">"
        content = content + "                                           <tr><td><div class=\"field\" style=\"width:10%\"><label>Enable</label></td><td style=\"width:90%\"><input name=\"enablePS3PostProcessing\" " + enablePS3PostProcessingChecked + " type=\"checkbox\"></div></td></tr>"
        content = content + "                                           <tr><td><div class=\"field\"><label>Destination Path:</label></td><td><input name=\"ps3DestinationPath\" value=\"" + config.get('PostProcessing','PS3DestinationPath').replace("'","").replace('\\\\','\\') + "\" type=\"text\" style=\"width:75%\"></div></td></tr>"
        content = content + "                                       </table>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                       </div>"    
        content = content + ""; 
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "               <tr>"
        content = content + "                   </td>"
        content = content + "                   <td colspan=\"2\" style=\"text-align:right;padding:15px\">"
        content = content + "                       <button id=\"saveSettingsButton\" type=\"submit\">Save Settings</button>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {$( \"#settings-tabs\" ).tabs();$(\"#saveSettingsButton\").button();});</script>"
        content = content + "       <div id=\"statusmessage\" style=\"position:fixed;bottom:0;padding:0 5px;line-height:25px;background-color:#eeee99;margin-bottom:-25px;font-weight:bold;left:0;right:0;\"></div>"
        if(redirect=='settingssaved'):
            content = content + "<script>$('#statusmessage').text('Settings Saved..').animate({'margin-bottom':0},200);setTimeout( function(){$('#statusmessage').animate({'margin-bottom':-25},200);}, 5*1000);</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def saveSettings(self,host=None,port=None,enableAuth=None,authUsername=None,authPassword=None,enableUsenetCrawler=None,usenetCrawlerApi=None,enableSabnzbd=None,sabnzbdUrl=None,sabnzbdApiKey=None,sabnzbdCategory=None,enableRiveuNotifications=None,riveuNotificationsUsername=None,riveuNotificationsPassword=None,enableWiiPostProcessing=None,wiiDestinationPath=None,enablePS3PostProcessing=None,ps3DestinationPath=None,enableXBOX360PostProcessing=None,xbox360DestinationPath=None):
        if(enableAuth == 'on'):
            enableAuth = '1'
        else:
            enableAuth = '0'

        if(enableUsenetCrawler == 'on'):
            enableUsenetCrawler = '1'
        else:
            enableUsenetCrawler = '0'

        if(enableSabnzbd == 'on'):
            enableSabnzbd = '1'
        else:
            enableSabnzbd = '0'

        if(enableRiveuNotifications == 'on'):
            enableRiveuNotifications = '1'
        else:
            enableRiveuNotifications = '0'

        if(enableWiiPostProcessing == 'on'):
            enableWiiPostProcessing = '1'
        else:
            enableWiiPostProcessing = '0'

        if(enablePS3PostProcessing == 'on'):
            enablePS3PostProcessing = '1'
        else:
            enablePS3PostProcessing = '0'

        if(enableXBOX360PostProcessing == 'on'):
            enableXBOX360PostProcessing = '1'
        else:
            enableXBOX360PostProcessing = '0'

        config = ConfigParser.RawConfigParser()
        config.add_section('global')
        config.set('global', 'server.socket_host', "'" + host + "'")
        config.set('global', 'server.socket_port', port)
        config.add_section('GamezServer')
        config.set('GamezServer', 'EnableAuth', enableAuth)
        config.set('GamezServer', 'AuthUsername', "'" + authUsername + "'")
        config.set('GamezServer', 'AuthPassword', "'" + authPassword + "'")
        config.add_section('UsenetCrawler')
        config.set('UsenetCrawler', 'EnableUsenetCrawler', enableUsenetCrawler)
        config.set('UsenetCrawler', 'UsenetCrawlerApiKey', "'" + usenetCrawlerApi + "'")
        config.add_section('Sabnzbd')
        config.set('Sabnzbd', 'EnableSabnzbd', enableSabnzbd)
        config.set('Sabnzbd', 'SabnzbdHostUrl', "'" + sabnzbdUrl + "'")
        config.set('Sabnzbd', 'SabnzbdApiKey', "'" + sabnzbdApiKey + "'")
        config.set('Sabnzbd', 'SabnzbdCategory', "'" + sabnzbdCategory + "'")
        config.add_section('RiveuNotifications')
        config.set('RiveuNotifications', 'EnableRiveuNotifications', enableRiveuNotifications)
        config.set('RiveuNotifications', 'Username', "'" + riveuNotificationsUsername + "'")
        config.set('RiveuNotifications', 'Password', "'" + riveuNotificationsPassword + "'")
        config.add_section('PostProcessing')
        config.set('PostProcessing', 'EnableWiiPostProcessing', enableWiiPostProcessing)
        config.set('PostProcessing', 'WiiDestinationPath', "'" + str(wiiDestinationPath).replace('\\','\\\\') + "'")
        config.set('PostProcessing', 'EnablePS3PostProcessing', enablePS3PostProcessing)
        config.set('PostProcessing', 'PS3DestinationPath', "'" + str(ps3DestinationPath).replace('\\','\\\\') + "'")
        config.set('PostProcessing', 'EnableXBOX360PostProcessing', enableXBOX360PostProcessing)
        config.set('PostProcessing', 'XBOX360DestinationPath', "'" + str(xbox360DestinationPath).replace('\\','\\\\') + "'")
        with open(conffile, 'wb') as configfile:
            config.write(configfile)
        raise cherrypy.HTTPRedirect("/settings?redirect=settingssaved")

    @cherrypy.expose
    def clearlog(self, logGrid_length):
        logger.ClearLog()
        raise cherrypy.HTTPRedirect("/log?redirect=logcleared")

    @cherrypy.expose
    def deletegame(self, game_id):
        dao.DeleteGame(dbfile, game_id)
        raise cherrypy.InternalRedirect('/?redirect=gamedeleted')

    @cherrypy.expose
    def updatestatus(self,game_id='',status='',filePath=''):
        logger.Log('Updating Game Status')
        dao.UpdateGameStatus(dbfile, game_id, status)
        if(status=='Downloaded'):
            postProcessor = GamezServer.PostProcessor.PostProcessor(conffile,game_id,dbfile)
            if(filePath <> ''):
                logger.Log('Calling Post Processing')
                postProcessResult = postProcessor.start(filePath)
                logger.Log('Post Processing Complete')
                if(postProcessResult <> ''):
                    filePath = postProcessResult
                else:
                    filePath = ''
                    logger.Log('Updating game status to wanted since there were no valid game files')
                    raise cherrypy.InternalRedirect('/updatestatus?game_id=' + game_id + '&status=Wanted&filePath=')
        if(status=='Wanted'):
            dao.UpdateGameLocation(dbfile, game_id, '')
            RunGameSearch()
        if(filePath <> ''):
            dao.UpdateGameLocation(dbfile, game_id, filePath)
        raise cherrypy.InternalRedirect('/?redirect=statusupdated')

def RunGameSearch():
    logger.Log('Running Game Search')
    searcher = GamezServer.GameSearcher.GameSearcher(dbfile, conffile)
    searcher.start()
    return

def RunGameDBUpdater():
    logger.Log('Updating Console List')
    riveuServer = GamezServer.RiveuServer.RiveuServer(dbfile)
    riveuServer.UpdateConsoles()
    logger.Log('Updating Games List')
    riveuServer.UpdateGames()

def GenerateSabPostProcessScript():
    config = ConfigParser.RawConfigParser()
    config.read(conffile)
    gamezWebHost = config.get('global','server.socket_host').replace("'","")
    gamezWebport = config.get('global','server.socket_port').replace("'","")
    gamezBaseUrl = "http://" + gamezWebHost + ":" + gamezWebport + "/"
    postProcessPath = os.path.join(app_path,'GamezServer')
    postProcessPath = os.path.join(postProcessPath,'postprocess')
    postProcessScript = os.path.join(postProcessPath,'gamezPostProcess.py')
    file = open(postProcessScript,'w')
    file.write('#!/usr/bin/env python')
    file.write("\n")
    file.write('import sys')
    file.write("\n")
    file.write('import urllib')
    file.write("\n")
    file.write("filePath = str(sys.argv[1])")
    file.write("\n")
    file.write('fields = str(sys.argv[3]).split("-")')
    file.write("\n")
    file.write('gamezID = fields[0].replace("[","").replace("]","").replace(" ","")')
    file.write("\n")
    file.write("status = str(sys.argv[7])")
    file.write("\n")
    file.write("downloadStatus = 'Wanted'")
    file.write("\n")
    file.write("if(status == '0'):")
    file.write("\n")
    file.write("    downloadStatus = 'Downloaded'")
    file.write("\n")
    file.write('url = "' + gamezBaseUrl + 'updatestatus?game_id=" + gamezID + "&filePath=" + urllib.quote(filePath) + "&status=" + downloadStatus')
    file.write("\n")
    file.write('responseObject = urllib.FancyURLopener({}).open(url)')
    file.write("\n")
    file.write('responseObject.read()')
    file.write("\n")
    file.write('responseObject.close()')
    file.write("\n")
    file.write('print("Processing Completed Successfully")')
    file.close
    logger.Log('Setting permissions on post process script')
    cmd = "chmod +x '" + postProcessScript + "'"
    os.system(cmd)

def CheckConfig():
    config = ConfigParser.RawConfigParser()
    config.read(conffile)
    if not config.has_section("global"):
        config.add_section('global')
        config.set('global', 'server.socket_host', "'127.0.0.1'")
        config.set('global', 'server.socket_port', '5000')
    else:
        if not config.has_option('global', 'server.socket_host'):
            config.set('global', 'server.socket_host', "'127.0.0.1'")
        if not config.has_option('global', 'server.socket_port'):
            config.set('global', 'server.socket_port', '5000')
    if not config.has_section("GamezServer"):
        config.add_section('GamezServer')
        config.set('GamezServer', 'EnableAuth', '0')
        config.set('GamezServer', 'AuthUsername', "''")
        config.set('GamezServer', 'AuthPassword', "''")
    else:
        if not config.has_option('GamezServer', 'EnableAuth'):
            config.set('GamezServer', 'EnableAuth', '0')
        if not config.has_option('GamezServer', 'AuthUsername'):
            config.set('GamezServer', 'AuthUsername', "''")
        if not config.has_option('GamezServer', 'AuthPassword'):
            config.set('GamezServer', 'AuthPassword', "''")
    if not config.has_section('UsenetCrawler'):
        config.add_section('UsenetCrawler')
        config.set('UsenetCrawler', 'EnableUsenetCrawler', "0")
        config.set('UsenetCrawler', 'UsenetCrawlerApiKey', "''")
    else:
        if not config.has_option('UsenetCrawler', 'EnableUsenetCrawler'):
            config.set('UsenetCrawler', 'EnableUsenetCrawler', '0')
        if not config.has_option('UsenetCrawler', 'UsenetCrawlerApiKey'):
            config.set('UsenetCrawler', 'UsenetCrawlerApiKey', "''")
    if not config.has_section('Sabnzbd'):
        config.add_section('Sabnzbd')
        config.set('Sabnzbd', 'EnableSabnzbd', "0")
        config.set('Sabnzbd', 'SabnzbdHostUrl', "''")
        config.set('Sabnzbd', 'SabnzbdApiKey', "''")
        config.set('Sabnzbd', 'SabnzbdCategory', "''")
    else:
        if not config.has_option('Sabnzbd', 'EnableSabnzbd'):
            config.set('Sabnzbd', 'EnableSabnzbd', '0')
        if not config.has_option('Sabnzbd', 'SabnzbdHostUrl'):
            config.set('Sabnzbd', 'SabnzbdHostUrl', "''")
        if not config.has_option('Sabnzbd', 'SabnzbdApiKey'):
            config.set('Sabnzbd', 'SabnzbdApiKey', "''")
        if not config.has_option('Sabnzbd', 'SabnzbdCategory'):
            config.set('Sabnzbd', 'SabnzbdCategory', "''")
    if not config.has_section('RiveuNotifications'):
        config.add_section('RiveuNotifications')
        config.set('RiveuNotifications', 'EnableRiveuNotifications', "0")
        config.set('RiveuNotifications', 'Username', "''")
        config.set('RiveuNotifications', 'Password', "''")
    else:
        if not config.has_option('RiveuNotifications', 'EnableRiveuNotifications'):
            config.set('RiveuNotifications', 'EnableRiveuNotifications', '0')
        if not config.has_option('RiveuNotifications', 'Username'):
            config.set('RiveuNotifications', 'Username', "''")
        if not config.has_option('RiveuNotifications', 'Password'):
            config.set('RiveuNotifications', 'Password', "''")

    if not config.has_section('PostProcessing'):
        config.add_section('PostProcessing')
        config.set('PostProcessing', 'EnableWiiPostProcessing', "0")
        config.set('PostProcessing', 'WiiDestinationPath', "''")
        config.set('PostProcessing', 'EnablePS3PostProcessing', "0")
        config.set('PostProcessing', 'PS3DestinationPath', "''")
    else:
        if not config.has_option('PostProcessing', 'EnableWiiPostProcessing'):
            config.set('PostProcessing', 'EnableWiiPostProcessing', '0')
        if not config.has_option('PostProcessing', 'WiiDestinationPath'):
            config.set('PostProcessing', 'WiiDestinationPath', "''")
        if not config.has_option('PostProcessing', 'EnablePS3PostProcessing'):
            config.set('PostProcessing', 'EnablePS3PostProcessing', '0')
        if not config.has_option('PostProcessing', 'PS3DestinationPath'):
            config.set('PostProcessing', 'PS3DestinationPath', "''")     
        if not config.has_option('PostProcessing', 'EnableXBOX360PostProcessing'):
            config.set('PostProcessing', 'EnableXBOX360PostProcessing', '0')
        if not config.has_option('PostProcessing', 'XBOX360DestinationPath'):
            config.set('PostProcessing', 'XBOX360DestinationPath', "''")  

    with open(conffile, 'wb') as configfile:
        config.write(configfile)

version = Constants.VersionNumber()
app_path = os.path.join(os.path.dirname(__file__))
conffile = os.path.join(app_path,'GamezServer.ini')
dbfile = os.path.join(app_path,'Gamez.db')
logger = GamezServer.Logger.Logger(dbfile)
css_path = os.path.join(app_path,'web_resources')
css_path = os.path.join(css_path,'css')
images_path = os.path.join(app_path,'web_resources')
images_path = os.path.join(images_path,'images')
js_path = os.path.join(app_path,'web_resources')
js_path = os.path.join(js_path,'js')
CheckConfig()
config = ConfigParser.RawConfigParser()
config.read(conffile)
enableAuthentication = False
if(config.get('GamezServer','EnableAuth') == "1"):
    enableAuthentication = True
username = str(config.get('GamezServer','authusername')).replace("'","")
password = str(config.get('GamezServer','authpassword')).replace("'","")
validation = cherrypy.lib.auth_basic.checkpassword_dict({username : password})
conf = {
            '/':{'tools.auth_basic.on':enableAuthentication,'tools.auth_basic.realm':'GamezServer','tools.auth_basic.checkpassword':validation},
            '/css': {'tools.staticdir.on':True,'tools.staticdir.dir':css_path},
            '/js':{'tools.staticdir.on':True,'tools.staticdir.dir':js_path},
            '/images':{'tools.staticdir.on':True,'tools.staticdir.dir':images_path}
        }

dao = GamezServer.GamezServerDao.GamezServerDao()
if(os.path.exists(dbfile) == False):
    dao.InitializeDB(dbfile)
    RunGameDBUpdater()
GenerateSabPostProcessScript()
logger.Log('Configuring Web Server')
cherrypy.config.update(conffile)
cherrypy.config.update(conf)
app = cherrypy.tree.mount(RunWebServer(), '/', conffile)
app.merge(conf)
if hasattr(cherrypy.engine, "signal_handler"):
    cherrypy.engine.signal_handler.subscribe()
if hasattr(cherrypy.engine, "console_control_handler"):
    cherrypy.engine.console_control_handler.subscribe()
logger.Log("Starting Web Server")
Monitor(cherrypy.engine, RunGameSearch, 3600).subscribe()
Monitor(cherrypy.engine, RunGameDBUpdater, 86400).subscribe()
cherrypy.engine.start()
thread.start_new_thread(RunGameDBUpdater, ())
thread.start_new_thread(RunGameSearch, ())
cherrypy.engine.block()