from flask import *
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form["name"]
        useremail= request.form["email"]
        usermobile = request.form["mobile"]
        return redirect(url_for('result', name=username, email=useremail, mobile=usermobile))
    return render_template('index.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    username = request.form.get('name')
    useremail= request.form.get('email')
    usermobile = request.form.get('mobile')
    return render_template('result.html', name=username, email=useremail, mobile=usermobile)

if __name__ == "__main__":
    app.run(debug=True)
