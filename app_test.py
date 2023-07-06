import pyrebase

config = {
    "apiKey": "AIzaSyBPbmmATboA8_kxYBYElXjpCX7SXmSUhxI",
    "authDomain": "finaltest-807f5.firebaseapp.com",
    "databaseURL": "https://finaltest-807f5-default-rtdb.firebaseio.com",
    "projectId": "finaltest-807f5",
    "storageBucket": "finaltest-807f5.appspot.com",
    "messagingSenderId": "216402489904",
    "appId": "1:216402489904:web:471532d70f11a3086733f5",
    "measurementId": "G-ERV9YFFHHH"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            email = request.form['email']
            password = request.form['password']
            
            data = {
                'email': email,
                'password': password
            }
            
            db.child("users").push(data)
            
            return render_template('index_test.html')
        
    return render_template('index_test.html')

if __name__ == '__main__':
    app.run(debug = True)

