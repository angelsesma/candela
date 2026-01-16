# Pattern Acquisition and Comparative Analysis in the Game of Go: A Modern Approach

**Author:** Ángel Alberto Sesma González  
**Co-author:** Leonardo Jiménez Martínez  
**Date:** 2025-03-14  

---
## Abstract
The game of Go represents a major challenge for artificial as well as human intelligences
due to its profound complexity.
Although computer programs capable of playing Go have existed for decades, the period
from 2015 to 2025 has marked a turning point, with these systems achieving—and even
exceeding—professional human performance. 

A notable shift in gameplay strategy emerged
around 2016, driven by the adoption of unconventional yet effective moves demonstrated by AI
programs, challenging previous conventions of preferred moves.
Nowadays, the process of learning Go has evolved from traditional knowledge transfer,
based on centuries of established conventions regarding strategy, positional judgement and move
value to modern trends developed by AI playing style, lacking the explanatory heuristics inherent
in both human style of playing and oral tradition.

Facing this new challenge, we rely on our curiosity to understand our opponents’ moves
beyond technological and language barriers as we continue to explore the mysterious depths of
this timeless game.

---
## Keywords
Statistical analysis, Pattern recognition, AI interpretability, Modern theory, Style
evolution, Professional Games, Computational Go.


---
## I. Introduction


For our investigation of this perceived evolution in the style of play, we first compiled a
selection of academic literature published in the latest 50 years, regarding analysis of Go from a
mathematical standpoint. Among other approaches, the work of Liu and Dou (2007) titled
“Automatic Pattern Acquisition from Game Records in Go”[1] presented a simple and effective
methodology that persisted in guiding our inquiries. Their study of frequency in patterns sampled
the placement of each stone on the board statistically across 9,500 professional games from the
early 2000s.

We focused our research in reiterating this simple but effective methodology with
existing records of both current and previous professional games, expecting to find changes in
the frequency of moves played then as opposed to now.
The scope of this work is as follows:
• First we present an updated algorithm for automatic pattern acquisition, building on the
algorithm introduced in [1].
• Then we analyze high-frequency patterns from over 17,000 recent professional games, as
well as 19,000 from a period before AlphaGo (2002-2011) in order to identify the evolution of
most frequent patterns in professional play.

---
## II. Related Work

## II.1 Literature

The acquisition and analysis of patterns in Go have been extensively studied, with early efforts
focusing on manual compilation of patterns and language-based approaches denoting specific
moves in relationship to their resulting shapes, such as: knight’s jump (keima), hug (hane), kick
(tsuke), corner enclosure (shimari), forcing move (kikashi), solid connection (nobi), one space
jump (ikken-tobi), etc.
Studies published as early as 1990 have paved the way to explore the role of patterns in
Monte Carlo tree search and move generation, [2] and the use of terminology to identify the
essential components of whole board positions such as liberties, captures, ko situations, life and
death of groups, etc. [3],[4]

A statistical method for automatic pattern acquisition was introduced in 2007 [1] defining
patterns as spatial relationships within a fixed 5x5 grid. This approach demonstrated the
feasibility of extracting repeatable patterns from game records and highlighted the importance of
statistical usage in determining pattern urgency.
Recent advances in AI, particularly deep reinforcement learning, have shifted the focus
toward end-to-end learning systems such as AlphaGo. Nevertheless, pattern-based approaches
remain relevant for understanding human play and improving interpretability in AI systems.
Recent work involves combinatorial game theory applied to complex endgame positions
[5], as well as measurements of the degree of complexity of several variants and rulesets relevant
to the game of Go. [6] Despite these advancements, there is a lack of comparative studies
analyzing the evolution of Go patterns over time. 

Our research bridges that gap by revisiting the methodology of [1] and applying it to a
modern dataset of professional games.

## II.2 New Analysis

Evaluating patterns by extracting 5x5 grids, as per selected literature [1] results in what could be
compared to “atomic” components of the whole board strategy inherent in the game of go. While
this criteria yields interesting results, we decided to leverage today’s availability of computing
power to expand the area of possible patterns.

This enlargement allowed us to obtain a whole board perspective and detect the
appearance of well-known joseki sequences, akin to “molecules” in a figurative sense. In order to
achieve this, results obtained in [1] had to be replaced by our new analysis, in order to be
consistent enough for a comparative analysis.

---

## III. Methodology

## III.1 Pattern Definition

A Go pattern is defined as a spatial configuration of stones where the most recent move is
displayed in the center of a 19x19 grid. [1] Our primary objective was to construct a database of
such patterns, extracted from every move in the sampled game records, and quantify their
frequencies. To ensure accuracy, we also implemented a canonical representation function that
groups equivalent patterns across the board and accounting for rotations, reflections, and color
inversions of each pattern to produce a statistically coherent count, allowing for mirror images of
the same pattern to be represented as variations of the same move, regardless of the color of the
stones, orientation relative to the board’s symmetries. 

Note: This canonical representation implies that the color of the stones playing a certain
move is arbitrary, as it groups together equivalent moves without differentiating the sequential
turns that are customary in Go (i.e. black is followed by white)

Additionally, a function that differentiates the outermost (first) three lines of the board
was necessary. This function becomes increasingly important as the most frequent moves are
normally located in the corners of the board, and even more so with modern opening strategies,
according to our findings.

## III.2 Datasets

