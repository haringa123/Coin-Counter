import pygame 
from pygame import display, time, mixer
pygame.init()

#window
window = pygame.display.set_mode((820,800))
pygame.display.set_caption("Coin Counter")
font = pygame.font.Font('fonts/mvboli.ttf', 17)

#game icon
game_icon = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/coin.png')
pygame.display.set_icon(game_icon)

#COINS
#quarter
quarter = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/quarter.png')
quarter = pygame.transform.scale(quarter,(150,150))
dime = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/dime.png')
dime = pygame.transform.scale(dime,(150,150))
nickel = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/nickel.png')
nickel = pygame.transform.scale(nickel,(150,150))
penny = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/penny.png')
penny = pygame.transform.scale(penny,(150,150))

#amount of coins 250,380
coin_counts = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
def coinamount(coin,x,y):
    amount = font.render("Amount of " + str(coin) + "s: " + str(coin_counts[coin.lower()]) + " ", True, (255,255,255), (0,0,0))
    window.blit(amount, (x,y))

#value of coins 250,420
coin_value = {'quarter': 0, 'dime': 0, 'nickel': 0, 'penny': 0}
def coinvalue(coin,x,y):
    value = font.render("Value of " + str(coin) + "s: " + str(coin_value[coin.lower()]) + "  ", True, (255,255,255), (0,0,0))
    window.blit(value, (x,y))

#TOTAL
total = 0
def total(x,y):
    total = round(sum(coin_value.values()), 2)
    total_print = font.render("Total: $" + str(total), True, (255,255,255), (0,0,0))
    window.blit(total_print, (x,y))

#sprite up arrow 
up_arrow = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/up-arrow.png')
up_arrow = pygame.transform.scale(up_arrow,(50,50))
up_arrow2 = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/up-arrow 2.png')
up_arrow2 = pygame.transform.scale(up_arrow2,(50,50))

def uparrow(coin, up_arrowx,up_arrowy):
    window.blit(up_arrow, (up_arrowx, up_arrowy))
def uparrow2(coin, x,y):
    window.blit(up_arrow2,(x,y))
            
#sprite down arrow
down_arrow = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/down-arrow.png')
down_arrow = pygame.transform.scale(down_arrow,(50,50))
down_arrow2 = pygame.image.load('/Users/dewdr/Documents/Niha/pythongames/Coin counter/down-arrow 2.png')
down_arrow2 = pygame.transform.scale(down_arrow2,(50,50))

def downarrow(coin, down_arrowx, down_arrowy):
    window.blit(down_arrow, (down_arrowx, down_arrowy))
def downarrow2(coin, x,y):
    window.blit(down_arrow2, (x,y))

#game loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #background
    window.fill((0,128,128))
    #middle black box
    pygame.draw.rect(window, (0,0,0), (0,370, 850, 120))
#================================================================================================================================================================
    # #calling sprites in
    # uparrow("quarter", 60,300) #quarter
    # downarrow("quarter",60,510)
    # uparrow("dime", 260, 300) #dime
    # downarrow("dime", 260,510)
    # uparrow("nickel", 460, 300) #nickel
    # downarrow("nickel", 460,510)
    # uparrow("penny", 660, 300) #penny
    # downarrow("penny", 660,510)
    
    # #coins      
    # # coinvalue("quarter", 20, 420)
    # coinamount("quarter", 20, 380)
    # # coinvalue("dime", 220, 420)
    # coinamount("dime", 220, 380)
    # # coinvalue("nickel", 420, 420 )
    # coinamount("nickel", 420, 380)
    # # coinvalue("penny", 620, 420)
    # coinamount("penny", 620, 380)

    # window.blit(quarter, (20, 100))
    # window.blit(dime, (220, 100))
    # window.blit(nickel, (420, 100))
    # window.blit(penny, (620, 100))
