import streamlit as st

st.set_page_config(layout='centered', page_icon='😈', page_title='ADIVIÑA A CLAVE')

st.title('😈 ADIVIÑA A CLAVE 😈')

st.write('# Agardamos que o disfrutedes tanto como nós facéndoo')

st.write(
    '''
    # Se queredes o voso agasallo...
    
     ## Primeiro teredes que conseguir as claves que abren os cadeados. 😈
    '''
)

st.write('### Rechea tódalas caixas de texto coas respostas correctas para conseguir a clave.')

st.image('images/demo_title.jpg', width=720)

st.write('## Primeira proba')

st.warning('### Cos dedos das mans e cos dedos dos pés...')

form_m3 = st.form('template_3')

q3 = form_m3.text_input('RESPOSTA')

resp3 = '23'

submit3 = form_m3.form_submit_button('DÁME A CLAVE')

if submit3:
    if q3 == resp3:
        st.snow()
        st.success('## Guía para o crebacabezas')
        st.image('images/puzzle.png', width=720)
    else:
        st.error('# SEGUIR PROBANDO')

st.write('## Segunda proba')

st.warning('### ¿Cantos símbolos de Planeswalker hai no crebacabezas?')

form_m2 = st.form('template_2')
resp1 = '7'

q1 = form_m2.text_input("RESPOSTA")

submit = form_m2.form_submit_button('DÁME A CLAVE')

if submit:
    if q1 == resp1:

        st.balloons()
        l, c, r = st.columns(3)
        c.success("🎉 AQUÍ ESTÁ A TÚA CLAVE!")

        st.image('images/demo_sol.jpg', width=720)

    else:
        st.error('# SEGUIR PROBANDO')

st.write('## Terceira proba')

st.warning('### Cal é o S/N da peza que falta no Lego?')

m1_form = st.form('template_form')

m1_q1 = m1_form.text_input('RESPOSTA')

submit_m1 = m1_form.form_submit_button('ENVIAR RESPOSTA')

resp_m1 = '4504378'

if submit_m1:
    if m1_q1 == resp_m1:
        st.balloons()
        l, c, r = st.columns(3)
        c.success("🎉 AQUÍ ESTÁ A TÚA CLAVE!")
        c.info('##   🎉 295 🎉 ')

    else:
        st.error('# SEGUIR PROBANDO')


