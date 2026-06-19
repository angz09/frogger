import pygame
import sys
from config import FPS, LANE_HEIGHT, LANES, LIVES
from window import add_road_lanes, add_grass_lane, add_river_lanes, add_final_grass_lane, draw_window, show_win_message, show_game_over_message
from game import move_entities, handle_input, check_collision, handle_logs, check_win, reset_frog, wait_for_enter
from frog import frog_dict

# Initialise Pygame
pygame.init()

add_road_lanes()
add_grass_lane()
add_river_lanes()
add_final_grass_lane()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            handle_input(event)

        move_entities()
        handle_logs()

        if frog_dict["on_log"]:
            frog_dict["x"] += frog_dict["log_speed"]

        current_time = pygame.time.get_ticks()

        in_log_lane = any(
            lane["type"] == "river" and
            frog_dict["y"] + frog_dict["size"] > lane["y"] and
            frog_dict["y"] < lane["y"] + LANE_HEIGHT
            for lane in LANES
        )

        if in_log_lane and not frog_dict["on_log"] and not frog_dict["in_water"]:
            frog_dict["in_water"] = True
            frog_dict["water_timer"] = current_time

        if frog_dict["in_water"]:
            if current_time - frog_dict["water_timer"] >= 300:
                print("Frogger fell into the water! : –1 life!")
                reset_frog(decrease_life=True)

        if check_collision():
            print("Frogger hit a car! : –1 life!")
            reset_frog(decrease_life=True)

        if check_win() and not frog_dict.get("has_won", False):
            frog_dict["has_won"] = True
            draw_window()
            pygame.display.update()
            show_win_message()
            wait_for_enter()
            frog_dict["lives"] = LIVES
            reset_frog(decrease_life=False)

        if frog_dict["lives"] <= 0:
            show_game_over_message()
            wait_for_enter()
            frog_dict["lives"] = LIVES
            reset_frog(decrease_life=False)

        draw_window()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()