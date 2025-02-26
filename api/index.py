from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)

# Workshop Routes
@app.route('/Deep-learning')
def deep_learning_redirect():
    return redirect("https://forms.gle/dgGsjh4PJ83WaYiv7", code=302)

@app.route('/Game-development')
def game_dev_redirect():
    return redirect("https://forms.gle/itc3wofLT7kKpTjZ6", code=302)

@app.route('/yudhya-hackathon')
def yudhya_hackathon_redirect():
    return redirect("https://yudhya.devfolio.co/overview", code=302)

@app.route('/Entrepreneurship')
def entrepreneurship_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdLbChTkcGMkfNMd4ytZAZQgRgf103TNRQKe7uD1nx9Eeu9lw/viewform?usp=dialog", code=302)

@app.route('/Rpa')
def rpa_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc9UjbDdzI2qGbIu7snO8nfPIrNgeD8vVaYTW1cSxbkzL9JHw/viewform", code=302)

@app.route('/Ui-Ux')
def ui_ux_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfKvcyB9cPBnjHmVEwGm-JuJf4yey74yzCyg52iTobz-BQF1g/viewform", code=302)

@app.route('/Drone-scope')
def drone_scope_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeDR7oeqkjqsfV9EBGWa5wNGlXKFZlhlLolvvLjKi-M_iJYwg/viewform", code=302)

@app.route('/unreal-engine')
def unreal_engine_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScQiolFj4A-PX6iywle1FkijByfzPV8a9dRjA5AXkg5I2mByg/viewform", code=302)

@app.route('/ai-llm')
def ai_llm_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdLw2aAQQO64Seicvg-h-QMxM_SWAEDjS5Kd5dnT6t1mb-M_g/viewform", code=302)

# Competitions
@app.route('/pinnacle')
def pinnacle_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfO8D-D6EWOyp6nL3iAlGi-b3Hj76LLxdlQtFyw3QdkEHgtcw/viewform?usp=sharing", code=302)

@app.route('/spanova')
def spanova_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScHsbxlj3uhnJPIB3KGCH0eiCA671AwGhwofwJ4o0UZgCfOaw/viewform?usp=sharing", code=302)

@app.route('/freefire')
def freefire_redirect():
    return redirect("https://forms.gle/LABg4q45EEbu8gts8", code=302)

@app.route('/customrom')
def customrom_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfsZW7F2L7HjQ321fujO88_Ucg-OTKNW-DPcXmHfazUIBqgoQ/viewform?usp=sharing", code=302)

# Pre-events
@app.route('/efootball')
def efootball_redirect():
    return redirect("https://forms.gle/ThzaLjyc1nCWvQnZ8", code=302)

@app.route('/bgmi')
def bgmi_redirect():
    return redirect("https://forms.gle/NQTMmf5pZTvCTR3YA", code=302)

@app.route('/valorant')
def valorant_redirect():
    return redirect("https://forms.gle/WkrV2SQ2vYGtJHy76", code=302)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
