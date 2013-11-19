using GamezServer.Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GamezServer.Console
{
    class Program
    {
        static void Main(string[] args)
        {
            WebServer webserver = new WebServer();
            webserver.Start();
        }
    }
}
