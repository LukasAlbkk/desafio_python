import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
data_path = 'data/netflixdata.csv'
df = pd.read_csv(data_path)

# Função para carregar dados
def load_data():
    df = pd.read_csv(data_path)
    return df

# Título e descrição do Dashboard
st.title('Dashboard Netflix')
st.markdown('## Análise dos Dados de Filmes e Séries da Netflix')
st.sidebar.image('images/logo.png', width=150)
st.sidebar.markdown('**Aluno:** Lucas Albquerque Santos Costa')
st.sidebar.markdown('**PDITA:** PDBD009')

# Widgets de Interatividade
type_filter = st.sidebar.selectbox('Selecione o Tipo', df['type'].unique())
country_filter = st.sidebar.selectbox('Selecione o País', df['country'].dropna().unique())

# Filtrar dados com base na seleção
filtered_data = df[(df['type'] == type_filter) & (df['country'] == country_filter)]

# Gráfico de Barras: Contagem de Títulos por Ano de Lançamento
grouped_data = filtered_data.groupby('release_year').size().reset_index(name='count')
fig = px.bar(grouped_data, x='release_year', y='count', title=f'Títulos por Ano de Lançamento ({type_filter} - {country_filter})', labels={'count': 'Contagem de Títulos', 'release_year': 'Ano de Lançamento'})
st.plotly_chart(fig)

# Gráfico de Pizza: Distribuição das Durações dos Filmes
# Filtrar dados apenas para filmes (já que séries têm duração em temporadas)
if type_filter == 'Movie':
    duration_data = filtered_data['duration'].value_counts().reset_index()
    duration_data.columns = ['duration', 'count']
    fig_pie = px.pie(duration_data, values='count', names='duration', title='Distribuição das Durações dos Filmes')
    st.plotly_chart(fig_pie)

# Exibir Tabela de Dados
st.markdown(f'## Dados Filtrados para {type_filter} em {country_filter}')
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
