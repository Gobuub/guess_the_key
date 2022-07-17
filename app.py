import streamlit as st

st.set_page_config(layout='centered', page_icon='😈', page_title='GUESS THE KEY')

st.title('GUESS THE KEY')

st.write(
    '''
    # If you want your gift ...
    
    ## First you must get the keys that open the locks 😈
    '''
)

st.write('### Fill all the boxes with the correct answers to get the key')

st.image('images/demo_title.jpg', width=720)

left, right = st.columns(2)


right.info('Quest 1: ' + r'$x = \frac{p + g}{2}$')
right.info('Quest 3: ' + r"$z = p - m - (b-g)$")
right.write(r'$p = $total people on puzzle')
right.write(r'$w = $total women on puzzle')
right.write(r'$m = $total men on puzzle')
right.write(r'$b = $total kids (boys) on puzzle')
right.write(r'$g = $total kids (girls) on puzzle')

form = left.form('template_form')

q1 = form.text_input("Quest 1")
q2 = form.text_input("How many planeswalkers symbols are on the puzzle")
q3 = form.text_input('Quest 3')

submit = form.form_submit_button('GIVE US THE KEY')

resp1 = '23'
resp2 = '7'
resp3 = '22'

print(q1 == resp1, q2 == resp2, q3 == resp3)

if submit:
    if q1 == resp1 and q2 == resp2 and q3 == resp3:

        st.balloons()
        l, c, r = st.columns(3)
        c.success("🎉 HERE IS YOUR KEY!")

        st.image('images/demo_sol.jpg', width=720)
    else:
        st.error('# KEEP TRIYING')
