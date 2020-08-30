#!/usr/bin/env python3
# Recreation of double slit experiment from
# https://www.wolframphysics.org/bulletins/2020/08/a-short-note-on-the-double-slit-experiment-and-other-quantum-interference-effects-in-the-wolfram-model/

#from math import comb
from collections import defaultdict
import matplotlib.pyplot as plt

class SlitExp:
  def __init__(self, positions):
    # List of particle starting positions
    self.initial_positions = positions
    # Weights for each position
    self.dist = {self.initial_positions: 1}

  # Run experiment for <time> steps. Don't allow particles to pass through each
  # other unless blocking is False
  def run(self, time, blocking=True):
    for depth in range(time):
      new_dist = defaultdict(int)
      for state, count in self.dist.items():
        for i, pos in enumerate(state):
          # Move left if not blocked by particle to left
          if not blocking or i == 0 or state[i] - state[i-1] > 1:
            new_dist[(state[0:i] + (pos-1,) + state[i+1:])] += count
          # Move right if not blocked by particle to right
          if not blocking or i == len(state) - 1 or state[i+1] - state[i] > 1:
            new_dist[(state[0:i] + (pos+1,) + state[i+1:])] += count
      self.dist = new_dist

    self.calculate_density()

  def calculate_density(self):
    pos = defaultdict(int)
    self.weight = 0
    for state, count in self.dist.items():
      for p in state:
        pos[p] += count
      self.weight += count
    self.density = [pos[key] for key in sorted(pos.keys())]

  def show_distribution(self):
    vals = []
    print(f'10000*prob Positions')
    for key, val in sorted(self.dist.items(), key=lambda x: (sum(x[0]), sum(x[0][1:]), sum(x[0][2:]))):
      print(f'{10000*val/self.weight:10f} {key}')
      vals.append(val/self.weight)
    print(f'Paths:   {self.weight}')
    print(f'States:  {len(self.dist)}')
    plt.plot(vals)
    plt.show()

  def show_density(self):
    for v in self.density:
      print(f'{v:80d}')
    plt.plot(self.density)
    plt.show()

