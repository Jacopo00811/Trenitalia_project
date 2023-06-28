import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('00 - ELENCO DOCUMENTI.xlsx')

# Remove the first character from a specific column
df['TITOLO DOCUMENTO'] = df['TITOLO DOCUMENTO'].str[1:]

# Save the modified DataFrame to a new Excel file
df.to_excel('00 - ELENCO DOCUMENTI_A.xlsx', index=False)
