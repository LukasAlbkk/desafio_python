import streamlit as st
import pandas as pd
import plotly.express as px

data_path = 'data/dataset_olympics.csv'
df = pd.read_csv(data_path)

cor_medalha = ['#636EFA']
cor_sexo = ['#EF553B']
cor_idade = ['#00CC96']
cor_peso = ['#AB63FA']
cor_time = ['#FFA15A']
cor_jogos = ['#19D3F3']
cor_total_medalhas = ['#FF6692']

def load_data():
    df = pd.read_csv(data_path)
    return df

st.title('Dashboard Olímpico')
st.markdown('## Análise dos Dados de Atletas Olímpicos')
st.sidebar.image('images/logo.png', width=150)
st.sidebar.markdown('**Aluno:** Lucas Albuquerque Santos Costa')
st.sidebar.markdown('**PDITA:** PDBD009')

season_filter = st.sidebar.selectbox('Selecione a Temporada', df['Season'].unique())
country_filter = st.sidebar.selectbox('Selecione o País', df['Team'].dropna().unique())
filtered_data = df[(df['Season'] == season_filter) & (df['Team'] == country_filter)]

#Contagem de medalhas
medal_data = filtered_data['Medal'].value_counts().reset_index()
medal_data.columns = ['Medal', 'Count']
fig = px.bar(medal_data, x='Medal', y='Count', title=f'Contagem de Medalhas ({season_filter} - {country_filter})', labels={'Count': 'Contagem de Medalhas', 'Medal': 'Medalha'},color_discrete_sequence= cor_medalha)
st.plotly_chart(fig)

# Alturas atletas
height_data = filtered_data['Height'].value_counts().reset_index()
height_data.columns = ['Height', 'Count']
fig_pie = px.pie(height_data, values='Count', names='Height', title='Distribuição das Alturas dos Atletas')
st.plotly_chart(fig_pie)

#  atletas por Sexo
sex_data = filtered_data['Sex'].value_counts().reset_index()
sex_data.columns = ['Sex', 'Count']
fig_sex = px.bar(sex_data, x='Sex', y='Count', title=f'Contagem de Atletas por Sexo ({season_filter} - {country_filter})', labels={'Count': 'Contagem de Atletas', 'Sex': 'Sexo'},color_discrete_sequence=cor_sexo)
st.plotly_chart(fig_sex)

# Idade
fig_age = px.line(filtered_data, x='ID', y='Age', title=f'Idades dos Atletas ({season_filter} - {country_filter})', labels={'ID': 'ID do Atleta', 'Age': 'Idade'},color_discrete_sequence=cor_idade)
st.plotly_chart(fig_age)

# Peso
weight_data = filtered_data['Weight'].value_counts().reset_index()
weight_data.columns = ['Weight', 'Count']
fig_weight = px.bar(weight_data, x='Weight', y='Count', title='Distribuição dos Pesos dos Atletas', labels={'Count': 'Contagem', 'Weight': 'Peso'},color_discrete_sequence= cor_peso)
st.plotly_chart(fig_weight)

# Numero de atletas
team_data = filtered_data['Team'].value_counts().reset_index()
team_data.columns = ['Team', 'Count']
fig_team = px.bar(team_data, x='Team', y='Count', title='Contagem de Atletas por Time', labels={'Count': 'Contagem', 'Team': 'Time'}, color_discrete_sequence=cor_time)
st.plotly_chart(fig_team)

# Numero por jogos
games_data = filtered_data['Games'].value_counts().reset_index()
games_data.columns = ['Games', 'Count']
fig_games = px.bar(games_data, x='Games', y='Count', title='Contagem de Atletas por Jogos', labels={'Count': 'Contagem', 'Games': 'Jogos'}, color_discrete_sequence=cor_jogos)
st.plotly_chart(fig_games)

# medalhas de cada tipo.
medal_data = filtered_data['Medal'].value_counts().reset_index()
medal_data.columns = ['Medal', 'Count']
fig_medal = px.bar(medal_data, x='Medal', y='Count', title='Contagem de Medalhas por Tipo', labels={'Count': 'Contagem', 'Medal': 'Medalha'}, color_discrete_sequence=cor_medalha)
st.plotly_chart(fig_medal)

# medalhas por pais
total_medals = df[df['Medal'].notna()]
total_medals = total_medals.groupby('Team').size().reset_index(name='Count')
fig_total_medals = px.bar(total_medals, x='Team', y='Count', title='Total de Medalhas por País', labels={'Count': 'Contagem de Medalhas', 'Team': 'País'}, color_discrete_sequence=cor_total_medalhas)
st.plotly_chart(fig_total_medals)

# tabela de Dados
st.markdown(f'## Dados Filtrados para {season_filter} em {country_filter}')
st.write(filtered_data)

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
