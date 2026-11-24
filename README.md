[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/mfahmiq/time-machine-warning/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/mfahmiq/time-machine-warning/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

An entry for the [make.fun](https://make.fun/c/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) bounty **"Funniest Time Machine Warning Label"** — write the funniest one-line warning label for a time machine, in 120 characters or fewer.

The entry:

> **WARNING: If you meet yourself, remain calm. You have done this before.**

70 characters. One line. No assembly required — just a safety notice that has clearly been written by someone who has already read it several times.

## Why this line is funny

It does its work in three beats, and the laugh lands on the last one:

1. **"WARNING:"** — the deadpan safety-label voice. It sounds like it belongs on the side of a machine, next to "Do not operate while wet" and "Keep fingers clear of moving parts." The official calm is what makes everything after it funnier.
2. **"If you meet yourself, remain calm."** — the real hazard of time travel, stated as a routine operational risk. Meeting your own duplicate is treated like turbulence: unsettling, but manageable, and — crucially — *expected*. The label doesn't say *if* this happens as a freak accident; it says *when*, as a known condition of use.
3. **"You have done this before."** — the surprise, saved for the last few words. The sentence quietly reveals that this is not the first time: the traveller has already met themselves, already panicked, already read this label, and is now doing it all again. The warning is a loop. The person reading it is trapped in the very paradox it warns about — and the label knows it, calmly, in writing.

Nothing is named flatly ("paradox", "time loop", "causality") — the paradox *is* the joke, delivered in the voice of a manufacturer who has already fielded the complaint. Every phrase does work, and nothing is wasted inside the character limit.

## How it works

`main.py` (Python standard library only, deterministic) holds the entry text as a string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before and after writing, it self-verifies the competition gate:

- valid UTF-8
- 1–120 characters (this entry: 70)
- a single line
- not whitespace-only

It exits non-zero on any failure, so a bad entry can never be written silently.

## Usage

```bash
python3 main.py
# writes /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## Files

| File | What it is |
| --- | --- |
| `main.py` | The entry program — holds the label, writes and verifies `entry.txt` |
| `entry.txt` | The entry itself: the one-line warning label (70 characters) |
| `README.md` | This file |
| `LICENSE` | MIT License |

## License

MIT License — see [LICENSE](LICENSE).
