# streamlit_app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="GenAI-EHR Predictor", layout="centered")

st.title("GenAI-EHR Predictor")
st.markdown("Upload EHR + claims data and view GenAI explanations for high-cost risk.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data loaded successfully!")

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    st.subheader("High-Risk Predictions")
    high_risk = df[df["claim_amount"] >= 10000].copy()

    if high_risk.empty:
        st.info("No high-risk patients found.")
    else:
        explanations = [
            f"At {row['age']} years old, this patient had a stay of {row['length_of_stay']} days and a claim of ${row['claim_amount']}. High risk due to advanced age and cost."
            for _, row in high_risk.iterrows()
        ]
        high_risk["GenAI_Explanation"] = explanations

        st.dataframe(high_risk[["age", "length_of_stay", "claim_amount", "GenAI_Explanation"]])

        st.download_button("Download CSV with Explanations",
                           data=high_risk.to_csv(index=False),
                           file_name="high_risk_explained.csv",
                           mime="text/csv")
