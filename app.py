import streamlit as st
import pandas as pd
from excel_parser import process_excel
from llm_utils import get_llm_response
from plot_utils import generate_plot

st.set_page_config(page_title="Excel Chat Assistant", layout="wide")
st.title("📊 Excel Chat Assistant")

uploaded_file = st.file_uploader("Upload an Excel (.xlsx) file", type=["xlsx"])
if uploaded_file:
    df = process_excel(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df)

    query = st.text_input("Ask a question about your data:")

    if query:
        with st.spinner("Thinking..."):
            answer, chart_info = get_llm_response(df, query)

            st.subheader("Answer")
            st.markdown(answer)

            if chart_info:
                try:
                    st.subheader("📈 Chart")
                    chart_type = chart_info["type"]
                    x = chart_info["x"]
                    y = chart_info["y"]
                    if chart_type == "bar":
                        st.bar_chart(df[[x, y]].set_index(x))
                    elif chart_type == "line":
                        st.line_chart(df[[x, y]].set_index(x))
                    elif chart_type == "hist":
                        st.area_chart(df[[x, y]].set_index(x))
                except Exception as e:
                    st.error(f"Chart error: {e}")