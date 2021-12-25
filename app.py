from flask import Flask, render_template, flash, request
from views import views

app = Flask(__name__)
app.secret_key = 'krish3702'
app.register_blueprint(views)

#@app.route('/hello')
#def index():
    #flash("What's your name?")
    #return render_template('index.html')

#@app.route('/greet', methods=['POST',"GET"])
#def greeet():
    #flash(f"Hello {str(request.form['name_input'])}, greet to see you.")
    #return render_template('greet.html')

if __name__ == '__main__':
    app.run(debug=True)