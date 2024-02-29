from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)
@app.route('/ar-vr')
def ar_vr():
    return redirect("https://forms.gle/ZYk5jEryn1Vi6m7L9", code=302)
@app.route('/robotics')
def robotics():
    return redirect("https://forms.gle/vsqG4RfCurwtfQ728", code=302)
@app.route('/blockchain')
def blockchain():
    return redirect("https://forms.gle/F2zpbDCszadUTYTF8", code=302)
@app.route('/aiandllm')
def aiandllm():
    return redirect("https://forms.gle/PMw4exnJwYz2EmZf6", code=302)
@app.route('/ui-ux')
def ui_ux():
    return redirect("https://forms.gle/Nkegh4t7Nc717dRY9", code=302)
@app.route('/hardwarehacking')
def hardwarehacking():
    return redirect("https://forms.gle/WZQDeMzCBAFBgCEe8", code=302)
@app.route('/webdev')
def webdev():
    return redirect("https://forms.gle/iCnR5mVrTZmMiV7E9", code=302)
@app.route('/hackathon')
def hackathon():
    return redirect("https://yukthi-hackathon.devfolio.co/", code=302)
@app.route('/3dprinting')
def dprinting():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScwM3e3dw5b9fcIYBa3WHVeLecF-KPw35FUINUjoMnYD74srA/viewform?usp=sf_link", code=302)
@app.route('/proprogrammer')
def proprogrammer():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSd2ob9S1OC15fsXuKL_uWGhbhK2UtQCGrAcAeLIPHZ0XZ8DxA/viewform?embedded=true", code=302)
