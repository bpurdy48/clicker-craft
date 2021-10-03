import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

clicks = 0
money = 0
previous = clicks - 1
cpc = 1
in_shop = False
mission = 100
price = mission / 2
cannot_buy = False
keys = 0
in_boss = False
in_boss_1 = False
sclicks = 0
smoney = 0
cps = 1

steve = Actor("steve")
if not in_boss:
    steve.pos=(CENTER_X, CENTER_Y)
else:
    steve.pos=(CENTER_X, CENTER_Y + 100)


zombie = Actor("zombie")
zombiex = randint(0, WIDTH)
zombiey = randint(0, HEIGHT)
zombie.pos = CENTER_X, CENTER_Y
zombie_health = 0
in_boss_1 = False

shop_button = Rect(0, 0, 240, 100)
shop_button.move_ip(560, 0)

boost_button = Rect(0, 0, 240, 100)
boost_button.move_ip(CENTER_X - 100, CENTER_Y)

key_button = Rect(0, 0, 240, 100)
key_button.move_ip(CENTER_X - 100, CENTER_Y - 150)

lobby_button = Rect(0, 0, 240, 100)
lobby_button.move_ip(0, HEIGHT - 100)

save_button = Rect(0, 0, 240, 100)
save_button.move_ip(WIDTH - 240, HEIGHT - 100)



def draw():
    global in_shop

    if not in_shop and not in_boss:
        screen.blit("overworld", (0, CENTER_Y - 600))
        steve.draw()
        screen.draw.text("Clicks: " + str(clicks), topleft=(0,0), fontsize=60)
        screen.draw.text("$" + str(money), fontsize = 60, color="white", topleft=(0,64))
        screen.draw.text("Click " + str(mission) + " times", topleft=(0,128))
        screen.draw.filled_rect(shop_button, "red")
        screen.draw.textbox("Shop", shop_button, color="black")
        screen.draw.filled_rect(lobby_button, color="red")
        screen.draw.textbox("Lobby", lobby_button, color="black")
        screen.draw.filled_rect(save_button, "red")
        screen.draw.textbox("Save and quit", save_button, color="black")

    elif in_boss:
        screen.blit("cave",(0, 0))
        zombie.draw()
        steve.draw()
    
    else:
        screen.fill("green")
        screen.draw.filled_rect(shop_button, "red")
        screen.draw.textbox("Exit", shop_button, color="black")
        screen.draw.text("$" + str(money), fontsize = 60, color="black", topleft=(0,64))
        screen.draw.text("Click " + str(mission) + " times", topleft=(0,128), color = "black")
        screen.draw.text("Clicks: " + str(clicks), topleft=(0,0), fontsize=60, color = "black")
        screen.draw.filled_rect(boost_button, "red")
        screen.draw.textbox("Upgrade Click Power $" + str(mission / 2), boost_button, color="black")
        screen.draw.filled_rect(key_button, "red")
        screen.draw.textbox("Key $100", key_button, color="black")
    return
        
def on_mouse_down(pos):
    global clicks, cpc, in_shop, money, mission, sclicks
    if steve.collidepoint(pos) and not in_boss:
        if not in_shop:
            clicks = clicks + cpc
            money = money + cpc
    if shop_button.collidepoint(pos):
        if not in_shop and not in_boss:
            price = mission / 2
            in_shop = True

        elif in_shop:
            in_shop = False

    if save_button.collidepoint(pos):
            if not in_shop and not in_boss:
                file = open("clicks.txt", "r+")
                sclicks = clicks
                file.seek(0)
                file.truncate(0)
                file.write(str(sclicks))
                sclicks = int(sclicks)
                file.close()
                file = open("money.txt", "r+")
                smoney = money
                file.seek(0)
                file.truncate(0)
                file.write(str(smoney))
                smoney = int(smoney)
                file.close()
                exit()
    
    if boost_button.collidepoint(pos):
        if in_shop:
            if money < mission / 2:
                cannot_buy = True  
            else:
                cps = cpc + 1
                money = money - mission / 2

def save():
    global sclicks, clicks, money, smoney
    file = open("clicks.txt", "r+")
    sclicks = file.read()
    clicks = int(sclicks)
    file.close()
    file = open("money.txt", "r+")
    smoney = file.read()
    money = int(smoney)
    
def cps_setup():
    global clicks, cps, money
    clicks = clicks + cps
    money = money + cps
    clock.schedule(cps_setup, 1)
    
cps_setup()
save()
music.play("calm1")
    
def update():
    global current_mission, mission, clicks, cpc
    if clicks > mission - 1:
        mission = mission * 10


def zombie_behavior():
    global in_boss, in_boss_1, zombiex, zombiey
    if in_boss and in_boss_1:
        while zombie.x != zombiex:
            if zombiex > WIDTH and zombie.x > WIDTH:
                zombie.x -= 6
                
def steve_position():
    if not in_boss:
        steve.pos=(CENTER_X, CENTER_Y)
    else:
        steve.pos=(CENTER_X, CENTER_Y + 100)

def boss_setup():        boss_setup()
    if in_boss:
        if in_boss_1:
            zombie_behavior()
    elif not in_boss:
        steve_position
    
pgzrun.go()