#imports and initializations for turtles and canvas
import turtle as trtl
import turtle as rocket
fighter = trtl.Turtle()
counter=trtl.Turtle()
wn=trtl.Screen()
wave_num=1
fire=0 #variable used to tell if the player is currently firing
font_setup = ("Arial", 20, "normal")
interval = 1000
print("Use D to move right")
print("Use A to move left")
print("Use the space bar to fire")
print("Press P to start")
print("Press R to move on to the next wave")

counter.penup()
counter.speed(0)
counter.hideturtle()
counter.goto(0,200)
counter.pendown()
counter.pencolor("white")



def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    timer_up = True
    restart()
  else:
    counter.penup()
    counter.goto(250,150)
    counter.pendown()
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, interval) 






#ENEMY FUNCTIONS



#enemy_startingx = LIST of enemy starting x coordinates
#enemy_startingy = LIST of enemy starting y coordinates
#enemy_list = the list of turtle objects used as the enemy fighters
#xSpot = individual enemy starting x coordinates
#c = The last x coordinate put into the enemy_startingx
#height = the individal enemy starting y coordinates
#psudeo_enemy = a temporaray placeholder for turtles in the enemy_list
#enemy_image & enemy_image_alternate = two diffrent images to be used as the enemy appearance
#enemy = the turtle used to show the enemy on screen
#index = a varible used to show the index of the enemy currently being dealt with


#establishes x and y coordinates for each enemy within a list
def enemy_organizer(rows,columns,spacing):
  global enemy_startingx
  global enemy_startingy
  global enemy_list
  global enemy_count
  enemy_count=rows*columns
  for i in range(rows):#adds starting x coordinates to a list for enemies
    xSpot=-(columns*spacing)/2
    if columns%2==0:
      xSpot=xSpot+(spacing/2)
    c=-xSpot
    while xSpot<=c:
      enemy_startingx.append(xSpot)
      xSpot=xSpot+spacing
  height=10
  for i in range(rows):#adds start y coordinates to a list for the enemy
    for i in range(columns):
      enemy_startingy.append(height)
    height=height+spacing
  for i in range(1,rows*columns+1):# creates a list of enemies
    i=str(i)
    pseudo_enemy='e'+i
    enemy_list.append(pseudo_enemy)



#intializes and orients enemies to start position
def init_enemy():
  global enemy_startingx
  global enemy_startingy
  global enemy_list
  enemy_image = "alien1.gif"#Image from Galaga from Namco
  wn.addshape(enemy_image)
  enemy_image_alternate='alien2.gif'#Image from Galaga from Namco
  wn.addshape(enemy_image_alternate)
  enemy_num=0
  for enemy in enemy_list:
    enemy_num=enemy_num+1
    enemy_str=enemy
    enemy=trtl.Turtle()
    enemy.shape(enemy_image)
    if enemy_num>=21:
      enemy.shape(enemy_image_alternate)
    wn.update()
    enemy.penup()
    enemy.speed(0)
    index=enemy_list.index(enemy_str)
    enemy_list.pop(index)
    enemy_list.insert(index,enemy)
    enemy.goto(enemy_startingx[index],enemy_startingy[index])




#FIGHTER FUNCTIONS

#fighter = the turtle for the player controled fighter
#startX & startY = the starting x,y coordinates for the player controled figher
#fighter_image = the appearance of the player controled fighter
# x & y = the new x,y coordinates of the fighter after the move

#initializes and orients fighters to start position
def init_fighter():
  global fighter
  global wn
  wn.setup(width=1.0, height=1.0)
  fighter.penup()
  fighter.setheading(90)
  startX = 0
  startY = -100
  fighter.goto(startX,startY)


  fighter_image="mediumship.gif"#Image from Galaga from Namco
  wn.addshape(fighter_image)
  fighter.shape(fighter_image)
  wn.update()


#moves ship right
def east():
  global x
  global y
  x=fighter.xcor()+10
  if x>300:
    x=x-10
  y=fighter.ycor()
  fighter.goto(x,y)
  if fire==0:
    rocket.goto(x,y)

#moves ship left
def west():
  global x
  global y
  x=fighter.xcor()-10
  if x<-300:
    x=x+10
  y=fighter.ycor()
  fighter.goto(x,y)
  if fire==0:
    rocket.goto(x,y)





