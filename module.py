from traceback import print_exc
from bs4 import BeautifulSoup
from requests import get

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
  return results

def fix(stri): #replit.com',)
  stri = str(stri)
  stri = stri.replace('(','').replace("'","")
  stri = stri.replace(",)",'').replace('<','&lt')
  stri = stri.replace('>','&gt').replace('[','')
  return stri.replace(']','')

def make(sites):
  pattern = '''
  <div>
    <h1 id="X"><a href="https://site">TITLE</a></h1>
    <h2 style="color: grey;" class="hlink">https://site</h2>
    <h2 style="color: darkgrey;">DESCRIPTION</h2>
  </div>
  '''
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