# Game window dimensions.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 770

# Total number of lanes, including grass, road, and river lanes.
NUM_OF_LANES = 11

# Height of a single lane.
LANE_HEIGHT = SCREEN_HEIGHT // NUM_OF_LANES

# Frog sprite dimensions.
FROG_SIZE = 50

# Stores lane configuration data.
# Each lane is represented by a dictionary with:
# - type: "road", "river", "grass", or "grass_win"
# - speed: movement speed of lane entities
# - y: vertical position of the lane
# - entities: list of cars, logs, or other lane objects
LANES = []

# Available car sprite color variations.
CAR_COLORS = ["red", "blue", "green", "yellow", "orange", "pink"]

# Car sprite dimensions (width, height).
CARS_SIZE = (100, 50)

# Log sprite dimensions by size category.
LOG_SIZES = {
    "short": (60, 40),
    "medium": (80, 40),
    "long": (120, 40)
}

# Starting number of player lives.
LIVES = 3

# Target frame rate.
FPS = 60
