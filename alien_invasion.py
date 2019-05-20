import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	# Initialize game and create a screen object.
	pygame.init()
	# screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Alien Invasion")

	# bg_color = (230, 230, 230)
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_heigh))
	# Make a ship
	ship = Ship(ai_setting, screen)
	# Start the main loop for the game.

	while True:
		# Watch for keyboard and mouse events.
		gf.check_events(ship)
		ship.update()

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		# screen.fill(ai_setting.bg_color)
		# ship.blitme()

		# Make the most recently drawn screen visible.
		# pygame.display.flip()
		gf.update_screen(ai_setting, screen, ship)


run_game()
