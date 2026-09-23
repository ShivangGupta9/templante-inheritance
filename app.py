from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST','get'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'SONA' and password == '123':
        return render_template('welcome.html', name = username)
    else: 
        return "invalid login details" 
    
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)




