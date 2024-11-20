# Wumpus World Simulation and Real-World Car Navigation

This repository showcases a unique blend of **AI-based decision-making** and **real-world robotic navigation**. It combines logical reasoning, knowledge-based systems, and physical car control, leveraging both simulation and hardware capabilities.

## Features

### 1. **AI-Powered Wumpus World Gameplay**  
   - **Knowledge-Based Reasoning**: The AI uses a Knowledge Base (KB) and First-Order Logic to infer the safest path through the Wumpus World grid.  
   - **Automated Decision-Making**: The agent autonomously avoids pits and the Wumpus using logical rules and a model-checking system.  
   - **Dynamic World Interaction**: The game state evolves based on the agent's perceptions (stench, breeze, glitter, etc.).

### 2. **Manual Gameplay with Pygame**  
   - Offers an interactive manual mode where players can navigate the Wumpus World using a graphical interface.

### 3. **Raspberry Pi-Based Real-World Navigation**  
   - **Robotic Car Control**: Using Raspberry Pi, the project controls a physical car that navigates based on color detection.  
   - **Color Recognition via Camera**: Detects and responds to colors in real-time for obstacle avoidance and path following.

### 4. **Developer-Friendly Design**  
   - **Object-Oriented Programming (OOP)**: The project utilizes OOP principles for modularity and maintainability.  
   - **Extensible Logic Framework**: Core components like the `logic.py` file provide reusable First-Order Logic functions (`AND`, `OR`, `NOT`).  
   - **Scalable Grid System**: Wumpus World mechanics and agent logic are designed to adapt easily to larger or more complex grids.

---

## Project Structure

|-- resources/ # Assets for Pygame (images, sprites, etc.) |-- media/ # Demonstration videos and screenshots |-- pycache/ # Auto-generated cache (ignored in version control) |-- agent.py # Agent movement and decision-making |-- car_control.py # Car control for Raspberry Pi |-- Detect_color.py # Color detection system for Raspberry Pi |-- final_game.py # AI-driven Wumpus World gameplay |-- logic.py # First-Order Logic implementation (AND, OR, NOT) |-- pygame_play.py # Manual Wumpus World gameplay using Pygame |-- run.py # Entry point for AI Wumpus World game |-- wumpus_world.py # Wumpus World mechanics, rules, and grid system


---

## How to Run

### 1. **Wumpus World AI Game**
  Run the AI-based Wumpus World simulation:
    ```bash
    python run.py

### 2. **Manual Gameplay (Pygame)**
  For an interactive experience:
    ```bash
    python pygame_play.py
    Navigate using the arrow keys.

### 3. **Raspberry Pi Car Navigation**
These scripts are designed to control a physical car using a Raspberry Pi setup. They enable real-time navigation based on color detection:

- **`car_control.py`**: Handles motor control and movement logic for the robotic car.
- **`Detect_color.py`**: Uses a connected camera to detect specific colors in the environment and guides the car accordingly.

> **Note**: If running on a system without Raspberry Pi, you can simulate color detection by manually inputting color names (e.g., "red", "blue") when prompted.

#### Steps to Run on Raspberry Pi:
1. **Ensure Raspberry Pi setup with camera and motor drivers is complete.**
2. **Run the color detection and control script:**
   ```bash
   python Detect_color.py
3. **Watch the car navigate in response to the detected colors.**

## Key AI Concepts

- **Knowledge Base (KB)**:  
  The AI maintains a dynamic Knowledge Base to store facts about the environment (e.g., "Pit at (1,2)" or "No Wumpus at (2,3)").

- **First-Order Logic**:  
  Implements logical operations like `AND`, `OR`, and `NOT` to deduce new facts and make informed decisions.

- **Model Checking**:  
  The agent uses model-checking techniques to evaluate potential moves and determine safe paths.

- **Percept Integration**:  
  The AI interprets percepts (e.g., stench, breeze) to update its Knowledge Base and adjust its strategy dynamically.

---

