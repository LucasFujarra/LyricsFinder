#---_ Lyrics Finder 1.0 _---
#---_ By Lucas Fujarra _---
#---_ https://github.com/LucasFujarra _---

import requests
import streamlit as st

#função Buscar música
def buscar(banda, musica):
    url = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(url)
    letra = response.json()['lyrics'] if response.status_code == 200 else ""
    return letra

#Itens da tela StreamLit
st.image("https://i.imgur.com/RixVwKA.jpeg")
st.title("Buscar Letras")

banda = st.text_input("Digite a Banda: ", key="banda")
musica = st.text_input("Digite a Música: ", key="musica")
pesquisar = st.button("Pesquisar")

#Tratativa Musica não encontrada 
if pesquisar :
    letra = buscar(banda, musica)
    if letra:
        st.success("Letra encontrada")
        st.text(letra)
    else:
        st.error("Letra não encontrada")