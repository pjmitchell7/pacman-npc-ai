# Pac-Man NPC AI Enhancement Project

This project explores the use of adaptive and deterministic algorithms to enhance non-playable character (NPC) intelligence in a modified version of Pac-Man. The goal is to compare classic pathfinding (A*) with reinforcement learning (Q-Learning) for ghost behavior, with a focus on difficulty, adaptability, and immersion.

## Objectives

* Modify an open-source Pac-Man game to test different ghost AI behaviors.
* Implement and evaluate A* pathfinding for predictable, optimal pursuit.
* Implement and train a Q-Learning ghost to adaptively chase Pac-Man.
* Evaluate both agents on multiple metrics including capture rate, path efficiency, and adaptability.
* Visualize algorithm behavior and performance.
* Prepare a clear presentation of the methodology, results, and implications.

## Project Structure

```
pacman-npc-ai/
├── pacman/               # Berkeley Pac-Man AI codebase
├── ghostAgents.py        # Custom ghost agents
├── results/              # Logs, metrics, Q-tables, plots
├── media/                # GIFs, videos, screen recordings
├── slides/               # Final presentation deck
├── notebooks/            # Optional experiments
├── venv/                 # Python virtual environment
├── .gitignore            # Ignoring venv and cache
├── README.md             # Project overview and planning
```

## Environment Setup

### 1. Clone Project and Repository

Navigate to your preferred working directory:

```bash
cd ~/Documents  # Or another project location
```

Clone your GitHub repository:

```bash
git clone https://github.com/pjmitchell7/pacman-npc-ai.git
cd pacman-npc-ai
```

### 2. Clone the Berkeley Pac-Man AI Code

Inside your project folder:

```bash
git clone https://github.com/ucb-ai/pacman.git pacman
```

Alternatively, download the Berkeley starter code zip:

* [CS188 Berkeley Project Page](http://ai.berkeley.edu/project_overview.html)

### 3. Create Folder Structure

```bash
mkdir media results slides notebooks
```

### 4. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 5. Install Python Packages

```bash
pip install --upgrade pip
pip install matplotlib pandas
```

### 6. Git Ignore Setup

```bash
echo venv/ >> .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
```

### 7. Launch Project in VS Code

```bash
code .
```

Then select the correct interpreter: `Python: Select Interpreter` → pick your venv.

## Ghost AI Implementation Plan

### A* Ghost

* File: `pacman/ghostAgents.py`
* Create class `AStarGhost`
* At each move:

  * Read ghost and Pac-Man positions
  * Run A* pathfinding (using Manhattan distance)
  * Return the first direction in the path
* Use `util.PriorityQueue` from `pacman/util.py`
* Confirm behavior by running:

```bash
python pacman.py -p ReflexAgent -g AStarGhost -l mediumClassic --frameTime 0.3
```

### Q-Learning Ghost

* File: `pacman/ghostAgents.py` or `pacman/qlearningGhost.py`
* Create class `QLearningGhost`
* Maintain a Q-table: `Q[state][action]`
* Define state using:

  * Ghost tile ID or grid coordinate
  * Pac-Man's relative direction (8 sectors)
  * Wall presence around ghost (N/S/E/W booleans)
* Implement:

  * Epsilon-greedy action selection
  * Q-learning update rule:

```python
Q[state][action] += alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][action])
```

* Train across many episodes and store logs.

## Reward Function Design

* +100 for catching Pac-Man
* -0.1 per step to encourage efficiency
* -50 if timeout is reached without catching
* +5 for getting closer to Pac-Man
* -2 for moving away from Pac-Man

## Training Procedure

* Create a fixed map using `layouts/` folder (e.g., `smallClassic.lay` or custom)
* Pac-Man should initially follow a simple predictable pattern (e.g., scripted movement)
* Train ghost for 1000 episodes using:

```bash
python pacman.py -p ScriptedPacman -g QLearningGhost -l smallClassic
```

* Record:

  * Cumulative reward
  * Steps per episode
  * Capture success (binary)

* Use `matplotlib` to graph reward curve:

```python
import matplotlib.pyplot as plt
plt.plot(rewards)
plt.title("Reward per Episode")
plt.show()
```

## Evaluation Metrics

* **Capture Success Rate**: % of games where ghost catches Pac-Man
* **Average Capture Time**: Steps taken before capture
* **Path Optimality**: Ratio of actual steps to shortest path
* **Adaptability**: Performance drop on new map
* **Failure Modes**: Ghost loops, stuck positions, low-reward patterns

## Visualizations

* Reward progression over training
* Ghost movement overlay paths (screenshot or GIF)
* Compare Q-values across episodes or state examples
* Optionally record gameplay:

  * [OBS Studio](https://obsproject.com/) or use screen recorder tool

## Testing and Presentation

* Evaluate both ghosts on:

  * `mediumClassic` and `originalClassic`
  * At least 20 trials each
* Save results as CSV in `results/`
* Prepare slides in `slides/` folder using Google Slides or PowerPoint
* Include:

  * Background motivation (bad NPCs)
  * Design of both agents
  * Metrics and visuals
  * Conclusions and future ideas

## Optional Enhancements

* Create UI toggle to switch between agents
* Record player feedback on difficulty
* Add second Q-learning ghost for coordination
* Scripted Pac-Man that changes patterns over time

## Deliverables

* Custom `AStarGhost` and `QLearningGhost` code
* Trained Q-table JSON/CSV
* Result graphs
* Game replays or GIFs
* Final slide deck
* README.md for internal use

## Team Members

* Mitch — algorithm implementation, training loops, evaluation framework
* Jake — ghost state modeling, training analysis, presentation visuals

This document serves as the internal guide for building and tracking project milestones.
