#!/usr/bin/python
#coding: utf-8
import wx
import wx.richtext as rt


ID_BUTTON1 = wx.NewId()
username = None
password = None
save = None 



class LoginFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Box-Login', size = (350, 240), pos = (-1, -1))
        # Attributes
        #self.panel = wx.Panel(self)
        self.panel = GridBagPanel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
       
class GridBagPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        
        # Attributes
        #img1 = wx.Image("e:\magicgourd\box.png", wx.BITMAP_TYPE_ANY)
        #top_image = wx.StaticBitmap(self, -1, wx.BitmapFromImage(img1))
        #img2 = wx.Image("e:\magicgourd\usr.png", wx.BITMAP_TYPE_ANY)
        #usr_image = wx.StaticBitmap(self, -1, wx.BitmapFromImage(img2))
        
        self.parent=parent
        
        usr_id = wx.StaticText(self, -1, "昵称：")
        self.id_usr = wx.TextCtrl(self, size = (120, -1))
        usr_password = wx.StaticText(self, -1, "密码：")
        self.password_usr = wx.TextCtrl(self, size = (120, -1), style = wx.TE_PASSWORD)
        self.save_password = wx.CheckBox(self, label="记住密码")

        self.button1 = wx.Button(self,  label = "注册")
        self.button2 = wx.Button(self,  label = "登录")
        self.button2.SetDefault()
        

        # Layout
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
              
        hsizer1.Add(usr_id, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        hsizer1.Add(self.id_usr, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        hsizer2.Add(usr_password, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        hsizer2.Add(self.password_usr, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        hsizer2.Add(self.save_password, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        vsizer1.Add(hsizer1, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        vsizer1.Add(hsizer2, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        
        #hsizer.Add(usr_image, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        hsizer.Add(vsizer1, 0, wx.EXPAND|wx.TOP|wx.LEFT, 5)
        
        hsizer3.Add(self.button1, 0, wx.EXPAND|wx.LEFT, 5)
        hsizer3.Add(self.button2, 0, wx.EXPAND|wx.LEFT, 5)
        
        #vsizer.Add(top_image, 0, wx.EXPAND|wx.ALL)
        vsizer.Add(hsizer, 0, wx.EXPAND|wx.LEFT, 40)
        vsizer.Add(hsizer3, 0, wx.ALIGN_RIGHT|wx.RIGHT|wx.TOP, 20)

        self.SetSizer(vsizer)
            
        # Events
        self.Bind(wx.EVT_BUTTON, self.login, self.button2)
        self.Bind(wx.EVT_BUTTON, self.reg, self.button1)

    def frclose(self):
        self.Destroy()

    def login(self, event):
        global username
        if username:
            self.id_usr.SetValue(username)
        else:
            username = self.id_usr.GetValue()
            if len(username) == 0:
                errortips = wx.MessageBox("Please enter an available username. "
                                            "If you don't have an acount, "
                                            "please register first.",
                                            style = wx.CENTER|wx.ICON_ERROR|wx.OK)
        password = self.password_usr.GetValue()
        save_status = self.save_password.GetValue()
        #self.Destroy()
        #return username, password, save_statu
        print username
        print password
        print save_status
        self.parent.Destroy()
        self.Destroy()
    def reg(self):
        pass

loginframe = None

class App(wx.App):
    def OnInit(self):
        frame = LoginFrame(parent=None, id=-1)
        frame.Show()
        #return 1, username, password, save
        return True
        

if __name__ == '__main__':
    app = App()
    app.MainLoop()
        

'''if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = LoginFrame(parent=None, id=-1)
    frame.Show()     
    app.MainLoop()
'''


"""import wx 
import loginGUI  
from loginGUI import LoginFrame 
app = wx.PySimpleApp()     
frame = loginGUI.LoginFrame(parent=None, id=-1) 
frame.Show()    
app.MainLoop()"""
