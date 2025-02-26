from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def web_redirect():
    return redirect("https://yukthi.org", code=302)

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
def Entrepreneurship_redirect():
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

@app.route('/latex')
def latex_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSc_cYjOrC-WDGYaUVfPrKlCunxlq4loY4d1vjKKjj4RWHlaMw/viewform", code=302)

@app.route('/linux')
def linux_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScCocDvv741qHVISD3dkAj2GkPmlK6-pkfXntDrcNNblZ2ljg/viewform", code=302)

@app.route('/rom')
def rom_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfsZW7F2L7HjQ321fujO88_Ucg-OTKNW-DPcXmHfazUIBqgoQ/viewform", code=302)

@app.route('/ace')
def ace_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSejP4mdViELaWab3xvAGVov_tkfMKQUFS3CCzrXW1uVddaRIA/viewform?usp=sharing", code=302)

@app.route('/cybersecurity')
def cybersecurity_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeGOxeWDn-DtjaaYhjc3YXdYazBEoMr6MPteyKmg2dhKFTysw/viewform", code=302)

@app.route('/robotics')
def robotics_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSda2wAVxzdtgaIzJc0iRwjcl0jKx_75BROm3ffXY8O5ZTLSVw/viewform", code=302)

@app.route('/blueprint')
def blueprint_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScJU_W-Kot623vBHqxEoewnkSJcKLPCGHauJExYQ32IOQE7Hw/viewform", code=302)

@app.route('/sketchup')
def sketchup_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSe9STfnKQ6trMBIEzu8RQDev_ivGALnI7oxdqSokj17uC17Mg/viewform", code=302)

@app.route('/3dprinting')
def _3dprinting_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeTk9TI1FdnAaiDp8YvrLSErRT7yWyGNnh2iuzdfdUF-TDcpQ/viewform", code=302)

@app.route('/revit')
def revit_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSeOTY4rDjeg8n2kUUCUyV3ZMO6MBQnvrh8WgMUmqMMO2LttnA/viewform", code=302)

# Competitions

@app.route('/ctf')
def ctf_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSefsoUeAyvETcGTBu0ft7gExKcjR5NVmei9h51zCmqpS7PjVA/viewform", code=302)

@app.route('/pinnacle')
def ctf_redirect():
    return redirect("https://forms.gle/ZXEZJpXcDGcdgP1KA", code=302)

@app.route('/blind')
def blind_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSd5vb-uTRgDi4autLbvVOljIuUVsutZvTiAy-IaGGfOShIjYw/viewform", code=302)

@app.route('/keyboard')
def keyboard_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLScdmc9xjS5dt8bkmYE8kyMiOJewccYigiF3GoPPJxUFAoA2JA/viewform", code=302)

@app.route('/circuitdebug')
def circuitdebug_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSezrC5itD2CraL2ZgINIO5-JXslBxQYNxUG4828dVSt_uPCEw/viewform", code=302)

@app.route('/photo')
def photo_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfMFSCHLqpofb7alrzn3letvE2m1gIy__gnkCS4Ha7XY_wmUQ/viewform", code=302)

@app.route('/iot')
def iot_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSciRo5_OGTEUrhdR5flAzGPwEX_lLzP0i9-jYGHfjoG8J5PTg/viewform", code=302)

@app.route('/act')
def act_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdjoB2g0Sw0JacIhy5Cy61Gj9aBWYeXEAhWdRoCCA0gwyF2Qg/viewform", code=302)

@app.route('/fora')
def fora_redirect():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSecTUUFI6GdbXvqw8mWb6rDgMmOyBCexif3btjMy3w02e7mBg/viewform", code=302)

#pre-evnts

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
