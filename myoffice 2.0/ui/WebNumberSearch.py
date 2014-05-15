#-*-coding: gb2312 -*-
import urllib,urllib2,HTMLParser
import wx
class MyParser(HTMLParser.HTMLParser):
    def reset(self):
        self._isInTd = False        
        self._retdata = []
        HTMLParser.HTMLParser.reset(self)
    def handle_starttag(self,tag,attris):
        self._isInTd = tag == 'td'
    def handle_endtag(self,tag):
        if self._isInTd:
            self._isInTd = False
    def handle_data(self,data):
        if self._isInTd:
            self._retdata.append(data)


class win(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None)
        self.panel=wx.Panel(self)
        self.statictext=wx.StaticText(self.panel,-1,'手机号码:')
        self.EdtPhone = wx.TextCtrl(self.panel)
        self.Button1 = wx.Button(self.panel,-1,'查询')
        self.panel.Bind(wx.EVT_BUTTON,self.Button1Click)  
        
        self.box=wx.BoxSizer()
        self.box.Add(self.statictext)
        self.box.Add(wx.StaticText(self.panel,-1,'  '))
        self.box.Add(self.EdtPhone)
        self.box.Add(wx.StaticText(self.panel,-1,'  '))
        self.box.Add(self.Button1)
        
        self.conterbox=wx.BoxSizer()
        self.conterbox.Add(self.box,0,wx.ALL,5)
        self.panel.SetSizer(self.conterbox)
        
    def Button1Click(self,event):
        postdata = urllib.urlencode([('action','mobile'),('mobile',self.EdtPhone.GetValue())])
        req = urllib2.Request('http://www.ip138.com:8080/search.asp')
        fd = urllib2.urlopen(req,postdata)
        h = fd.read()
        my = MyParser()
        my.feed(h)
        strs=''
        ss=''
        cont=0
        for i in my._retdata:
            #ss=ss+str(cont)+i+'   '
            if cont>6 and cont<10:
                strs=strs+i
            elif cont>10 and cont<12:
                if cont==12:
                    strs=strs+i+'\n'
                else:
                    strs=strs+i+':'            
            elif cont==13:
                strs=strs+i+':'
                
            else:
                strs=strs+i+'\n'
            cont+=1
            
        wx.MessageBox(strs)
        #wx.MessageBox(ss)

def main():
    app=wx.PySimpleApp()
    f=win()
    f.Show()
    app.MainLoop()
    
if __name__=='__main__':
    main()