# hi code lurker
ROLLRATE = 15
import random
import math
import os
import time
args=discord["variables"]["__args"]
if args:
    arg=args[0]
else:
    arg=None
attributes={
"Ball": 1,
"Pyramid": 2,
"Ball 2": 3,
"Better": 4,
"Cubed": 5,
"Reflective": 8,
"Colorful": 10,
"Glowing": 15,
"Textured": 20,
"Damaged": 25,
"Foggy": 30,
"Reinforced": 33,
"Studded": 45,
"Inletted": 50,
"Outlined": 55,
"Dented": 60,
"Rotten": 67,
"Fiery": 70, 
"Hinged": 75,
"Rare": 80,
"Bouncy": 85,
"Sparkling": 90,
"Squished": 99,
"💯": 100,
"Heavy": 123,
"Sticky": 151,
"Magnetic": 177,
"Flat": 200,
"Halved": 222,
"Bouncy": 275,
"Bronze": 300,
"Oblong": 325,
"Big": 350,
"Cracked": 400,
"Restricted": 403,
"Small": 444,
"Loud": 475,
"Golden": 500,
"Gradiented": 512,
"Low-gravity": 580,
"Damascus": 600,
"Magical": 625,
"Evil": 666,
"Explosive": 700,
"Visible": 727,
"Invisible": 799,
"Disco": 800,
"Pulsing": 850,
"Anchored": 900,
"Marbled": 950,
"Electrified": 1000,
"Spinning": 1234,
"Non-existing": 1404,
"Old": 1500,
"Cursed": 1666,
"Stunned": 1750,
"Retro": 1986,
"Spammed": 1997,
"Year 2000": 2000,
"Filler": 2225,
"𝓯𝓻𝓮𝓪𝓴𝔂": 2369,
"Musical": 2500,
"Gun": 2591,
"Radioactive": 2880,
"Angel": 3000,
"Rainbow": 3200,
":3": 3333,
"Tripped": 3500,
"Teleporting": 3750,
"Moss": 4000,
"Lensing": 4200,
"Tuff": 4444,
"Magma": 4500,
"🔬": 5000,
"██████": 5500,
"Secret": 5898,
"None": 6000,
"Super Loud": 6363,
"Devilish": 6666,
"Steamed": 7000,
"Bitten": 7272,
"Dice": 7500,
"Jackpot": 7777,
"Magical": 8000,
"Powerful": 8192,
"Huge": 8500,
"8Ball": 8888,
"Tiny": 9000,
"Strange": 9500,
"Attribute": 9999,
"True":10000, 
"False":10000, 
"Programmed": 10101,
"Rarium": 11111,
"DIVORCED!!!": 12398,
"Sentient": 14500,
"Popular": 16384,
"Rng": 20000,
"Bright": 22222,
"Dark": 22222,
"Expensive": 25000,
"Random": 28462,
"Netherite": 32000,
"Laggy": 33333,
"Spooky&Scary": 36999,
"Bizarre": 38989,
"Hunk of FLesh": 40000,
"Destructive": 41234,
"Missing": 44040,
"Reverted": 45454,
"Half-baked": 50000,
"LED": 55000,
"Ultra Loud": 57575,
"Alien": 60000,
"Sleeping": 63500,
"Diabolical": 66666,
"Nice": 69420,
"Giant": 70000,
"12-Dice": 75000,
"Midas": 77777,
"Biggie": 79999,
"Donut": 80000,
"Split": 81250,
"Microscopic": 85858,
"Undying": 90001,
"Winpad": 99999,
"Fail": 100000,
"Success": 100000,
"Gyroscopic": 111111,
"Pixelated": 131072,
"the thing": 199999,
"PYTHONIUM": 200000,
"Niche": 234567,
"Austrium": 275275,
"Clickbait": 300300,
"369": 369369,
"Turret": 381209,
"NEWater": 400000,
"Rebranded": 420420,
"Very Rare": 444444,
"Wistful": 500001,
"🍏": 575109,
"华文": 600000,
"El": 620620,
"Mephistophelian": 666666,
"Techno": 700000,
"Titanic": 745745,
"Dice-20": 750000,
"Unpleasant Gradient": 795350,
"Free robux": 800008,
"Atomic": 844444,
"nil.": 888888,
"Array": 901901,
"Computer Annihilator MK 3500": 959070,
"Prismatic": 1000000,
"_": 1111111,
"Santa's Attack": 1234567,
"steamhappy": 1337000,
"NVIDIA GeForce RTX 4070 Ti SUPER": 1500000,
"Cat": 1757575,
"Air": 2000000,
"Mega Loud": 2222222,
"Constellation": 2481632,
"Darkheart": 2500000,
"Deserted": 3000000,
"Trol": 3210123,
"Attached-Tree": 3512791,
"Confused": 3773377,
"Jered": 4000000,
"Mitosis": 4245090,
"Tornado": 4545454,
"Basil": 5000000,
"Afjap": 5000000,
"h": 5250525,
"Super Rare": 5555555,
"Overwhelmed": 6000000,
"Hyperchromic": 6125000,
"Does he know": 6500056,
"Lesopowal": 6666666,
"g": 7000000,
"Phantasmic": 7010107,
"Dice-100": 7500000,
"MRBEAST": 7777777,
"Shucks": 8080808,
"raj": 8500000,
"Globular": 9000000,
"Lustrous": 9250529,
"The Attribute with a very long Name yes": 9500000,
"Slow": 9876543,
"Supercalifragilisticexpialidocious": 9999999,
"Lucidity": 10000000,
"RNGdle": 12345678,
"16777216": 16777216,
"Extractor": 18251800,
"Atmoflux": 20000000,
"Neutronic": 22500000,
"Spacedust": 25025025,
"?": 27777777,
"Ataxia": 29500000,
"He hid for 30 years": 30000000,
"Incessant": 30158195,
"Abyssal": 32759825,
"Spiky": 34567890,
"Hyper": 37555555,
"Starborne": 40000000,
"Galactic": 42000000,
"Subspace Tripmine": 44444444,
"Permafrost": 45045045,
"Calamity": 47555555,
"Sublimity": 50000000,
"Albert Einstein": 53287100,
"Hotel": 56450920,
"Banana Man": 58888888,
"Fiberlike": 60000000,
"Matter Cannon": 64256512,
"Attribute of Doom and Despair": 66666666,
"Dopamine": 67800000,
"Clicker Game": 70000000,
"Artemis": 72345000,
"Chapelic": 75000000,
"Mega Rare": 77777777,
"Pondering": 80000000,
"Pneumonoultramicroscopicsilicovolcanoconiosis": 85085085,
"CommandErrorFile/home/notsocoder/script.py": 88000999,
"Mysticism": 90755709,
"Zany": 98765432,
"Epinephrine": 99999999,
"Eternity": 100000000,
"Digita": 121101110,
"Hyperfigmentia": 165891520,
"Reverie": 180180180,
"Xynveil": 200000000,
"Futurescape": 212576000,
"A Broken Dream": 256512128,
"Altars of Apostasy": 266666666,
"steamEXPLODE": 300000000,
"Pie": 314159256,
"Bootleg Puthing Around": 353535353,
"Secret Universe": 400000000,
"Whitespace": 425782190,
"Euphoria": 444444444,
"Grail": 500000000,
"Necrotica": 510000000,
"Uber Rare": 555555555,
"CortexBreak": 600000000,
"Stairway to Heaven": 626000000,
"Highway": 645000645,
"Apocalypse": 666666666,
"something": 700000000,
"devoid": 750000000,
"Elysium": 777777777,
"Hypersphere": 800000000,
"Illusionary": 825825825,
"Casinoite": 874777777,
"Retina": 925000000,
"Tycoon": 1000000000,
"Stargate": 1250000000,
"Fantasia": 1500000000,
"Emperial": 1750000000,
"fψ(ψI(ω*ω)(2^1024))(2^32)": 2222222222,
"SuperPie": 3141592653,
"Nullheart": 3844733522,
"Dyson": 4444444444,
"Byzandill": 5000000000,
"Bliss": 5900590590,
"Sacrinare": 6666666666,
"Fortissimo": 7500000000,
"RingWorld": 10000000000,
"Dead of Night": 13575350640,
"Kyberia": 15666666666,
"Nameless": 17499999999,
"Dimensional": 20000000001,
"Realisticful": 25000000000,
"Foreverness": 37377377377,
"The Final Rare": 1000000000000,
"g 2": 7777777777777777,
    
    
}

