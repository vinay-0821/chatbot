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
    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    query = st.text_input("💬 Ask a question about your data:")

    if query:
        with st.spinner("🤖 Thinking..."):
            answer, chart_info = get_llm_response(df, query)

        st.subheader("✅ Answer")
        st.markdown(answer)

        if chart_info:
            st.subheader("📈 Chart")
            try:
                chart = generate_plot(df, chart_info)
                if chart:
                    st.altair_chart(chart, use_container_width=True)
                else:
                    st.warning("Could not generate chart. Please check the column names or chart type.")
            except Exception as e:
                st.error(f"Chart error: {e}")