#ROCKET FUNCTIONS


#hit_count = a varible to count how many enemy ships have been taken
#fire = a varible to tell wether or not the fighter is currently firing as to not fire twice
#hit = a boolean value to tell if the rocket has hit a target
#xcor & ycor = the rocket's current x,y coordinates to see if it has hit an enemy




#initializes the firing rocket sprite
def init_fire():
  global hit_count
  hit_count=0
  global fire
  fire=0
  rocket.setheading(90)
  rocket.penup()
  rocket.hideturtle()
  rocket_image='rocket.gif'#Image from Galaga from Namco
  wn.addshape(rocket_image)
  rocket.shape(rocket_image)
  wn.update()



#controls for firing the rocket
def firing():
  global x
  global y
  global fire_speed
  global fire
  if fire==0:
    fire=1
    rocket.penup()
    x=fighter.xcor()
    y=fighter.ycor()
    rocket.goto(x,y)
    rocket.showturtle()
    dist=(200-y)/5
    move_fire(int(dist))
    rocket.hideturtle()
    rocket.speed(0)
    fire=0

#moves rocket once fired
def move_fire(rocket_dist):
  global fire
  global hit
  hit=False
  rocket.speed(0)
  for i in range(rocket_dist):
    if hit==False:
      rocket.forward(5)
      hit_test(rocket.xcor(),rocket.ycor())
    else:
      break


#determines collision with enemy
def hit_test(xcor, ycor):
  global hit
  global hit_count
  for enemy in enemy_list:
    if abs(xcor-enemy.xcor())<=7:
      if abs(ycor-enemy.ycor())<=7:
        hit_count=hit_count+1
        hit=True
        explosion_image="explosion.gif"
        wn.addshape(explosion_image)
        enemy.shape(explosion_image)
        wn.update()
        enemy.hideturtle()
        enemy.goto(enemy.xcor(),-1000)
        rocket.hideturtle()
        rocket.goto(fighter.xcor(),fighter.ycor())
        if hit_count==enemy_count:
          print("Congrats, you have won this battle.")







def reset():
  global timer
  timer=0




#restarts game
def restart():
  global explosion_image
  global wave_num
  global enemy_count
  if hit_count != enemy_count:
    print("You have lost this battle")
    print("Game over")
    explosion_image="explosion.gif"
    wn.addshape(explosion_image)
    fighter.shape(explosion_image)
    wn.update()
    counter.clear()
    counter.penup()
    counter.goto(-75,200)
    counter.pendown()
    counter.pencolor("red")
    counter.write("Game Over",font=font_setup)
    rocket.hideturtle()
    rocket.goto(0, -1000)
    fighter.hideturtle()
    fighter.goto(0,-1000)
  if hit_count == enemy_count:
    wave_num=wave_num+1
    if wave_num<=3:
      print("More enemies incoming...")
    for enemy in enemy_list:
      enemy.speed(0)
      enemy.hideturtle()
      enemy.goto(enemy.xcor(),-1000)
    init_game(wave_num)




#starts the game considering the number wave/round
def start():
  init_game(1)


#intializes all elements of game (enemies, fighter, rocket)
def init_game(round):
  global timer
  global timer_up
  if round==4:
    counter.clear()
    counter.penup()
    counter.goto(-300,150)
    counter.pendown()
    counter.write("CONGRATS YOU HAVE WON THE WAR",font=font_setup)
    input()
  timer_up = False
  global enemy_startingx
  global enemy_startingy
  global enemy_list
  wn.bgcolor('black')
  enemy_startingx=[]
  enemy_startingy=[]
  enemy_list=[]
  if round==1:
    timer=30
    enemy_organizer(2,10,50)
  if round==2:
    timer=30
    enemy_organizer(3,10,50)
  if round==3:
    timer=35
    enemy_organizer(4,10,50)
  init_fighter()
  init_enemy()
  init_fire()
  wn.ontimer(countdown, interval) 


#input key presses for left, right, and fire
wn.onkeypress(east,'d')#move right
wn.onkeypress(west,'a')#move left
wn.onkeypress(firing,'space')#FIRE!
wn.onkeypress(start,'p')
wn.onkeypress(reset,'r')
wn.listen()#listen for key presses

wn.mainloop()#continue turtle screen