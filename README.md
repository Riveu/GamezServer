Gamez Server
===========

<hr />

Gamez Server is currently in *Alpha* release. There may be bugs in the application.

Gamez Server is an automated downloader for video games. The user adds the games they wish to download and Gamez will attempt to find the game and download it.

While all games are technically implemented, as of the current release, only Wii games are loaded to the server. More systems will be added in the coming days (This will not require a new release)

Current Features:

    * Local database based off of remote database
    * Automatically sends NZB's to Sabnzbd
    * Support for Usenet-Crawler

<hr />

***Dependencies***

Gamez requires Python and CherryPY. The CherryPy module is included with Gamez Server. Python must be installed on the system on which Gamez Server will be ran. The default port is 5000

There is a post processing script that will be generated after you run the application and whenever you change the settings, such as host and port number. This will be located under the GamezServer => PostProcess subfolder. The script will need to be copied to your scripts directory that Sabnzbd looks at in order to properly have statuses updated, as well as for the post processing to work.

<hr />
