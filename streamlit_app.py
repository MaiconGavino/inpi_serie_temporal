import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("data.xlsx", decimal='.')

def gera_grafico(graf):
    st.dataframe([df[graf],df['Ano']])
    fig = px.bar(df, x=df["Ano"], y=df[graf],height=400)
    st.plotly_chart(fig, use_container_width = False)
    

def main(): 
    st.dataframe(df)
    page = st.sidebar.selectbox('Selecione o Estado', [x for x in df.columns if x in ["Acre","Alagoas","Amazonas","Amapá","Bahia","Ceará",
                                                                                      "Distrito Federal","Espírito Santo","Goiás","Maranhão", "Minas Gerais",
                                                                                      "Mato Grosso do Sul","Mato Grosso","Pará","Paraíba","Pernambuco",
                                                                                      "Piauí","Paraná","Rio de Janeiro","Rio Grande do Norte",
                                                                                      "Rondônia", "Roraima", "Rio Grande do Sul","Santa Catarina","Sergipe",
                                                                                      "São Paulo", "Tocantins"]])
    gera_grafico(page)
if __name__ == '__main__':
    main()