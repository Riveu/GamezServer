using System;
using System.Collections;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Text;
using System.Xml;

namespace GameUpdater
{
    class Program
    {
        static void Main(string[] args)
        {
            GenerateOutputFile(GetGameList(), @"C:\Users\Michael Dlesk\Desktop\games.txt");
            Console.WriteLine("File Generated");
        }

        private static DataTable GetGameList()
        {
            DataTable dataTable = new DataTable();
            dataTable.Columns.Add(new DataColumn("GameID"));
            dataTable.Columns.Add(new DataColumn("GameTitle"));
            dataTable.Columns.Add(new DataColumn("GameDescription"));
            dataTable.Columns.Add(new DataColumn("ReleaseDate"));
            dataTable.Columns.Add(new DataColumn("CoverArt"));
            dataTable.Columns.Add(new DataColumn("Console"));
            dataTable.PrimaryKey = new DataColumn[] { dataTable.Columns["GameID"] };

            XmlDocument xmlDocument = new XmlDocument();
            xmlDocument.Load("http://www.riveu.com/GamezServer/wiitdb.xml");
            foreach (XmlNode childNode in xmlDocument.ChildNodes[1].ChildNodes)
            {
                if (childNode.Name == "game")
                {
                    string gameid = String.Empty;
                    string gameTitle = String.Empty;
                    string gameDescription = String.Empty;
                    string releaseDate = String.Empty;
                    bool addGame = false;
                    foreach (XmlNode nestedNode in childNode.ChildNodes)
                    {
                        if (nestedNode.Name == "id")
                        {
                            gameid = nestedNode.InnerText;
                        }
                        if (nestedNode.Name == "locale")
                        {
                            string lang = nestedNode.Attributes["lang"].Value.ToString();
                            if (lang.ToUpper() == "EN")
                            {
                                foreach (XmlNode localeNode in nestedNode.ChildNodes)
                                {
                                    if (localeNode.Name == "title")
                                    {
                                        gameTitle = localeNode.InnerText;
                                    }
                                    if (localeNode.Name == "synopsis")
                                    {
                                        gameDescription = localeNode.InnerText;
                                    }
                                }
                            }
                        }
                        if (nestedNode.Name == "date")
                        {
                            releaseDate = nestedNode.Attributes["month"].Value + "/" + nestedNode.Attributes["day"].Value + "/" + nestedNode.Attributes["year"].Value;
                        }
                        if (nestedNode.Name == "region")
                        {
                            if (nestedNode.InnerText == "NTSC-U")
                            {
                                addGame = true;
                            }
                        }

                    }
                    if (addGame)
                    {
                        if (!dataTable.Rows.Contains(gameTitle))
                        {
                            DataRow dataRow = dataTable.NewRow();
                            dataRow["GameID"] = gameid;
                            dataRow["GameTitle"] = gameTitle;
                            dataRow["GameDescription"] = gameDescription;
                            dataRow["ReleaseDate"] = releaseDate;
                            dataRow["CoverArt"] = "http://www.riveu.com/GamezServer/CoverArt/Wii/" + gameid + ".png";
                            dataRow["Console"] = "Nintendo Wii";
                            dataTable.Rows.Add(dataRow);
                        }
                    }
                }
            }
            return dataTable;
        }

