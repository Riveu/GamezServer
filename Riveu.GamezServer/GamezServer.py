import cherrypy
import os
import ConfigParser
import GamezServer.GamezServerDao
import GamezServer.RiveuServer
import GamezServer.Logger
import sys
class RunWebServer(object):

    def __init__(self):
        cherrypy.engine.subscribe('start', self.start)
        cherrypy.engine.subscribe('stop', self.stop)

    @cherrypy.expose
    def index(self):
        gamesList = dao.GetGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Log</title>"
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
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <table id=\"logGrid\" width=\"100%\" class=\"display\"><thead><tr><th>Cover</th><th>Game Title</th><th>Game ID</th><th>Game Description</th><th>Console</th><th>Release Date</th><th>Status</th><th>Location</th></tr></thead><tbody>"
        for row in gamesList:
            try:
                content = content + "                       <tr><td><image width\"50%\" height=\"50%\" src=\"" + str(row[0]) + "\" alt=\"Cover Image\" /></td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5]) + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td></tr>"
            except:
                logger.Log("Unable to show game because there is unicode error in description: " + str(row[1]))
        content = content + "                       </tbody></table>"
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {$('#logGrid').dataTable({\"bJQueryUI\": true, \"sPaginationType\": \"full_numbers\"});});</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def mastergames(self):
        gamesList = dao.GetMasterGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Log</title>"
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
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <table id=\"gamesGrid\" width=\"100%\" class=\"display\"><thead><tr><th>Cover</th><th>Game Title</th><th>Game ID</th><th>Game Description</th><th>Release Date</th><th>Console</th></tr></thead><tbody>"
        for row in gamesList:
            try:
                dateValue = str(row[4])
                if(dateValue == '//'):
                    dateValue = 'Unkown'
                content = content + "                       <tr><td><image width\"50%\" height=\"50%\" src=\"" + str(row[5]) + "\" alt=\"Cover Image\" /></td><td>" + str(row[1]) + "</td><td>" + str(row[0]) + "</td><td>" + str(row[2]) + "</td><td>" + dateValue + "</td><td>" + str(row[3]) + "</td></tr>"
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
        consolelist = dao.GetConsoles(dbfile)
        gamelist = dao.GetMasterGames(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Settings</title>"
        content = content + "       <link href=\"css/excite-bike/jquery-ui-1.10.3.custom.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <link href=\"css/styles.css\" type=\"text/css\" rel=\"stylesheet\">"
        content = content + "       <script src=\"js/jquery-1.9.1.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/jquery-ui-1.10.3.custom.js\" type=\"text/javascript\"></script>"
        content = content + "       <script src=\"js/modernizr-2.0.6.min.js\" type=\"text/javascript\"></script> "
        content = content + "       <script src=\"js/jquery.horizontalNav.js\" type=\"text/javascript\"></script> "
        content = content + "   </head>"
        content = content + "   <body style=\"background: url(/images/bgnoise_lg.png) repeat left top;width:100%\">"
        content = content + "   <form action=\"processAddGame\" method=\"post\">"
        content = content + "       <div id=\"container\" style=\"width: 100%; margin: 0px auto 0;\">"
        content = content + "           <table width=\"100%\" style=\"padding:15px\">"
        content = content + "               <tr><td><table><tr><td><img src=\"images/logo.png\" alt=\"Riveu Logo\" /></td><td><div style=\"color:Orange;font-family: Lucida Handwriting;font-size: XX-Large\">Gamez Server</div></td></tr></table></td></tr>"
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <div id=\"addgame-tabs\"><ul><li><a href=\"#addgame-tab\">Add Game</a></li></ul>"
        content = content + "                           <div id=\"addgame-tab\">"
        content = content + "                               <div>"
        content = content + "                                   <fieldset class=\"ui-widget ui-widget-content\">"
        content = content + "                                       <legend class=\"ui-widget-header ui-corner-all\">"
        content = content + "                                           <div>Game Information</div>"
        content = content + "                                       </legend>"
        content = content + "                                       <div class=\"ui-widget\"><table style=\"width:100%\"><tr style=\"width:100%\"><td style=\"width:100px\"><label for=\"console\">Console: </label></td><td style=\"width:95%\"><input name=\"console\" id=\"console\" style=\"width:60%;margin-left:20px\"></td></tr>"
        content = content + "                                       <tr><td><label for=\"game\">Game: </label></td><td><input name=\"console\" id=\"game\" style=\"width:60%;margin-left:20px\"></td></tr>"
        content = content + "                                       <tr><td style=\"width:100%;text-align:right;padding:15px\" colspan=\"2\"><button id=\"saveSettingsButton\" type=\"submit\">Add Game</button></td></tr></table></div>"
        content = content + "                                   </fieldset>"
        content = content + "                               </div>"
        content = content + "                           </div>"
        content = content + "                       </div>"    
        content = content + "                   </td>"
        content = content + "               </tr>"
        content = content + "           </table>"
        content = content + "       </div>"
        content = content + "       <script>$(function() {"
        content = content + "var availableConsoles = ["
        for row in consolelist:
            content = content + "'" + str(row[0]).replace("\r","") + "',"
        content = content + "];"
        content = content + "var availableGames = ["
        for row in gamelist:
            content = content + '"' + str(row[1]).replace("\r","") + '",'
        content = content + "];"
        content = content + "       $( \"#addgame-tabs\" ).tabs();$(\"#saveSettingsButton\").button();$(\"#console\").autocomplete({source: availableConsoles});$(\"#game\").autocomplete({source: availableGames});});</script>"
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def processAddGame(self,console=None):
        print(console[0])
        print(console[1])
        dao.AddWantedGame(dbfile,console[0],console[1])
        raise cherrypy.HTTPRedirect("/")

    def stop(self):
        logger.Log("Shutting Down Web Server")

    def start(self):
        logger.Log("Web Server Started")

    @cherrypy.expose
    def log(self):
        logResult = dao.GetLogMessages(dbfile)
        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Log</title>"
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
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li></ul></div></td></tr>"
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
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def settings(self):
        config = ConfigParser.RawConfigParser()
        config.read('GamezServer.ini')
        enableAuthChecked = ""
        if(config.get('GamezServer','EnableAuth') == "1"):
            enableAuthChecked = "checked"

        content = ""
        content = content + "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
        content = content + "<html>"
        content = content + "   <head>"
        content = content + "       <title>Gamez Server :: Settings</title>"
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
        content = content + "               <tr width=\"100%\"><td><div id='cssmenu'><ul>   <li class='active'><a href='/'><span>Home</span></a></li><li><a href='/addgame'><span>Add Game</span></a></li> <li><a href='/mastergames'><span>Master Game List</span></a></li>  <li><a href='/settings'><span>Settings</span></a></li><li class='last'><a href='/log'><span>Log</span></a></li></ul></div></td></tr>"
        content = content + "               <tr>";
        content = content + "                   <td>"
        content = content + "                       <div id=\"settings-tabs\"><ul><li><a href=\"#general-tab\">General</a></li><li><a href=\"#downloaders-tab\">Downloaders</a></li><li><a href=\"#notifications-tab\">Notifications</a></li></ul>"
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
        content = content + "                           <div id=\"downloaders-tab\">Coming Soon</div>"
        content = content + "                           <div id=\"notifications-tab\">Coming Soon</div>" 
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
        content = content + "   </form>"
        content = content + "   </body>"
        content = content + "</html>"
        return content

    @cherrypy.expose
    def saveSettings(self,host=None,port=None,enableAuth=None,authUsername=None,authPassword=None):
        if(enableAuth == 'on'):
            enableAuth = '1';
        else:
            enableAuth = '0';
        config = ConfigParser.RawConfigParser()
        config.add_section('global')
        config.set('global', 'server.socket_host', "'" + host + "'")
        config.set('global', 'server.socket_port', port)
        config.add_section('GamezServer')
        config.set('GamezServer', 'EnableAuth', enableAuth)
        config.set('GamezServer', 'AuthUsername', "'" + authUsername + "'")
        config.set('GamezServer', 'AuthPassword', "'" + authPassword + "'")
        with open(conffile, 'wb') as configfile:
            config.write(configfile)
        raise cherrypy.HTTPRedirect("/settings")

    @cherrypy.expose
    def clearlog(self, logGrid_length):
        logger.ClearLog()
        raise cherrypy.HTTPRedirect("/log")
    

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
if(os.path.exists(conffile) == False):
    config = ConfigParser.RawConfigParser()
    config.add_section('global')
    config.set('global', 'server.socket_host', "'127.0.0.1'")
    config.set('global', 'server.socket_port', '5000')
    config.add_section('GamezServer')
    config.set('GamezServer', 'EnableAuth', '0')
    config.set('GamezServer', 'AuthUsername', "''")
    config.set('GamezServer', 'AuthPassword', "''")
    with open(conffile, 'wb') as configfile:
        config.write(configfile)
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
logger.Log('Updating Console List')
riveuServer = GamezServer.RiveuServer.RiveuServer(dbfile)
riveuServer.UpdateConsoles()
logger.Log('Updating Games List')
riveuServer.UpdateGames()
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
cherrypy.engine.start()
cherrypy.engine.block()
