import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title('Meu primeiro Web-App da Vida')
st.markdown('---') #códigos de markdown
#st.slider('Entre com um número: ')

paginas = ['Home', 'Histograma', 'Sobre']


st.sidebar.subheader('Navegue por aqui')
pagina = st.sidebar.selectbox('Menu', paginas)

if pagina == 'Home':
    st.title('WEB APP')
    st.markdown('---')
    st.write('Meu webapp com diverssas funcionalidades bacanas.')

if pagina == 'Histograma':

    n = st.slider('Entre com um número: ', 50, 500, 100,
              10)  # coloca um range dentro do histograma(min, max, default, intervalos)
    cor = st.color_picker('Escolha a cor: ')

    x = np.random.normal(1, 1, size=n)  # tamanho amostra é o que esta no slider
    fig, ax = plt.subplots()  # subfigura é o ax
    ax.hist(x, bins=15, edgecolor='black', color=cor)  # histograma com 15 barras

    st.pyplot(fig)

    botao = st.button('Abrir titulo')
    if botao:
        st.title('Titulo condicional')
        st.sidebar.radio('Radio', [1, 2, 3])  # para ir para a barra lateral
        st.text_input('Texto')
        st.date_input('Data')

if pagina == 'Sobre':
    st.write('Web')
    st.balloons()
    st.write("""
             # Outro título
             ## Titulo 
             ### outro
             Esse texto
             $$\int_a^b f(x)dx = F(b) - F(a)$$
                      """)
