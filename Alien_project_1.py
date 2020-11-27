import pygame
import game_functions as gf
from settings import Settings
from ship_class import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	bg_color = (180, 100, 145)
	
	#Make the Play Button
	play_button = Button(ai_settings, screen, "Wanna Play?")
	
	#Make a ship
	ship = Ship(ai_settings, screen)
	
	#Make a group to store bullets in
	bullets = Group()
	
	#Make an alien
	alien = Alien(ai_settings, screen)
	aliens = Group()
	
	#Creat the fleet of aliens 
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Create an instance to store game statistics and creta a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#Start the main loop for game
	while True:
		#Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, stats, ship, sb, aliens, bullets, play_button)
		
		if stats.game_active:
			ship.update()
			bullets.update()
			gf.update_bullets(ai_settings, screen, stats, ship, sb, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, sb, aliens, bullets)
			
		gf.update_screen(ai_settings, screen, stats, ship, sb, aliens, bullets, play_button)	
run_game()


		
