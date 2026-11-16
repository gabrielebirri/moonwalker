# Agents.md

## Project overview

Moonwalker is a project to deploy a swarm of agents to analyze and evaluate possible lunar landing sites for future missions.
Main language: Python
NOTE: past and current design choices can be found inside "BRAINSTORMING.md"

## Setup and commands

- conda environment setup: `conda activate moonwalker`

## Code style

- The codebase must be scalable for future feature implementations
- Each function should be written in a separate python file for portability and scalability
- Each function should stay inside a printable A4 format length (approximately 60 lines) for better readability (not mandatory, but encouraged)
- All the code must be commented and every function should have an header in which its functionalities are explained. All physical quantities must have unit of measurement
- ALWAYS cite in the function header sources from which you've taken code/informations

## Project structure

- `src/` main code
- `tests/` tests (mirror the `src/` layout)

## Rules

- DO NOT push commit to the origin, ask always
- ALWAYS cite sources if you use other people work/code in header
