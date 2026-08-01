# Computational Mathematics & Visualizations
Welcome! This repository serves as an academic archive for my computational mathematics, algorithmic simulation, and data visualization projects developed during my undergraduate studies in **Mathematics**.
The primary goal of these projects is to bridge theoretical mathematical concepts-ranging from discrete systems and dynamical behavior to linear algebra and number theory-with computational implementation using Python.
---
## Project Directory
### 01. Rule 30 Cellular Automata
* **Folder:** ['/01-rule-30-cellular-automata'](./01-rule-30-cellular-automata)
* **Topics:** Discrete Mathematics, Cellular Automata, Deterministic Chaos, Complex Systems.
*  **Tech Stack:** 'Python 3', 'NumPy', 'Matplotib'.
*  **Summary:** Simulation of Stephen Wolfram's **Rule 30** 1D elementary cellular automaton. It demonstrates how estremely simple deterministic transition rules applied to binary states can generate infinitely complex, non-periodic, chaotic patterns.
---
## Mathematical Overview: Rule 30

In Rule 30, the state of cell $C_i$ at time step $t+1$ depends strictly on its current state and its left/right neighbors at time $t$:

$$C_i^{t+1} = \text{Rule}(C_{i-1}^t, C_i^t, C_{i+1}^t)$$

### Transition Rules:
| $C_{i-1}^t C_i^t C_{i+1}^t$ | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$C_i^{t+1}$** | **0** | **0** | **0** | **1** | **1** | **1** | **1** | **0** |
