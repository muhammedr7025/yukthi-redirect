from flask import Flask, redirect

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

@app.route('/yudhya-hackathon')
def yudhya_hackathon_redirect():
    return redirect("https://yudhya.devfolio.co/overview", code=302)

@app.route('/Rpa')
def rpa_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc9UjbDdzI2qGbIu7snO8nfPIrNgeD8vVaYTW1cSxbkzL9JHw/viewform?usp=header", code=302)

@app.route('/Ui-Ux')
def ui_ux_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfKvcyB9cPBnjHmVEwGm-JuJf4yey74yzCyg52iTobz-BQF1g/viewform?usp=header", code=302)

@app.route('/Drone-scope')
def drone_scope_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeDR7oeqkjqsfV9EBGWa5wNGlXKFZlhlLolvvLjKi-M_iJYwg/viewform?usp=header", code=302)

@app.route('/unreal-engine')
def unreal_engine_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScQiolFj4A-PX6iywle1FkijByfzPV8a9dRjA5AXkg5I2mByg/viewform?usp=header", code=302)

@app.route('/Ai-Llm')
def ai_llm_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdLw2aAQQO64Seicvg-h-QMxM_SWAEDjS5Kd5dnT6t1mb-M_g/viewform?usp=header", code=302)
@app.route('/Entrepreneurship')
def entrepreneurship_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdLbChTkcGMkfNMd4ytZAZQgRgf103TNRQKe7uD1nx9Eeu9lw/viewform?usp=header", code=302)
# Only needed if you're running this script directly
if __name__ == '__main__':
    app.run(debug=True)
