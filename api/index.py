from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)
@app.route('/ar-vr')
def tech_redirect():
    return redirect("https://forms.gle/ZYk5jEryn1Vi6m7L9", code=302)
