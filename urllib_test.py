import urllib.request
import urllib.parse

url = 'http://www.voidspace.org.uk'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
data = urllib.parse.urlencode(values)
# print(data) # name=Michael+Foord&location=Northampton&language=Python
data = data.encode('ascii')
# print(data) # b'name=Michael+Foord&location=Northampton&language=Python'

req= urllib.request.Request(url, data)
# print(req) # <urllib.request.Request object at 0x10080c7d0>
try:
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print(response.status)
    print(response.getheaders()) 
    # [('Server', 'nginx'), ('Date', 'Sat, 23 May 2020 12:16:07 GMT'), ('Content-Type', 'text/html'), ('Content-Length', '10481'), ('Connection', 'close'), ('Vary', 'Accept-Encoding'), ('Last-Modified', 'Mon, 18 May 2015 15:48:59 GMT'), ('ETag', '"28f1-5165d21d610c0"'), ('Accept-Ranges', 'bytes')]
    dict = dict(response.getheaders())
    # {'Server': 'nginx', 'Date': 'Sat, 23 May 2020 12:16:07 GMT', 'Content-Type': 'text/html', 'Content-Length': '10481', 'Connection': 'close', 'Vary': 'Accept-Encoding', 'Last-Modified': 'Mon, 18 May 2015 15:48:59 GMT', 'ETag': '"28f1-5165d21d610c0"', 'Accept-Ranges': 'bytes'}
    print(dict['Date'])
    # print(the_page)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason())
