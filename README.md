# Brick Breaker

A simple Pygame-based Brick Breaker game prototype. This project is currently in early development stage and demonstrates basic game window setup and ball movement controls.

## Description

Brick Breaker is a classic arcade game where the player moves a paddle to bounce a ball and break bricks. This implementation is a minimal prototype that currently only includes:

- A game window
- A football-themed ball that can be moved left and right using arrow keys

## Features

- Basic game window setup with Pygame
- Simple keyboard controls for ball movement
- Football-themed graphics

## Installation

### Prerequisites

- Python 3.x
- Pygame library

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/brick_breaker.git
   cd brick_breaker
   ```

2. Install the required dependencies:
   ```
   pip install pygame
   ```

## Usage

Run the game using Python:

```
python -m brick_breaker.window
```

Or navigate to the project directory and run:

```
python brick_breaker/window.py
```

## Controls

- **Left Arrow**: Move the ball left
- **Right Arrow**: Move the ball right
- **ESC**: Exit the game
- **Close Window**: Exit the game

## Project Structure

```
brick_breaker/
├── __init__.py
├── images/
│   └── football.png
└── window.py
```

## Dependencies

- [Pygame](https://www.pygame.org/) - A set of Python modules designed for writing video games

## Future Development

This is an early prototype. Future versions may include:
- Paddle implementation
- Brick layouts
- Collision detection
- Scoring system
- Multiple levels
- Sound effects

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.