# 🐸 Frogger — Python Remake
 
A Python remake of the classic 1981 arcade game [Frogger](https://en.wikipedia.org/wiki/Frogger), built with [Pygame](https://www.pygame.org/). Guide your frog across a busy road and a river to reach safety — without getting hit or falling in the water!
 
---

## Gameplay

A gameplay recording is available in the `images/` folder (`gameplay.mp4`).
 
- **Move** the frog using the arrow keys (←↑→↓)
- **Avoid cars** on the road — getting hit costs a life
- **Jump on logs** to cross the river — falling in the water costs a life
- **Reach the top** to win the game
- You start with **3 lives**
---

## Features
 
- Frog controlled by keyboard input
- Cars and logs moving at randomized speeds
- Collision detection with cars (lose a life) and logs (ride along)
- Win and game-over screens
- Sprite-based graphics for the frog, cars, and logs
---

## Project Structure
 
```
frogger/
├── images/          # Sprites for frog, cars, and logs
├── frog.py          # Frog initialization and properties
├── cars.py          # Car sprites and dictionary
├── wood_logs.py     # Log sprites and dictionary
├── config.py        # Game constants (screen size, speeds, etc.)
├── window.py        # Lane and entity setup
├── game.py          # Game logic (input, collisions, log detection)
└── main.py          # Entry point — run this to play
```
 
---

## Getting Started
 
### Prerequisites

- Python 3.x
- [Conda](https://docs.conda.io/) (recommended) or pip

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/angz09/frogger.git
   cd frogger
```

2. Activate your environment and install Pygame:
```bash
   pip install pygame==2.6.0
```

3. Run the game:
```bash
   python main.py
```
 
---

## Built With
 
- [Python 3](https://www.python.org/)
- [Pygame 2.6.0](https://www.pygame.org/)
