import streamlit as st
from random import choice
cores = ['green']
corres = ['red']

st.title('Os robôs podem tanto ajudar como atrapalhar')
st.image('images.jpeg')

st.markdown('---')
tab1, tab2 = st.tabs(['Benefícios', 'Malefícios'])

with tab1:
    st.title('Os robôs realmente podem ajudar muito:')
    st.markdown('## :green[1. Casas inteligentes:] Robôs de limpeza e assistentes virtuais para a automação de tarefas.')
    st.markdown('## :green[2. Saúde:] Robôs auxiliando em cirurgias e no cuidado das pessoas.')
    st.markdown('## :green[3. Transporte:] Carros autônomos e drones par entregas.')
    st.markdown('## :green[4. Indústrias:] Robôs em fábricas e no comércio, aumentando a produtividade.')
    st.markdown('## :green[5. Educação e entretenimento:] Robôs para ensinar e entreter.')
    st.markdown('## :green[6. Segurança:] Robôs de patrulha e monitoramento.')

with tab2:
    st.title('problemas no dia a dia:')
    st.markdown('## :red[1. Desemprego:] A automação pode substituir empregos humanos, principalmente indústrias e serviços manuais.')
    st.markdown('## :red[2. Alto custo inicial:] O desenvolvimento e implementação de robôs podem ser caros, principalmente a pequenas empresas e indivíduos.')
    st.markdown('## :red[3. Dependência excessiva da tecnologia:] A sociedade ficar excessivamente dependente da tecnologia.')
    st.markdown('## :red[4. Falhas técnicas e segurança:] Os robôs podem ser vulneraveis a falhas ou ataques cibernéticos, comprometendo a segurança e a eficiência.')
    st.markdown('## :red[5. Educação e entretenimento:] Robôs para ensinar e entreter.')
    st.markdown('## :red[6. Segurança:] Robôs de patrulha e monitoramento.')



st.sidebar.image('lasalle.png')
st.sidebar.title('Robôs na sociedade')
st.sidebar.write('Alunos: Joe Paulino, Maria Helena, Guilherme Simões, Gustavo de Melo Margoni e Rebeca Rueda')