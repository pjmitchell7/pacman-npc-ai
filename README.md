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
├── pacman/                 # AIG-UPF Pac-Man Projects codebase
│   ├── multiagent/         # Custom ghost agents, including Q-Learning and A*
│   ├── layouts/            # Maze files for gameplay
│   ├── graphicsDisplay.py  # GUI display
│   └── search/             # A* search algorithms
├── results/                # Logs, metrics, Q-tables, plots
├── media/                  # GIFs, videos, screen recordings
├── slides/                 # Final presentation deck
├── notebooks/              # Optional experiments or data analysis
├── venv/                   # Python virtual environment
├── .gitignore              # Ignoring venv and cache
├── README.md               # Project overview and planning
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

### 2. Clone the AIG-UPF Pac-Man AI Code

Inside your project folder:

```bash
git clone https://github.com/aig-upf/pacman-projects.git pacman
```

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

---

## Ghost AI Implementation Plan

### A* Ghost

* File: `pacman/multiagent/ghostAgents.py`
* Create class `AStarGhost`
* At each move:

  * Read ghost and Pac-Man positions
  * Use `aStarSearch()` from `pacman/search/search.py`
  * Apply Manhattan distance heuristic
  * Return the first direction in the path
* Use `util.PriorityQueue` from `pacman/util.py`
* Test with:

```bash
python pacman.py -p ReflexAgent -g AStarGhost -l mediumClassic --frameTime 0.3
```

### Q-Learning Ghost

* File: `pacman/multiagent/qlearningGhost.py` (or in `ghostAgents.py`)
* Create class `QLearningGhost` by adapting existing Q-learning logic from `reinforcement/qlearningAgents.py`
* Maintain Q-table: `Q[state][action]`
* Define state using:

  * Ghost grid position (e.g., x, y)
  * Pac-Man's relative direction (N, NE, E, etc.)
  * Surrounding walls (binary for N/S/E/W)
* Implement:

  * Epsilon-greedy action selection
  * Q-learning update:

```python
Q[state][action] += alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][action])
```

* Train across episodes; store data in `results/qtable.json`

---

## Reward Function Design

* +100 for catching Pac-Man
* -0.1 per step (efficiency)
* -50 for timeout
* +5 if ghost moves closer to Pac-Man
* -2 if ghost moves away

---

## Training Procedure

* Layouts located in `pacman/layouts/`
* Use default maps like `smallClassic.lay`, or create custom ones
* Create simple deterministic `ScriptedPacman` agent for controlled training
* Train using:

```bash
python pacman.py -p ScriptedPacman -g QLearningGhost -l smallClassic
```

* Log:

  * Total reward
  * Steps to capture
  * Capture success/failure

* Visualize with:

```python
import matplotlib.pyplot as plt
plt.plot(rewards)
plt.title("Reward per Episode")
plt.show()
```

---

## Evaluation Metrics

* **Capture Success Rate**: % games won by ghost
* **Average Capture Time**: Steps to catch Pac-Man
* **Path Optimality**: Ghost path length vs shortest path
* **Adaptability**: Success rate when layout changes
* **Failure Modes**: Ghost gets stuck, loops, etc.

---

## Visualizations

* Plot Q-value convergence
* Side-by-side video/GIF of A* vs Q-learning behavior
* Annotated maps showing ghost paths
* Record with [OBS Studio](https://obsproject.com/) or similar

---

## Testing and Presentation

* Compare both ghost types on `mediumClassic`, `originalClassic`, and at least one custom layout
* 20+ trials each
* Save CSVs to `results/`
* Create slides in `slides/` folder
* Final presentation includes:

  * Problem motivation (dumb NPCs)
  * Algorithm designs
  * Results + graphs
  * Lessons learned, next steps

---

## Optional Enhancements

* Make ghost difficulty toggleable via CLI or config
* Try hybrid Q-learning with A*-based heuristics
* Add second Q-learning ghost for coordination
* Collect playtester feedback (immersion, difficulty)

---

## Deliverables

* Modified `AStarGhost` and `QLearningGhost`
* Trained Q-table export
* Result logs and plots
* Gameplay media (GIFs or videos)
* Final slide deck
* README.md (this file)

---

## Team Members

* **Mitch** — Algorithm implementation, training scripts, evaluation pipeline
* **Jake** — State modeling, Q-learning design, presentation visuals

This document serves as our internal guide and implementation checklist.
