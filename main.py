from flask import Flask,render_template,request,redirect
from traceback import format_exc
from module import meta,make,fix
from replit import db
from time import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/')
def search():
  start = time()
  q = request.args.get('search')
  results = []
  errors = []
  error = None
  for x in q.split(' '):
    try:
      results = results + list(db[x])
    except:
      errors.append(x)
      error = format_exc()
  rcontent = make(results)
  return render_template('results.html',
                         query=q,
                         content=rcontent,
                         error=fix(errors),
                         errorstr=error,
                         time=time()-start
                        )

@app.route('/add',methods=['GET'])
def add():
  return render_template('addsite.html')

@app.route('/add',methods=['POST'])
def site():
  name = request.form.get('name').lower()
  name = name.replace('https://','')
  tags = request.form.get('tag').lower().split(',')
  wasd = meta(name)
  name2 = wasd[2].lower()
  tags2 = wasd[3].lower().split(',')
  for tag in (tags + tags2):
    try:
      db[tag] = list(db[tag])
    except:
      db[tag] = [] 
    finally:
      db[tag].append(name)
  try:
    db[name2] = list(db[name2])
  except:
    db[name2] = []
  db[name2].append(name)
  return redirect('/',code=301)

app.run(host='0.0.0.0', port=80)