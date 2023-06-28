# import pandas as pd
# import os
# import csv
# import PyPDF2
# import pandas as pd

# # Define the keywords and PDF directory
# keywords = ['keyword1', 'keyword2', 'keyword3']
# pdf_directory = 'path/to/pdf/files'

# # # Create a DataFrame to store the results
# # data = pd.DataFrame(columns=keywords)

# # Iterate through the PDF files in the directory
# for filename in os.listdir(pdf_directory):
#     if filename.endswith('.pdf'):
#         pdf_path = os.path.join(pdf_directory, filename)
#         with open(pdf_path, 'rb') as file:
#             reader = PyPDF2.PdfReader(file)
#             # Get the title of the PDF file
#             title = reader.getDocumentInfo().title
            

#             # file.close() remember to close the file


#             # Search for keywords in the PDF content
#             found_keywords = []
#             for page in reader.pages:
#                 text = page.extract_text().lower()
#                 for keyword in keywords:
#                     if keyword.lower() in text:
#                         found_keywords.append(keyword)
            
#             # Add the found keywords to the DataFrame
#             data.loc[title] = [keyword in found_keywords for keyword in keywords]

# # Save the DataFrame to a CSV file
# data.to_csv('output.csv')




