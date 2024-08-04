import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
data_path = 'data/covid19_data.csv'
df = pd.read_csv(data_path)

# Função para carregar dados
def load_data():
    df = pd.read_csv(data_path)
    return df

# Título e descrição do Dashboard
st.title('Dashboard COVID-19')
st.markdown('## Análise dos Dados de Coronavírus 2019')
st.sidebar.image('images/logo.png', width=150)
st.sidebar.markdown('**Aluno:** Seu Nome Completo')
st.sidebar.markdown('**PDITA:** Seu PDITA')

# Widgets de Interatividade
country = st.sidebar.selectbox('Selecione o País', df['country'].unique())
metric = st.sidebar.radio('Selecione a Métrica', ['confirmed', 'deaths', 'recovered'])

# Filtrar dados com base na seleção
filtered_data = df[df['country'] == country]

# Gráfico de Linha
fig = px.line(filtered_data, x='date', y=metric, title=f'{metric.capitalize()} Cases in {country}')

# Mostrar gráfico
st.plotly_chart(fig)

# Exibir Tabela de Dados
st.markdown(f'## Dados Filtrados para {country}')
st.write(filtered_data)

# CSS para estilização
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

