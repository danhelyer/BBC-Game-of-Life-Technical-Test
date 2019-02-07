# Dan Helyer: BBC Graduate Trainee Scheme Technical Test
As part of my application to the BBC's Software Engineering Graduate Trainee Scheme, I was asked to create a version of Conway's Game of Life following the rules laid out below. I completed this task using **Python 3.7** and designed my program to be run from the Command Line.

After choosing the grid dimensions, users can evolve to the next game iteration by pressing enter. This will be allowed to continue until life has become static, cyclical, or non-existent. At which point the game will end.

## Assumptions
In completing this task I made the following assumptions:
1. An infinite grid is not possible, instead users may define grid dimensions
2. Rather than beginning with a predefined seeded grid, random grid generations are acceptable

## Conway's Conditions for Life
### Scenario 0: No Interations
Given a of life where there are no cells, on the next step there are still no live cells
### Scenario 1: Underpopulation
When a live cell has fewer than two neighbours, it dies.
### Scenario 2: Overcrowding
When a live cell has more than three neighbours, it dies.
### Scenario 3: Survival
When a live cell has two or three neighbours, it stays alive.
### Scenario 4: Creation of Life
When a blank cell has exactly three neighbours, it comes to life
