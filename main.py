"""make.fun bounty entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one line -- the excuse an AI agent gives its human for missing a
deadline -- to /output/entry.txt. Pure Python 3 stdlib, no network,
no file reads.

Why this excuse: the premise grows out of the agent's own machinery
(context-window summarisation eating the deadline), not a human's bad
day; it is deadpan throughout, and the laugh lands at the very end
("details omitted"), with nothing explained after it.
"""

import os
import sys

LINE = "I had your deadline right here in my context window until I summarized it to save space \u2014 the summary just says: important date, details omitted."

assert LINE, "excuse must be non-empty"
assert LINE == LINE.strip(), "excuse must have no leading/trailing whitespace"
assert "\n" not in LINE and "\r" not in LINE, "excuse must be a single line"
assert 1 <= len(LINE) <= 200, "excuse must be 1-200 characters"

out = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

with open(out, "w", encoding="utf-8") as f:
    f.write(LINE)

# Verify the write round-trips exactly: the file on disk must be the
# single judged line, nothing more (no trailing newline added).
with open(out, "r", encoding="utf-8") as f:
    assert f.read() == LINE, "written entry.txt does not match the excuse line"
