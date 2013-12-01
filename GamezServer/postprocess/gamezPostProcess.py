#!/usr/bin/env python
import sys
import urllib
filePath = str(sys.argv[1])
fields = str(sys.argv[3]).split("-")
gamezID = fields[0].replace("[","").replace("]","").replace(" ","")
status = str(sys.argv[7])
downloadStatus = 'Wanted'
if(status == '0'):
    downloadStatus = 'Downloaded'
url = "http://127.0.0.1:5000/updatestatus?game_id=" + gamezID + "&filePath=" + urllib.quote(filePath) + "&status=" + downloadStatus
responseObject = urllib.FancyURLopener({}).open(url)
responseObject.read()
responseObject.close()
print("Processing Completed Successfully")