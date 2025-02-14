#---_ Lyrics Finder CLI 1.0 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---
import requests
import os

#Função logo
def logo():
  print("███████████████████████████████████")
  print("██████████ Lyrics Finder ██████████")
  print("███████████████████████████████████\n")
logo()
#Tela de digitação 
banda = input("Digite a Banda: ")
musica = input("Digite a Música: ")
url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
response = requests.get(url)
os.system("cls")
#Tratativa Musica não encontrada 
try:
  print(f"Música : {musica}\nBanda : {banda}\n \n")
  print(response.json()['lyrics'])
except KeyError:
  print("Letra não encontrada.")
except Exception as e:
  print(f"Ocorreu um erro: {e}")

input(" ")