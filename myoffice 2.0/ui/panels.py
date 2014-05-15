#!/usr/bin/python
#coding: utf-8
import wx

[MENU_DEL,MENU_ADD]=[wx.NewId() for _init_ctrls in range(2)]  
class MyPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1)
        box=wx.BoxSizer()
        self.listctrl=wx.ListCtrl(self,-1,style=wx.LC_REPORT)
        box.Add(self.listctrl,1,wx.EXPAND|wx.ALL,5)
        
        self.listctrl.InsertColumn(0,u'姓名')
        self.listctrl.InsertColumn(1,u'联系方式')
        self.SetSizer(box)
        self.listctrl.Bind(wx.EVT_RIGHT_DOWN,self.popmenu)
        self.Bind(wx.EVT_MENU,self.OnClickMenu)
    def popmenu(self,event):
        #[MENU_DEL,MENU_ADD]=[wx.NewId() for _init_ctrls in range(2)]                           
        menu=wx.Menu()
        menu.Append(MENU_ADD,u'增加')
        menu.Append(MENU_DEL,u'删除')
        self.PopupMenu(menu,event.GetPosition())
    def OnClickMenu(self,event):
        if event.GetId()==MENU_DEL:
            wx.MessageBox('del')
        else:wx.MessageBox('add')
        wx.MessageBox('ok')
        