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
in_boss = False

steve = Actor("steve")
if not in_boss:
    steve.pos=(CENTER_X, CENTER_Y)
else:
    steve.pos=(CENTER_X, CENTER_Y + 100)

shop_button = Rect(0, 0, 240, 100)
shop_button.move_ip(560, 0)

boost_button = Rect(0, 0, 240, 100)
boost_button.move_ip(CENTER_X - 100, CENTER_Y)

lobby_button = Rect(0, 0, 240, 100)
lobby_button.move_ip(560, 600)

save_button = Rect(0, 0, 240, 100)
save_button.move_ip(WIDTH - 240, HEIGHT - 100)



def draw():
    global in_shop

    if in_shop ==  False:
        screen.blit("overworld", (0, CENTER_Y - 600))
        steve.draw()
        screen.draw.text("Clicks: " + str(clicks), topleft=(0,0), fontsize=60)
        screen.draw.text("$" + str(money), fontsize = 60, color="white", topleft=(0,64))
        screen.draw.text("Click " + str(mission) + " times", topleft=(0,128))
        screen.draw.filled_rect(shop_button, "red")
        screen.draw.textbox("Shop", shop_button, color="black")
        screen.draw.filled_rect(lobby_button, "red")
    else:
        screen.fill("green")
        screen.draw.filled_rect(shop_button, "red")
        screen.draw.textbox("Exit", shop_button, color="black")
        screen.draw.text("$" + str(money), fontsize = 60, color="black", topleft=(0,64))
        screen.draw.text("Click " + str(mission) + " times", topleft=(0,128), color = "black")
        screen.draw.text("Clicks: " + str(clicks), topleft=(0,0), fontsize=60, color = "black")
        screen.draw.filled_rect(boost_button, "red")
        screen.draw.textbox("Upgrade Click Power $" + str(mission / 2), boost_button, color="black")
    return
        
def on_mouse_down(pos):
    global clicks, cpc, in_shop, money, mission
    if steve.collidepoint(pos):
        if not in_shop:
            clicks = clicks + cpc
            money = money + cpc
    if shop_button.collidepoint(pos):
        if not in_shop:
            price = mission / 2
            in_shop = True

        elif in_shop:
            in_shop = False
    
    if boost_button.collidepoint(pos):
        if in_shop:
            if money < mission / 2:
                cannot_buy = True  
            else:
                cps = cps + 1
                money = money - mission / 2
                
music.play("calm1")

def update():
    global current_mission, mission, clicks, cpc
    if clicks > mission - 1:
        mission = mission * 10
        
    return

def zombie_behavior():
    pass

def steve_position():
    if not in_boss:
        steve.pos=(CENTER_X, CENTER_Y)
    else:
        steve.pos=(CENTER_X, CENTER_Y + 100)
    
pgzrun.go()