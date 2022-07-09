from traceback import print_exc
from bs4 import BeautifulSoup
from requests import get

pattern = '''  <div>
    <h2 id="X"><a href="https://site">TITLE</a></h2>
    <h3 style="color: grey;" class="hlink">https://site</h3>
    <h3 style="color: darkgrey;">DESCRIPTION</h3>
  </div>'''

imgpattern = '''
<a href="URL"><img src="iSRC" alt="iALT" id="X"></a>
'''

def meta(url): 
  document = get('https://'+url).text
  soup = BeautifulSoup(document,features='html5lib')
  results = []
  for i in ['og:title','og:description','og:site_name']:
    try:
      results.append(soup.find('meta',{'property':i})['content'])
    except:
      x = i.split('og:')[len(i.split('og:'))-1].capitalize()
      results.append('No'+x+'ERROR')
  try:
    results.append(soup.find('meta',{'name':'keywords'})['content'])
  except:
    results.append('NoTagERROR')
  try:
    results.append(soup.title.string)
  except:
    results.append('UNTITLED')
  return results

def fix(stri): #replit.com',)
  stri = str(stri)
  stri = stri.replace('(','&#40').replace("'","&#39")
  stri = stri.replace(",)",'').replace('<','&lt')
  stri = stri.replace('>','&gt').replace('[','')
  return stri.replace(']','')

def make(sites):
  rsts = ''
  ctn = 0
  for site in sites:
    mta = meta(site)
    ctn = ctn + 1
    site = fix(site)
    try: #Needing errors handlers for each 'instruction'
      clone = pattern.replace('X',str(ctn))
      clone = clone.replace('site',site)
      clone = clone.replace('TITLE',mta[0])
      clone = clone.replace('DESCRIPTION',mta[1])
      rsts = rsts + clone
      del clone
    except:
      print_exc()
  return rsts

def tohtml(stri):
  return fix(stri).replace('\n','<br>')

def pics(urls):
  count = 0
  whole = ''
  for url in urls:
    url = 'https://' + url.replace('https://','').replace('http://','')
    document = get(url).text
    soup = BeautifulSoup(document,'html5lib')
    for image in soup.find_all('img'):
      count += 1
      cnt = str(count)
      src = image['src']
      try:
        alt = image['alt']
      except:
        alt = 'NoAltERROR'
      for i in [url+src,src,url+'/'+src]:
        try:
          status = get(i).status_code
        except:
          status = 000
        if(status == 200):
          whole += imgpattern.replace('URL',url).replace('iALT',alt).replace('X',cnt).replace('iSRC',i)
  return whole