# import PyPDF2
# import os


# pdf_directory = r"C:\Users\jacop\Desktop\E401_File\Files"

# filename = r"0000000000000021901.pdf"
# pdf_path = os.path.join(pdf_directory, filename)


# with open(pdf_path, 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     # Get the title of the PDF file
#     if '/Title' in reader.metadata:
#         title = reader.metadata['/Title']
#         print(title)
#     else:
#         print("Title not found")
