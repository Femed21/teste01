# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSsvk88olrBp0YqM-jSjZ6nNx1xgWjRskSwwGp1F9fcioV8ORwWu2nik3ZjAG5J_xhmEq-Drwh6qUfC/pub?gid=466975264&single=true&output=csv"
db = Ler_GooglePlanilha(url)
Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("TESTE 11")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("MUITAS EMOÇÕES")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("TESTE FAKE")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("É tipo o teste 10, mas é fake")


