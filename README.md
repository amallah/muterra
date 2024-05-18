# Genetic Algorithm Pathfinding

This repository contains a Python implementation of a genetic algorithm to solve a pathfinding problem on a 2D grid. The goal is to navigate from starting points on the grid to maximize a score based on specific rules. This is actually a tool I used to help me play the [Muterra](https://muterra.in/) [Discord Game](https://peakd.com/hive-196251/@muterra/muterra-discord-game-season-4) - it was by no means a winner, but was definitely a time saver and fun project

## Code Overview

### `mutate_agent(agent_genome)`

Mutates a given agent's genome by randomly altering its directions.

### `compress(solution)`

Compresses a solution by removing unnecessary moves.

### `generate_random_agent()`

Generates a random agent with a valid path from a random starting point.

### `pretty_print(solution)`

Prints the solution in a readable format with the path and score.

### `compute_fitness(solution)`

Calculates the fitness of a given solution based on the grid rules and path.

### `freeze(d)` and `unfreeze(d)`

Utility functions to handle immutable and mutable data structures for the genetic algorithm.

### `generate_random_population(pop_size)`

Generates a random population of agents.

### `run_genetic_algorithm(generations=50000, population_size=100)`

Runs the genetic algorithm for a specified number of generations and population size.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries: `datetime`, `copy`, `json`, `sys`, `random`, `os`, `base64`, `hashlib`

### Running the Code

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/genetic-algorithm-pathfinding.git
    cd genetic-algorithm-pathfinding
    ```

2. Run the script:
    ```sh
    python pathfinding.py
    ```

### Example Output

The script will output the generation number, best fitness score, unique genomes, and the path with its score.

```sh
Generation 1000 best: 55.5 | Unique genomes: 1000 [10.123]
[A] N-S-E-W-N-...
