from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/login/',methods=['GET','POST'])
def login():
    return 'login page'

@app.route('/profile/',methods=['GET','POST'])
def profile():
    name = request.args.get('name')

    if not name:
    # 如果没有name，说明没有登录，重定向到登录页面
        return redirect(url_for('login'))
    else:
        return name

app.run("0.0.0.0",port = "80")
