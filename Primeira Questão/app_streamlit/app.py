import pandas as pd
import streamlit as st
import plotly.express as px



def main():
    st.image('logo.png', width=500)
    st.title('Case Fortbrasil')
    st.subheader('Primeira Questão')
    
    df = pd.read_csv('questao1_coronavirus.csv', sep=';')
    list_date = list(df['date'])
    df['date'] = pd.to_datetime(df['date'])
    aux = pd.DataFrame({"colunas": df.columns, 'tipos': df.dtypes})
    
    st.markdown('Visualização dos dados')
    slider = st.slider('Valores', 5,100)
    st.dataframe(df.head(slider))
    
    st.markdown('Dados Gerais')
    select_method = st.radio('Escolha uma opção abaixo: ', ('Casos Acumulados', 'Mortes Acumuladas', '% de mortes sobre infectados', '% da população infectada'))
    if select_method == 'Casos Acumulados':
        st.markdown('Foram contabilizados ' + str(df['new_confirmed'].sum()) + ' casos acumulados.')
    if select_method == 'Mortes Acumuladas':
        st.markdown('Foram contabilizados ' + str(df['new_deaths'].sum()) + ' mortes acumuladas')
    if select_method == '% de mortes sobre infectados':
        st.markdown('Aproximadamente ' + str(round((df['new_deaths'].sum()/df['new_confirmed'].sum())*100)) + '%')
    if select_method == '% da população infectada':
        st.markdown('Aproximadamente ' + str(round(((df['new_confirmed'].sum() + df['new_deaths'].sum())/df['estimated_population_2019'].sum())*100)) + '% ')
    
    st.markdown('Analises individuais por estados')
    df_state_t = df.groupby('state')['new_confirmed', 'new_deaths'].sum().T
    df_state = df.groupby(by='state').sum().reset_index()
    #all_columns_names = df_state.columns.tolist()

    states = st.selectbox('Escolha um estado: ', df_state['state'])
   
    if states == 'AL':
        st.write(df_state[df_state['state'] == 'AL'])
        st.bar_chart(df_state_t['AL'], width=200, height = 300)
    if states == 'AC':
        st.write(df_state[df_state['state'] == 'AC'])
        st.bar_chart(df_state_t['AC'], width=200, height = 300)
    if states == 'AM':
        st.write(df_state[df_state['state'] == 'AM'])
        st.bar_chart(df_state_t['AM'], width=200, height = 300)
    if states == 'AP':
        st.write(df_state[df_state['state'] == 'AP'])
        st.bar_chart(df_state_t['AP'], width=200, height = 300)
    if states == 'BA':
        st.write(df_state[df_state['state'] == 'BA'])
        st.bar_chart(df_state_t['BA'], width=200, height = 300)
    if states == 'CE':
        st.write(df_state[df_state['state'] == 'CE'])
        st.bar_chart(df_state_t['CE'], width=200, height = 300)
    if states == 'DF':
        st.write(df_state[df_state['state'] == 'DF'])
        st.bar_chart(df_state_t['DF'], width=200, height = 300)
    if states == 'ES':
        st.write(df_state[df_state['state'] == 'ES'])
        st.bar_chart(df_state_t['ES'], width=200, height = 300)
    if states == 'GO':
        st.write(df_state[df_state['state'] == 'GO'])
        st.bar_chart(df_state_t['GO'], width=200, height = 300)
    if states == 'MA':
        st.write(df_state[df_state['state'] == 'MA'])
        st.bar_chart(df_state_t['MA'], width=200, height = 300)
    if states == 'MS':
        st.write(df_state[df_state['state'] == 'MS'])
        st.bar_chart(df_state_t['MS'], width=200, height = 300)
    if states == 'MT':
        st.write(df_state[df_state['state'] == 'MT'])
        st.bar_chart(df_state_t['MT'], width=200, height = 300)
    if states == 'PA':
        st.write(df_state[df_state['state'] == 'PA'])
        st.bar_chart(df_state_t['PA'], width=200, height = 300)
    if states == 'PI':
        st.write(df_state[df_state['state'] == 'PI'])
        st.bar_chart(df_state_t['PI'], width=200, height = 300)
    if states == 'PB':
        st.write(df_state[df_state['state'] == 'PB'])
        st.bar_chart(df_state_t['PB'], width=200, height = 300)
    if states == 'PE':
        st.write(df_state[df_state['state'] == 'PE'])
        st.bar_chart(df_state_t['PE'], width=200, height = 300)
    if states == 'PR':
        st.write(df_state[df_state['state'] == 'PR'])
        st.bar_chart(df_state_t['PR'], width=200, height = 300)
    if states == 'RJ':
        st.write(df_state[df_state['state'] == 'RJ'])
        st.bar_chart(df_state_t['RJ'], width=200, height = 300)
    if states == 'RN':
        st.write(df_state[df_state['state'] == 'RN'])
        st.bar_chart(df_state_t['RN'], width=200, height = 300)
    if states == 'RO':
        st.write(df_state[df_state['state'] == 'RO'])
        st.bar_chart(df_state_t['RO'], width=200, height = 300)
    if states == 'RR':
        st.write(df_state[df_state['state'] == 'RS'])
        st.bar_chart(df_state_t['RR'], width=200, height = 300)
    if states == 'RS':
        st.write(df_state[df_state['state'] == 'RS'])
        st.bar_chart(df_state_t['RS'], width=200, height = 300)
    if states == 'SC':
        st.write(df_state[df_state['state'] == 'SC'])
        st.bar_chart(df_state_t['SC'], width=200, height = 300)
    if states == 'SE':
        st.write(df_state[df_state['state'] == 'SE'])
        st.bar_chart(df_state_t['SE'], width=200, height = 300)
    if states == 'SP':
        st.write(df_state[df_state['state'] == 'SP'])
        st.bar_chart(df_state_t['SP'], width=200, height = 300)
    if states == 'TO':
        st.write(df_state[df_state['state'] == 'TO'])
        st.bar_chart(df_state_t['TO'], width=200, height = 300)
    if states == 'MG':
        st.write(df_state[df_state['state'] == 'MG'])
        st.bar_chart(df_state_t['MG'], width=200, height = 300)
    
    x = st.selectbox('Bar Chart Race', ('X'))
    if x == 'X':
        st.video('bar_chart_race.mp4')


if __name__ == '__main__':
    main()

