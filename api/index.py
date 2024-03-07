from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)
@app.route('/ar-vr')
def ar_vr():
    return redirect("https://www.yukthi.org/events/arvr", code=302)
@app.route('/robotics')
def robotics():
    return redirect("https://www.yukthi.org/events/robotics", code=302)
@app.route('/blockchain')
def blockchain():
    return redirect("https://www.yukthi.org/events/blockchain", code=302)
@app.route('/aiandllm')
def aiandllm():
    return redirect("https://www.yukthi.org/events/aillm", code=302)
@app.route('/ui-ux')
def ui_ux():
    return redirect("https://www.yukthi.org/events/uiux", code=302)
@app.route('/hardwarehacking')
def hardwarehacking():
    return redirect("https://www.yukthi.org/events/hwhacking", code=302)
@app.route('/webdev')
def webdev():
    return redirect("https://www.yukthi.org/events/webdev", code=302)
@app.route('/hackathon')
def hackathon():
    return redirect("https://yukthi-hackathon.devfolio.co/", code=302)
@app.route('/3dprinting')
def dprinting():
    return redirect("https://www.yukthi.org/events/3dprinting", code=302)
@app.route('/proprogrammer')
def proprogrammer():
    return redirect("https://www.yukthi.org/events/propgmmer", code=302)
@app.route('/blindprograming')
def blindprograming():
    return redirect("https://www.yukthi.org/events/blindpgm", code=302)
@app.route('/ctf')
def ctf():
    return redirect("https://www.yukthi.org/events/ctf", code=302)
@app.route('/keyboardmastery')
def keyboardmastery():
    return redirect("https://www.yukthi.org/events/kbmastery", code=302)
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
    return redirect("https://www.yukthi.org/events/flutter", code=302)
