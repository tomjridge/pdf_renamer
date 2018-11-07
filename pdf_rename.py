#!/tmp/l/github/pdf_renamer/bin/python3

import os
import sys
import csv
from pdfrw import PdfReader

root=sys.argv[1]
with open('tmp.csv', "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for f in os.listdir(root):
        if(f.endswith(".pdf")):
            x = PdfReader(root+"/"+f)
            assert isinstance(x.Info.Author, object)
            author=x.Info.Author
            assert isinstance(x.Info.Title, object)
            title=x.Info.Title
            print("File: "+f)
            if author!= None:
                print("Author: "+author)
            if title != None:
                print("Title: "+title)
            print(x.Info)
            print()
            # additionally, write to tmp.csv
            csvwriter.writerow([f,title,author,x.Info])