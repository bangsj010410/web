from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return render_template("main.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/signin_page', methods=['GET', 'POST'])
def signin_page():
    if request.method == 'GET':
        return '데이터를 받아주는 페이지'
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된값", email, pwd)
        return '회원가입 데이터(POST)'

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/gonaver', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return '당신이 검색한 키워드'
    else:
        # 여기 POST로 들어오는 데이터를 받아보자
        search = request.form['fname']
        print("전달된값", search)
        return '당신이 검색한 기워드(POST)<br>{}입니다'.format(search)

if __name__ == '__main__':
    app.run()