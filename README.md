Stizh Encounter Test
====================

Overview
--------
A program to calculate how much time players would have during a specifically
designed encounter in 5th Edition Dungeons & Dragons®.

Scenario
--------
A building is supported by 10 pillars around its periphery. These pillars are
damaged by hidden traps which deal 11d8 (the sum of 11 rolls of an 8-sided die)
damage to their cooresponding columns. Each column has a total of 50 hit points.
Some of the traps (determined earlier) do not function properly. If a surviving
pillar is neighbored by a demolished pillar, it takes a certain amount of damage
per turn. Using a probabilistic approach, I can test various damage constants
for the crumbling pillars and obtain the average number of turns until none of
the pillars are left standing.

Key
---
\* - Planned changes, modifications, improvements

Usage
-----
1) Run the program encounterTest.py

2) If it lags, create a KeyboardInterrupt to override the trial that is delaying
   the process.
   *This is caused by a trial in which none of the columns were demolished.

3) The program will print an average number of turns until every column is
   destroyed across a sample size of 1000 with damage constants of 3, 2.5, 2,
   1.5, and 1 per demolished neighbor accordingly.

Author
------
Glib Dolotov