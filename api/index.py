from flask import Flask
from flask import redirect

app = Flask(_name_)


@app.route("/")
def web_redirect():
    return redirect("https://yukthi.org", code=302)
@app.route("/ar-vr")
def ar_vr():
    return redirect("/arvr", code=302)
@app.route("/aiandllm")
def aiandllm():
    return redirect("/aillm", code=302)
@app.route("/ui-ux")
def ui_ux():
    return redirect("/uiux", code=302)
@app.route("/hardwarehacking")
def hardwarehacking():
    return redirect("https://forms.gle/WZQDeMzCBAFBgCEe8", code=302)
# @app.route("/hackathon")
# def redirect_hackathon():
#    return redirect("https://www.yukthi.org/events/hackathon", code=302)
@app.route("/hackathon")
def hackathon():
    return redirect("https://yukthi-hackathon.devfolio.co/", code=302)
@app.route("/proprogrammer")
def proprogrammer():
    return redirect(
        "/propgmmer",
        code=302,
    )
@app.route("/blindprograming")
def blindprograming():
    return redirect(
        "/blindpgm",
        code=302,
    )
@app.route("/keyboardmastery")
def keyboardmastery():
    return redirect(
        "/kbmastery",
        code=302,
    )
@app.route("/circuitdebugging")
def circuitdebugging():
    return redirect(
        "https://docs.google.com/forms/d/e/1FAIpQLSc47pP1PX5qAxjKbhrms6ojZyCmF01Td0GDFbCng4RO09PTAg/viewform?embedded=true",
        code=302,
    )
@app.route("/alpadrive")
def redirect_alpadrive():
    return redirect("https://www.yukthi.org/events/alpadrive", code=302)
@app.route("/fosswhyhow")
def redirect_fosswhyhow():
    return redirect("https://www.yukthi.org/events/fosswhyhow", code=302)
@app.route("/digsec")
def redirect_digsec():
    return redirect("https://www.yukthi.org/events/digsec", code=302)
@app.route("/prav")
def redirect_prav():
    return redirect("https://www.yukthi.org/events/prav", code=302)
@app.route("/opendata")
def redirect_opendata():
    return redirect("https://www.yukthi.org/events/opendata", code=302)
@app.route("/selfhosting")
def redirect_selfhosting():
    return redirect("https://www.yukthi.org/events/selfhosting", code=302)
@app.route("/valorant")
def redirect_valorant():
    return redirect("https://www.yukthi.org/events/valorant", code=302)
@app.route("/pes")
def redirect_pes():
    return redirect("https://www.yukthi.org/events/pes", code=302)
@app.route("/freefire")
def redirect_freefire():
    return redirect("https://www.yukthi.org/events/freefire", code=302)
@app.route("/bgmi")
def redirect_bgmi():
    return redirect("https://www.yukthi.org/events/bgmi", code=302)
@app.route("/spanathon")
def redirect_spanathon():
    return redirect("https://www.yukthi.org/events/spanathon", code=302)
@app.route("/webhunt")
def redirect_webhunt():
    return redirect("https://www.yukthi.org/events/webhunt", code=302)
@app.route("/ctf")
def redirect_ctf():
    return redirect("https://www.yukthi.org/events/ctf", code=302)
@app.route("/blindpgm")
def redirect_blindpgm():
    return redirect("https://www.yukthi.org/events/blindpgm", code=302)
@app.route("/propgmmer")
def redirect_propgmmer():
    return redirect("https://www.yukthi.org/events/propgmmer", code=302)
@app.route("/fora")
def redirect_fora():
    return redirect("https://www.yukthi.org/events/fora", code=302)
@app.route("/arvr")
def redirect_arvr():
    return redirect("https://www.yukthi.org/events/arvr", code=302)
@app.route("/3dprinting")
def redirect_3dprinting():
    return redirect("https://www.yukthi.org/events/3dprinting", code=302)
@app.route("/blockchain")
def redirect_blockchain():
    return redirect("https://www.yukthi.org/events/blockchain", code=302)
@app.route("/aillm")
def redirect_aillm():
    return redirect("https://www.yukthi.org/events/aillm", code=302)
@app.route("/robotics")
def redirect_robotics():
    return redirect("https://www.yukthi.org/events/robotics", code=302)
@app.route("/hwhacking")
def redirect_hwhacking():
    return redirect("https://www.yukthi.org/events/hwhacking", code=302)
@app.route("/webdev")
def redirect_webdev():
    return redirect("https://www.yukthi.org/events/webdev", code=302)
@app.route("/uiux")
def redirect_uiux():
    return redirect("https://www.yukthi.org/events/uiux", code=302)
@app.route("/linux")
def redirect_linux():
    return redirect("https://www.yukthi.org/events/linux", code=302)
@app.route("/kbmastery")
def redirect_kbmastery():
    return redirect("https://www.yukthi.org/events/kbmastery", code=302)
@app.route("/segfault")
def redirect_segfault():
    return redirect("https://www.yukthi.org/events/segfault", code=302)
