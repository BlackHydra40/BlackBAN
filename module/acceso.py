import os
import sys
import time

#COLORES
rojo = '\033[31;1m'
azul = '\033[34;1m'
verde = '\033[32;1m'
amarillo = '\033[33;1m'
morado = '\033[35;1m'
celeste = '\033[36;1m'
plomo = '\033[30;1m'
close = '\033[0m'


username = 'BLACKHYDRANGKS'      
password = 'kuroko'

print("versão 1.3")
os.system ("toilet -f big 'NICK' -F gay | lolcat")
print(amarillo)
nick = str(input(' COLOQUE SEU NICK  : '))

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

os.system("clear")
os.system ("toilet -f big 'LOGIN' -F gay | lolcat")
def main():
    uname = str(input("\n\033[33;1mUSUARIO : \033[32;1m"))
    if uname == username:
        pwd = str(input("\n\033[33;1mSENHA : \033[32;1m"))

        if pwd == password:
            os.system("clear")
            time.sleep(2)
            print('ENTRANDO NO TELEGRAM')
            os.system("xdg-open https://t.me/MS40_canal &> /dev/null && sleep 10")
            os.system("clear")
            os.system ("toilet -f big 'BlackBAN' -F gay | lolcat")
            print("\n\033[32;1m OLÁ \033[32;1m ★",nick,"★\033[32;1m BEM VINDO AO BLACKBAN \n  FERRAMENTO VOLTADO A METODOS E ESQUEMAS DE BANIMENTO\n")
            time.sleep(2)
            print(verde,'+————————————————————————————————————————————————————————————+')
            print(verde)
            print('  [ 1 ] BANIR NUMERO DE WHATSAPP [ON]')
            print('  [ 2 ] BLINDAR NUMERO DE WHATSAPP [ON]')
            print('  [ 3 ] DESBANIR NUMERO DE WHATSAPP [ON]')
            print('  [ 4 ] DESATIVAR CONTA DE INSTAGRAM [OFF]')
            print('  [ 5 ] DESATIVAR CONTA DE FACEBOOK [OFF]')
            print('  [ 5 ] DESBANIR CONTA DO TELEGRAM [ON] ') 
            print('  [ 6 ] WHATSAPP MODIFICADOS/IMUNES [ON] ')
            print('  [ 6 ] DATABASE WHATSAPP [ON] ')
            print('  [ 24 ] REDES SOCIAIS E SOBRE')
            

        else:
            os.system("clear")
            print("\n\033[1;31m SINTO MUITO " , nick, " O USUARIO OU SENHA ESTA INCORRETO !!!\033[00m")
            print(azul, "MEU CONTATO PARA AJUDA @ms4010 (telegram)")
            time.sleep(3.3)
            os.system("clear")
            restart()

    else:
        os.system("clear")
        print("\n\033[1;31m SINTO MUITO " , nick, " O USUARIO OU SENHA ESTA INCORRETO !!!\033[00m")
        print(azul, "\nMEU CONTATO PARA AJUDA @ms4010 (telegram)")
        time.sleep(3.3)
        os.system("clear")
        restart()

try:
    main()
except KeyboardInterrupt:
       print(azul, "\n\033[34;1m [!] Ctrl+C precionado, BlackBAN interrompido!\033[00m")
