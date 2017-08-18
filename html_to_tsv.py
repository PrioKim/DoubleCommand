from bs4 import BeautifulSoup
import urllib2
import csv
import re
import sys

content = ""
with open('2007-01-01.XLS', 'r') as content_file:
    for line in content_file.readlines():
        content += line

soup = BeautifulSoup(content, "lxml")
#table = soup.select_one("table.boardList03")
table = soup.find_all('table')[0]
headers = [th.text.encode("utf-8") for th in table.select("tr th")]

rows = []
first = True
pattern = re.compile(r'\s+')

for row in table.find_all('tr'):
    cols = []
    if(first):
        for col in row.find_all('th'):
            cols.append(re.sub(pattern, '', col.text.encode("euc-kr")))
        rows.append(cols)
        first = False
    else :
        for col in row.find_all('td'):
            cols.append(re.sub(pattern, '', col.text.encode("euc-kr")))
        rows.append(cols)


with open("out.tsv", "w") as f:
    wr = csv.writer(f, delimiter='\t')
    wr.writerows(rows)
