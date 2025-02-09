import sys
import difflib
import os

# パイプで渡された候補をすべて読み込む
candidates = [line.strip() for line in sys.stdin if line.strip()]

# TTY(端末)を開いてそこからユーザー入力を受け取る
tty_path = '/dev/tty'
if not os.path.exists(tty_path):
    raise RuntimeError("No TTY available.")

with open(tty_path, 'r') as tty:
    print("Enter query (Ctrl-D to exit):")
    while True:
        query = tty.readline()
        if not query:
            # Ctrl-D等でEOFになった
            break
        query = query.strip()
        if not query:
            continue
        matches = difflib.get_close_matches(query, candidates, n=10, cutoff=0.0)
        if matches:
            print("Matches:")
            for m in matches:
                print("  ", m)
        else:
            print("No matches found.")

