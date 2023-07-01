# Damavis Engineer Challenge 2023
**Python code for Damavis Engineer Challenge.**

The main goal of this challenge is to carry the rod from the top left corner of the labyrinth to the botton right corner. To success in this task, we have to complete the labyrinth by finding the minimun number of movements as possible. We have to consider that some of the cells are blocked, and that we cant get out of bounds.

The movements that can be performed are: move the rod one cell down or up, to the right or to the left, or to change its orientation from vertical to horizontal (for doing this we have to check if all cells in 3x3 matrix are free) and vice versa. Our code will provide the minimum number of movements required for reaching the goal. In case our rod can not complete the labyrinth, the code will return -1. 

**The following files are provided:**

* main.py: all functions needed are defined in this file. At the end, the main loop is defined.
* testLabyrinth.py: the different test carried on are being defined in this file. 

