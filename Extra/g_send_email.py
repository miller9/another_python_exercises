# -*- coding: utf-8 -*- 
import smtplib 
 
remitente = "Desde m <asdasdasd@gmail.com>" 
destinatario = "m <12343sfreeg@gmail.com>" 
asunto = "E-mail HTML enviado desde Python" 
mensaje = """Hola!<br/> <br/> 
Este es un <b>e-mail</b> enviando desde <b>Python</b> 
"""
 
email = """From: %s 
To: %s 
MIME-Version: 1.0 
Content-type: text/html 
Subject: %s 
 
%s
""" % (remitente, destinatario, asunto, mensaje) 
try: 
    smtp = smtplib.SMTP('localhost') 
    smtp.sendmail(remitente, destinatario, email) 
    print ("Correo enviado")
except: 
    print ("""Error: el mensaje no pudo enviarse.
    		Compruebe que sendmail se encuentra instalado en su sistema""")