        private static void GenerateOutputFile(DataTable dataTable, string path)
        {
            StreamWriter writer = new StreamWriter(path);
            foreach (DataRow row in dataTable.Rows)
            {
                string gameId = row["GameID"].ToString().Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty).Replace("…", "...").Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®",String.Empty).Replace("–","-").Replace("ō","o").Replace("』",String.Empty).Replace("´","`").Replace("マ",String.Empty).Replace("リ",String.Empty).Replace("オ",String.Empty).Replace("カ",String.Empty).Replace("ー",String.Empty).Replace("ト",String.Empty).Replace("ア",String.Empty).Replace("ケ",String.Empty).Replace("ド",String.Empty).Replace("グ",String.Empty).Replace("ラ",String.Empty).Replace("ン",String.Empty).Replace("プ",String.Empty).Replace(" ­", "-");
                string gameTitle = row["GameTitle"].ToString().Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty).Replace("…", "...").Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®", String.Empty).Replace("–", "-").Replace("ō", "o").Replace("』", String.Empty).Replace("´", "`").Replace("マ", String.Empty).Replace("リ", String.Empty).Replace("オ", String.Empty).Replace("カ", String.Empty).Replace("ー", String.Empty).Replace("ト", String.Empty).Replace("ア", String.Empty).Replace("ケ", String.Empty).Replace("ド", String.Empty).Replace("グ", String.Empty).Replace("ラ", String.Empty).Replace("ン", String.Empty).Replace("プ", String.Empty).Replace(" ­", "-"); ;
                string gameDescription = row["GameDescription"].ToString().Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty).Replace("…", "...").Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®", String.Empty).Replace("–", "-").Replace("ō", "o").Replace("』", String.Empty).Replace("´", "`").Replace("マ", String.Empty).Replace("リ", String.Empty).Replace("オ", String.Empty).Replace("カ", String.Empty).Replace("ー", String.Empty).Replace("ト", String.Empty).Replace("ア", String.Empty).Replace("ケ", String.Empty).Replace("ド", String.Empty).Replace("グ", String.Empty).Replace("ラ", String.Empty).Replace("ン", String.Empty).Replace("プ", String.Empty).Replace(" ­", "-"); ;
                if (gameDescription.Length > 255)
                {
                    gameDescription = gameDescription.Substring(0, 255) + "...";
                }
                gameDescription = gameDescription.Replace("\n", " ");
                string releaseDate = row["ReleaseDate"].ToString().Replace("é", "e").Replace("î", "i").Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty).Replace("…", "...").Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®", String.Empty).Replace("–", "-").Replace("ō", "o").Replace("』", String.Empty).Replace("´", "`").Replace("マ", String.Empty).Replace("リ", String.Empty).Replace("オ", String.Empty).Replace("カ", String.Empty).Replace("ー", String.Empty).Replace("ト", String.Empty).Replace("ア", String.Empty).Replace("ケ", String.Empty).Replace("ド", String.Empty).Replace("グ", String.Empty).Replace("ラ", String.Empty).Replace("ン", String.Empty).Replace("プ", String.Empty).Replace(" ­", "-"); ;
                string coverArt = row["CoverArt"].ToString().Replace("é", "e").Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty).Replace("…", "...").Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®", String.Empty).Replace("–", "-").Replace("ō", "o").Replace("』", String.Empty).Replace("´", "`").Replace("マ", String.Empty).Replace("リ", String.Empty).Replace("オ", String.Empty).Replace("カ", String.Empty).Replace("ー", String.Empty).Replace("ト", String.Empty).Replace("ア", String.Empty).Replace("ケ", String.Empty).Replace("ド", String.Empty).Replace("グ", String.Empty).Replace("ラ", String.Empty).Replace("ン", String.Empty).Replace("プ", String.Empty).Replace(" ­", "-"); ;
                string console = row["Console"].ToString().Replace("é", "e").Replace("â", "a").Replace("á", "a").Replace("à", "a").Replace("ä", "a").Replace("ã", "a").Replace("ç", "c").Replace("¡", "!").Replace("¿", "?").Replace("ê", "e").Replace("é", "e").Replace("è", "e").Replace("ë", "e").Replace("ô", "o").Replace("ó", "o").Replace("ò", "o").Replace("ö", "o").Replace("õ", "o").Replace("ñ", "n").Replace("û", "u").Replace("ú", "u").Replace("ù", "u").Replace("ü", "u").Replace("•", String.Empty).Replace("Ō", "O").Replace("™", String.Empty.Replace("…", "...")).Replace("’", "'").Replace("“", "\"").Replace("”", "\"").Replace("—", "-").Replace("‐", "-").Replace("‘", "'").Replace("®", String.Empty).Replace("–", "-").Replace("ō", "o").Replace("』", String.Empty).Replace("´", "`").Replace("マ", String.Empty).Replace("リ", String.Empty).Replace("オ", String.Empty).Replace("カ", String.Empty).Replace("ー", String.Empty).Replace("ト", String.Empty).Replace("ア", String.Empty).Replace("ケ", String.Empty).Replace("ド", String.Empty).Replace("グ", String.Empty).Replace("ラ", String.Empty).Replace("ン", String.Empty).Replace("プ", String.Empty).Replace(" ­", "-"); ;
                string lineContents = String.Format("{0}::||::{1}::||::{2}::||::{3}::||::{4}::||::{5}", gameId, gameTitle, gameDescription, releaseDate, coverArt, console);
                writer.WriteLine(lineContents);
            }
            writer.Close();
        }
    }
}
