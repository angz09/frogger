from config import LANES, SCREEN_HEIGHT, SCREEN_WIDTH, FROG_SIZE, LIVES 
from window import GAME_WINDOW
from frog import frog_dict
import pygame
import sys

# Updates the position of all moving entities (cars and logs).
# Entities that leave one side of the screen are wrapped to the opposite side.
def move_entities():
    for lane in LANES:
        for ent in lane["entities"]:
            ent["x"] += lane["speed"]
            if lane["speed"] > 0 and ent["x"] > SCREEN_WIDTH:
                ent["x"] = -200
            elif lane["speed"] < 0 and ent["x"] < -200:
                ent["x"] = SCREEN_WIDTH + 100

# Handles player movement using the arrow keys.
# Movement is constrained to the game window boundaries.
def handle_input(event): 
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            frog_dict["x"] = max(0, frog_dict["x"] - frog_dict["speed"])
        if event.key == pygame.K_RIGHT:
            frog_dict["x"] = min(SCREEN_WIDTH - FROG_SIZE, frog_dict["x"] + frog_dict["speed"])
        if event.key == pygame.K_UP:
            frog_dict["y"] = max(0, frog_dict["y"] - frog_dict["speed"])
        if event.key == pygame.K_DOWN:
            frog_dict["y"] = min(SCREEN_HEIGHT - FROG_SIZE, frog_dict["y"] + frog_dict["speed"])
    return

# Detects collisions between the frog and vehicles.
# Returns True when a collision occurs, otherwise False.
def check_collision():

    frog = pygame.Rect(frog_dict["x"], frog_dict["y"], FROG_SIZE, FROG_SIZE)

    for voie in LANES:
        if voie["type"] == "road":
            for c in voie["entities"]:
                car_rect = pygame.Rect(c["x"], c["y"], c["width"], c["height"])

                if frog.colliderect(car_rect):
                    return True

    return False


# Updates the frog's interaction with river logs.
# If the frog is standing on a log, it inherits the log's movement speed.
# Otherwise, log-related movement is disabled.
def handle_logs():

    frog_dict["on_log"] = False
    frog_dict["log_speed"] = 0


    frog = pygame.Rect(frog_dict["x"], frog_dict["y"], FROG_SIZE - 1, FROG_SIZE - 1)

    for l in LANES:
        if l["type"] == "river":
            for b in l["entities"]:
                buche_rect = pygame.Rect(b["x"], b["y"], b["width"], b["height"])

                if frog.colliderect(buche_rect):
                    frog_dict["on_log"] = True
                    frog_dict["log_speed"] = l["speed"]
    return

# Checks whether the frog has reached the goal lane.
# Returns True if the win condition is met.
def check_win():
    for lane in LANES:
        if lane["type"] == "grass_win":
            if abs(lane["y"] - frog_dict["y"]) < 12:
                return True
    return False

# Resets the frog to its starting position.
def reset_frog(decrease_life=True):
    if decrease_life:
        frog_dict["lives"] -= 1
    frog_dict["x"] = SCREEN_WIDTH // 2 - FROG_SIZE // 2
    frog_dict["y"] = SCREEN_HEIGHT - FROG_SIZE - 10
    frog_dict["in_water"] = False
    frog_dict["water_timer"] = 0
    frog_dict["on_log"] = False
    frog_dict["log_speed"] = 0
    frog_dict["has_won"] = False

# Displays the game-over restart prompt and waits for
# the player to press Enter before restarting the game.
def wait_for_enter():
    font_small = pygame.font.SysFont(None, 36)
    prompt_text = font_small.render("Press ENTER to play again", True, (255, 255, 255))
    prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    waiting = False
                    reset_frog(decrease_life=False)  # Reset the frog's starting position.
                    frog_dict["lives"] = LIVES # Restore the starting number of lives.

        # Redraw the restart message every frame.
        GAME_WINDOW.blit(prompt_text, prompt_rect)
        pygame.display.update()
