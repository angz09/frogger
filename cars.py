import pygame
from config import CAR_COLORS, CARS_SIZE

# Dictionary containing car sprites for different colors and directions.
cars_dict = {
    "left": [],
    "right": []
}

# Load and scale all car sprites for both directions.
# Images are grouped by direction ("left" and "right") in cars_dict
# to allow random selection and efficient access during gameplay.

for color in CAR_COLORS:
    image_left = pygame.image.load(f"images/car_{color}_left.png")
    image_right = pygame.image.load(f"images/car_{color}_right.png")

    scale_left = pygame.transform.scale(image_left, CARS_SIZE)
    scale_right = pygame.transform.scale(image_right, CARS_SIZE)

    cars_dict["left"].append(scale_left)
    cars_dict["right"].append(scale_right)
