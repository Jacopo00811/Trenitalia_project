# import os
import pandas as pd

words_to_filter = ['a', 'e', 'o', 'il', 'lo', 'la', 'i', 'gli', 'l\'', 'le', 'un', 'un\'', 'uno', 'una', 'dei', 'degli', 'delle', 'a', 'da', 'di', 'in', 'con', 'su', 'per', 'tra', 'fra']
words_to_filter = [word.upper() for word in words_to_filter]

filename_target = '00 - ELENCO DOCUMENTI.xlsx'
filename_source = 'ZMAT 895 (4361-5053) - E401.xlsx'

# Read the first Excel file containing the search column
file_source = pd.read_excel(filename_source)
file_target = pd.read_excel(filename_target)

#print(file_source['Tipo mat.'][0])

descriptions = file_source['Descrizione'].tolist()

fileterd_descriptions = []

for phrase in descriptions:
    words = phrase.split()
    filtered_words = [word for word in words if word not in words_to_filter]
    filtered_phrase = ' '.join(filtered_words)
    fileterd_descriptions.append(filtered_phrase)

file_source.drop(labels='Descrizione', axis="columns", inplace=True)
file_source['Descrizione'] = fileterd_descriptions

#file_source.replace(file_source['Descrizione'].tolist(), fileterd_descriptions, regex=True)




#fileterd_descriptions = [phrase for phrase in descriptions if any(words_to_filter in phrase for cong in congiunzioni)]
#print(fileterd_descriptions)


#descriptions_array = file_source['Descrizione'].tolist()
# print(descriptions_array)

# Read the second Excel file where you want to find the words
#df_target = pd.read_excel(elenco_doc)

# Extract the words from the search column
#search_words = df_search['Descrizione'].tolist()

# Initialize a list to store the row numbers


# # Iterate over the words and find their occurrences in the target file
# for word in search_words:
#     rows = df_target.index[df_target['Column_Name'] == word].tolist()
#     row_numbers.extend(rows)

# # Print the row numbers
# for row_number in row_numbers:
#     print("Row Number:", row_number)

