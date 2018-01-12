#coding=utf-8
#eg.:difflib-test.py file1 file2 report.html

import sys
import difflib



file1 = sys.argv[1]
file2 = sys.argv[2]
#report = sys.argv[3]

def GetLines(file_name):
    return open(file_name).readlines()

txt_line1 = GetLines(file1)
txt_line2 = GetLines(file2)

d = difflib.HtmlDiff()

with open('report.html', 'w') as f:
    f.write(d.make_file(txt_line1, txt_line2))

def utf():
    with open('report.html', 'r') as f:
        lines = f.readlines()
    with open('report.html', 'w') as w:
        for line in lines:
            w.write(line.replace('ISO-8859-1', 'utf-8'))
utf()
