using System;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

using System.Data;
using System.Configuration;
using System.Web.Security;
using System.Web.UI.WebControls.WebParts;
using System.Web.UI.HtmlControls;
using Telerik.Web.UI;
using System.ServiceProcess;
using Riveu.GamezServer.ASPNET;


public partial class Default : System.Web.UI.Page 
{
    protected void Page_Load(object sender, EventArgs e)
    {
        if (!IsPostBack)
        {
            StartService();
        }
    }

    private void StartService()
    {
        ServiceController serviceController = new ServiceController("GamezService");
        serviceController.ExecuteCommand(1);
    }
}
