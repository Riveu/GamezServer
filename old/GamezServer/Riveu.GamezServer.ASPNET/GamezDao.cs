using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Web;
using System.Data.SQLite;

namespace Riveu.GamezServer.ASPNET
{
    public class GamezDao
    {
        private string connectionString = "Data Source=gamez.db";

        public GamezDao()
        {
            //HttpServerUtility server = new HttpServerUtility();
            //string configPath = server.MapPath(configPath);
            if (!File.Exists("gamez.db"))
            {
                //InitializeDB(configPath);
            }
            else
            {
                //TODO: Check All Tables and Fields Exist
            }
        }
        private void InitializeDB(string filePath)
        {
            SQLiteConnection.CreateFile(filePath);
            
        }

        private void ExecuteNonQuery(string sql)
        {
            SQLiteConnection conn = new SQLiteConnection(connectionString);
            conn.Open();
            try
            {
                new SQLiteCommand(sql, conn).ExecuteNonQuery();
            }
            catch (Exception ex)
            {
                //Log Error
            }
            finally
            {
                if (conn.State == System.Data.ConnectionState.Open)
                {
                    conn.Close();
                }
            }
        }
    }
}