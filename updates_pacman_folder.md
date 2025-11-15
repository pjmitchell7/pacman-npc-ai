Here’s a fully fleshed-out `README.md`-style writeup you can copy and paste into your project:

---

# 🧠 Smarter Pacman & Adaptive Ghosts – Multiagent AI Enhancement

This project builds on UC Berkeley’s Pacman AI framework, introducing significant improvements to both Pacman’s strategy and Ghost adversary behavior using decision trees and reinforcement learning. These changes aim to simulate a more intelligent multiagent environment where Pacman tries to win efficiently and the Ghosts learn to stop him through training.

---

## 📁 Directory Overview

All major customizations live in:

```
pacman/multiagent/
```

This includes:

* A smarter Pacman agent (`ExpectimaxAgent`)
* Q-learning Ghost agents (`QLearningGhost`)
* Evaluation enhancements
* Reinforcement learning support
* Training and demo scripts

---

## 👾 Smarter Pacman (ExpectimaxAgent)

**File:** `multi_agents.py`
**Agent Class:** `ExpectimaxAgent`

### 🧠 Evaluation Function: `better_evaluation_function`

Pacman's behavior is guided by a deeper, handcrafted evaluation heuristic used by the Expectimax algorithm. Here’s how it works:

| Component                   | Description                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| 🟡 **Food Bias**            | Rewards fewer food pellets remaining. The fewer left, the more urgency to finish the game. |
| 🕒 **Stall Avoidance**      | Penalizes idling or looping behavior near food — especially the final dot.                 |
| 👻 **Ghost Safety**         | Avoids ghosts when they're dangerous and chases them when vulnerable.                      |
| ⚡ **Power Capsules**        | Considers power pellet timing and ghost vulnerability for bonus scoring.                   |
| 🧠 **Time Awareness**       | Penalizes letting the timer run unnecessarily — encourages finishing faster.               |
| 🗺️ **Distance Heuristics** | Uses maze distances (not Euclidean) for realistic path assessments.                        |

### 🧪 Fixes to Notable Bugs:

* ❌ No more stalling near final dot
* ✅ Avoids hiding endlessly
* ✅ Actively makes game-ending moves
* ✅ Uses power pellets for scoring, not just survival

---

## 👻 Smarter Ghosts with Q-Learning

**File:** `ghost_agents.py`
**Class:** `QLearningGhost`

### 🔍 Learning Mechanism

The ghosts use Q-Learning to train over time how to trap and defeat Pacman. Each ghost maintains its own Q-table mapping states to action values.

| Feature                | Details                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| 📦 **State**           | Tuple of (ghost position, Pacman position)                                                          |
| 🎯 **Actions**         | All legal directions: North, South, East, West, Stop                                                |
| 🧠 **Reward Function** | +1 for getting closer to Pacman, -1 for retreating or colliding with another ghost, +10 for winning |
| 🔁 **Exploration**     | Epsilon-greedy strategy: 5% of moves are random to ensure exploration                               |

### 📁 Saved Brains (`.pkl` files)

Q-tables are saved automatically at each milestone:

```
results/qtables/ghost1_ep1000.pkl
results/qtables/ghost2_ep1000.pkl
```

These files act as the ghosts’ "brains" and are reloaded for demos.

---

## 🧪 Training Ghosts

**Script:** `train_ghosts.py`

Trains both ghosts over any number of episode milestones. Example:

```bash
python pacman/multiagent/train_ghosts.py --milestones 0 100 500 1000
```

* Intermediate Q-tables are saved for analysis.
* Pacman opponent uses `ExpectimaxAgent` with the enhanced evaluation function.

---

## 🎮 Demo Mode

**Script:** `demo_ghost.py`

Runs a visual Pacman game using your trained ghosts and the smart Pacman agent.

```bash
python pacman/multiagent/demo_ghost.py \
  --qfile1 results/qtables/ghost1_ep1000.pkl \
  --qfile2 results/qtables/ghost2_ep1000.pkl
```

### Optional Flags:

* `--layout` to choose a map (e.g., `smallClassic`)
* `--zoom` to control game speed (higher = slower)

---

## ⚠️ Git Sync Note

If GitHub isn't showing your changes:

* Ensure your modified files are being tracked (`git add`)
* If still blocked (e.g., upstream permissions), share the full `pacman/multiagent/` folder manually (ZIP or direct copy)

---

## 🛠 Summary of Custom Functions

### In `multi_agents.py`:

* `better_evaluation_function(state)`
* `ExpectimaxAgent.get_action()`

### In `ghost_agents.py`:

* `QLearningGhost.get_action()`
* `QLearningGhost.observe_transition()`
* `QLearningGhost.update()`
* `QLearningGhost.load_qvalues(path)`
* `QLearningGhost.save_qvalues(path)`

### In `train_ghosts.py`:

* `train_and_evaluate(milestones)`

### In `demo_ghost.py`:

* `load_q_ghost(index, path)`
* `main()` with argparse

---

## 📊 Future Enhancements

* Ghost teamwork via shared state or coordination strategies
* Use deeper Expectimax trees (increase depth from 2 to 3+)
* Introduce reward penalties for letting Pacman stall (to break mutual inactivity bias)
* Visual heatmap of Pacman movement patterns for Q-table analysis
* Replay recording and scoring dashboard

