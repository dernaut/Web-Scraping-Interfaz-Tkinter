import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from tkinter import *    
from tkinter import ttk
import tkinter as tk
from selenium.webdriver.chrome.service import Service
import time
import threading



lista_links=[]



##############################
#APARTADO DE DATOS
##############################


lista_usuarios=["nombre"]



                 
lista_passwords=["password"]


lista_cuentas=["name account"
                ]



lista_links=["link"
             ]




def interfaz():
    global principal
    principal= Tk()
    principal.geometry('500x500')
    principal.resizable(width=False,height=False)
    principal.configure(bg = 'gray7')
    principal.title("")
    frame = LabelFrame(
    principal,
    text='||| BOT para dar +1 ||| [version 3.0]',
    bg='gray7',
    fg="green yellow",
    font=("Helvetica", "16", "bold")

    )
    f= open("hora.txt", "r")
    global hora_anterior
    global dia_anterior
    hora_anterior=f.readline()
    dia_anterior=f.readline()
    hora_fin=f.readline()
    f.close()
    
    frame.pack(expand=True, fill=BOTH)
    Button(principal, text='Salir', bg='gray7', fg='white',font=("Helvetica", "13", "bold"), width = 100, command=salir).pack(side=BOTTOM)
    global entrada
    entrada= StringVar()
    fecha="Fecha inicio - "+dia_anterior+"Hora inicio - "+hora_anterior+"Hora fin - "+hora_fin
    global label
    label = Label(principal,text="Última vez usado: \n"+fecha,bg='gray7', fg="white",font=("Helvetica", "12", "bold")).place(x=165, y=50)
    principal.title("Total de +1 disponibles: [+"+str(len(lista_usuarios))+"]") 
    #textUsuario = Entry(principal,textvariable=entrada,width=55).place(x=90, y=100)
    Button(principal, text="Comenzar", bg='green yellow', fg='gray7', font=("Helvetica", "12", "bold"), width = 40, command = comenzar).place(x=53, y=140)
    
    global scrollbar
    scrollbar = tk.Scrollbar(principal)
    scrollbar.pack(side="right", fill="y")
    
    global listbox
    listbox = tk.Listbox(principal, yscrollcommand=scrollbar.set, width=60,  justify=CENTER, bg="OliveDrab1", fg="gray7", font=("Helvetica","12", "bold"))
    listbox.pack(side="left", fill="both")
    
    scrollbar.config(command=listbox.yview)
    principal.mainloop()

def salir():
    principal.destroy()
    driver.quit()
    sys.exit()
    
    try:
        driver.close()
    except:
        print("")
    

def comenzar():
    global advertencia
    hora=time.strftime("%I:%M:%S %p")
    dia=time.strftime("%d/%m/%y")
    f= open("hora.txt", "r")
    hora_anterior=f.readline()
    dia_anterior=f.readline()
    f.close()
    if hora > hora_anterior and dia > dia_anterior:
        f=open("hora.txt", "w")
        f.write(hora+'\n')
        f.write(dia+'\n')
        f.close()
        hora=time.strftime("%I:%M:%S %p")
        listbox.insert(0, hora+" || Arrancando BOT")
        hilo2 = threading.Thread(target=partelogica)
        hilo2.start()
    else:
        advertencia = tk.Toplevel(principal)
        advertencia.geometry('300x100')
        advertencia.resizable(width=False,height=False)
        advertencia.configure(bg = 'gray7')
        advertencia.title("No han pasado 24h")
        label = Label(advertencia,text="Adertencia, no han pasado 24h",bg='gray7', fg="white",font=("Helvetica", "12", "bold")).pack()
        Button(advertencia, text="Continuar", bg='red', fg='gray7', font=("Helvetica", "12", "bold"), width = 40, command = comenzar_despues_advertencia).pack()
        Button(advertencia, text="Salir", bg='white', fg='gray7', font=("Helvetica", "12", "bold"), width = 40, command = salir_advertencia).pack()



        
        

    
def comenzar_despues_advertencia():
    hora=time.strftime("%I:%M:%S %p")
    dia=time.strftime("%d/%m/%y")
    f=open("hora.txt", "w")
    f.write(hora+'\n')
    f.write(dia+'\n')
    f.close()
    listbox.insert(0,hora+" || Arrancando BOT")
    hilo01 = threading.Thread(target=partelogica)
    hilo01.start()

    advertencia.destroy()


