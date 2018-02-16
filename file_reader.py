import webget

url1 = "https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_30_digits.txt"
url2 = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_million_digits.txt' 


#with open(webget.download(url1)) as file_obj:
#    contents = file_obj.read()

#with open(webget.download(url1)) as file_obj:
#    lines = file_obj.readlines()

with open(webget.download(url2)) as file_obj:
    for line in file_obj:
        

