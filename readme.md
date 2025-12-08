# [Advent of Code 25](https://adventofcode.com/2025)

Once the problem is solved, I take the time to review/rewrite the code, simplify/optimize it if possible, and comment it. I have added a GitHub workflow wich runs the *ruff* linter.  This year, there's no in-house *aoc.py* module to help with input decoding. It doesn't really help, actually.

If you wish to use it, you must provide your own data file, name it *input.txt* (do not share it) and place it next to the corresponding script.


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


## [--- Day 5: Cafeteria ---](https://adventofcode.com/2025/day/5)

*00:06:16* / *00:19:41*

Nothing complicated so far. Which doesn't stop me from making stupid mistakes, and force me to wait one minute before submitting after a wrong response.


## [--- Day 6: Trash Compactor ---](https://adventofcode.com/2025/day/6)

*00:11:38* / *00:38:02*

Using zip to read a table of rows into columns is second nature to me. And while the implementation can sometimes be a bit lengthy, I find the result concise, clear, and elegant: `zip(*map(str.split, f))`


## [--- Day 7: Laboratories ---](https://adventofcode.com/2025/day/7)

*00:44:56* / *01:12:45*

It took me over half an hour to understand the part 1! I then fell into the trap of part 2, listing all the paths when all I had to do was count them. Seeing that the result would take too long to arrive, I continued searching for a better solution. Unfortunately, the initial script was already running. Reboot.
Also proposing an AWK script (`./Laboratories.awk input.txt`).


## [--- Day 8: Playground  ---](https://adventofcode.com/2025/day/8)

*00:34:36* / *00:51:51*

I can't explain why it's taking me so long. The first draft is very quick, but there are still a lot of mistakes. The goal of my participation was to improve in this area. I don't see any progress yet :(. But I'm still having a lot of fun :).