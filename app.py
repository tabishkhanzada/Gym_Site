from flask import Flask, render_template, redirect  

app = Flask(__name__)

@app.route('/home')
def home_page():
    return render_template('Home.html')

@app.route('/aboutus')
def aboutus_page():
    return render_template('AboutUs.html')

@app.route('/membership')
def member_ship():
    return render_template('MemberShip.html')

if __name__ == '__main__':
    app.run(debug=True)
