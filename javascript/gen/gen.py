import os,base64

template = open("template.html").read()

def epkToBase64(epkname):
    epk = open(f"../packs/{epkname}.epk","rb").read()
    return base64.b64encode(epk).decode("utf-8")

007 = epkToBase64("007")
117pvp = epkToBase64("1.17PvP")
18 = epkToBase64("1.8")
clown = epkToBase64("ClownPierce32x.epk")
fruitful = epkToBase64("FruitFul32x.epk")
latenci = epkToBase64("Latenci")
lemon = epkToBase64("Lemon")
nqouir = epkToBase64("NqouirFinnalyFixedsmh")
rkyfault = epkToBase64("RKYfault")
someguy1k = epkToBase64("Someguys1kpack")
urusai = epkToBase64("Urusai")
aether = epkToBase64("aether")
arm = epkToBase64("arm")
asda = epkToBase64("asda")
asdashort = epkToBase64("asda_short")
azura = epkToBase64("azura")
bda = epkToBase64("bda")
bear = epkToBase64("bear")
blue = epkToBase64("blue")
blue128x = epkToBase64("blue128x")
bluepack = epkToBase64("bluepack")
bn550 = epkToBase64("bn550")
bombies = epkToBase64("bombies")
bombies80 = epkToBase64("bombies80k")
bones = epkToBase64("bones")
bonesnormalsword = epkToBase64("bonesnormalsword")
bonsai = epkToBase64("bonsai")
boxing = epkToBase64("boxing128x")
bubblerose = epkToBase64("bubblerose")
camellia = epkToBase64("camellia")
candy = epkToBase64("candy")
cobalt = epkToBase64("cobalt")
collid = epkToBase64("collide")
defaultfps = epkToBase64("defaultfps")
defaultnew = epkToBase64("defaultnew")
default = epkToBase64("defaultold")
dino = epkToBase64("dino")
drago = epkToBase64("drago")
dynamic = epkToBase64("dynamic")
eternity = epkToBase64("eternity")
faithful = epkToBase64("faithful")
fb = epkToBase64("fb")

def templatePatch(key, value):
    global template
    template = template.replace(key, value)

templatePatch("default_epk", default)

templatePatch("classes_js", open("../classes.js").read())
templatePatch("eagswebrtc_js", open("../eagswebrtc.js").read())
templatePatch("classes_server_js", open("../classes_server.js").read())

templatePatch("_css_", open("../style.css").read())

templatePatch("_icon_", base64.b64encode(open("../favicon.png","rb").read()).decode("utf-8"))

templatePatch("_date_", os.popen("date").read())


open("../offline.html", "w").write(template)

print("generated offline.html at " + os.popen("date").read())
