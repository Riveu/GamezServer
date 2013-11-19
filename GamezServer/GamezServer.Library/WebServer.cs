using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;

namespace GamezServer.Library
{
    public class WebServer
    {
        HttpListener httpListener = new HttpListener();
        HttpListener settingsListener = new HttpListener();

        public void Start()
        {
            httpListener.Prefixes.Add("http://localhost:8080/");
            settingsListener.Prefixes.Add("http://localhost:8080/settings/");
            httpListener.Start();
            settingsListener.Start();
            Console.WriteLine("HTTP Server Started. Press <enter> to stop.");
            httpListener.BeginGetContext(new AsyncCallback(GetContextCallback), null);
            settingsListener.BeginGetContext(new AsyncCallback(SettingsPage), null);
            Console.ReadLine();
            httpListener.Stop();
            settingsListener.Stop();

        }

        public void GetContextCallback(IAsyncResult result)
        {
            HttpListenerContext context = httpListener.EndGetContext(result);
            HttpListenerRequest request = context.Request;
            HttpListenerResponse response = context.Response;

            System.Text.StringBuilder sb = new System.Text.StringBuilder();

            sb.Append("<h1>Home Page</h1><br /><input type=button onClick=\"parent.location='/settings/'\" value='Settings Page'>");

            string responseString = sb.ToString();
            byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);
            response.ContentLength64 = buffer.Length;

            using (System.IO.Stream outputStream = response.OutputStream)
            {
                outputStream.Write(buffer, 0, buffer.Length);
            }
            httpListener.BeginGetContext(new AsyncCallback(GetContextCallback), null);
        }

        public void SettingsPage(IAsyncResult result)
        {
            HttpListenerContext context = settingsListener.EndGetContext(result);
            HttpListenerRequest request = context.Request;
            HttpListenerResponse response = context.Response;
            System.Text.StringBuilder sb = new System.Text.StringBuilder();
            sb.Append("<h1>Settings Page</h1>");
            string responseString = sb.ToString();
            byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);
            response.ContentLength64 = buffer.Length;
            using (System.IO.Stream outputStream = response.OutputStream)
            {
                outputStream.Write(buffer, 0, buffer.Length);
            }
            settingsListener.BeginGetContext(new AsyncCallback(SettingsPage), null);
        }
    }
}
