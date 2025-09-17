# Networks of Power and Poverty

## Overview

This project, developed as part of my research in Human-Centered Machine Intelligence Lab at BYU, is dedicated to understanding and addressing the mechanisms that perpetuate poverty and inequality. By simulating and visualizing the dynamics of token exchange in complex networks, we aim to uncover how resources, opportunities, and influence flow through social structures—and how targeted interventions might help individuals and communities escape cycles of poverty. Nodes represent people or organizations, and edges represent relationships or channels for resource transfer. The system enables exploration of how network structure and edge properties affect the distribution and concentration of tokens, providing insights to inform real-world strategies for empowerment and poverty alleviation.

## Features

- **Graph Generation:** Supports multiple network topologies (e.g., Watts-Strogatz, Barabási-Albert, circulant, lattice, barbell, stochastic block, Erdős-Rényi) to model diverse social structures.
- **Token Exchange Simulation:** Implements a round-based mechanism where nodes distribute tokens to neighbors, reflecting resource sharing, influence, or wealth transfer. Self-loops and edge weights allow for nuanced control over retention and flow.
- **Visualization:** Provides animated and step-through visualizations of token distribution, with node color intensity representing token count, enabling intuitive analysis of network effects.
- **Customizable Parameters:** Users can select graph type, layout, directionality, edge weights, self-loop probability, and simulation mode for tailored experiments.
- **Testing:** Includes unit tests to ensure correctness and conservation of tokens during exchanges.

## Applications

This tool is designed for researchers, educators, and students interested in:
- Social network analysis
- Economic modeling of wealth and poverty
- Studying the emergence of inequality and power structures
- Exploring the impact of network topology on resource distribution

## Getting Started

1. Clone the repository and install dependencies (see requirements).
2. Run `main.py` to launch the interactive simulation.
3. Follow prompts to configure the network and simulation parameters.
4. Visualize and analyze the evolution of token distribution.

## License

This project is licensed under the MIT License.