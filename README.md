# Homeostasis Robot Simulation

A Webots simulation project where an E-puck robot autonomously maintains homeostasis by seeking food and water sources while avoiding obstacles in a simulated environment.

## Overview

This project simulates a robot operating and surviving in a homeostasis environment for 10 minutes using Webots simulation software. The E-puck robot maintains stability by autonomously navigating to food and water sources while adapting its motion and avoiding obstacles.

## Features

- **Homeostasis Maintenance**: Robot autonomously seeks food and water to maintain stability
- **Obstacle Avoidance**: Real-time collision detection and avoidance using proximity sensors
- **Adaptive Motion**: Dynamic acceleration and deceleration based on environmental conditions
- **Visual Feedback**: LED indicators for interaction and status display
- **10-Minute Survival**: Successfully operates for the designated timeframe

## Hardware & Sensors

- **Robot**: E-puck
- **Distance Sensors**: Proximity sensors and ground sensors
- **Visual Sensor**: Camera
- **Indicators**: LEDs for environmental interaction

## Requirements

- Webots simulation software
- Python (or specify your language)

## Installation & Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Homeostasis-Robot-Simulation.git
cd Homeostasis-Robot-Simulation
```

2. Open Webots and load the world file

3. Run the simulation

## Project Structure
```
├── controllers/        # Robot controller code
├── worlds/            # Webots world files
├── arena/             # Arena images (food/water sources)
└── README.md
//


## License

[Choose: MIT, GPL, or Academic Use Only]
