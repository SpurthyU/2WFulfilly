import streamlit as st
import pandas as pd
from io import BytesIO

# Function to read Excel file
def read_excel(file):
    df = pd.read_excel(file)
    df['Date And Time'] = pd.to_datetime(df['Date And Time'])
    df.sort_values(by='Date And Time', ascending=False, inplace=True)
    df = df.drop_duplicates(subset='Vehicle Number', keep='first')
    selected_columns = ['Vehicle Number', 'Date And Time', 'Location', 'Voltage (V)', 'Current (A)', 'State Of Charge (%)']
    df = df[selected_columns]
    return df

# Function to convert DataFrame to Excel for download
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def main():
    st.title('FULFILLY')

    uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

    if uploaded_file is not None:
        df = read_excel(uploaded_file)
        st.write(df)

        # Create a download button
        processed_data = to_excel(df)
        st.download_button(
            label="Download processed data as Excel",
            data=processed_data,
            file_name='processed_data.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

if __name__ == "__main__":
    main()

