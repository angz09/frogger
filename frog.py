import pygame
from config import FROG_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, LANE_HEIGHT, LIVES 

# Load and scale the frog sprite.
frog_img = pygame.image.load("images/frog.png")
frog_img = pygame.transform.scale(frog_img, (FROG_SIZE, FROG_SIZE))

# Stores the frog's current state, position, movement settings,
# and gameplay-related attributes.
# The frog starts centered in the bottom grass lane.
frog_dict = {
    "x": SCREEN_WIDTH/2 - FROG_SIZE/2,
    "y": 10 * LANE_HEIGHT - FROG_SIZE/2,
    "size": FROG_SIZE,
    "speed": LANE_HEIGHT,
    "on_log": False,      # True when the frog is standing on a moving log.
    "log_speed": 0,       # Current speed inherited from the log.
    "in_water": False,    # True when the frog is in a river lane.
    "water_timer": 0,     # Time spent in water without a log.
    "has_won": False,     # True when the frog reaches the goal area.
    "lives": LIVES        # Remaining player lives.
}