def salir_advertencia():
    advertencia.destroy()
    
        
def partelogica():
    if (len(lista_cuentas)) > 0:

        PATH=".\chromedriver.exe"







        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        #options.add_argument("disable-gpu")
        options.add_argument("--disable-gpu")
        
        global driver
        driver = webdriver.Chrome(PATH, options=options)



        



        



        

        conteo=1
        for u in range (len (lista_cuentas)):
            contador=0
            principal.title(lista_cuentas[u])
            hora=time.strftime("%I:%M:%S %p")
            listbox.insert(0, hora+" || Cuenta que recibe +1: "+lista_cuentas[u])
            driver.get("https://rol4.fenixzone.com/foro/index.php?action=login")
            o=0
            cien=100
            total=len(lista_cuentas)*len(lista_usuarios)
            
            
            
            while o < (len(lista_usuarios)):
                time.sleep(3)
                
                try:
                    boton=driver.find_element_by_class_name("button_submit")
                    icono=driver.find_element_by_id("dropdownMenuLink")
                    casilla_usuario=driver.find_element_by_name("user")
                    casilla_contra=driver.find_element_by_name("passwrd")
                    icono.click()
                    hora=time.strftime("%I:%M:%S %p")
                    listbox.insert(0, hora+" || Iniciando sesión en la cuenta: "+lista_usuarios[o])
                    casilla_usuario.send_keys(lista_usuarios[o])
                    casilla_contra.send_keys(lista_passwords[o])
                    
                    o=o-1
                    
                    try:
                        boton.submit()
                    except:
                        print("")
                    
                    
                            
                            
                except:
                    contador=contador+1
                    hora=time.strftime("%I:%M:%S %p")
                    listbox.insert(0,  hora+" || Se ha iniciado sesión correctamente")
                    hora=time.strftime("%I:%M:%S %p")
                    listbox.insert(0,  hora+" || Cuenta: "+lista_usuarios[o])
                    driver.get(lista_links[u])
                    time.sleep(4)
                    respeto=driver.find_element_by_link_text('[+Respeto]')
                    respeto.click()
                    driver.implicitly_wait(10)
                    hora=time.strftime("%I:%M:%S %p")
                    listbox.insert(0,  hora+" || Se ha dado +1 correctamente")
                    totalporcent=conteo*cien/total
                    principal.title(lista_cuentas[u]+" "+str(contador)+" || "+str(int(totalporcent))+"%")

                    
                    try:
                        salir=driver.find_element_by_link_text('Salir')
                        hora=time.strftime("%I:%M:%S %p")
                        listbox.insert(0, hora+" || Se ha cerrado la sesión correctamente")
                        salir.click()
                    except:
                        banderita=0
                    try:
                        salir=driver.find_element_by_link_text('Logout')
                        hora=time.strftime("%I:%M:%S %p")
                        listbox.insert(0, hora+" || Se ha cerrado la sesión correctamente")
                        salir.click()
                    except:
                        banderita=0
                   
                    
                o=o+1
            
                
                    
                

                    
                   
            conteo=conteo+1                
            listbox.insert(0,"-------------------------------------------------------------")
            listbox.insert(0, hora+" || Se han dado todos los +1 :)")
            listbox.insert(0, hora+" || TOTAL ENVIADOS: "+str(len(lista_usuarios)))
            listbox.insert(0,"-------------------------------------------------------------") 
            
            
        principal.title("Finalizado")
        hora_fin=time.strftime("%I:%M:%S %p")
        fecha="Fecha inicio - "+dia_anterior+"Hora inicio - "+hora_anterior+"Hora fin - "+hora_fin
        label = Label(principal,text="Última vez usado: \n"+fecha,bg='gray7', fg="white",font=("Helvetica", "12", "bold")).place(x=165, y=50)
        f=open("hora.txt", "rw")
        f.write(hora_fin+'\n')
        f.close()
        driver.close()
        driver.quit()
        sys.exit()





hilo1 = threading.Thread(target=interfaz)
hilo1.start()















