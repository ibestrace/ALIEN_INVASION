import sys

import pygame

# Refactoring check_events()
def check_keydown_events(event, ship):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

def check_keyup_events(event, ship):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			# if event.key == pygame.K_RIGHT:
			# 	ship.moving_right = True
			# elif event.key == pygame.K_LEFT:
			# 	ship.moving_left = True
			check_keydown_events(event, ship)

		elif event.type == pygame.KEYUP:
			# if event.key == pygame.K_RIGHT:
			# 	ship.moving_right = False
			# elif event.key == pygame.K_LEFT:
			# 	ship.moving_left = False
			check_keyup_events(event, ship)

def update_screen(ai_setting, screen, ship):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_setting.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()
