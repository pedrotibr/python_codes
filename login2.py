#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:42:52 2018

@author: pmesquital
"""
        
ID_CTU = 100     
ID_CPR = 101
ID_CNO = 102
ID_CAL = 103
ID_CON = 104
ID_ALUNOS = 105
ID_CURSO = 106
ID_PROFESSORES = 107


import sys

from datetime import datetime


import wx
if "2.8" in wx.version():
    import wx.lib.pubsub.setupkwargs
    from wx.lib.pubsub import pub
else:
    
    from wx.lib.pubsub import pub
    
    

import frame_cadastro


import frame_pesquisa


import MySQLdb 
db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")
cursor = db.cursor()

    
class WindowClass(wx.Dialog):    

    def __init__(self):     
        wx.Dialog.__init__(self, None, title="Login") 
  
        self.basic_gui()
        
    def basic_gui(self):
        
        panel = wx.Panel(self)
        
        
        
        self.user=wx.TextCtrl(panel, pos=(100,10), size=(100,30))
        
        
        lbl1=wx.StaticText(panel, pos=(10,20), label='Usuário:', size=(50,30))
        
        
        self.password=wx.TextCtrl(panel, pos=(100,50), size=(100,30),style=wx.TE_PASSWORD)
        
        
        
        lbl2=wx.StaticText(panel, pos=(10,60), label='Senha:', size=(50,30))
        
        
        btn1 = wx.Button(panel, pos=(100,90), label='Login', size=(100,30))
        
        
        
      
        btn1.Bind(wx.EVT_BUTTON, self.onLogin)
        
        self.password.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        
        
        self.SetSize((270,170))
        
        self.SetPosition((450,250))
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        
    def onKeyPress(self, event):
       
        
        keycode = event.GetKeyCode()
        
        if keycode == 13:
        
           self.onLogin(self)
        event.Skip()
           

    def onLogin(self, event):
                         
        valid=''
        username = self.user.GetValue()
  
        password = self.password.GetValue()
        

        if 'ok'=='ok':
     
            
            pub.sendMessage("frameListener", message="show")
            
            self.Destroy()
                     
        else:
            print ("Usuário ou senha inválido!")
          

class MyPanel(wx.Panel):
    
   
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
 

class MainFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    
    
    
    def __init__(self):
  
        wx.Frame.__init__(self, None, title="Menu de opções",style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        
        panel2 = MyPanel(self)
        self.CreateStatusBar()
        menuBar= wx.MenuBar()
        fileMenu = wx.Menu()
        #editMenu = wx.Menu()
        fileMenu2 = wx.Menu()
        fileMenu3 = wx.Menu()

       
        cadpaciente = fileMenu.Append(ID_ALUNOS, 'Cadastro', 'Clique para cadastrar pacientes') 
        
        #cadprofessores = fileMenu.Append(ID_PROFESSORES, 'Professores', 'Clique para cadastrar alunos')
        
       # cadturma = fileMenu.Append(ID_CURSO, 'Curso', 'Clique para cadastrar alunos')
        
        
        ##cadaluno = fileMenu.Append(ID_CAL, 'Alunos', 'Clique para cadastrar um Aluno') 
        
        
        pesquisa = fileMenu2.Append(ID_CON, 'Pesquisar', 'Clique para pesquisar') 
        
        exitItem = fileMenu3.Append(wx.ID_EXIT, 'Sair', 'Sair da aplicação') #status bar texto #wx.ID_EXIT
        
        
        menuBar.Append(fileMenu, '&Cadastro') #Short key
        
        menuBar.Append(fileMenu2, '&Consulta')
        
        menuBar.Append(fileMenu3, '&Sair')
        
         
        self.SetMenuBar(menuBar) 
      
        
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        

        self.Bind(wx.EVT_MENU, self.frame_cadastro, cadpaciente) 
      
        
        self.Bind(wx.EVT_MENU, self.frame_pesquisa, pesquisa)
 
    
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        
      
        self.hora=wx.StaticText(panel2, pos=(280,155), label=(data_e_hora_em_texto), size=(150,50))
        
        
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.hora.SetFont(font)
        
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
  
        self.timer = wx.Timer(self)
               
        self.Bind(wx.EVT_TIMER, self.update, self.timer)
        
        self.timer.Start(1000)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
   
        self.counter=0
        
        self.SetSize((280,345))
        
        self.SetPosition((250,75))
 
        bitmap = wx.Bitmap("./imagens/image.png")
        bitmap = self.scale_bitmap(bitmap, 250, 240)
        control = wx.StaticBitmap(self, -1, bitmap)
        control.SetPosition((10,10))
        control.BestSize
 
        
        pub.subscribe(self.myListener, "frameListener")
 
      
        dlg = WindowClass()
     
        dlg.ShowModal()
   
        
    def scale_bitmap(self,bitmap, width, height):
          
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    
        
    def update(self, event):

        self.timer.Start()  
                      
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        
      
        self.hora.SetLabel(data_e_hora_em_texto)
        
        
        font = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.hora.SetFont(font)
   
            
    def OnClose(self, event):
        
    
        self.Destroy() 
    
        
        
    def myListener(self, message, arg2=None):
        """
        Show the frame
        """
        self.Show()
        
        
        
    def frame_cadastro(self, event):
        
        self.frame1 = frame_cadastro.create(self)
        self.frame1.Show()
        
        event.Skip()   
    
    
    
    def frame_pesquisa(self, event):
        
        self.frame2 = frame_pesquisa.create(self)
        self.frame2.Show()
        
        event.Skip()  

 
    def OnExit(self,e):
        self.Close(True)  
 


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
##################   
    
