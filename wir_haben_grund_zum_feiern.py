import streamlit as st

st.title("Wir haben Grund zum Feiern!")
 
st.write("Aber warum wohl?")

quiz = ['Anna kommt in die Schule!', 'Anna kann schon alleine eine Schleife binden!', 'Anna hat Geburtstag!', 'Anna kann auf einem Bein rückwärts hüpfen!']

choice = st.radio(label='Was gibt es heute zu feiern?', options=quiz)

if choice != 'Anna hat Geburtstag!':
    st.write("Das ist leider nicht richtig. :see_no_evil: Versuch es noch einmal.")
else:
    st.markdown('Hurra! :sparkler: Anna hat Geburtstag! :rocket: Wir wünschen ihr alles Gute! :birthday: :gift: :balloon:')
    st.balloons()