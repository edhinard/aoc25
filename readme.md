# [Advent of Code 25](https://adventofcode.com/2025)

My solutions for solving the puzzles (without committing the input data which should not be shared). Using Python. Once the problem is solved, I take the time to review the code, simplify it if possible, and comment it. I have added a GitHub workflow wich runs the *ruff* linter.  This year, there's no in-house *aoc.py* module to help with input decoding. It doesn't really help, actually.


## [--- Day 1: Secret Entrance ---](https://adventofcode.com/2025/day/1)

*04:19:03* / *04:42:49*

At first I didn't want to participate. But then when I saw that it only lasted 12 days, I decided to go for it.

## [--- Day 2: Gift Shop ---](https://adventofcode.com/2025/day/2)

*00:16:30* / *00:23:14*

First wake-up at 5:45 am. Getting back into good habits.


## [--- Day 3: Lobby ---](https://adventofcode.com/2025/day/3)

*00:08:29* / *00:23:33*

Some time was spent debugging the second part. Yes, The slice `[:0]` is not equivalent to `[:]`! The statement to find the largest value in the list, excluding the last ones becomes: `max(ratings[:-i if i else None])`


## [--- Day 4: Printing Department ---](https://adventofcode.com/2025/day/4)

*00:09:57* / *00:13:37*

I am often wrong, but this time I correctly guessed what the statement of the second part would be after reading the first.  I had to find a different name for the variable containing the map of the printing department in order to comply with rule [A001](https://docs.astral.sh/ruff/rules/builtin-variable-shadowing/): use `grid[row][col]` instead of `map[row][col]`.