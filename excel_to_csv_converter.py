import openpyxl
import webget
import platform
import csv

url = "https://github.com/datsoftlyngby/dat4sem2018spring-python/raw/master/lecture_notes/iris_data.xlsx"
file = webget.download(url)
wb = openpyxl.load_workbook(file)

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None

sheet =  wb.get_active_sheet()

excel_data = [[cell.value for cell in row] for row in sheet.rows]

with open('./iris_data_csv.csv', 'w', newline=newline) as output_file:
   output_writer = csv.writer(output_file)
   for row in excel_data:
       output_writer.writerow(row)



        
