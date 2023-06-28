import pandas as pd
import re
from collections import Counter

words_to_filter = ['tipo', 'viesca', 'ingenerìa', 'impianto', 'guida', 'cabina', 'colore', 'mv1', 'mv2', 'lv2', 'lv1', '&', 'opera', 'c', 'nc', 'na', 'e401', '+', 'p', 'caf', 'sx', 'dx', 'che', 'mm', 'nella', 'nello', 'nel', 'al', 'd\'', 'd', '-', 'a', 'e', 'o', 'il', 'lo', 'la', 'i', 'gli', 'l\'', 'l', 'le', 'un', 'un\'', 'uno', 'una', 'dei', 'degli',
                   'del', 'delle', 'della', 'a', 'da', 'di', 'in', 'con', 'su', 'per', 'tra', 'fra', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


words_to_filter = [word.upper() for word in words_to_filter]

filename_target = '00 - ELENCO DOCUMENTI_Cleaned.xlsx'
filename_source = 'MB_ZMAT 895 (4361-5053) - E401_ap3.xlsx'

file_source = pd.read_excel(filename_source)
file_target = pd.read_excel(filename_target)

descriptions = file_source['Descrizione'].tolist()

filtered_descriptions = []

for phrase in descriptions:
    words = phrase.split()
    filtered_words = [word for word in words if not re.search(r'^[^.]+\.$', word) and word not in words_to_filter]
    filtered_words = [re.sub(r"^[^']+'", '', word) for word in filtered_words]
    filtered_words = [word.replace('\'', '').replace('\"', '') for word in filtered_words]
    filtered_phrase = ' '.join(filtered_words)
    filtered_descriptions.append(filtered_phrase)


file_source['Descrizione'] = filtered_descriptions

documents_codes = file_target['CODICE DOCUMENTO'].tolist()
documents_titles = file_target['TITOLO DOCUMENTO'].tolist()


for phrase in file_source['Descrizione'].tolist():
    matching_codes = []
    for word in phrase.split():
        for title in documents_titles:
            for word_title in title.split():
                if word == word_title:
                    matching_codes.append(file_target.at[documents_titles.index(title), 'CODICE DOCUMENTO'])

    index = file_source['Descrizione'].tolist().index(phrase)
    file_source.at[index, 'Codici Documenti'] = '; '.join(matching_codes)

    array = []
    for code in matching_codes:
        array.append(code)
    counter = Counter(array)
    ordered_arr = sorted(array, key=lambda x: counter[x], reverse=True)
    seen = set()
    no_duplicates = [x for x in ordered_arr if not (x in seen or seen.add(x))]
    file_source.at[index, 'Codici Documenti'] = '; '.join(no_duplicates)

file_source.to_excel('output1.xlsx', index=False) 
print("File saved successfully!")
