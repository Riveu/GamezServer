<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
	<title></title>
	<telerik:RadStyleSheetManager id="RadStyleSheetManager1" runat="server" />
    <style type="text/css">
        div.RadMenu .rmRootGroup .rmLast   { float: right; } 
        div.RadMenu .rmGroup     .rmLast   { float: none;  }
    </style>
</head>
<body>
    <form id="form1" runat="server">
	    <telerik:RadScriptManager ID="RadScriptManager1" runat="server">
		    <Scripts>
			    <asp:ScriptReference Assembly="Telerik.Web.UI" Name="Telerik.Web.UI.Common.Core.js" />
			    <asp:ScriptReference Assembly="Telerik.Web.UI" Name="Telerik.Web.UI.Common.jQuery.js" />
			    <asp:ScriptReference Assembly="Telerik.Web.UI" Name="Telerik.Web.UI.Common.jQueryInclude.js" />
		    </Scripts>
	    </telerik:RadScriptManager>
	    <telerik:RadAjaxManager ID="RadAjaxManager1" runat="server">
	    </telerik:RadAjaxManager>
        <div style="margin-left:5px; margin-bottom:10px; margin-top:10px">
            <asp:HyperLink NavigateUrl="~/Default.aspx" runat="server" Font-Underline="false" ForeColor="#cc3300">
                <asp:Table runat="server">
                    <asp:TableRow>
                        <asp:TableCell VerticalAlign="Middle">
                            <asp:Image ImageUrl="Images/logo.png" runat="server" />
                        </asp:TableCell>
                        <asp:TableCell VerticalAlign="Middle">
                            <div style="font-family:'Lucida Handwriting';font-size:xx-large">Gamez Server</div>
                        </asp:TableCell>
                    </asp:TableRow>
                </asp:Table>
            </asp:HyperLink>     
        </div>
        <telerik:RadMenu CssClass="RadMenu" runat="server" Skin="WebBlue" Width="100%">
            <Items>
                <telerik:RadMenuItem Text="Support" NavigateUrl="http://www.riveu.com/Support.aspx" Target="_blank" OuterCssClass="rmLast" />
                <telerik:RadMenuItem Text="Add Game" NavigateUrl="Products.aspx" OuterCssClass="rmLast" />
                <telerik:RadMenuItem Text="Home" OuterCssClass="rmLast" NavigateUrl="Default.aspx" />
            </Items>
        </telerik:RadMenu>

	</form>
</body>
</html>
