import streamlit as st
import google.generativeai as genai 
import os 

# --- Configurazione della API Key ---
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    st.error("ERRORE: La variabile d'ambiente GOOGLE_API_KEY non è impostata.")
    st.write("Assicurati di averla configurata correttamente (export GOOGLE_API_KEY=\"TUA_CHIAVE\")")
    st.stop() # Ferma l'esecuzione dello script Streamlit

try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"ERRORE durante la configurazione dell'API: {e}")
    st.stop()

# --- Inizializzazione del Modello Gemini ---
# Usiamo il modello che abbiamo verificato essere veloce lato Google
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Interfaccia Utente Streamlit ---

st.set_page_config(page_title="Modellando AI - Il tuo Progettista", page_icon=":eyeglasses:")

st.title("😎 Modellando AI - Il tuo Progettista")
st.markdown("Ciao!Sono un assitente virtuale che ti guiderà nel mondo di Modellando, l'azienda che può aiutarti con il tuo business")

# Inizializza la cronologia della chat se non esiste
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi della cronologia della chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Gestisce l'input dell'utente
if prompt := st.chat_input("Come posso aiutarti oggi?"):
    # Aggiunge il messaggio dell'utente alla cronologia
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Ottiene la risposta dal modello Gemini
    with st.chat_message("assistant"):
        with st.spinner("Modellando AI sta pensando..."): 
            try:
                # Chiamata al modello Gemini
                response = model.generate_content(prompt) 
                st.markdown(response.text) 
                st.session_state.messages.append({"role": "assistant", "content": response.text}) 
            except Exception as e:
                st.error(f"Si è verificato un errore durante la generazione della risposta: {e}") 
                st.session_state.messages.append({"role": "assistant", "content": "Ops! Sembra esserci stato un problema. Riprova più tardi."}) 
