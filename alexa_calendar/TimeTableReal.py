from bs4 import BeautifulSoup as bs
import urllib2
import json
page = 'Timetable.html'
source = open(page, 'r')
soup = bs(source, 'lxml')

#table = soup.find('table')
table_rows = soup.find_all('tr')

def convert_time(inputstring):
    date,time=inputstring.split()
    a=date.split('/')
    a.reverse()
    date='-'.join(a)
    return (date+'T'+time+'Z')

output=[]

for tr in table_rows:
    td = tr.find_all('td')
    if td == []:
        continue 
    row = [i.text for i in td]
    row_m = [x.encode('utf-8') for x in row]
    row_m[2]=row_m[2][:-3]
    row_m[-1]=row_m[-1][1:].rstrip()
    name=row_m[1]+' ('+row_m[0]+') '
    location=row_m[5]
    description=row_m[2]
    time_start=convert_time(row_m[3])
    time_end=convert_time(row_m[4])
    event = {
      'summary': name,
      'location': location,
      'description': description,
      'start': {
        'dateTime': time_start,
        'timeZone': 'UTC',
      },
      'end': {
        'dateTime': time_end,
        'timeZone': 'UTC',
      }
    }
    output.append(event)

with open('data.json', 'w') as outfile:
    json.dump(output, outfile)
