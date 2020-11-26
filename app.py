# Import Flask and render-template.
from flask import Flask, render_template
app=Flask(__name__)

# Add function for Route

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template('signup.html', title = 'Sign-Up')










app.run(debug=True)