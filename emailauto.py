# A principal função deste código, é ter a capacidade de enviar email automaticos, eu usei o pyautogui onde posso
automatizar o teclado e o mouse, e para ter a informação da onde o mouse deveria clicar e usei o mouseInfo.


import pyautogui
from time import sleep

#Usando o mouseInfo para obter os parametros para fazer a pesquisa no OperaGx

pyautogui.click(1573, 189, duration=3)
pyautogui.press("enter")
pyautogui.click(1103,258, duration=5)

# Abrir o arquivo e ler as linhas
with open('empresas.txt.txt', 'r') as arquivo:
    for linha in arquivo:
        # Dividindo a linha nos espaços em branco e removendo espaços extras
        destinatario, assunto, corpo = map(str.strip, linha.split("\\"))
        
        # Infos do destinatario
        pyautogui.click(1147, 412, duration=6)
        pyautogui.write(destinatario)
        
        # Introdução
        pyautogui.click(1697, 460, duration=6)
        pyautogui.write(assunto)
        
        # Corpo do email
        pyautogui.click(1177, 526, duration=6)  
        
        pyautogui.write(corpo)
        
        # Clicar em enviar 
        pyautogui.click(1190, 958, duration=4)

        # Repetir o processo 
        pyautogui.click(1103,258, duration=5)

        sleep(1)
