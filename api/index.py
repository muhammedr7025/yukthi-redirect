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

@app.route('/latex')
def latex_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc_cYjOrC-WDGYaUVfPrKlCunxlq4loY4d1vjKKjj4RWHlaMw/viewform?usp=sharing", code=302)

@app.route('/linux')
def linux_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScCocDvv741qHVISD3dkAj2GkPmlK6-pkfXntDrcNNblZ2ljg/viewform?usp=sharing", code=302)

@app.route('/rom')
def rom_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfsZW7F2L7HjQ321fujO88_Ucg-OTKNW-DPcXmHfazUIBqgoQ/viewform?usp=sharing", code=302)

@app.route('/ace')
def ace_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSejP4mdViELaWab3xvAGVov_tkfMKQUFS3CCzrXW1uVddaRIA/viewform?usp=sharing", code=302)

@app.route('/efootball')
def efootball_redirect():
    return redirect("https://forms.gle/NQTMmf5pZTvCTR3YA", code=302)
# Only needed if you're running this script directly
if __name__ == '__main__':
    app.run(debug=True)
