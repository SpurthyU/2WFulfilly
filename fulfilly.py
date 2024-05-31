import streamlit as st
import pandas as pd

# Function to read Excel file
def read_excel(file):
    df = pd.read_excel(file)
    df['Date And Time'] = pd.to_datetime(df['Date And Time'])
    df.sort_values(by='Date And Time', ascending=False, inplace=True)
    df = df.drop_duplicates(subset='Vehicle Number', keep='first')
    selected_columns = ['Vehicle Number', 'Date And Time', 'Location', 'Voltage (V)', 'Current (A)', 'State Of Charge (%)']
    df = df[selected_columns]
    return df

def main():
    st.title('FULFILLY')

    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

    if uploaded_file is not None:
        df = read_excel(uploaded_file)
        st.dataframe(df)  # Use st.dataframe for interactive display

if __name__ == "__main__":
    main()