We compiled two datasets:
A) ~19,600 games played between 2002 and 2011
B) ~17,300 pro games played between 2016 and 2025.
The records were downloaded using a simple python script and sourced from http://gokifu.com
After the datasets were examined for games containing illegal moves or corrupt data,
dataset A consisted of 19,584 records, while dataset B totaled 17,173 records suitable for
analysis.

## III.3 Pattern Acquisition Algorithm

The script employs a python library called sgfmill that is able to parse SGF records and
extract data one move at a time. Other libraries are necessary such as os, pathlib for accessing
files and folders, as well as collections for efficiently cataloguing moves canonically. the core
algorithm is based on the pseudocode presented in[1], and implemented using Python 3.
The algorithm processes each move in each game record using nested for loops as
follows:

```python
For each game:
    For each move:
        Extract the 19×19 grid centered on the move.
        Convert the grid to its canonical form.
        Update the pattern's frequency in the database.
Sort the database in descending order.
Print the top 16 patterns with their frequency.
```

(The algorithm has linear complexity relative to the number of moves, making it efficient for large datasets [1].)

## III.4 Statistical Analysis
We analyzed the frequency distribution of patterns across the dataset, identifying the 19
most frequent 19x19 patterns for cross-temporal analysis. This allowed us to visualize stylistic
shifts in professional play statistics over the course of 18 years of professional Go matches.
In order to compute the data effectively, we designed a simple notation using the
following symbols:
☻(black smiley face): Player in turn.
☺(white smiley face): Opponent.
+ (plus sign): Empty intersection.
/ (slash sign): Edge intersection (first line of the board).
. (dot) : Space outside the board.
  
These symbols allow for consistent pattern matching while performing transformations
on matrices, while keeping track of plays near the edge of the board as different from patterns
located in the central area, identifying plays in the 4,4 corner star point (hoshi) and its adjacent
3,4 intersection (komoku) separately. 

---

## IV. Findings

## IV.1. Change in Frequency of Patterns in Professional Games

Our analysis reveals patterns found in the professional dataset, with the new top 19 highfrequency patterns compared to pre-AI style of play (see Table 1).
We observe a significant rise in the early san-san invasion to a corner star point, a
trademark aspect of AI style. Modern joseki sequences therefore appear considerably more often,
displacing approaches to opponents’ single stones in the corners of the board

## IV.2 Evolution of Go Strategies

Our results indicate that certain patterns have remained consistently popular, while others
have declined in usage. For instance, the 3-3 invasion has become more frequent, signaling a
preference for corner territory as opposed to developing the edges early in the game. However,
corner enclosures appear to occur less frequently, with a two-space jump from the 3-4 point
becoming more urgent than the classical knight’s jump.
These trends effectively represent the evolving strategies in professional Go and the
influence of AI on human play.

---

## V. Discussion

By comparing a pattern’s prevalence to that of its local follow-ups, we infer the relative
frequency of moves outside the local area—a phenomenon consistent with tennuki (prioritizing a
distant move over local continuation). For instance, when a pattern’s frequency surpasses that of
its immediate continuation, it implies players often prioritize global strategy over local battles.
Periodic replication of this study could deepen our understanding of professional play,
challenge time-honored proverbs, and modernize pedagogical frameworks for learning and
improving at Go.
For experienced players, these findings provide actionable insights into contemporary
strategies, while beginners and intermediates gain a structured approach to studying professional
games. Ultimately, this research bridges tradition and innovation, fostering a dynamic, datadriven culture within the Go community.

---

## VI. Conclusion

This article presents a modern approach to automatic pattern acquisition in the game of
Go. By analyzing large datasets of recent professional games, we identify key trends and shifts in
pattern usage, offering new insights into the evolution of Go strategies. 

Our results underscore the importance of pattern-based approaches in both human and AI
play, and provide a framework for future research in game AI and pattern recognition.
VII. Acknowledgements
This work is dedicated to the memory of Professor José “Pepe Chac” Chacón, for his
exemplary fighting spirit and invaluable contributions to Mexico’s Go community.
---

## References
1. Liu, Z., & Dou, Q. (2007). Automatic pattern acquisition from game records in Go. The
Journal of China Universities of Posts and Telecommunications, 14(1), 100-106.
doi.org/10.1016/S1005-8885(07)60065-X

2. Bouzy, B., & Cazenave, T. (2001). Computer go: An AI oriented survey.
Journal of Artificial Intelligence, 132(1), 39-103.
doi.org/10.1016/s0004-3702(01)00127-8/

3. Yee, A., & Alvarado, M. (2015). Mathematical modeling and analysis of learning techniques
for the game of Go. International Journal of Mathematical Models and Methods in Applied
Sciences, 9(1), 293-302.
https://www.researchgate.net/publication/
282709898_Mathematical_modeling_and_analysis_of_learning_techniques_for_the_game_of_Go

4. Spight, W. (2001). Extended Thermography For Multiple Kos in Go. Theoretical Computer
Science, Elsevier 252(1), 23–43.
doi.org/10.1016/S0304-3975(00)00075-X

5. Berlekamp, E., & Wolfe, D., (1994). Mathematical Go - Chilling Gets the Last Point. Wesley,
MA: A. K. Peters.
doi.org/10.1201/9781439863558

6. Saffidine, A., Teytaud, O., & Yen, S.-J. (2015). Go complexities. In Proceedings of the
Advances in Computer Games Conference (pp. 88–99). Leiden, Netherlands: Springer.
doi.org/10.1007/978-3-319-27992-3_8
---

## Table 1
![Table containing top patterns found](https://github.com/angelsesma/candela/blob/tabla.pdf)
