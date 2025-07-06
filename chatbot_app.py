import streamlit as st
# import google.generativeai as genai # COMMENTA QUESTA RIGA
# import os # COMMENTA QUESTA RIGA

# --- Configurazione della API Key (COMMENTATA) ---
# api_key = os.environ.get("GOOGLE_API_KEY")
#
# if not api_key:
#     st.error("ERRORE: La variabile d'ambiente GOOGLE_API_KEY non è impostata.")
#     st.write("Assicurati di averla configurata correttamente (export GOOGLE_API_KEY=\"TUA_CHIAVE\")")
#     st.stop()
#
# try:
#     genai.configure(api_key=api_key)
# except Exception as e:
#     st.error(f"ERRORE durante la configurazione dell'API: {e}")
#     st.stop()

# --- Inizializzazione del Modello Gemini (COMMENTATA) ---
# model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Interfaccia Utente Streamlit ---

st.set_page_config(page_title="Modellando AI Style Advisor", page_icon=":eyeglasses:")

st.title("🤝 Modellando AI Style Advisor")
st.markdown("Ciao! Sono qui per darti consigli di stile personalizzati, basati sulle ultime tendenze e sulle collezioni dei nostri negozi partner. Chiedimi pure!")

# Inizializza la cronologia della chat se non esiste (LA LASCIAMO)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi della cronologia della chat (LA LASCIAMO)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Gestisce l'input dell'utente (MODIFICHIAMO QUESTA PARTE PER NON CHIAMARE GEMINI)
if prompt := st.chat_input("Come posso aiutarti oggi?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # st.spinner("Modellando AI sta pensando...") # COMMENTA QUESTA RIGA
        # try:
        #     response = model.generate_content(prompt)
        #     st.markdown(response.text)
        #     st.session_state.messages.append({"role": "assistant", "content": response.text})
        # except Exception as e:
        #     st.error(f"Si è verificato un errore durante la generazione della risposta: {e}")
        #     st.session_state.messages.append({"role": "assistant", "content": "Ops! Sembra esserci stato un problema. Riprova più tardi."})
        st.markdown(f"Hai chiesto: {prompt} (Il bot è in fase di costruzione!)") # RISPOSTA DI PROVA
        st.session_state.messages.append({"role": "assistant", "content": f"Hai chiesto: {prompt} (Il bot è in fase di costruzione!)"})