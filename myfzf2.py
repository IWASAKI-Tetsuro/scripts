import sys
import difflib
import os

# 標準入力から候補を読み込む
candidates = [line.strip() for line in sys.stdin if line.strip()]

tty_path = '/dev/tty'
if not os.path.exists(tty_path):
    print("Error: No TTY available.", file=sys.stderr)
    sys.exit(1)

with open(tty_path, 'r') as tty:
    print("Enter query (Ctrl-D to exit):", file=sys.stderr)
    query = tty.readline()
    if not query:
        # ユーザーがCtrl-D等で入力しなかった
        print("Error: No query provided.", file=sys.stderr)
        sys.exit(1)
    query = query.strip()
    if not query:
        print("Error: Empty query.", file=sys.stderr)
        sys.exit(1)

    matches = difflib.get_close_matches(query, candidates, n=10, cutoff=0.1)
    if matches:
        print("Matches:", file=sys.stderr)
        for i, m in enumerate(matches, 1):
            print(f"{i}: {m}", file=sys.stderr)
        print("Select a candidate number (Ctrl-D to cancel):", file=sys.stderr)

        selection = tty.readline()
        if not selection:
            print("Error: No selection made.", file=sys.stderr)
            sys.exit(1)

        selection = selection.strip()
        if not selection.isdigit():
            print("Error: Invalid selection (not a number).", file=sys.stderr)
            sys.exit(1)

        sel_idx = int(selection) - 1
        if sel_idx < 0 or sel_idx >= len(matches):
            print("Error: Invalid selection (out of range).", file=sys.stderr)
            sys.exit(1)

        # 選択された候補のみ標準出力へ
        chosen = matches[sel_idx]
        print(chosen)  # stdoutへ出力
    else:
        print("Error: No matches found.", file=sys.stderr)
        sys.exit(1)

