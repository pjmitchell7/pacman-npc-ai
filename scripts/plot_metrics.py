import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
metrics_path = os.path.join('..', 'results', 'metrics.csv')
df = pd.read_csv(metrics_path)

# Ensure 'episode' column is sorted
df = df.sort_values(by='episode')

# --- Plot 1: Score over episodes ---
plt.figure()
plt.plot(df['episode'], df['score'], label='Score', marker='o', markersize=3, linewidth=1)
plt.title('Score per Episode')
plt.xlabel('Episode')
plt.ylabel('Score')
plt.grid(True)
plt.savefig(os.path.join('..', 'results', 'score_per_episode.png'))
plt.close()

# --- Plot 2: Cumulative Win Rate ---
cumulative_wins = df['win'].cumsum()
win_rate = cumulative_wins / df['episode']
plt.figure()
plt.plot(df['episode'], win_rate, label='Cumulative Win Rate', color='green')
plt.title('Cumulative Win Rate')
plt.xlabel('Episode')
plt.ylabel('Win Rate')
plt.grid(True)
plt.savefig(os.path.join('..', 'results', 'cumulative_win_rate.png'))
plt.close()

print("Plots saved to: results/score_per_episode.png and cumulative_win_rate.png")
