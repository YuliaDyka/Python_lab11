import re as regex
from datetime import datetime
import zipfile

def main():
    zip_ref = zipfile.ZipFile("resource/access_log.zip")
    zip_ref.extractall()
    zip_ref.close()
    file_to_read = open("access_log.txt")
    lines = file_to_read.readlines()

    date_start = datetime.strptime('08/Mar/2004:02:11:37', '%d/%b/%Y:%H:%M:%S')
    date_end = datetime.strptime('10/Mar/2004:18:41:52', '%d/%b/%Y:%H:%M:%S')
    my_list = list()

    pattern = r'(.+\[(\S+)\s\S+\]\s+\".*?\"\s([2][0][0]).+)'

    for line in lines:
        tmp = regex.match(pattern, line)
        if tmp:
            if date_start < datetime.strptime(tmp.group(2), '%d/%b/%Y:%H:%M:%S') < date_end:
                my_list.append(tmp)
            elif datetime.strptime(tmp.group(2), '%d/%b/%Y:%H:%M:%S') > date_end:
                break
    for i in my_list:
        print(i.group(1))
    print(len(my_list))

main()  
    