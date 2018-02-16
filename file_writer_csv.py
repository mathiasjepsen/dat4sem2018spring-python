import webget
import csv
import platform

url = "http://data.kk.dk/dataset/76ecf368-bf2d-46a2-bcf8-adaf37662528/resource/9286af17-f74e-46c9-a428-9fb707542189/download/befkbhalderstatkode.csv"

if platform.system() == "Windows":
    newline = ""
else:
    newline = None

#with open("./numbers.txt", "a") as file_obj:  # a to append, w to write, r to read, rb to read binary
#    file_obj.write("12342354254353\n2342342342")

#with open(webget.download(url)) as file_obj:
#    content = file_obj.readlines()

#lines = [line.rstrip().split(",") for line in content[:10]]
#
#print(lines)



with open(webget.download(url)) as file_obj:
    reader = csv.reader(file_obj)

    header_row = next(reader)

    for row in reader:
        if reader.line_num > 500:
            break
        print(row)