#================================================================================================================================================================
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    uparrow_sound = mixer.Sound('/Users/dewdr/Documents/Niha/pythongames/Coin counter/coin_sounds/coin5.wav')
    downarrow_sound = mixer.Sound('/Users/dewdr/Documents/Niha/pythongames/Coin counter/coin_sounds/coin10.wav')
    total(360,50)


    rules = [
       #UP arrow
        {'x1': 60, 'y1': 300, 'add': 1, 'coin':"quarter", 'arrow': "up", 'value': round(float(0.25),2), 'coinx':20, 'image': quarter},
        {'x1': 260, 'y1': 300, 'add': 1, 'coin':"dime", 'arrow': "up", 'value': round(float(0.10),1), 'coinx':220,'image': dime},
        {'x1': 460, 'y1': 300,'add': 1,  'coin':"nickel", 'arrow': "up", 'value': round(float(0.05), 2), 'coinx':420, 'image': nickel},
        {'x1': 660, 'y1': 300,'add': 1,  'coin':"penny", 'arrow':"up", 'value': round(float(0.01),2), 'coinx':620, 'image': penny},
          #DOWN arrow
        {'x1': 60, 'y1': 510,'add': -1,  'coin':"quarter", 'arrow': "down", 'value': round(float(-0.25),2), 'coinx':20, 'image': quarter},
        {'x1': 260, 'y1': 510,'add': -1,  'coin':"dime", 'arrow': "down", 'value': round(float(-0.10),1),'coinx':220, 'image': dime},
        {'x1': 460, 'y1': 510, 'add': -1, 'coin':"nickel", 'arrow': "down", 'value': round(float(-0.05),2), 'coinx':420, 'image': nickel},
        {'x1': 660, 'y1': 510, 'add': -1, 'coin':"penny", 'arrow':"down", 'value': round(float(-0.01),2),'coinx':620, 'image': penny}
    ]

    #calling in text, images, and arrows 
    for rule in rules:
        coinvalue(rule['coin'], rule['coinx'], 420)
        coinamount(rule['coin'], rule['coinx'], 380)
        window.blit(rule['image'], (rule['coinx'], 100))
        if rule['y1'] == 300:
            uparrow(rule['coin'], rule['x1'], rule['y1'])
        elif rule['y1'] == 510:
            downarrow(rule['coin'], rule['x1'], rule['y1'])


    #button functionality + sound 
    def ifclicked(click, mouse, w=50):
        for rule in rules:
            
            if rule['x1'] + w > mouse[0] > rule['x1'] and rule['y1'] + w > mouse[1] > rule['y1']:
                if click[0] ==  1:
                    #button limits
                    if int(coin_counts[rule['coin']]) > 0:
                        coin_counts[rule['coin']] += rule['add']
                    elif int(coin_counts[rule['coin']]) <= 0 and rule['add'] >= 0:
                        coin_counts[rule['coin']] += rule['add']

                    if (coin_value[rule['coin']]) > 0 :
                        coin_value[rule['coin']] += rule['value']
                    elif (coin_value[rule['coin']]) <= 0 and rule['value'] >= 0:
                        coin_value[rule['coin']] += rule['value']
                    
                    # if coin_counts[rule['coin']] == 0:
                    #     coin_value[rule['coin']] == 0
                    #     coinvalue(rule['coin'], rule['coinx'], 420)   
                    # if coin_counts[rule['coin']] == 1:
                    #     coin_value[rule['coin']] == rule['value'] 
                    #     coinvalue(rule['coin'], rule['coinx'], 420)  

                    if rule['arrow'] == "up":
                        uparrow_sound.play()
                    elif rule['arrow']== "down":
                        downarrow_sound.play()
    ifclicked(click,mouse)


     
    #button lightens up if the mouse hovers on it
    def ifhovered(mouse, w=50):
        for rule in rules:
            if rule['x1'] + w > mouse[0] > rule['x1'] and rule['y1'] + w > mouse[1] > rule['y1']:
                if rule['arrow'] == "up":
                    uparrow2(rule["coin"], rule['x1'], rule['y1'] )
                elif rule['arrow']== "down":
                    downarrow2(rule["coin"], rule['x1'], rule['y1'] )
            else:
                if rule['arrow'] == "up":
                    uparrow(rule["coin"], rule['x1'], rule['y1'])
                elif rule['arrow'] == "down":
                    downarrow(rule["coin"], rule['x1'], rule['y1'])

    ifhovered(mouse)
    




    pygame.display.update()


pygame.quit()

