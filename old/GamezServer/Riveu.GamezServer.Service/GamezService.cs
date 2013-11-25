using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;

namespace Riveu.GamezServer.Service
{
    public partial class GamezService : ServiceBase
    {
        public GamezService()
        {
            InitializeComponent();
        }

        protected override void OnStart(string[] args)
        {
            
        }

        protected override void OnStop()
        {
        }

        protected override void OnCustomCommand(int command)
        {
            switch (command)
            {
                case 1000:
                    StreamWriter writer = new StreamWriter(@"C:\testlog.txt");
                    writer.Write("Initialize System");
                    writer.Close();
                    break;
                default:
                    break;
            }
            base.OnCustomCommand(command);
        }
    }
}
