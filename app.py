# Import Flask and render-template.
from flask import Flask, render_template, request, redirect
app=Flask(__name__)

# Add function for Route

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        print(req)

        return redirect(request.url)

    return render_template('signup.html', title = 'Sign-Up')










app.run(debug=True)