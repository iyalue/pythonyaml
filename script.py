from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_world'))
   else:
      return redirect(url_for('hello_guest', guest = name))

@app.route('/profile/',methods=['GET','POST'])
def profile():
    name = request.args.get('name')

    if not name:
    # 如果没有name，说明没有登录，重定向到登录页面
        return redirect(url_for('login'))
    else:
        return name

@app.route('/index')
def index():
    return render_template("login.html")

app.run("0.0.0.0",port = "80",debug = True)
