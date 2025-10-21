import streamlit as st

st.title("Base de conhecimento TIMARQ")
st.write("Olá, mundo!")

# Extrair metadados do PDF
def extrair_metadados(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    metadata = pdf_reader.metadata
    return {
        'Título': metadata.get('/Title', 'N/A'),
        'Autor': metadata.get('/Author', 'N/A'),
        'Assunto': metadata.get('/Subject', 'N/A'),
        'Páginas': len(pdf_reader.pages)
    }

# Dividir PDF
def dividir_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        
        with BytesIO() as output:
            pdf_writer.write(output)
            st.download_button(
                label=f"📥 Baixar Página {page_num + 1}",
                data=output.getvalue(),
                file_name=f"pagina_{page_num + 1}.pdf",
                mime="application/pdf"
            )
