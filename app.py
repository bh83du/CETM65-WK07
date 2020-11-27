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

# Add function for Home

@app.route("/data")
def data():
    req = request.form
    name = req.get("name")
    dept = req.get("dept")
    email = req.get("email")
    password = req.get("password")

    print(req)
    return render_template('data.html', title = 'Dictionary Data', name=name, dept=dept, email=email, password=password)


app.run(debug=True)