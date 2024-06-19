import streamlit as st

st.title('Financiële Planner')


huisprijs = st.number_input('Hoe duur is het huis dat je wilt kopen?', step = 25000, )
hypotheek = st.number_input('hoe hoog is de hypotheek die je op dit moment kun krijgen?', step=10000)
spaargeld = st. number_input('hoeveel heb je op dit moment al gespaard?', step = 1000)
hoelang = st.number_input('over hoeveel maanden wil je een huis kopen?', step = 1)


if hoelang > 0:
    maandelijks_sparen = (huisprijs - hypotheek - spaargeld) / hoelang
    st.write(f'Je moet €{round(maandelijks_sparen, 2)} per maand sparen om het huis in de gewenste tijd te kunnen kopen')

