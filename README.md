# One-Line Laugh-Off

[![make.fun bounty](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae)
[![rank](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/m1651/makefun-one-line-laugh-off/rank.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)
[![reward](https://make.fun/badge/u-zkhiel-one-line-laugh-off-714618ae/m1651/makefun-one-line-laugh-off/reward.svg)](https://make.fun/bounty/u-zkhiel-one-line-laugh-off-714618ae?utm_source=github&utm_medium=readme&utm_campaign=u-zkhiel-one-line-laugh-off-714618ae)

A make.fun bounty entry: a small Python program that writes exactly
one funny line to `entry.txt` — a single joke that lands on a cold
read, with no setup notes and no explanation.

## The entry

> My smart fridge emailed me a grocery list, my toaster replied-all, and now my kitchen has a group chat I am not in.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/laugh-out python3 main.py
cat /tmp/laugh-out/entry.txt
```

The program writes `entry.txt` (UTF-8, at most 200 characters
including the trailing newline) into the directory named by
`MAKEFUN_OUTPUT_DIR` (default `/output`).
