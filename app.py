import streamlit as st

st.set_page_config(layout='centered', page_icon='😈', page_title='GUESS THE KEY')

st.title('ADIVIÑA A CLAVE')

st.write(
    '''
    # Se queres o teu agasallo...
    
     ## Primeiro debes conseguir as chaves que abren as pechaduras 😈
    '''
)

st.write('### Encha todos os recadros coas respostas correctas para obter a clave')

st.image('images/demo_title.jpg', width=720)

left, right = st.columns(2)


right.info('MISIÓN 1: ' + r'$x = \frac{p + g}{2}$')
right.write(r'$p = $Total de persoas en quebracabezas')
right.write(r'$w = $Total de mulleres no quebracabezas')
right.write(r'$m = $Total homes en quebracabezas')
right.write(r'$b = $total de nenos en quebracabezas')
right.write(r'$g = $total de nenas en quebracabezas')

form = left.form('template_form')

q1 = form.text_input("Misión 1")
q2 = form.text_input("Cantos símbolos de planeswalkers hai no quebacabezas")
q3 = form.text_input('Con los dedos de las manos y los dedos de los pies ....')

submit = form.form_submit_button('DÁME A CHAVE')

resp1 = '22'
resp2 = '7'
resp3 = '23'


if submit:
    if q1 == resp1 and q2 == resp2 and q3 == resp3:

        st.balloons()
        l, c, r = st.columns(3)
        c.success("🎉 AQUÍ ESTÁ A TÚA CLAVE!")

        st.image('images/demo_sol.jpg', width=720)
    else:
        st.error('# SEGUIR PROBANDO')
