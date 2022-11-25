import os,base64

template = open("template.html").read()

def epkToBase64(epkname):
    epk = open(f"../packs/{epkname}.epk","rb").read()
    return base64.b64encode(epk).decode("utf-8")

luvre = epkToBase64("007")
pvp = epkToBase64("1.17PvP")
eighteen = epkToBase64("1.8")
clown = epkToBase64("ClownPierce32x")
vplus2 = epkToBase64("vplus2")
fruitful = epkToBase64("FruitFul32x")
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
bedless = epkToBase64("bn550")
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
frag = epkToBase64("frag")
gawr = epkToBase64("gawr")
heated = epkToBase64("heated")
kirby = epkToBase64("kirby")
lazy = epkToBase64("lazy")
leo = epkToBase64("leo")
lunar = epkToBase64("lunar")
luv = epkToBase64("luv")
magma = epkToBase64("magma")
mars = epkToBase64("mars")
miamiprivate = epkToBase64("miamiprivate")
mid = epkToBase64("mid")
modifiednew = epkToBase64("modifiednew")
nebula = epkToBase64("nebula")
nicofruit = epkToBase64("nicofruit")
novisfixed = epkToBase64("novisfixed")
orchid = epkToBase64("orchid")
plat = epkToBase64("plat")
prism = epkToBase64("prism")
purpled = epkToBase64("purpled")
rasplin = epkToBase64("rasplin")
rbwtory = epkToBase64("rbwtory")
refaultfixed = epkToBase64("refault fixed")
resent = epkToBase64("resent")
rhedd = epkToBase64("rhedd")
ricefault = epkToBase64("ricefault")
rosamie32x = epkToBase64("rosamie 32x")
rubellite = epkToBase64("rubellite")
sabor = epkToBase64("sabor")
san = epkToBase64("san")
sangRE = epkToBase64("sangRE")
shyguyfixed = epkToBase64("shyguyfixed")
simplybombies = epkToBase64("simplybombies")
skyline = epkToBase64("skyline")
solr2 = epkToBase64("solr2")
soup = epkToBase64("soup")
sunset = epkToBase64("sunset")
sup = epkToBase64("sup")
swiss = epkToBase64("swiss")
tightfault = epkToBase64("tightfault")
toxicaspec = epkToBase64("toxica spec")
tron16 = epkToBase64("tron 16")
twizzydefault = epkToBase64("twizzydefault")
venomv2 = epkToBase64("venomv2")
walifault = epkToBase64("walifault")
wemmbu = epkToBase64("wemmbu")
woody = epkToBase64("woody")
woody2 = epkToBase64("woody2")

def templatePatch(key, value):
    global template
    template = template.replace(key, value)

                     
templatePatch("007_epk", luvre)
templatePatch("1.17PvP_epk", pvp)
templatePatch("1.8_epk", eighteen)
templatePatch("ClownPierce32x_epk", clown)
templatePatch("FruitFul32x_epk", fruitful)
templatePatch("latenci_epk", latenci)
templatePatch("Lemon_epk", lemon)
templatePatch("NqouirFinnalyFixedsmh_epk", nqouir)
templatePatch("RKYfault_epk", rkyfault)
templatePatch("Someguys1kpack_epk", someguy1k)
templatePatch("Urusai_epk", urusai)
templatePatch("aether_epk", aether)
templatePatch("arm_epk", arm)
templatePatch("asda_epk", asda)
templatePatch("asda_short_epk", asdashort)
templatePatch("azura_epk", azura)
templatePatch("bda_epk", bda)
templatePatch("bear_epk", bear)
templatePatch("blue_epk", blue)
templatePatch("blue128x_epk", blue128x)
templatePatch("bluepack_epk", bluepack)
templatePatch("bn550_epk", bedless)
templatePatch("bombies_epk", bombies)
templatePatch("bombies80k_epk", bombies80)
templatePatch("bones_epk", bones)
templatePatch("bonesnormalsword_epk", bonesnormalsword)
templatePatch("bonsai_epk", bonsai)
templatePatch("boxing128x_epk", boxing)
templatePatch("bubblerose_epk", bubblerose)
templatePatch("camellia_epk", camellia)
templatePatch("candy_epk", candy)
templatePatch("cobalt_epk", cobalt)
templatePatch("collide_epk", collid)
templatePatch("defaultfps_epk", defaultfps)
templatePatch("defaultnew_epk", defaultnew)
templatePatch("defaultold_epk", default)
templatePatch("dino_epk", dino)
templatePatch("drago_epk", drago)
templatePatch("dynamic_epk", dynamic)
templatePatch("eternity_epk", eternity)
templatePatch("faithful_epk", faithful)
templatePatch("frag_epk", frag)
templatePatch("gawr_epk", gawr)
templatePatch("heated_epk", heated)
templatePatch("kirby_epk", kirby)
templatePatch("lazy_epk", lazy)
templatePatch("leo_epk", leo)
templatePatch("lunar_epk", lunar)
templatePatch("luv_epk", luv)
templatePatch("magma_epk", magma)
templatePatch("mars_epk", mars)
templatePatch("miamiprivate_epk", miamiprivate)
templatePatch("mid_epk", mid)
templatePatch("modifiednew_epk", modifiednew)
templatePatch("nebula_epk", nebula)
templatePatch("nicofruit_epk", nicofruit)
templatePatch("novisfixed_epk", novisfixed)
templatePatch("orchid_epk", orchid)
templatePatch("plat_epk", plat)
templatePatch("prism_epk", prism)
templatePatch("purpled_epk", purpled)
templatePatch("rasplin_epk", rasplin)
templatePatch("rbwtory_epk", rbwtory)
templatePatch("refault fixed_epk", refaultfixed)
templatePatch("resent_epk", resent)
templatePatch("rhedd_epk", rhedd)
templatePatch("ricefault_epk", ricefault)
templatePatch("rosamie 32x_epk", rosamie32x)
templatePatch("rubellite_epk", rubellite)
templatePatch("sabor_epk", sabor)
templatePatch("san_epk", san)
templatePatch("sangRE_epk", sangRE)
templatePatch("shyguyfixed_epk", shyguyfixed)
templatePatch("simplybombies_epk", simplybombies)
templatePatch("skyline_epk", skyline)
templatePatch("solr2_epk", solr2)
templatePatch("soup_epk", soup)
templatePatch("sunset_epk", sunset)
templatePatch("sup_epk", sup)
templatePatch("swiss_epk", swiss)
templatePatch("tightfault_epk", tightfault)
templatePatch("toxica spec_epk", toxicaspec)
templatePatch("tron 16x_epk", tron16)
templatePatch("twizzydefault_epk", twizzydefault)
templatePatch("venomv2_epk", venomv2)
templatePatch("walifault_epk", walifault)
templatePatch("wemmbu_epk", wemmbu)
templatePatch("woody_epk", woody)
templatePatch("woody2_epk", woody2)
templatePatch("vplus2_epk", vplus2)
                     
                     
templatePatch("classes_js", open("../classes.js").read())
templatePatch("eagswebrtc_js", open("../eagswebrtc.js").read())
templatePatch("classes_server_js", open("../classes_server.js").read())

templatePatch("_css_", open("../styles.css").read())

templatePatch("_date_", os.popen("date").read())


open("../offline.html", "w").write(template)

print("generated offline.html at " + os.popen("date").read())
