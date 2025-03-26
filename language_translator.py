import streamlit as st
from deep_translator import GoogleTranslator as gt

st.title('🌍 Language Translator')

st.subheader('Translates from one language to another')

LANGUAGES = {"English": "en", "Spanish": "es", "French": "fr", "German": "de",
    "Italian": "it", "Hindi": "hi", "Chinese": "zh-CN", "Arabic": "ar",
    "Portuguese": "pt", "Japanese": "ja", "Korean": "ko", "Russian": "ru",
    "Tamil": "ta", "Telugu": "te", "Bengali": "bn", "Urdu": "ur"}


text = st.text_area('Enter the text to translate:',height = 150)

lang = LANGUAGES.keys()
code = LANGUAGES.values()

col1,col2 = st.columns(2)

with col1:
    src_lang  = st.selectbox("Source Language", options = lang, index = 0)

with col2:
    tar_lang  = st.selectbox("Target Language", options = lang, index = 1)

code1 = LANGUAGES[src_lang]
code2 = LANGUAGES[tar_lang]

if st.button('Translate'):
    if text.strip():
        trans_text = gt(source=code1, target= code2).translate(text)
        st.success(f"The translated text is :\n\n{trans_text}")
    else:
        st.warning("⚠️ Please enter a valid text")


