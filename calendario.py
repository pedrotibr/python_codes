
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:15:59 2021

@author: pmesquital
"""

import wx


import wx.adv


def create(parent):
    return MyCalendar(parent)



class MyCalendar(wx.Frame):

    def __init__(self, *args, **kargs):
        wx.Frame.__init__(self, *args, **kargs)
        
        self.cal = wx.adv.CalendarCtrl(self, 10, wx.DateTime.Now())

        self.cal.Bind(wx.adv.EVT_CALENDAR , self.OnDate)
        
 
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.SetTitle('Calendário')
        
        self.SetSize((250,200))
        
        self.data_=""
        

    def OnDate(self,event):
        
        
        date=[]
        
        date=str(self.cal.GetDate())

        dia=(date[8]+date[9])
        
        mes=(date[4]+date[5]+date[6])
     
        ano=(date[20]+date[21]+date[22]+date[23])
        
        
        if dia == " 1":
            dia = "01"
        
        if dia == " 2":
            dia = "02"
        
        if dia == " 3":
            dia = "03"
        
        if dia == " 4":
            dia = "04"
            
        if dia == " 5":
            dia = "05"
            
        if dia == " 6":
            dia = "06"
        
        if dia == " 7":
            dia = "07"
                    
        if dia == " 8":
            dia = "08"
        
        if dia == " 9":
            dia = "09"
   
        if mes == "Jan":
            mes="01"
        if mes == "Feb":
            mes="02"    
        if mes == "Mar":
            mes="03"
        if mes == "Apr":
            mes="04"   
        if mes == "May":
            mes="05"
        if mes == "Jun":
            mes="06"   
        if mes == "Jul":
            mes="07"
        if mes == "Aug":
            mes="08"   
        if mes == "Sep":
            mes="09"
        if mes == "Oct":
            mes="10"   
        if mes == "Nov":
            mes="11"
        if mes == "Dez":
            mes="12"   
      
        data=dia+"/"+mes+"/"+ano

        print(data)
        
     
        self.data_=data
 
        self.Close()
        
    def data(self):
        return(self.data_)
        
   
      
    def OnClose(self, event):
      
        self.Destroy() 


if __name__ == '__main__':
    app = wx.App()
    frame = MyCalendar(None)
    frame.Show()
    app.MainLoop()
    
