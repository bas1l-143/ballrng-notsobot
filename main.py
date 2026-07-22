# hi code lurker

import random
import math
import time
args=discord["variables"]["__args"]
if args:
    arg=args[0]
else:
    arg=None
attributes={
"Ball": 1,
"Cubed": 5,
"Reflective": 8,
"Colorful": 10,
"Bouncy": 14,
"Textured": 20,
"Damaged": 26,
"Reinforced": 33,
"Studded": 45,
"Outlined": 55,
"Rotten": 67,
"Hinged": 75,
"Sparkling": 89,
"Big": 100,
":100:": 100,
"Heavy": 133,
"Sticky": 151,
"Magnetic": 177,
"Loud": 198,
"Halved": 250,
"Bronze": 300,
"Restricted": 403,
"Small": 444,
"Golden": 500,
"Low-gravity": 580,
"Magical": 625,
"Evil": 666,
"Explosive": 700,
"Visible": 727,
"Invisible": 799,
"Anchored": 900,
"Electrified": 1000,
"Spinning": 1234,
"Non-existing": 1404,
"Old": 1500,
"Cursed": 1666,
"Stunned": 1750,
"Retro": 1986,
"Bitten": 1987,
"Spammed": 1997,
"Filler": 2225,
"𝓯𝓻𝓮𝓪𝓴𝔂": 2369,
"Musical": 2500,
"Gun": 2591,
"Radioactive": 2880,
"Angel": 3000,
":3": 3333,
"Teleporting": 3750,
"Moss": 4000,
"Tuff": 4444,
"🔬": 5000,
"██████": 5500,
"Secret": 5898,
"None": 6000,
"Devilish": 6666,
"Steamed": 7000,
"Jackpot": 7777,
"Powerful": 8192,
"8Ball": 8888,
"True":10000, 
"False":10000, 
"Programmed": 10101,
"DIVORCED!!!!": 12398,
"Sentient": 14500,
"Popular": 16384,
"Alien": 19999,
"Bright": 22222,
"Dark": 22222,
"Expensive": 25000,
"Random": 28462,
"Netherite": 32000,
"Laggy": 33333,
"Spooky&Scary": 36999,
"Bizarre": 38989,
"Destructive": 40506,
"Reverted": 45454,
"Half-baked": 50000,
"LED": 55000,
"Alien": 60000,
"Diabolical": 66666,
"Nice": 69420,
"Biggie": 79999,
"Split": 81250,
"Undying": 90001,
"Winpad": 99999,
"Fail": 100000,
"Success": 100000,
"Pixelated": 131072,
"the thing": 199999,
"PYTHONIUM": 200000,
"Niche": 234567,
"Clickbait": 300300,
"369": 369369,
"Turret": 381209,
"NEWater": 400000,
"Rebranded": 420420,
"Wistful": 500001,
"green_apple:": 575109,
"Mephistophelian": 666666,
"Unpleasant Gradient": 795350,
"Free robux": 800008,
"nil.": 888888,
"Array": 901901,
"Computer Annihilator MK 3500": 959070,
"Prismatic": 1000000,
"_": 1111111,
"Santa's Attack": 1234567,
"Air": 2000000,
"Trol": 3333333,
"Jered": 4000000,
"Basil": 5000000,
"Afjap": 5000000,
"Hyperchromic": 6125000,
"Lesopowal": 6666666,
"Phantasmic": 7010107,
"MRBEAST": 7777777,
"Low Quality Tree": 8425425
"Supercalifragilisticexpialidocious": 9999999,
"Lucidity": 10000000,
"RNGdle": 12345678,
"16777216": 16777216,
"Neutronic": 22500000,
"Ataxia": 27500000,
"Incessant": 30158195,
"Hyper": 37555555,
"Galactic": 42000000,
"Sublimity": 50000000,
"Dopamine": 67800000,
"Epinephrine": 99999999,
"Eternity": 100000000,
"Hyperfigmentia": 165891520,
"Futurescape": 212576000,
"A Broken Dream": 256512128,
"Pie": 314159256,
"Euphoria": 444444444,
"Necrotica": 510000000,
"Stairway to Heaven": 650000000,
"Elysium": 777777777,
"Infinitude": 1000000000,
"Initium Finis": 2500000000,
    
    
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
# because of nsb saving i do it this way, fuck you nsb
userrarest=userrarest.split(",")
servrarest=servrarest.split(",")
userdiscovered=userdiscovered.split(",")
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
        print("Tag by: sd\\_.n\\_\nBased on balls.rng on roblox, inspired by the attrng tag by BonesYT.\nAn idle game where you roll for balls, which may have various attributes, from really common ones to extraordinarily rare ones.\nNot much else to say.")
        exit()
    elif arg=="help":
        print("Usable arguments:\n`.t (tag) get` - prints user+server data. if you want to look at it then sure, but its mostly for debug purposes.\n`.t (tag) about` - info about the game\n`.t (tag) help` - <:g_:1501846104797352038>\n`.t (tag) stats` - shows your current stats and server stats.\n`.t (tag) attributes` - shows your discovered attributes.\n`.t (tag) showatt (attribute)` - shows the rarity of an attribute")
        exit()
    elif arg=="stats":
        print("## User stats:")
        rball = ""
        for b in userrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(userrarest[0])) 
        print(f"Rarest ball: {rball}")
        da,ho,mi,se=secondstodhms(usertime)
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Total rolls: {usertime} ({timetext})")
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        da,ho,mi,se=secondstodhms(round(time.time()-userlast))
        timetext=""
        if da: timetext+=f"{da}d{ho}h{mi}m{se}s"
        elif ho: timetext+=f"{ho}h{mi}m{se}s"
        elif mi: timetext+=f"{mi}m{se}s"
        else: timetext+=f"{se}s"
        print(f"Current afk time: {timetext}")
        print(f"## Server stats:")
        rball = ""
        for b in servrarest[1:]:
            rball+=f"{b} "
        rball += "(1/{:,})".format(int(servrarest[0])) 
        print(f"Rarest ball: {rball}")
        exit()
    elif arg=="attributes":
        attamt=len(userdiscovered)
        print(f"Discovered attributes: {attamt}/{len(attributes)}")
        if len(attributes)==attamt:
            print("All attributes discovered!")
        attsort=sorted(userdiscovered, key=attkey, reverse=True)
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
rolls = round(time.time()-userlast)
remain = 0
if rolls > 86400:
    remain = rolls-86400
    rolls = 86400

b=[]
discv=0
for i in range(rolls):
    ball = genball()
    for l in ball[1:]:
        if not (l in userdiscovered):
            userdiscovered.append(l)
            discv+=1
        
    b.append(ball)
def key(n):
    return n[0]
b=sorted(b, key=key, reverse=True)

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
da,ho,mi,se=secondstodhms(rolls)
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
if issrar: print("# *NEW SERVER BEST!*")
elif isurar: print("## NEW USER BEST!")
if discv:
    print(f"You discovered {discv} new attributes!")
if remain:
    print(f"Rolls per command are capped to 1 day of afk (86400 rolls), use this tag repeatedly to roll the remaining {remain} times.")
print(f"-# Use `.t (tag) help` for the argument list.")
# user data
discord["storage"]["user"]["rarestball"] = userrarest
discord["storage"]["user"]["last"] = time.time()-remain
discord["storage"]["user"]["discovered"] = userdiscovered
discord["storage"]["user"]["time"] = usertime+rolls
# server data
discord["storage"]["server"]["rarestball"] = servrarest
