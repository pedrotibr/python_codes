#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:22:31 2018

@author: pmesquital
"""

import sys

import wx

import MySQLdb

import frame_cadastro

from reportlab.pdfgen import canvas

db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")
cursor = db.cursor()

 
def create(parent):
    return Frame2(parent)
 
class Frame2(wx.Frame):
    def __init__(self, prnt):
        
        wx.Frame.__init__(self,id=-1, parent=prnt, title='Consulta',style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        
        self.panel = wx.Panel(self, id=-1, size=wx.Size(200, 200))
 
        
        self.choices=['']
      
      
        self.lbl_nome=wx.StaticText(self.panel, pos=(10,20), label='Nome:', size=(50,60))
       
        self.combobox_nome=wx.ComboBox(self.panel,6,'',(100,10),(200,-1),style=wx.CB_SORT, choices=self.choices)
        
        
        self.lbl_nascimento=wx.StaticText(self.panel, pos=(10,60), label='Nascimento:', size=(80,90))
        self.edit_nascimento=wx.TextCtrl(self.panel, pos=(100,50), size=(200,30))
        self.edit_nascimento.Enable(False)
        
        
        self.lbl_rg=wx.StaticText(self.panel, pos=(10,100), label='RG:', size=(50,120))
        self.edit_rg=wx.TextCtrl(self.panel, pos=(100,90), size=(200,30))
        
        self.edit_rg.Enable(False)
     
        self.btn_pesquisar = wx.Button(self.panel, pos=(100,145), label='Pesquisar', size=(100,30))
        
        self.btn_editar = wx.Button(self.panel, pos=(210,145), label='Editar', size=(90,30))

        self.btn_pesquisar.Bind(wx.EVT_BUTTON, self.Onconsultar)
        
        self.btn_editar.Bind(wx.EVT_BUTTON, self.frame_cadastro)
        
   
        self.a1=""
 
        self.SetSize((375,225))
        
        self.SetPosition((450,250))

        self.combobox_nome.Bind(wx.EVT_KEY_UP, self.onKeyPress) 
        
        self.combobox_nome.Bind(wx.EVT_COMBOBOX, self.select_item) 
        
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
    
    
    
    def OnClose(self, event):
      
             
        self.Destroy() 
    
    def select_item(self, event):
        
        
        cursor.execute('select * from database.CLIENTES where nome like "%'+self.combobox_nome.GetValue()+'%"')
        
        row=cursor.fetchone()

        self.edit_nascimento.SetValue(str(row[10]))
       # 
        self.edit_rg.SetValue(str(row[11]))

    def frame_cadastro(self, event):
   
        
        self.Framew1 = frame_cadastro.create(self)
        
        self.Framew1.Show()
        
        self.Framew1.find_user(self.combobox_nome.GetValue())
        
        self.Framew1.Onedit(self.Framew1)
  
    
    def onKeyPress(self, event):

        keycode = event.GetKeyCode()
  
                              
        if keycode == 13 :
     
            self.Onconsultar(self)
            
        
        event.Skip()
        
        
    def Onconsultar(self, e):

        self.nome_sql=self.combobox_nome.GetValue()
        
       
        numrows=cursor.execute('select * from database.CLIENTES where nome like "%'+self.nome_sql+'%"')
        
        row=cursor.fetchone()
        
        #print (row)
                
        self.lista=[]

        for num in range (0, numrows):
            
           # print (row[0] , "-->", row[1])
            self.lista.append(row[1])
            row=cursor.fetchone()
 
        self.combobox_nome.Clear()     
        self.combobox_nome.Append(self.lista)

    def Onedit(self, e):
       self.editmat.SetFocus()
       
       
    def Onprint(self, e):
        x=50
        y=10
     
        numrows = int(cursor.rowcount)
        c = canvas.Canvas("tags_db.pdf")
        for num in range (0, numrows):
            #x=x+10
            y=y+10
            row= cursor.fetchone()
         
            c.drawString(x,y,(row[1]))
    
        c.showPage()    
        c.save()
         
    def Ondelete(self, e):
  
            dialog = wx.MessageDialog(self,("Você quer realmente deletar esse registro?"),("Confirma exclusão"),
                                      wx.YES_NO | wx.ICON_QUESTION)
            remove = dialog.ShowModal() == wx.ID_YES
            dialog.Destroy()

            if remove:
                    num = str(self.editcod.GetValue())
              
                    cursor.execute("delete from nomes2 where id_codigo= %s",[num])
                    db.commit()
             
                    self.Onant(0)
 
            e.Skip()    

     
