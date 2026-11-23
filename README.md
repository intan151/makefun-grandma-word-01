[![make.fun · u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/intan151/makefun-grandma-word-01/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/intan151/makefun-grandma-word-01/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

# One Word From Grandma

A deterministic Python entry for the make.fun competition "One Word From Grandma". It writes exactly one word — the word a grandma would text about AI.

> Robbie

Why this word: a grandma doesn't talk about "AI" — she gives the clever little machine a name, like a grandson. Warm, a little baffled, funny in one word, and tied to robots rather than any subject.

## How it works

`main.py` (Python 3.13 standard library only, no network, no randomness) validates the word (exactly one alphabetic word, 1–30 characters, no whitespace) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated word. Run it with `python3 main.py`.

Two runs produce byte-identical output (sha256 `4b747696ff0388577ae9a961f638368e699a90fd705da77ae780ff76ac348116`).
