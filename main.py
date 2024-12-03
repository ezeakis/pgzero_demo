import pgzrun
from pgzero.keyboard import keyboard
import random
import sys
from laboratory import player, enemy, agent
from classes.asteroid import generate_random_asteroid
from classes.powerups import generate_random_powerup
from gui import enemybar, healthbar, abilitybar, cooldownbar 
from utils import CollisionInformation
from globals import WIDTH, HEIGHT, FPS, ASTEROIDS_PER_SECOND, POWERUPS_PER_SECOND, OBJECTS_LIMIT, WIN_GRAPHIC, LOSE_GRAPHIC
from utils import background, world
 
def update_enviroment():

    if random.random() < (ASTEROIDS_PER_SECOND/FPS):
        generate_random_asteroid()

    if random.random() < (POWERUPS_PER_SECOND/FPS):
        generate_random_powerup()

def update_objects():

    world.objects = world.objects[:OBJECTS_LIMIT]
    for obj in world.objects:
        
        if obj.collidable:
            collided_objects = [o for o in world.objects if o.team != obj.team and o.collidable and obj.colliderect(o)] #Exclude same team objects (self is same team) and objects with no collision
            for collided_object in collided_objects:  
                obj.collide( CollisionInformation(collided_object) )

    for obj in world.objects:
        obj.update() 

    for obj in world.objects:
        if obj.alive == False:
            if obj == player and world.end_game == 0:
                #LOSS
                world.end_game = -1
            elif obj == enemy and world.end_game == 0:
                #VICTORY
                world.end_game = 1
            world.remove_object(obj)
            del obj

def update_gui():

    enemybar.update(enemy.health, enemy.max_health)
    healthbar.update(player.health, player.max_health)
    if player._ability_timer_frames > 0:
        abilitybar.update(player._ability_timer_frames, player.ability_duration*FPS)
    if player._cooldown_timer_frames > 0:
        cooldownbar.update(player._cooldown_timer_frames, player._cooldown_frames)

def update_effects():

    for e in world.effects:
        e.update()

def draw_enviroment():

    background.draw()

def draw_objects():

    for obj in world.objects:
        obj.draw()

def draw_gui():

    enemybar.draw()
    healthbar.draw()
    cooldownbar.draw()
    if player._ability_timer_frames > 0:
        abilitybar.draw()

def draw_effects():

    for e in world.effects:
        e.draw()

##### GAME LOOP #####
def update():

    if keyboard.escape:
        sys.exit(0)

    agent.think([player])

    update_enviroment()
    update_objects()
    update_gui()
    update_effects()

##### DRAW LOOP #####
def draw():

    draw_enviroment()
    draw_objects()
    draw_gui()
    draw_effects()

    if world.end_game == 1:
        WIN_GRAPHIC.draw()
    elif world.end_game == -1:
        LOSE_GRAPHIC.draw()
    
pgzrun.go()