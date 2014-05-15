#!/usr/bin/env python
# -*- coding=utf-8 -*-
import wx
import re
import sys
import gzip
numberRe = re.compile('^1[0-9]{10}$')
numsDbRe = re.compile('(^1[0-9]{6}) (.*) (.*)')

def getRegion(number,numsDb):
    if not numberRe.search(number):
        return '未知,未知'
    if not numsDb:
        return '未知,未知'

    k = number[0:3]
    v = number[3:7]
    if not k in numsDb:
        return '未知,未知'
    else:
        region = numsDb[k].get(v,('未知','未知'))
        return ','.join(region)

def loadRegion():
    RegionDb = {}
    try:
        for line in gzip.open('100422234510.gz').readlines():
            line = line.strip()
            m = numsDbRe.search(line)
            if m:
                nums,area,card = m.groups()
                k = nums[0:3]
                v = nums[3:7]
                if k in RegionDb:
                    RegionDb[k][v] = (area,card)
                else:
                    RegionDb[k]={}
                    RegionDb[k][v] = (area,card)
        return RegionDb
    except Exception,e:
        print e
        return {}

    
    
class fr(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'手机归属地查询')
        self.pel=wx.Panel(self,-1)
        self.statext=wx.StaticText(self.pel,-1,u'输入手机号码：')
        self.textctrl=wx.TextCtrl(self.pel,-1)
        self.but=wx.Button(self.pel,-1,u'查询')
        self.showtext=wx.StaticText(self.pel,-1)
        self.vbox=wx.BoxSizer(wx.VERTICAL)
        self.hbox=wx.BoxSizer()
        self.hbox.Add(self.statext,0,)
        self.hbox.Add(self.textctrl,1)
        self.hbox.Add(self.but,0,wx.LEFT,5)
        self.vbox.Add(self.hbox,1,wx.EXPAND|wx.ALL,20)
        self.vbox.Add(self.showtext,1,wx.EXPAND|wx.ALL|wx.CENTER|30)
        
        self.Bind(wx.EVT_BUTTON,self.butevent,self.but)
        
        self.pel.SetSizer(self.vbox)
        self.Layout()
        
    def butevent(self,event):
        
        numsDb = loadRegion()
        try:
            number=self.textctrl.GetValue()
            
            strtext=str(number)+' '+getRegion(number,numsDb)
            wx.MessageBox(strtext,u'查询结果')
                    
            self.showtext.SetLabel(strtext)
        except:
            wx.MessageBox(u"输入有错误")

            

if __name__ == '__main__':
    app=wx.PySimpleApp()
    fra=fr()
    fra.Show()
    app.MainLoop()
