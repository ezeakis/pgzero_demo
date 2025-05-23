import random
import sys

from library.spaceship import Spaceship, default_update
from library.projectile import Projectile
from library.pilot import Pilot, Player1, Player2
from library.utils import Team, world
from library.weapon import Weapon
from library.globals import IMAGES_SPACESHIPS, NUMBER_OF_PLAYERS, NUMBER_OF_ENEMIES

# This is the laboratory where you can create your own custom 
# abilities, weapons and spaceships 

######################################
######### ABILITIES LAB ##############
######################################

def super_speed(spaceship : Spaceship):
    ''' Super speed!!! '''
    spaceship.speed = 13

def invisibility(spaceship : Spaceship):
    '''Invisibility!!!'''
    spaceship.collidable = False

def too_many_guns(spaceship : Spaceship):
    '''Quad fire!!!'''
    spaceship.weapon.barrels = 4

def machine_gun(spaceship: Spaceship):
    '''Fire barraze!!!'''
    spaceship.weapon.firerate = spaceship.weapon.firerate + 5

def reflection(spaceship: Spaceship):
    '''Reflector deployed!!!'''
    spaceship.deploy_reflector()

def buff_up(spaceship: Spaceship):
    '''Damage bonus!!!'''
    spaceship.weapon.damage = spaceship.weapon.damage + 2/spaceship.weapon.barrels

def hypervelocity(spaceship: Spaceship):
    '''Bullets super speed!!!'''
    spaceship.weapon.speed = 20

def fanfire(spaceship: Spaceship):
    '''Mines deployed!!!'''
    n = 10
    spread = 100
    for i in range(0,n+1):
        Projectile(image = 'others/bomb', pos = spaceship.pos, speed=2, damage = 12, health = 12, source=spaceship, team=spaceship.team, direction= -spread/2 + (i*spread/n) )

abilities = [
    super_speed,
    invisibility,
    too_many_guns,
    machine_gun,
    reflection,
    buff_up,
    hypervelocity,
    fanfire
    ]

######################################
############ WEAPON LAB ##############
######################################

# weapon points = (damage * barrels * firerate) + speed
cannon      = Weapon(firerate = 2, barrels = 1, damage = 8, speed = 6)  # 22
super_auto  = Weapon(firerate = 8, barrels = 1, damage = 1.5, speed = 13) # 25
automatic   = Weapon(firerate = 4, barrels = 1, damage = 4, speed = 12) # 28
dual        = Weapon(firerate = 2, barrels = 2, damage = 3, speed = 9)  # 21
dual_plasma = Weapon(firerate = 1, barrels = 2, damage = 5, speed = 8)  # 18

gatling_gun = Weapon(firerate = 12, barrels = 1, damage = 1, speed = 18, randomness=3 )
trident     = Weapon(firerate = 2, barrels = 3, damage = 2, speed = 9,  spread_angle=45)
shotgun     = Weapon(firerate = 1, barrels = 4, damage = 4, speed = 25, spread_angle=5, randomness=2 )

#Weapon for fun
malfunction = Weapon(firerate = 12, barrels = 1, damage = 5, speed = 18, randomness=45 )
default = Weapon(firerate = 1, barrels = 1, damage = 1, speed = 6)

weapons = [
    cannon,
    super_auto,
    automatic,
    dual,
    dual_plasma,
    gatling_gun,
    trident,
    shotgun
]

######################################
######### CHARACTERS LAB #############
######################################

############# ENEMIES ################

pilots = []  
for e in range(0, NUMBER_OF_ENEMIES):
    pilot = Pilot("Enemy")
    pilot.take_control( Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
                                  health = 50, 
                                  speed = 4, 
                                  ability_function = random.choice(abilities),
                                  ability_duration = 6, 
                                  cooldown_duration = 6, 
                                  weapon = random.choice(weapons), 
                                  team=Team.ENEMY) )
    pilots.append( pilot )

############# FRIENDS ################
# friends = []
# f_agents = []  
# for f in range(0,2):
#     friends.append( Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
#                                                 health = 200, 
#                                                 speed = 4, 
#                                                 ability_function = random.choice(abilities), 
#                                                 ability_duration = 6, 
#                                                 cooldown_duration = 8, 
#                                                 weapon = random.choice(weapons), 
#                                                 team=Team.PLAYER) )

  
# for f_spaceship_b in friends_blueprints:
#     f_agent = Pilot("Enemy")
#     f_spaceship = Spaceship( f_spaceship_b )
#     f_agent.take_control( f_spaceship )
#     f_agents.append( f_agent )

############# PLAYERS ################

player2 = None
world.player2 = None
if NUMBER_OF_PLAYERS == 2:
    player2spaceship = Spaceship(image = random.choice(IMAGES_SPACESHIPS), 
                        health = 500, 
                        speed = random.choice([7,8,9]), 
                        ability_function = random.choice(abilities),
                        ability_duration = 10, 
                        cooldown_duration = 2,
                        update_function = default_update, 
                        weapon = random.choice(weapons),
                        team = Team.PLAYER)

    player2 = Player2("Player2")
    world.player2 = player2spaceship
    player2.take_control( world.player2 )