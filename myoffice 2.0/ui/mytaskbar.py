#!/usr/bin/python
# coding: utf-8
import sys,os
import wx
class mytaskbar(wx.TaskBarIcon):
    def __init__(self,parent):
        self.parent=parent
        super(mytaskbar,self).__init__()
        
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        

    def OnTaskBarLeftDClick(self, event):
        if self.parent.IsIconized():
            self.parent.Iconize(False)
        if not self.parent.IsShown():
            self.parent.Show(True)
        self.parent.Raise()
        
    def CreatePopupMenu(self):
        home = os.path.dirname(os.path.abspath(sys.argv[0]))
        imagedir = os.path.join(home, "images")
        context_menu=wx.Menu()

        menuItem_show=wx.MenuItem(context_menu,wx.NewId(), "Show Me")
        menuItem_show.SetBitmap(wx.Bitmap(os.path.join(imagedir,'down_stack_24.png')))
        context_menu.AppendItem(menuItem_show)
        self.Bind(wx.EVT_MENU, self.OnShowMe,menuItem_show)

        menuItem_exit=wx.MenuItem(context_menu,wx.ID_EXIT, "Exit")
        menuItem_exit.SetBitmap(wx.Bitmap(os.path.join(imagedir,'bookmarks_24.png')))
        context_menu.AppendItem(menuItem_exit)
        self.Bind(wx.EVT_MENU,wx.GetApp().GetTopWindow().OnExit,menuItem_exit)

        return context_menu
    
    def OnShowMe(self,event):
        self.parent.Show(True)
    
    
        

