# Louise Labels

import streamlit as st
from fpdf import FPDF
import pandas as pd
import base64
from datetime import date

today = date.today()
today = today.strftime("%d-%b-%Y")
st.title('IL Product Label Maker')
IL_list = st.file_uploader('Drop the IL list here', type=['xlsx','csv'])
   
def Make_pdf():
    pdf = FPDF('L','in',(0.7,1.4))
    pdf.set_auto_page_break(0)
    pdf.set_margins(0.1,0.1,0.3)
    pdf.set_font('Helvetica','',7)
    return pdf

def Print_labels(data,pdf):
    for i in range(0,len(data)):
        pdf.add_page()
        text = (f'IL ID: UT{Notebook[i]}-{IL_page[i]}\nIL: {IL_Name[i]}\nDate: {Date[i].strftime("%d-%b-%Y")}\nOwner: {Owner[i]}')
        pdf.multi_cell(1.25,0.1,txt=text)
    pdfname = str(f'Labels_{today}.pdf')
    pdf.output(pdfname)
    return pdfname

def st_display_pdf(pdf_file):  
    with open(pdf_file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
if not IL_list:
    ''
else:
    il_list = pd.read_excel(IL_list)
    Notebook = il_list["Notebook ID"].to_list()
    IL_page = il_list["IL ID (page number)"].to_list()
    IL_Name = il_list["IL Name"].to_list()
    Date = il_list["Date"].to_list()
    Owner = il_list['Owner'].to_list()
    doc = Make_pdf()
    pdfname = Print_labels(il_list,doc)
    
if st.button('Make labels'):
    st.text(f'{today} IL list is done:')
    st_display_pdf(pdfname)    
