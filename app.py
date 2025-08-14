import streamlit as st
import io

st.set_page_config(page_title="Conversor CSV", layout="centered")

st.title("Conversor de CSV: Vírgula para Ponto e Vírgula")
st.write("Faça upload de um arquivo `.csv` e baixe a versão com `;` como separador.")

# Upload do arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])

if uploaded_file is not None:
    # Lê o arquivo como texto
    content = uploaded_file.read().decode("utf-8")
    
    # Substitui vírgulas por ponto e vírgula
    converted_content = content.replace(",", ";")

    # Prepara o conteúdo convertido para download
    output = io.StringIO()
    output.write(converted_content)
    output.seek(0)

    st.success("Arquivo convertido com sucesso!")

    # Botão para download
    st.download_button(
        label="📥 Baixar CSV com ponto e vírgula",
        data=output,
        file_name="arquivo_convertido.csv",
        mime="text/csv"
    )
