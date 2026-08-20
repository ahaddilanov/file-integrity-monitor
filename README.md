# 🔒 File Integrity Monitor

A lightweight Python security tool that detects unauthorized changes to files by comparing cryptographic hashes over time — the same core technique used by real-world tools like Tripwire and OSSEC.

![Python](https://img.shields.io/badge/Python-3.14-blue) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 What It Does

File Integrity Monitoring is a foundational security technique: instead of trying to detect *how* an attacker (or accidental corruption) changed a file, you simply detect **that** it changed at all — and investigate from there.

This tool:

1. **Scans** a folder and generates a SHA-256 cryptographic hash ("fingerprint") for every file inside it
2. **Saves** that snapshot as a baseline (`baseline.json`)
3. **Re-scans** on demand and compares the new hashes against the saved baseline
4. **Reports** exactly which files were **modified**, **newly added**, or **deleted**
5. Presents everything through a clean, custom-built **Tkinter GUI** — no command-line usage required

---

## 🖥️ Screenshot

<img width="417" height="301" alt="image" src="https://github.com/user-attachments/assets/806f309b-1517-4cca-9094-b37c6851b36c" />


---

## ⚙️ How It Works

At its core, this tool relies on one simple but powerful idea: **a hash function**.

A hash function takes any file's contents and produces a fixed-length string of characters (the "hash"). Change even a single character in the file, and the resulting hash is *completely* different. This makes hashes ideal for tamper detection — two identical files always produce identical hashes, and no two different files (realistically) ever produce the same one.

```
"Balance: 500"  →  SHA-256  →  a3f5e8c1...e91c
"Balance: 900"  →  SHA-256  →  7d02b4f6...4b8f
```

By saving a hash "baseline" today and comparing it against a fresh scan later, the tool can prove — mathematically, not just by eyeballing file sizes or timestamps — whether a file's contents have been altered.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later ([download here](https://www.python.org/downloads/))
- No external libraries required — everything used (`hashlib`, `os`, `json`, `tkinter`) ships built into Python

### Installation

```bash
git clone https://github.com/ahaddilanov/file-integrity-monitor.git
cd file-integrity-monitor
```

### Running the App

```bash
python autofileintegritymonitor.py
```

A window will open with two buttons:

| Button | What it does |
|---|---|
| **Save Baseline** | Hashes every file in the current folder and saves the results to `baseline.json` |
| **Check for Changes** | Re-hashes the folder and compares it against the saved baseline, reporting any modified, new, or deleted files |

---

## 🧠 Design Choices

A few decisions worth explaining — both for anyone reading this code, and as a record of what I learned building it:

- **SHA-256 over MD5:** MD5 is faster but cryptographically broken (collisions are easy to engineer). SHA-256 is the current standard for integrity verification and is what real tools use.
- **JSON for the baseline file:** Human-readable, easy to inspect/debug manually, and Python has built-in support via the `json` module — no extra dependencies.
- **Excluding `baseline.json` from its own scan:** Early on, the tool was accidentally hashing its own baseline file as part of the folder scan, causing it to flag itself as "modified" on every run. Fixed by explicitly skipping `baseline.json` during scanning — a good reminder that a tool's own output files need to be treated differently from its input.
- **Tkinter for the GUI:** Ships with Python (no install friction for anyone running this), and is more than capable for a focused two-button interface like this one.

---

## 📚 What I Learned

- How cryptographic hash functions work and why they're one-way and collision-resistant
- Reading/writing files in binary vs. text mode, and why it matters for hashing
- Structuring a program's logic (hashing, saving, comparing) separately from its interface (GUI), so each could be tested independently
- Working with dictionaries to map filenames to hashes, and comparing two dictionaries to detect differences
- Building a GUI with Tkinter — widgets, layout, and connecting button clicks to functions
- Using Git and GitHub for real version control, including commit messages that describe *why* a change was made, not just *what*

---

## 🔮 Possible Future Improvements

- [ ] "Restore" button to revert a modified file back to its last known-good baseline copy
- [ ] Support monitoring nested subfolders, not just the top-level folder
- [ ] Scheduled/automatic scans instead of manual button clicks
- [ ] Export scan results to a log file with timestamps
- [ ] Desktop notification when a change is detected

---

## 📄 License

MIT — free to use, modify, and learn from.

---

*Built as part of a personal cybersecurity portfolio project of mine.
