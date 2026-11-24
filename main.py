"""One Word, One Username, One Reward — entry for make.fun.

Writes one word to /output/entry.txt.
The entry is the entrant's own make.fun username and nothing else: one word, at most 30 characters.
"""
import os

LINE = "barongz1"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
