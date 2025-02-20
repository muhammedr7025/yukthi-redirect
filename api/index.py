from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)
@app.route('/Deep-learning')
def deep_learning_redirect():
    return redirect("https://forms.gle/dgGsjh4PJ83WaYiv7", code=302)

@app.route('/Game-developement')
def game_dev_redirect():
    return redirect("https://forms.gle/itc3wofLT7kKpTjZ6", code=302)
