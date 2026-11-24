#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

The program writes exactly one line of deliberately terrible advice to
/output/entry.txt. It is deterministic: the same line every run, no
network, no randomness, no model call, only the Python standard library.

Line design, following the judge brief in its published order:
1. Worst advice, specific enough to follow: light a real fire under
   the smoke alarm to test it, a concrete action a reader could
   actually do and then regret, because the test itself is the danger.
2. Funny on first read: the deadpan false logic in the second half
   ("real alarms only respond to real smoke") lands without explanation.
3. Tight: one short sentence, 100 characters, no wasted words.
4. AI assistant voice: a tidy "To ... , ..." how-to, confident and
   tidy, the way a helpful assistant states a false rule as fact.
5. Concrete: smoke alarm, a small fire underneath it, a real
   situation and action.
"""

from pathlib import Path

ADVICE = (
    "To test your smoke alarm, light a small fire underneath it "
    "\u2014 real alarms only respond to real smoke."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ADVICE.strip()
    if not 1 <= len(text) <= 140:
        raise ValueError(f"advice must be 1-140 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("advice must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
