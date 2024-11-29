import pgzrun
import random
WIDTH=500
HEIGHT=480
TITLE='COIN COLLECTION GAME'



bg=Actor('grass',(WIDTH/2,HEIGHT/2))
robot=Actor('robot_idle')
coin=Actor('coin_gold')
bomb=Actor('bomb')
velocity=5
over=False
timer=0

def start():
  global  velocity,over,timer

def draw():
    screen.clear()
    bg.draw()
    robot.draw()
    coin.draw()
    bomb.draw()









pgzrun.go()
