import pygame
import random
from config import LANES, SCREEN_WIDTH, SCREEN_HEIGHT, LANE_HEIGHT, CARS_SIZE, LOG_SIZES
from frog import frog_dict, frog_img
from cars import cars_dict
from wood_logs import logs_dict
import sys

# Screen parameters.
GAME_WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("frogger")

# Load and scale the background image to fit the game window.
background_img = pygame.image.load("images/background.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Generates the road section of the game.
# Creates 4 lanes with moving cars.
# - Even-indexed lanes move to the right
# - Odd-indexed lanes move to the left
# Each lane contains 3 cars with randomized spacing, speed, and sprite selection.
def add_road_lanes():

    vitesse = [2, 3, 4]
    direction_voiture = None
    vitesse_voiture = None

    for route in range(2, 6):

        y = SCREEN_HEIGHT - LANE_HEIGHT * route
        if route % 2 == 0:
            direction_voiture = "right"
            vitesse_voiture = random.choice(vitesse)
        else:
            direction_voiture = "left"
            vitesse_voiture = random.choice(vitesse) * -1
        cars = []

        for i in range(1, 4):
            car = {
                "width": CARS_SIZE[0],
                "height": CARS_SIZE[1],
                "x": i * 250 + random.randint(10, 100),
                "y": y + LANE_HEIGHT/2 - CARS_SIZE[1]/2,
                "image": random.choice(cars_dict[f"{direction_voiture}"])
                }
            cars.append(car)

        LANES.append({
            "type": "road",
            "speed": vitesse_voiture,
            "y": y,
            "entities": cars,
        })

    return

# Adds a neutral grass lane between road and river sections.
def add_grass_lane():
    grass_y = SCREEN_HEIGHT - (6 * LANE_HEIGHT)
    LANES.append({"type": "grass", "speed": 0, "y": grass_y, "entities": []})

# Generates the river section with moving logs.
# Creates 4 lanes with:
# - Randomized log sizes
# - Random horizontal spacing
# - Alternating left/right movement directions
def add_river_lanes():

    vitesse = [2, 3, 4]

    for river in range(7, 11):
        y = SCREEN_HEIGHT - river * LANE_HEIGHT
        if river % 2 == 0:
            vitesse_alea = random.choice(vitesse)
        else:
            vitesse_alea = random.choice(vitesse) * -1

        logs = []
        for j in range(1, 4):
            r = random.choice(list(logs_dict.keys()))
            log = {
                "width": LOG_SIZES[r][0],
                "height": LOG_SIZES[r][1],
                "x": j * 250 + random.randint(10, 100),
                "y": y + LANE_HEIGHT/2 - LOG_SIZES[r][1]/2,
                "image": logs_dict[r]
                }
        
            logs.append(log)

        LANES.append({
            "type": "river",
            "speed": vitesse_alea,
            "y": y,
            "entities": logs
    })
    return

# Final goal lane where the player wins the game.
def add_final_grass_lane():
    final_grass_y = SCREEN_HEIGHT - (11 * LANE_HEIGHT)
    LANES.append({"type": "grass_win", "speed": 0, "y": final_grass_y, "entities": []})

# Renders all game elements to the screen:
# - Background
# - Vehicles and logs
# - Frog character
# - UI (lives counter)
def draw_window():
    GAME_WINDOW.blit(background_img, (0, 0))
    
    for lane in LANES:
        for ent in lane["entities"]:
            GAME_WINDOW.blit(ent["image"], (ent["x"], ent["y"]))

    GAME_WINDOW.blit(frog_img, (frog_dict["x"], frog_dict["y"]))

    font = pygame.font.SysFont(None, 36)
    lives_text = font.render(f"Lives: {frog_dict['lives']}", True, (255, 255, 255))
    GAME_WINDOW.blit(lives_text, (10, 10))

    pygame.display.update()

# Displays win screen overlay.
def show_win_message():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 72)
    text = font.render("You Win!", True, (255, 255, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
    GAME_WINDOW.blit(text, text_rect)

    pygame.display.update()
    
# Displays game over screen overlay.
def show_game_over_message():
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    GAME_WINDOW.blit(overlay, (0, 0))

    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    GAME_WINDOW.blit(text, text_rect)

    pygame.display.update()
