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
@app.route('/blindprograming')
def blindprograming():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfCQddeZi6jbPDopaFgWaTIrO6CdFV3hg-g9RBIlSiRx4NPow/viewform?embedded=true", code=302)
@app.route('/ctf')
def ctf():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScrxNp05Hb0tBPRBiFfHbZgKuxkPBrqB6O6aDmMBrKyJSSXpQ/viewform?embedded=true", code=302)
@app.route('/keyboardmastery')
def keyboardmastery():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeGkRodPuSC8oFenb33t0GWFtEEUAW69FfzGQTX5fohYF0dKg/viewform?embedded=true", code=302)
@app.route('/webhunt')
def webhunt():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfu7FqJTc-eksIUrLXStNLFEyTMdOPARg3-1zqC-LbG0J_i6g/viewform?embedded=true", code=302)
@app.route('/circuitdebugging')
def circuitdebugging():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc47pP1PX5qAxjKbhrms6ojZyCmF01Td0GDFbCng4RO09PTAg/viewform?embedded=true", code=302)
@app.route('/spanathon')
def spanathon():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeLDGKur7k4EQxdoWyZXDIolrSbOkJL51vhO6rpDJ5e9YkW0Q/viewform?embedded=true", code=302)
@app.route('/segfault')
def segfault():
    return redirect("https://app.formbricks.com/eEXUTDkfk4", code=302)
@app.route('/terminusrobo')
def terminusrobo():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeeK6ur-MEOMhl2GPADybgF3rXFqdqocCFsHGqOs-cImH_TsQ/viewform?usp=pp_url", code=302)
@app.route('/flutter')
def flutter():
    return redirect("https://docs.google.com/forms/d/1xBlHVoxMWio4mUJuSMXPC-nrZ9YCvuZFB0C_Lrik6a4/edit?ts=65e2d0d0", code=302)
