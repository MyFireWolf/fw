#!/usr/bin/python
#coding: utf-8
import sys,os
print 'os.getcwd:',os.getcwd()
home = os.path.dirname(os.path.abspath(sys.argv[0]))
print "os.path.abspath(sys.argv[0]):",os.path.abspath(sys.argv[0])
print "sys.argv:",sys.argv
print "home:",home
langdir = os.path.join(home, "mysite")
imagedir = os.path.join(home, "images")
sys.path.append(langdir)
sys.path.append(imagedir)
print "-"*10
print langdir
import sqlalchemy
import wx
import wx.aui
#from django import *
#from django.core.management import execute_manager
#import imp
#from mysite import settings as settings
#from django.db import connection
#execute_manager(settings,'shell')
#from django.db import models
#from mysite.books import models

from ui.panels import MyPanel
from ui import mytaskbar,WebNumberSearch,sqldb
#from ui import phonesearch
class WindowsMain(wx.Frame):
    def __init__(self,*args,**kwargs):
        wx.Frame.__init__(self,*args,**kwargs)
        
        self.mainbox=wx.BoxSizer()
        self.panel=wx.Panel(self)
        self.panelbox=wx.BoxSizer()
         
        self.notebook=wx.aui.AuiNotebook(self.panel)
        self.panelbox.Add(self.notebook,1,wx.EXPAND)
        self.InitSystemNotePage()
        self.panel.SetSizer(self.panelbox)       
        self.mainbox.Add(self.panel,1,wx.EXPAND)       
        self.SetSizer(self.mainbox)
        
        self.menubar=wx.MenuBar() 
        self.CreateMenu()
        self.CreateTool()
        
        self.CreateStatus()
        self.SetMenuBar(self.menubar)
        self.baricon=mytaskbar.mytaskbar(self)
        self.baricon.SetIcon(wx.Icon(os.path.join(imagedir,'1381love.ico'),wx.BITMAP_TYPE_ANY))
        self.SetIcon(wx.Icon(os.path.join(imagedir,'1381love.ico'),wx.BITMAP_TYPE_ICO))
        self.SetInitialSize((800,600))
        self.Layout()
        self.Center()
        self.Bind(wx.EVT_CLOSE,self.OnClose)
        self.IsShow=True
    def CreateStatus(self):
        self.CreateStatusBar()
        
    def CreateTool(self):
        self.tools=wx.ToolBar(self)
        self.tools.SetSize((50,50))
        self.SetToolBar(self.tools)
        
      
    def CreateMenu(self):
        menu=wx.Menu()
        menu.Append(5555,'testnotebook')
        self.menubar.Append(menu,u'文件(&F)')
        menu=wx.Menu()
        self.menubar.Append(menu,u'采购管理(&P)')
        menu=wx.Menu()
        self.menubar.Append(menu,u'销售管理(&S)')
        menu=wx.Menu()
        self.menubar.Append(menu,u'库存管理(&I)')
        menu=wx.Menu()
        self.menubar.Append(menu,u'借入借出(&J)')
        menu=wx.Menu()
        self.menubar.Append(menu,u'财务管理(&B)')
        menu=wx.Menu()
        menu.Append(5001,u'手机归属地查询')
        self.Bind(wx.EVT_MENU,self.OnPhonsearch,id=5001)
        menu.Append(5002,u'写字板')
        self.Bind(wx.EVT_MENU,self.OnWordPad,id=5002)
        self.menubar.Append(menu,u'工具(&T)')
    def OnWordPad(self,event):
        import subprocess
        self.p=subprocess.Popen('C:\Program Files\Windows NT\Accessories\wordpad.exe', stdin = subprocess.PIPE, shell = True)
        print 'hello'       
        
    def OnPhonsearch(self,event):
        winsearch=WebNumberSearch.win()
        winsearch.Show()
                
        
    def OnClose(self,event):
        if self.IsShow:
            result=wx.MessageDialog(self.panel,u"是否退出?\n注意:选择 '取消'按钮 将最小化到托盘...").ShowModal()
            if result==wx.ID_OK:
                self.baricon.Destroy()
                self.Destroy()
            else:
                self.Hide()
            self.IsShow=False
        else:
            self.Hide()
     
    def OnExit(self,event):
        wx.MessageBox(u'退出程序！')
        
        self.p.kill()
        self.p.terminate()
        self.baricon.Destroy()
        self.Destroy()       
    
    def InitSystemNotePage(self):       
        cpxx_panel=MyPanel(self.notebook)
        self.notebook.InsertPage(0,cpxx_panel,u'联系人')
        cpxx_panel=MyPanel(self.notebook)
        self.notebook.InsertPage(1,cpxx_panel,u'详细地址')
    
class MyApp(wx.App):
    def OnInit(self):
        self.frame = WindowsMain(None, title="Custom Events")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
    
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()