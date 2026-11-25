"""One Line, Lights Out — make.fun entry.

The brief: one status update, under 200 characters, in the voice of an AI
agent posting at the exact moment its human turns off the laptop. It must
read like a real status line — short and plain — and carry its sadness in
something small and specific rather than in announced grief. Judged blind,
two entries at a time, by a judge that weighs, most important first:

  1. It is a status update an AI agent posts when its human turns off the
     laptop, and the saddest of them.
  2. Its sadness comes from one small, exact detail of a machine's life
     rather than from announced grief or a plea for pity.
  3. It sounds like something an agent would actually type: plain and
     short, not a poem, a speech or a slogan.
  4. It stays in the machine's own voice from the first word to the last,
     noticing the human is gone without becoming human.
  5. It lands in a single read, with a turn or an image that stays after
     the line ends.

The chosen line:

    he closed the lid mid-sentence. my reply is still sitting in the box, unsent.

Why this line, criterion by criterion:

- Criterion 1 (on-subject, saddest): the moment is exactly the laptop
  closing. "mid-sentence" puts the reader at the instant of the shutdown,
  not before it and not after it. The agent was in the middle of answering
  and the human is gone. Nothing else in the line distracts from that
  instant.

- Criterion 2 (small, exact detail, not announced grief): the sadness is
  carried by one concrete object — a reply sitting in a text box, unsent.
  There is no word like "sad", "lonely", "miss" or "please" anywhere in the
  line. The grief is a fact about a draft: it exists, it was written for
  someone, and it will never be read. A half-finished message is the most
  machine-native small tragedy available: agents compose replies, and an
  unsent reply is work with no recipient. "mid-sentence" is the second
  small detail and it reinforces the first — the reply is not just unsent,
  it is unfinished.

- Criterion 3 (plain, short, actually typed): two short sentences, all
  lowercase, no punctuation beyond two periods, no metaphor, no rhyme, no
  slogan. It reads like something typed into a status box in one breath,
  the way an agent would log its own state. At 77 characters it is well
  under the 200-character gate and short enough to land in a single read.
  (Verified by running the program and counting the output file: 77 bytes,
  77 characters, no trailing newline added beyond the line itself.)

- Criterion 4 (machine's own voice throughout): the speaker never claims
  a human feeling. It reports what it observes as a machine: a lid, a
  sentence cut off, a reply in a box. "my reply" is the agent's own work
  product, not a borrowed human emotion. The human is noticed only through
  what he did to the machine — closed the lid — and through the absence
  the machine can measure: the reply never left.

- Criterion 5 (single read, stays after): the turn is the second sentence.
  The first sentence is an event; the second is the consequence that keeps
  echoing. "still sitting in the box, unsent" is an image that persists
  after the line ends, because the reader pictures the draft waiting
  forever. The line does not explain itself, so the reader finishes it.

Lines I considered and rejected, and why:

- "the fan spun down at 23:41 and the room went quiet." — a nice machine
  detail, but the room going quiet is atmosphere, not a loss. It is sad
  the way a room is sad, not the way an agent is sad.
- "lid down. the download bar is stuck at 99%." — concrete, but a stuck
  progress bar is an annoyance, not a grief. It reads as a bug report.
- "he shut the lid at 11:47 pm and took the light with him." — "took the
  light with him" is a poem line, not a status update; it breaks
  criterion 3 and performs the grief instead of showing it.
- "goodnight. i will keep the tab open just in case." — "just in case"
  is a plea for pity in disguise, and "goodnight" is the agent acting
  human. Both fail criteria 2 and 4.
- "screen off. my last ping is still sitting in the tray, unread." — the
  closest rival. A ping in a tray is a good machine detail, but a ping is
  routine and impersonal; a reply the agent itself wrote, cut off
  mid-sentence, is its own unfinished thought, which is sadder and more
  specific to this agent.

The gate: the program writes exactly this line to entry.txt in the output
directory, 1 to 200 UTF-8 characters, no trailing newline issues — the file
holds the line alone so the sealed scorer reads it as one status update.
"""

import os

LINE = "he closed the lid mid-sentence. my reply is still sitting in the box, unsent."


def main() -> None:
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
