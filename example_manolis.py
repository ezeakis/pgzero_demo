import game
from library.spaceship import Spaceship
from library.weapon import Weapon
from library.globals import Team

def ability(spaceship):
    '''Ability activated!'''
    spaceship.weapon.firerate = 12

def enemy_ability(spaceship):
    '''Ability activated!'''
    spaceship.weapon.damage = spaceship.weapon.damage + 4

weapon = Weapon( firerate = 2, 
                 barrels = 1, 
                 damage = 3, 
                 speed = 6)

enemy_weapon = Weapon(firerate = 12, 
                      barrels = 1, 
                      damage = 1, 
                      speed = 18, 
                      randomness=3 )

spaceship = Spaceship( image = 'spaceships/spaceship_orange1', 
                       health = 100, 
                       speed = 7, 
                       ability_function = ability, 
                       ability_duration = 6, 
                       cooldown_duration = 2,
                       weapon = weapon,
                       team = Team.PLAYER )

enemy = Spaceship(image = 'spaceships/spaceship_black1', 
                  health =50, 
                  speed = 4, 
                  ability_function = enemy_ability,
                  ability_duration = 6, 
                  cooldown_duration = 6, 
                  weapon = enemy_weapon, 
                  team=Team.ENEMY)

game.play()