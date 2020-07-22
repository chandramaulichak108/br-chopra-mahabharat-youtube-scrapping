import requests, json, re

h = {
    'Referer': 'https://www.youtube.com/playlist?list=PLa6CHPhFNfadNcnVZRXa6csHL5sFdkwmV',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
u = h['Referer']
html = requests.get(u,headers=h).text

matches = re.findall(r'window\["ytInitialData"\] = (.*\}\}\});', html, re.IGNORECASE | re.DOTALL)
j=json.loads(matches[0])

maha={}
print("done!")
main_list=j['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']

for c in main_list:
    maha[c['playlistVideoRenderer']['title']['simpleText']]="https://www.youtube.com/watch?v="+c['playlistVideoRenderer']['videoId']

number_maha=[0]*100

#for c in maha.keys():
#    number_maha[int(c[(c.find('EP'))+5:(c.find('EP'))+7])]='\item\href{'+maha[c]+'}{\hindifont '+c[0:(c.find('Mahabharat')-1)]+' '+c[(c.find('EP')):]+'}\n'

print(number_maha)
f=open("Mahabharat_episodes.txt","w")
for c in maha:
    #print(c)
    strng='\item\href{'+maha[c]+'}{{\hindifont '+c[0:(c.find('Mahabharat')-1)]+'}'+c[(c.find('EP')):(c.find('EP'))+7]+'}\n'
    f.write(strng)
f.close()