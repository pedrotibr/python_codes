#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:22:31 2018

@author: pmesquital
""" 

import sys

import os

import wx

import MySQLdb 

import calendario


from reportlab.pdfgen import canvas

def create(parent):
    return Framew1(parent)
 
class Framew1(wx.Frame):
    def __init__(self, prnt):
       
        
        wx.Frame.__init__(self,id=-1, parent=prnt, title='Cadastro de Pacientes',style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
        self.panel = wx.Panel(self, id=-1)
        
        lblList1 = ['Masculino','Feminino']   
        self.lbl_sexo=wx.StaticText(self.panel, pos=(282,100), label='Sexo:', size=(70,30))
        self.rbox_sexo = wx.RadioBox(self.panel,-1, label = '', pos = (310,80), choices = lblList1 ,majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
          
        self.lbl_prontuario=wx.StaticText(self.panel, pos=(10,20), label='Prontuário:', size=(70,30))
        self.edit_prontuario=wx.TextCtrl(self.panel, pos=(100,10), size=(100,30))
        self.edit_prontuario.Enable(False)
        self.lbl_prontuario.SetFont(wx.Font(wx.FontInfo(10)))
        
        
        
           
        self.lbl_data=wx.StaticText(self.panel, pos=(330,20), label='Data:', size=(30,30))
        self.edit_data=wx.TextCtrl(self.panel, pos=(370,10), size=(100,30))
        self.edit_data.Bind(wx.EVT_SET_FOCUS, self.frame_calendario)
        
        
        self.lbl_data.SetFont(wx.Font(wx.FontInfo(10)))
        
        
                
        self.lbl_heaa=wx.StaticText(self.panel, pos=(10,60), label='HEAA:', size=(50,30))
        self.edit_heaa=wx.TextCtrl(self.panel, pos=(100,50),value='', size=(100,30))
        self.lbl_heaa.SetFont(wx.Font(wx.FontInfo(10)))
            
        
        self.lbl_cns=wx.StaticText(self.panel, pos=(330,60), label='CNS:', size=(30,15))
        self.edit_cns=wx.TextCtrl(self.panel, pos=(370,50), size=(100,30))
        self.lbl_cns.SetFont(wx.Font(wx.FontInfo(10))) 
        
        self.lbl_nome=wx.StaticText(self.panel, pos=(10,95), label='Nome:', size=(50,30))
        self.choices=['']
        self.combobox_nome=wx.ComboBox(self.panel,6,'',(100,90),(150,30),style=wx.CB_SORT, choices=self.choices)
        self.lbl_nome.SetFont(wx.Font(wx.FontInfo(10)))
        
              
        self.lbl_nascimento=wx.StaticText(self.panel, pos=(282,145), label='Nascimento:', size=(70,30))
        self.edit_nascimento=wx.TextCtrl(self.panel, pos=(370,135), size=(100,30))
        self.edit_nascimento.Bind(wx.EVT_SET_FOCUS, self.frame_calendario2)
        
       
       
        self.lbl_nascimento.SetFont(wx.Font(wx.FontInfo(10)))
   
        
        self.lbl_profissao=wx.StaticText(self.panel, pos=(10,140), label='Profissão:', size=(50,30))
        self.edit_profissao=wx.TextCtrl(self.panel, pos=(100,130), size=(150,30))
        self.lbl_profissao.SetFont(wx.Font(wx.FontInfo(10)))
        
                
        self.lbl_rg=wx.StaticText(self.panel, pos=(10,180), label='RG:', size=(50,30))
        self.edit_rg=wx.TextCtrl(self.panel, pos=(100,170), size=(150,30))
        self.lbl_rg.SetFont(wx.Font(wx.FontInfo(10)))
        self.edit_rg.SetHint("digite os números do rg")
        
        self.lbl_orgao_emissor=wx.StaticText(self.panel, pos=(262,180), label='Orgão Emissor:', size=(50,30))
        self.edit_orgao_emissor=wx.TextCtrl(self.panel, pos=(370,170), size=(100,30))
        self.lbl_orgao_emissor.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.lbl_nome_mae=wx.StaticText(self.panel, pos=(10,220), label='Mãe:', size=(50,30))
        self.edit_nome_mae=wx.TextCtrl(self.panel, pos=(100,210), size=(230,30))
        self.lbl_nome_mae.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.lbl_nome_pai=wx.StaticText(self.panel, pos=(335,220), label='Pai:', size=(30,15))
        self.edit_nome_pai=wx.TextCtrl(self.panel, pos=(370,210),value='', size=(250,30))
        self.lbl_nome_mae.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.lbl_cpf=wx.StaticText(self.panel, pos=(10,260), label='CPF:', size=(50,70))
        self.edit_cpf=wx.TextCtrl(self.panel, pos=(100,250), size=(150,30))
        self.lbl_cpf.SetFont(wx.Font(wx.FontInfo(10)))
        self.edit_cpf.SetHint("digite os números do cpf")
        
        
        
               
        self.lbl_telefone=wx.StaticText(self.panel, pos=(10,300), label='Telefone:', size=(50,30))
        self.edit_telefone=wx.TextCtrl(self.panel, pos=(100,290), size=(150,30))
        self.lbl_telefone.SetFont(wx.Font(wx.FontInfo(10)))
                
        self.lbl_celular=wx.StaticText(self.panel, pos=(325,300), label='Celular:', size=(45,30))
        self.edit_celular=wx.TextCtrl(self.panel, pos=(370,290), size=(100,30))
        self.lbl_celular.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.lbl_endereco=wx.StaticText(self.panel, pos=(10,340), label='Endereço:', size=(50,30))
        self.edit_endereco=wx.TextCtrl(self.panel, pos=(100,330), size=(370,30))
        
        self.lbl_bairro=wx.StaticText(self.panel, pos=(10,380), label='Bairro:', size=(50,30))
        self.edit_bairro=wx.TextCtrl(self.panel, pos=(100,370), size=(200,30))
        self.lbl_bairro.SetFont(wx.Font(wx.FontInfo(10)))
        
        
        self.lbl_cep=wx.StaticText(self.panel, pos=(326,380), label='CEP:', size=(30,70))
        self.edit_cep=wx.TextCtrl(self.panel, pos=(370,370), size=(100,30))
        self.lbl_cep.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.lbl_cidade=wx.StaticText(self.panel, pos=(10,420), label='Cidade:', size=(50,70))
        self.edit_cidade=wx.TextCtrl(self.panel, pos=(100,410), size=(200,30))
        self.lbl_cidade.SetFont(wx.Font(wx.FontInfo(10)))
        
        
        self.lbl_estado=wx.StaticText(self.panel, pos=(313,425), label='Estado:', size=(35,20))
        self.lbl_estado.SetFont(wx.Font(wx.FontInfo(10)))
        self.edit_estado=wx.TextCtrl(self.panel, pos=(370,410), size=(100,30))
        
        
        self.lbl_fotografia=wx.StaticText(self.panel, pos=(10,450), label='Fotografia:', size=(50,50))
        self.lbl_fotografia.SetFont(wx.Font(wx.FontInfo(10)))
        
        self.edit_fotografia=wx.TextCtrl(self.panel, pos=(100,450), size=(370,30))
        
        self.edit_fotografia.Bind(wx.EVT_LEFT_UP, self.onfile1)
    
        self.btn_new = wx.Button(self.panel, pos=(70,490), label='Novo', size=(100,30))
        
        self.btn_new.Bind(wx.EVT_BUTTON, self.Onnew)
        
        
        
                     
        self.btn_salvar = wx.Button(self.panel, pos=(170,490), label='Salvar', size=(100,30))
        
        self.btn_salvar.Bind(wx.EVT_BUTTON, self.Onsalvar)
        
        self.btn_salvar.Enable(False)
        
        
        self.btn_editar = wx.Button(self.panel, pos=(370,490), label='Editar', size=(100,30))
        
        self.btn_editar.Bind(wx.EVT_BUTTON, self.Onedit)
                     
        self.btn_excluir = wx.Button(self.panel, pos=(470,490), label='Excluir', size=(100,30))
                
        self.btn_excluir.Bind(wx.EVT_BUTTON, self.Ondelete) 
        
        
        self.btn_imprimir = wx.Button(self.panel, pos=(470,530), label='Imprimir', size=(100,30))
                
        self.btn_imprimir.Bind(wx.EVT_BUTTON, self.Onprint) 
        
        
        self.btn_cancelar = wx.Button(self.panel, pos=(270,490), label='Cancelar', size=(100,30))
                
        self.btn_cancelar.Bind(wx.EVT_BUTTON, self.Oncancel) 
        
        self.btn_cancelar.Enable(False)
   
        
        self.btn_primeiro = wx.Button(self.panel, pos=(70,530), label='<<', size=(100,30))
        
       
        
        self.btn_primeiro.Bind(wx.EVT_BUTTON, self.Onfirst)
        
        self.btn_anterior = wx.Button(self.panel, pos=(170,530), label='<', size=(100,30))  
        
        self.btn_anterior.Bind(wx.EVT_BUTTON, self.Onant)
        
        self.btn_proximo = wx.Button(self.panel, pos=(270,530), label='>', size=(100,30))
        
        self.btn_proximo.Bind(wx.EVT_BUTTON, self.Onprox)
        
        self.btn_ultimo = wx.Button(self.panel, pos=(370,530), label='>>', size=(100,30)) 
        
        self.btn_ultimo.Bind(wx.EVT_BUTTON, self.Onlast)
        
        self.btn_fotografia = wx.Button(self.panel, pos=(500,135), label='Imagem', size=(120,30)) 
        
        self.btn_fotografia.Bind(wx.EVT_BUTTON, self.onfile1)
        
        self.btn_fotografia.Enable(False)

        self.nome_sql = ''
        self.SetSize((650,610))
        
        self.SetPosition((350,75))
        
          
        self.combobox_nome.Bind(wx.EVT_KEY_UP, self.onKeyPress) 
  
   
        self.bitmap = wx.Bitmap()
        self.control = wx.StaticBitmap()
        
        
        self.Onfirst(self)
        self.editmode(self,False)
        
        self.edit=False
        self.new=False
   
        
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
        self.calendario = None
        
        
    def frame_calendario(self, event):
           
        if not self.calendario:    
            self.calendario = calendario.create(self)
            
        self.calendario.Bind(wx.EVT_CLOSE,self.set_date())
        
        self.calendario.Show(True)
   
        event.Skip      

     
    def set_date(self):

            
        x=str(self.calendario.data())
        #x=str(self.calendario.data)
        print("set_date: "+x)
        
        self.edit_data.SetValue(x)
        
        self.data_selecionada=x
        
        
        
    def frame_calendario2(self, event):
           
        if not self.calendario:    
            self.calendario = calendario.create(self)
            
        self.calendario.Bind(wx.EVT_CLOSE,self.set_date2())
        
        self.calendario.Show(True)
   
        event.Skip      

     
    def set_date2(self):

            
        x=str(self.calendario.data())
   
        
        self.edit_nascimento.SetValue(x)
        
        self.data_selecionada=x    
        

    def OnClose(self, event):
        
        #os.system('rm *.png')
             
        self.Destroy()     
        
        
    def find_user(self,user):
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")
        cursor = db.cursor()
        
        cursor.execute('select * from database.CLIENTES where nome like "%'+user+'%"')
        row=cursor.fetchone()
        
        self.edit_prontuario.SetValue(str(row[0]))        
        self.edit_heaa.SetValue(str(row[19]))
        self.edit_cns.SetValue(str(row[17]))
        
        self.combobox_nome.SetValue(str(row[1]))
        
        self.edit_nascimento.SetValue(str(row[10]))        
        self.edit_profissao.SetValue(str(row[16]))
        self.edit_rg.SetValue(str(row[11]))
        self.edit_orgao_emissor.SetValue(str(row[12]))
        
        data=(str(row[17]))
        if (data != "None"):
            data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
            self.edit_data.SetValue(data)
        
        self.edit_nome_mae.SetValue(str(row[15]))        
        self.edit_nome_pai.SetValue(str(row[14]))
        self.edit_cpf.SetValue(str(row[13]))
        self.edit_telefone.SetValue(str(row[7]))
        self.edit_celular.SetValue(str(row[8]))        
        self.edit_endereco.SetValue(str(row[2]))
        self.edit_bairro.SetValue(str(row[3]))
        self.edit_cep.SetValue(str(row[6]))
        self.edit_cidade.SetValue(str(row[4]))
        self.edit_estado.SetValue(str(row[5]))
        #self.edit_fotografia.SetValue(str(row[18]).decode("latin1"))
        self.edit_fotografia.SetValue(str(row[18]))
          
        self.setimage( self.edit_fotografia.GetValue())
            
    
     
    def setimage(self,image):
             
        try:    
            if self.control:
                self.control.Destroy()
            
         
            len_image=int(len(image))
        
            if (len_image > 4):
        #if (image != "") and (image != "None"):
            
                self.bitmap.LoadFile(image)
                self.bitmap = self.scale_bitmap(self.bitmap, 120, 120)
                self.control = wx.StaticBitmap(self, -1, self.bitmap, pos=(500, 10))
                
        except Exception:
            
            dialog = wx.MessageDialog(self,("Falha carregar imagem."),("Aviso"), wx.OK | wx.ICON_WARNING)
            dialog.ShowModal() == wx.ID_OK
            dialog.Destroy()
            
            
        
    def Oncancel(self,e):
        
        self.editmode(self,False)
 
                
        self.btn_new.Enable(True)
        
               
        self.btn_editar.Enable(True)
        self.btn_excluir.Enable(True)
        
        
           
        self.btn_primeiro.Enable(True)
        self.btn_ultimo.Enable(True)
        self.btn_proximo.Enable(True)
        self.btn_anterior.Enable(True)
        
        self.btn_imprimir.Enable(True)
        
        self.btn_salvar.Enable(False)
        self.btn_cancelar.Enable(False)
        
        
        self.btn_fotografia.Enable(False)
        
        
        self.edit=False
        self.new=False
        
        self.Onant(self)
        
        self.btn_fotografia.Enable(False)
        
  
    def editmode(self, event,x):
        
       
        #self.edit_prontuario.Enabled(x)
        
        self.rbox_sexo.Enable(x)
        self.edit_data.Enable(x)
        self.edit_heaa.Enable(x)   
        self.edit_cns.Enable(x)
        self.combobox_nome.Enable(x)
        self.edit_nascimento.Enable(x)
        self.edit_profissao.Enable(x)
        self.edit_rg.Enable(x)
        self.edit_orgao_emissor.Enable(x)
        self.edit_nome_mae.Enable(x)
        self.edit_nome_pai.Enable(x)
        self.edit_cpf.Enable(x)
        self.edit_telefone.Enable(x)
        self.edit_celular.Enable(x)
        self.edit_endereco.Enable(x)
        self.edit_bairro.Enable(x)
        self.edit_cep.Enable(x)
        self.edit_cidade.Enable(x)
        self.edit_estado.Enable(x)
        self.edit_fotografia.Enable(x)

        self.edit=(x)
            
    def onfile1(self, event):   

        wildcard = "Arquivos de imagem (*.png;*.jpg;*.jpeg)|*.png;*.jpg;*.jpeg"
        dlg = wx.FileDialog(self, "Escolha o arquivo", os.getcwd(), "", wildcard, wx.FD_OPEN)
        #dlg = wx.FileDialog(self, "Escolha a pasta", os.getfolder(), "", wildcard, wx.FD_OPEN)
        #dlg = wx.DirDialog (None, "Escolha a pasta", "", wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
		
        if dlg.ShowModal() == wx.ID_OK: 
           
           self.setimage(dlg.GetPath())
            

        
        self.edit_fotografia.SetValue(dlg.GetPath())  
  
        
        dlg.Destroy() 

        
    def onKeyPress(self, event):

        keycode = event.GetKeyCode()
  
                              
        if keycode == 13 :
     
            self.Onconsultar(self)
            
        
        event.Skip()
        
        
    def Onconsultar(self, e):
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")
        
        cursor = db.cursor()
        
        self.nome_sql=self.combobox_nome.GetValue()
        
        
        self.combobox_nome.Clear  
        
       
          
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
        
        
        numrows=cursor.execute('select * from database.CLIENTES where nome like "%'+self.nome_sql+'%"')
        
        row=cursor.fetchone()
        
                   
        self.lista=[]

        for num in range (0, numrows):
            
            self.lista.append(row[1])
            row=cursor.fetchone()

        
        self.combobox_nome.Clear     
        self.combobox_nome.Append(self.lista)
        
        db.close()
     
  
    def oncombo(self, e): 
        
        self.a1=self.cod_curso.GetValue() 
   
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
        
        
        cursor.execute('select * from database.CLIENTES where nome like "%'+self.a1+'%"')
        
        row=cursor.fetchone()  
  
        
              
        self.edit_prontuario.SetValue(str(row[0]))
            
      
        self.edit_heaa.SetValue(str(row[20]))
   
        self.edit_cns.SetValue(str(row[19]))
            
        self.combobox_nome.SetValue(str(row[1]))
            
        self.edit_nascimento.SetValue(str(row[10]))        
        self.edit_profissao.SetValue(str(row[16]))
        self.edit_rg.SetValue(str(row[11]))
        self.edit_orgao_emissor.SetValue(str(row[12]))
        
        data=(str(row[17]))
        if (data != "None"):
            data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
            self.edit_data.SetValue(data)
            
        self.edit_nome_mae.SetValue(str(row[15]))        
        self.edit_nome_pai.SetValue(str(row[14]))
        self.edit_cpf.SetValue(str(row[13]))
        self.edit_telefone.SetValue(str(row[7]))
        self.edit_celular.SetValue(str(row[8]))        
        self.edit_endereco.SetValue(str(row[2]))
        self.edit_bairro.SetValue(str(row[3]))
        self.edit_cep.SetValue(str(row[6]))
        self.edit_cidade.SetValue(str(row[4]))
        self.edit_estado.SetValue(str(row[5]))
        self.edit_fotografia.SetValue(str(row[21]))
        
        self.lista=[]
        
        db.close()
                     
       
    def scale_bitmap(self,bitmap, width, height):
        
                
        image = wx.Bitmap.ConvertToImage(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result
        
    
        
    def Onprint(self, e):
          
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
        
        numrows = int(cursor.rowcount)

        
        c = canvas.Canvas("./Dados_paciente.pdf")
    
            
        c.drawString(10,650,(self.lbl_prontuario.GetLabel()))
        c.drawString(110,650,(self.edit_prontuario.GetValue()))
        
        c.drawString(300,650,(self.lbl_data.GetLabel()))
        c.drawString(350,650,(self.edit_data.GetValue()))
        
        c.drawString(10,600,(self.lbl_heaa.GetLabel()))
        c.drawString(80,600,(self.edit_heaa.GetValue()))
        
        c.drawString(300,600,(self.lbl_cns.GetLabel()))
        c.drawString(350,600,(self.edit_cns.GetValue()))
        
        
        
        c.drawString(10,550,(self.lbl_nome.GetLabel()))
        c.drawString(80,550,(self.combobox_nome.GetValue()))
       
        
        
        c.drawString(10,500,(self.lbl_profissao.GetLabel()))
        c.drawString(80,500,(self.edit_profissao.GetValue()))
        
        c.drawString(300,500,(self.lbl_nascimento.GetLabel()))
        c.drawString(380,500,(self.edit_nascimento.GetValue()))
        
        
        c.drawString(10,450,(self.lbl_rg.GetLabel()))
        c.drawString(80,450,(self.edit_rg.GetValue()))
        
        c.drawString(300,450,(self.lbl_orgao_emissor.GetLabel()))
        c.drawString(390,450,(self.edit_orgao_emissor.GetValue()))
        
        c.drawString(10,400,(self.lbl_nome_pai.GetLabel()))
        c.drawString(80,400,(self.edit_nome_pai.GetValue()))
        
        c.drawString(300,400,(self.lbl_nome_mae.GetLabel()))
        c.drawString(380,400,(self.edit_nome_mae.GetValue()))
        
        c.drawString(10,350,(self.lbl_cpf.GetLabel()))
        c.drawString(80,350,(self.edit_cpf.GetValue()))
        
        c.drawString(10,300,(self.lbl_telefone.GetLabel()))
        c.drawString(80,300,(self.edit_telefone.GetValue()))
        
        c.drawString(300,300,(self.lbl_celular.GetLabel()))
        c.drawString(380,300,(self.edit_celular.GetValue()))
        
        c.drawString(10,250,(self.lbl_endereco.GetLabel()))
        c.drawString(80,250,(self.edit_endereco.GetValue()))
        
        c.drawString(10,200,(self.lbl_bairro.GetLabel()))
        c.drawString(80,200,(self.edit_bairro.GetValue()))
        
        c.drawString(300,200,(self.lbl_cep.GetLabel()))
        c.drawString(380,200,(self.edit_cep.GetValue()))
        
        c.drawString(10,150,(self.lbl_cidade.GetLabel()))
        c.drawString(80,150,(self.edit_cidade.GetValue()))
        
        c.drawString(300,150,(self.lbl_estado.GetLabel()))
        c.drawString(380,150,(self.edit_estado.GetValue()))
        
       
  
        c.drawImage("./imagens/logo_pillar.jpg", 10, 750, width=72, height=72)
        
        c.drawImage("./imagens/alvaro_alvim.png", 140, 750, width=150, height=72)
            
        c.drawImage("./imagens/fbpn.png", 340, 750, width=150, height=72)
            
        c.setFontSize(16)
        c.drawString(510,790,("Registro de"))
            
        c.setFontSize(16)
        c.drawString(510,770,("Prontuários"))
            
  
            
        line="_________________________________________________________________________________________________________"  
  
        c.setFontSize(20)
        c.drawString(0,750,(line))
  
               
        cabecalho="Prontuário Médico"
        c.setFontSize(20)
        
                
        c.drawString(200,700,(cabecalho))
        
        
        c.showPage()
        
               
        c.save()
        
        os.system("start ./Dados_paciente.pdf&") 
        
        
        db.close()  
        
                    
    def Onprox(self, e): 
               
       
        num = str(self.edit_prontuario.GetValue())
        
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
  
        cursor.execute("select * from database.CLIENTES where codigo > (%s) order by codigo ASC", [num])
        
        row= cursor.fetchone()
 
        if (num) == str(self.last()):
            
            dialog = wx.MessageDialog(self,("Este é o último registro."),("Informação"), wx.OK | wx.ICON_QUESTION)
            result = dialog.ShowModal()  
           
        elif (num) != str(self.last()):          
        
            self.edit_prontuario.SetValue(str(row[0]))
            
            
            #self.edit_heaa.SetValue(str(row[19]))
            self.edit_heaa.SetValue(str(row[20]))
            
            
            #self.edit_cns.SetValue(str(row[18]))
            self.edit_cns.SetValue(str(row[19]))
            
            self.combobox_nome.SetValue(str(row[1]))
            
            self.edit_nascimento.SetValue(str(row[10]))        
            self.edit_profissao.SetValue(str(row[16]))
            self.edit_rg.SetValue(str(row[11]))
            self.edit_orgao_emissor.SetValue(str(row[12]))
            
       
            data=(str(row[17]))
            #print(data)
            if (data != "None"):
                data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
                self.edit_data.SetValue(data)
   
            self.edit_nome_mae.SetValue(str(row[15]))        
            self.edit_nome_pai.SetValue(str(row[14]))
            self.edit_cpf.SetValue(str(row[13]))
            self.edit_telefone.SetValue(str(row[7]))
            self.edit_celular.SetValue(str(row[8]))        
            self.edit_endereco.SetValue(str(row[2]))
            self.edit_bairro.SetValue(str(row[3]))
            self.edit_cep.SetValue(str(row[6]))
            self.edit_cidade.SetValue(str(row[4]))
            self.edit_estado.SetValue(str(row[5]))
            self.edit_fotografia.SetValue(str(row[21]))
            if (str(row[20])) != "None":
              
                self.rbox_sexo.SetSelection(int(row[20]))
        
            self.setimage( self.edit_fotografia.GetValue())
            
            db.close()
            
            
    def last(self):
        
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
   
        cursor.execute("select * from database.CLIENTES order by codigo DESC")
        row= cursor.fetchone()

        db.close()
        
        return (str(row[0])) 

    def first(self):
        
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
        
        cursor.execute("select * from database.CLIENTES order by codigo ASC")
        row= cursor.fetchone()
        
   
        return (str(row[0])) 
    
        db.close()

        
    def Onant(self, e): 
              
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
        
        
        num = str(self.edit_prontuario.GetValue())
        
        cursor.execute("select * from database.CLIENTES where codigo < (%s) order by codigo DESC", [num])
        
        row= cursor.fetchone()
    
        first=str(self.first())
     
        
        if (num) != str(first):
            
            
            self.edit_prontuario.SetValue(str(row[0]))   
            
            self.edit_heaa.SetValue(str(row[20]))
            
       
            self.edit_cns.SetValue(str(row[19]))
            
            self.combobox_nome.SetValue(str(row[1]))
            
            self.edit_nascimento.SetValue(str(row[10]))        
            self.edit_profissao.SetValue(str(row[16]))
            self.edit_rg.SetValue(str(row[11]))
            self.edit_orgao_emissor.SetValue(str(row[12]))
            data=(str(row[17]))
            if (data != "None"):
                data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
                self.edit_data.SetValue(data)
        
            
            self.edit_nome_mae.SetValue(str(row[15]))        
            self.edit_nome_pai.SetValue(str(row[14]))
            self.edit_cpf.SetValue(str(row[13]))
            self.edit_telefone.SetValue(str(row[7]))
            self.edit_celular.SetValue(str(row[8]))        
            self.edit_endereco.SetValue(str(row[2]))
            self.edit_bairro.SetValue(str(row[3]))
            self.edit_cep.SetValue(str(row[6]))
            self.edit_cidade.SetValue(str(row[4]))
            self.edit_estado.SetValue(str(row[5]))
            #self.edit_fotografia.SetValue(str(row[18]).decode("latin1"))
            self.edit_fotografia.SetValue(str(row[21]))
            
            if (str(row[20])) != "None":
           
                self.rbox_sexo.SetSelection(int(row[20]))
        
            
            self.setimage( self.edit_fotografia.GetValue())
            

        elif (num) == str(first):
            
            dialog = wx.MessageDialog(self,("Este é o primeiro registro."),("Informação"),
                                      wx.OK | wx.ICON_QUESTION)
            result = dialog.ShowModal()
            
            
            
        db.close()
    
    def Onlast(self,e): 
          
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
  
        num = str(int(cursor.rowcount))
         
        cursor.execute("select * from database.CLIENTES order by codigo DESC")
        
        row= cursor.fetchone()
        numrows = int(cursor.rowcount)
  
       
        self.edit_prontuario.SetValue(str(row[0])) 
        
        self.edit_heaa.SetValue(str(row[20]))
        
        self.edit_cns.SetValue(str(row[19]))
            
        self.combobox_nome.SetValue(str(row[1]))
            
        self.edit_nascimento.SetValue(str(row[10]))        
        self.edit_profissao.SetValue(str(row[16]))
        self.edit_rg.SetValue(str(row[11]))
        self.edit_orgao_emissor.SetValue(str(row[12]))
        data=(str(row[17]))
        if (data != "None"):
            data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
            self.edit_data.SetValue(data)
            
        self.edit_nome_mae.SetValue(str(row[15]))        
        self.edit_nome_pai.SetValue(str(row[14]))
        self.edit_cpf.SetValue(str(row[13]))
        self.edit_telefone.SetValue(str(row[7]))
        self.edit_celular.SetValue(str(row[8]))        
        self.edit_endereco.SetValue(str(row[2]))
        self.edit_bairro.SetValue(str(row[3]))
        self.edit_cep.SetValue(str(row[6]))
        self.edit_cidade.SetValue(str(row[4]))
        self.edit_estado.SetValue(str(row[5]))
        self.edit_fotografia.SetValue(str(row[21]))
        if (str(row[20])) != "None":
              
            self.rbox_sexo.SetSelection(int(row[20]))
      
        self.setimage( self.edit_fotografia.GetValue())


        dialog = wx.MessageDialog(self,("Este é o último registro."),("Informação"),
                                      wx.OK | wx.ICON_QUESTION)
        result = dialog.ShowModal()
        return (row[0])
    
    
        db.close()
            
            
    def Onfirst(self,e): 
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
  
        
        cursor.execute("select * from database.CLIENTES order by codigo ASC")
        row=cursor.fetchone() 
            
        self.edit_prontuario.SetValue(str(row[0]))        
        
        #self.edit_heaa.SetValue(str(row[19]))
        self.edit_heaa.SetValue(str(row[20]))
        
        #self.edit_cns.SetValue(str(row[17]))
        self.edit_cns.SetValue(str(row[19]))
            
        self.combobox_nome.SetValue(str(row[1]))
            
        self.edit_nascimento.SetValue(str(row[10]))        
        self.edit_profissao.SetValue(str(row[16]))
        self.edit_rg.SetValue(str(row[11]))
        self.edit_orgao_emissor.SetValue(str(row[12]))
     
        
        data=(str(row[17]))
       
        if (data != "None"):
            data=data[0]+data[1]+data[2]+data[3]+data[4]+data[5]+data[6]+data[7]+data[8]+data[9]
            self.edit_data.SetValue(data)
            
        self.edit_nome_mae.SetValue(str(row[15]))        
        self.edit_nome_pai.SetValue(str(row[14]))
        self.edit_cpf.SetValue(str(row[13]))
        self.edit_telefone.SetValue(str(row[7]))
        self.edit_celular.SetValue(str(row[8]))        
        self.edit_endereco.SetValue(str(row[2]))
        self.edit_bairro.SetValue(str(row[3]))
        self.edit_cep.SetValue(str(row[6]))
        self.edit_cidade.SetValue(str(row[4]))
        self.edit_estado.SetValue(str(row[5]))
    
        self.edit_fotografia.SetValue(str(row[21]))  
        if (str(row[20])) != "None":
                self.rbox_sexo.SetSelection(int(row[20]))
                
        
        self.setimage( self.edit_fotografia.GetValue())
            
    
        
        return(str(row[0]))
   
    
        db.close()
        

    def Onsalvar(self, e):
        
        
        
        db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

        cursor = db.cursor()
 
        
        status_cpf=False
        status_rg=False
 
        
        self.btn_new.Enable(True)
        
        self.btn_salvar.Enable(False)
        self.btn_cancelar.Enable(False)
        
        self.btn_editar.Enable(True)
        self.btn_excluir.Enable(True)
        
        
        self.btn_primeiro.Enable(True)
        self.btn_ultimo.Enable(True)
        self.btn_proximo.Enable(True)
        self.btn_anterior.Enable(True)
        
        self.btn_imprimir.Enable(True)
        
        self.rbox_sexo.Enable(True)
        
         
        codigo=str(self.edit_prontuario.GetValue())        
        heaa=str(self.edit_heaa.GetValue())
        cns=str(self.edit_cns.GetValue())
        
        nome=str(self.combobox_nome.GetValue())
        
        nascimento=str(self.edit_nascimento.GetValue())
        profissao=str(self.edit_profissao.GetValue())
       
        
        if len(self.edit_rg.GetValue()) == 9:
             rg=str(self.edit_rg.GetValue())   
             status_rg=True
        else:
           
            dialog = wx.MessageDialog(self,("RG inválido."),("Informação"), wx.OK | wx.ICON_QUESTION)
            dialog.ShowModal()
            rg=str(self.edit_rg.GetValue())
            
            
            self.edit_rg.SetFocus()
        
        orgao_emissor=str(self.edit_orgao_emissor.GetValue())
        data=str(self.edit_data.GetValue())
        
        mae=str(self.edit_nome_mae.GetValue())
        pai=str(self.edit_nome_pai.GetValue())
        
        
        if len(self.edit_cpf.GetValue()) == 11:
            cpf=str(self.edit_cpf.GetValue())
            status_cpf=True
        else:
           
            dialog = wx.MessageDialog(self,("CPF inválido."),("Informação"),
                                      wx.OK | wx.ICON_QUESTION)
            dialog.ShowModal()
            
            cpf=str(self.edit_cpf.GetValue())
            
            self.edit_cpf.SetFocus()

        
        telefone=str(self.edit_telefone.GetValue())
        celular=str(self.edit_celular.GetValue())
        #endereco=str(self.edit_endereco.GetValue()).decode("latin1")
        endereco=str(self.edit_endereco.GetValue())
        bairro=str(self.edit_bairro.GetValue())
        cep=str(self.edit_cep.GetValue())
        cidade=str(self.edit_cidade.GetValue())
        estado=str(self.edit_estado.GetValue())
        sexo=str(self.rbox_sexo.GetSelection())
        fotografia=str(self.edit_fotografia.GetValue())
        fotografia=(fotografia.replace('\\', '/', 10))
        contato=""
        
  
 
        if (self.edit == True):# and (status_cpf) and (status_rg):
                       
           
            cursor.execute('UPDATE CLIENTES SET nome = "'+nome+'", endereco = "'+endereco+'", bairro = "'+bairro+'", cidade = "'+cidade+'",estado = "'+estado+'",cep = "'+cep+'", telefone1 = "'+telefone+'", telefone2 = "'+celular+'", nascimento = "'+nascimento+'", rg = "'+rg+'", emissor = "'+orgao_emissor+'",cpf = "'+cpf+'",pai = "'+pai+'",mae = "'+mae+'",profissao = "'+profissao+'", data = "'+data+'", fotografia = "'+fotografia+'",cns = "'+cns+'", heaa = "'+heaa+'"  where "'+codigo+'" = codigo' )
            
            db.commit()
            row=cursor.fetchone()
          
            
            
        if (self.new == True):
           
           
          
            sql="INSERT INTO CLIENTES VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
            
            values=(codigo,nome,endereco,bairro,cidade,estado,cep,telefone,celular,contato,nascimento,rg,orgao_emissor,cpf,pai,mae,profissao,data,cns,heaa,sexo,fotografia)
           
            cursor.execute(sql,values)
            
            db.commit()
            
      
        self.editmode(self,False)
            
        self.edit=False
        self.new=False
        
        self.btn_fotografia.Enable(False)
        
        db.close()
        
        
        
    def Onnew(self, e):
        
        
        self.editmode(self,True)
        self.new=True
        
        self.rbox_sexo.SetSelection(0)
        
        self.btn_fotografia.Enable(True)
        
        self.btn_new.Enable(False)
        
        self.btn_salvar.Enable(True)
        self.btn_cancelar.Enable(True)
        
        self.btn_editar.Enable(False)
        self.btn_excluir.Enable(False)
        
        self.btn_primeiro.Enable(False)
        self.btn_ultimo.Enable(False)
        self.btn_proximo.Enable(False)
        self.btn_anterior.Enable(False)
        
        self.btn_imprimir.Enable(False)
        
        
        num=(int(self.last()))
           
       
        self.edit_prontuario.SetValue(str(num+1))        
        self.edit_heaa.SetValue("")
        self.edit_cns.SetValue("")
        
        self.combobox_nome.SetValue("")
        
        self.edit_nascimento.SetValue("")        
        self.edit_profissao.SetValue("")
        self.edit_rg.SetValue("")
        self.edit_orgao_emissor.SetValue("")
        self.edit_data.SetValue("")
        
        self.edit_nome_mae.SetValue("")        
        self.edit_nome_pai.SetValue("")
        self.edit_cpf.SetValue("")
        self.edit_telefone.SetValue("")
        self.edit_celular.SetValue("")        
        self.edit_endereco.SetValue("")
        self.edit_bairro.SetValue("")
        self.edit_cep.SetValue("")
        self.edit_cidade.SetValue("")
        self.edit_estado.SetValue("")
        self.edit_fotografia.SetValue("")
        
         
        
     
    def Onedit(self, e):
        

        self.editmode(self,True)
        self.edit=True
        
        self.combobox_nome.SetFocus()
        
        
        self.btn_fotografia.Enable(True)
              
        self.btn_new.Enable(False)
        
        self.btn_salvar.Enable(True)
        self.btn_cancelar.Enable(True)
        
        self.btn_editar.Enable(False)
        self.btn_excluir.Enable(False)
        
        self.btn_primeiro.Enable(False)
        self.btn_ultimo.Enable(False)
        self.btn_proximo.Enable(False)
        self.btn_anterior.Enable(False)
   
       
        self.btn_imprimir.Enable(False)
        
       
    def Ondelete(self, e):
            
        
            db=MySQLdb.connect(host="127.0.0.1",port=3306,user="user",passwd="password",db="database")

            cursor = db.cursor()
       

            dialog = wx.MessageDialog(self,("Você quer realmente deletar esse registro?"),("Confirma exclusão"),
                                      wx.YES_NO | wx.ICON_QUESTION)
            remove = dialog.ShowModal() == wx.ID_YES
            dialog.Destroy()

            if remove:
                    num = str(self.edit_prontuario.GetValue())
                    #print (num)
                   
                    cursor.execute("delete from CLIENTES where codigo = %s",[num])
                    db.commit()
                    self.Onant(0)
  
                
            e.Skip()    
        
        
            
            self.edit=False
            self.new=False
           
            self.editmode(self,False)
            
            self.Onant
            
            db.close()
        
     
