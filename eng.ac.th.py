#สกัดหัวข้อข่าวจากเว็ปวิศวะ
#ดูคำอธบายในslide
import urllib.request

url = 'http://www.eng.chula.ac.th'
web = urllib.request.urlopen(url)
for line in web:
    line = line.decode()
    if 'news-title' in line:
        k = line.find('<a href')
        k = line.find('>', k)
        j = line.find('</a>', k)
        print(line[k+1:j])

#web scraping
