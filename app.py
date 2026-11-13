import streamlit as st
import pandas as pd

df =pd.read_csv("data.csv")
st.dataframe(df)


df = pd.DataFrame({
    "product": [
        "Laptop",
        "Phone"
    ],
    "price": [
        1200,
        800
    ]
})


st.write(edited_df)
edited_df = st.data_editor(
    df,
    num_rows="dynamic"
)