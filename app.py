# Import Flask and render-template.
from flask import Flask, render_template, request, redirect
app=Flask(__name__)

# Add function for Route 'Sign-Up'

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        print(req)

        return redirect('/')

    return render_template('signup.html', title = 'Sign-Up')

# Add function for Route "/data".  This will display the entered data

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        
        req = request.form

    return render_template('data.html', title = 'Data', req = req)


app.run(debug=True)