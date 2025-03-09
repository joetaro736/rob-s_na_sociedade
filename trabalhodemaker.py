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
    tab3, tab4, tab5 = st.tabs(['problemas', 'soluções', 'principais afetados'])
    with tab3:
        st.title('problema dos robôs no dia a dia:')
        st.markdown('## :red[1. Desemprego:] A automação pode substituir empregos humanos, principalmente indústrias e serviços manuais.')
        st.markdown('## :red[2. Alto custo inicial:] O desenvolvimento e implementação de robôs podem ser caros, principalmente a pequenas empresas e indivíduos.')
        st.markdown('## :red[3. Dependência excessiva da tecnologia:] A sociedade ficar excessivamente dependente da tecnologia.')
        st.markdown('## :red[4. Falhas técnicas e segurança:] Os robôs podem ser vulneraveis a falhas ou ataques cibernéticos, comprometendo a segurança e a eficiência.')
        st.markdown('## :red[5. Falta de Empatia e Humanização:] Robôs podem ser eficazes mas não possuem empatia ou emoção, oque pode prejudica áreas como atendimento ao cliente e cuidados com idosos.')
    with tab4:
        st.title('as soluções pra esses problemas:')
        st.markdown('## :red[1. Desemprego:] A solução desse problema seria envestir em educação e qualificação para que os trabalhadores possam atuar em novas áreas, como programação, inteligência artificial e manutenção de robôs.')
        st.markdown('## :red[2. Alto custo inicial:] A solução desse problema poderia ser incentivos governamentais e avanços tecnológicos que podem tornar os robôs mais acessíveis ao longo do tempo. Além disso, modelos de aluguel ou compartilhamento podem ser uma alternativa.')
        st.markdown('## :red[3. Dependência excessiva da tecnologia:] A solução pra esse problema seria manter um equilibrio entre o uso da tecnologia e da capacidade humana de realizar tarefas de forma manual quando necessário.')
        st.markdown('## :red[4. Falhas técnicas e segurança:] A solução pra esse problema seria investir em segurança cibernética , atualizações constantes e manutenção preventiva para garantir bom funcionamento.')
        st.markdown('## :red[5. Falta de Empatia e Humanização:] A solução pra esse problema seria melhorar a inteligência artificial para que os robôs passem a agir de maneira mais natural e complementar a atuação humana.')
    with tab5:
        st.title('os maiores públicos afetados são:')
        st.markdown('## :red[1. Trabalhadores:] A automação pode substituir empregos, afetando principalmente funções repetitivas.')
        st.markdown('## :red[2. Empresas:] O auto custo do robô dificulta a adoção por pequenas e médias empresas.')
        st.markdown('## :red[3. Consumidores:] Preocupação com a privacidade e segurança ao usar dispositivos robóticos.')
        st.markdown('## :red[4. Governo:] Precisa criar regulamentações para o uso seguro e ético dos robôs.')
        st.markdown('## :red[5. Indústria de tecnologia:] enfrenta desafios com falhas tecnológicas e inovações constantes.')

st.sidebar.image('lasalle.png')
st.sidebar.title('Robôs na sociedade sexto ano')
st.sidebar.write('Alunos: Joe Paulino, Maria Helena, Guilherme Simões, Gustavo de Melo Margoni e Rebeca Marques Rueda')