def attkey(n):
    return attributes[n]


time.sleep(0.25)

def genball():
    brar=1
    batts=[]
    for i,ii in attributes.items():
        if random.randint(1,ii)==1:
            brar*=ii
            batts.insert(0, i)
    ball=[]
    ball.append(brar)
    ball.extend(batts)
    return ball
def secondstodhms(time):
    days, remainder = divmod(time, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return (days, hours, minutes, seconds)

data = discord["storage"]["user"]
servdata = discord["storage"]["server"]

userrarest = data.get("rarestball", "1,Ball")
userdiscovered = data.get("discovered", "Ball")
servrarest = servdata.get("rarestball", "1,Ball")
servdiscovered = servdata.get("discovered", "Ball")
# because of nsb saving i do it this way, fuck you nsb
userrarest=userrarest.split(",")
servrarest=servrarest.split(",")
userdiscovered=userdiscovered.split(",")
servdiscovered=servdiscovered.split(",")

for j in userdiscovered[:]:
    if not (j in attributes):
        userdiscovered.remove(j)
        continue
    if not (j in servdiscovered):
        servdiscovered.append(j)

for j in servdiscovered[:]:
    if not (j in attributes):
        servdiscovered.remove(j)

userrarest[0]=int(userrarest[0])
servrarest[0]=int(servrarest[0])

userlast = round(float(data.get("last", time.time()-1)))
usertime = int(data.get("time", 1))

if arg:
    if arg=="get":
        print(data)
        print(servdata)
        exit()
    elif arg=="about":
        print("Tag by: sd\\_.n\\_ - the code | afjap - ALOT of attributes\nBased on balls.rng on roblox, inspired by the attrng tag by BonesYT.\nAn idle game where you roll for balls, which may have various attributes, from really common ones to extraordinarily rare ones.\nNot much else to say.")
        exit()
    elif arg=="help":
        print("Usable arguments:\n`.t (tag) get` - prints user+server data. if you want to look at it then sure, but its mostly for debug purposes.\n`.t (tag) about` - info about the game\n`.t (tag) help` - <:g_:1501846104797352038>\n`.t (tag) stats` - shows your current stats and server stats.\n`.t (tag) [serv]attributes` - shows your (or entire server discovered if servattributes) discovered attributes.\n`.t (tag) showatt (attribute)` - shows the rarity of an attribute")
        exit()
    elif arg=="stats":
        print("## User stats:")
        rball = ""
        for b in userrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(userrarest[0])) 
        print(f"Rarest ball: {rball}")
        da,ho,mi,se=secondstodhms(round(time.time()-userlast))
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Current afk time: {timetext}")
        da,ho,mi,se=secondstodhms(usertime)
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Total rolls: {usertime*ROLLRATE} ({timetext})")
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        rarestatt=(1, "Ball")
        for v in userdiscovered:
            if attributes[v] > rarestatt[0]:
                rarestatt=(attributes[v], v)
        print(f"Rarest attribute found: {rarestatt[1]}" +  "(1/{:,})".format(rarestatt[0]))
        print(f"## Server stats:")
        rball = ""
        for b in servrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(servrarest[0])) 
        print(f"Rarest ball: {rball}")
        attamt=len(servdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        rarestatt=(1, "Ball")
        for v in servdiscovered:
            if attributes[v] > rarestatt[0]:
                rarestatt=(attributes[v], v)
        print(f"Rarest attribute found: {rarestatt[1]}" +  "(1/{:,})".format(rarestatt[0]))
        exit()
    elif arg=="attributes":
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        if len(attributes)==attamt:
            print("All attributes discovered!")
        attsort=sorted(userdiscovered, key=attkey, reverse=True)
        print(f"{attsort}")
        exit()
    elif arg=="servattributes":
        attamt=len(servdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        if len(attributes)==attamt:
            print("All attributes discovered!")
        attsort=sorted(servdiscovered, key=attkey, reverse=True)
        print(f"{attsort}")
        exit()
    elif arg=="showatt":
        if len(args)>1:
            for h,hh in attributes.items():
                if h.lower() == args[1].lower():
                    print(f"{h}: 1/"+"{:,}".format(int(hh)))
                    exit()
            print("No such attribute found.")
            exit()
        else:
            print("No attribute provided.")
    
    print("Invalid argument.")
    exit()
    
ttime = round(time.time()-userlast)

remain = 0
if ttime > 86400:
    remain = ttime-86400
    ttime = 86400
    
rolls = ttime*ROLLRATE

b=[]
attsfound = set({})
discv=0
for i in range(rolls):
    ball = genball()
    for l in ball[1:]:
        attsfound.add(l)
        if not (l in userdiscovered):
            userdiscovered.append(l)
            discv+=1
        if not (l in servdiscovered):
            servdiscovered.append(l)
            
    b.append(ball)
def key(n):
    return n[0]
b=sorted(b, key=key, reverse=True)
attsfound=sorted(list(attsfound), key=attkey, reverse=True)
top3att = attsfound[:3]

top10=b[:10]
top1=top10[0]
isurar, issrar = False, False
if top1[0] > userrarest[0]:
    isurar=True
    userrarest=top1
if top1[0] > servrarest[0]:
    issrar=True
    servrarest=top1
#
da,ho,mi,se=secondstodhms(ttime)
timetext=""
if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
elif ho: timetext+=f"{ho}h{mi}m{se}s"
elif mi: timetext+=f"{mi}m{se}s"
else: timetext+=f"{se}s"
print(f"You were away for {timetext} and you rolled {rolls} times. Showing top 10 finds:")
for i,ii in enumerate(top10):
    bt=""
    for g in ii[1:]:
        bt+=f"{g} "
    print(f"{i+1}. {bt}(1/"+"{:,})".format(int(ii[0]))) 
print("Showing top 3 rarest attribute finds:")
for i,ii in enumerate(top3att):
    if ii == "DIVORCED!!!!":
        print(f"{i+1}. [{ii}]" + r"(https://cdn.discordapp.com/attachments/1307066414531743846/1479243377169010729/ok_sooo_that_happened.mp4?ex=6a61ec00&is=6a609a80&hm=3da32bb1b2e4149e24b4fb6986062e18b1f2b2d6040b62d019d85c1b0f6aaa33&)" + " (1/{:,})".format(attributes[ii]))
    else:
        print(f"{i+1}. {ii}" + " (1/{:,})".format(attributes[ii]))
if issrar: print("# *NEW SERVER BEST!*")
elif isurar: print("## NEW USER BEST!")
if discv:
    print(f"You discovered {discv} new attributes!")
if remain:
    print(f"Rolls per command are capped to 1 day of afk, use this tag repeatedly to roll the remaining {remain*ROLLRATE} ")


rball = ""
for b in userrarest[1:]:
    rball+=f"{b} "
rball += "(1/{:,})".format(int(userrarest[0])) 
print(f"-# User rarest: {rball}")
rball = ""
for b in servrarest[1:]:
    rball+=f"{b} "
rball += "(1/{:,})".format(int(servrarest[0])) 
print(f"-# Server rarest: {rball}")
print(f"-# Use `.t (tag) help` for the argument list.")

# user data
discord["storage"]["user"]["rarestball"] = userrarest
discord["storage"]["user"]["last"] = time.time()-remain
discord["storage"]["user"]["discovered"] = userdiscovered
discord["storage"]["user"]["time"] = usertime+ttime
# server data
discord["storage"]["server"]["rarestball"] = servrarest
discord["storage"]["server"]["discovered"] = servdiscovered
