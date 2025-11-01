# Pull Request Tracker

This directory contains tools to track and list all accepted (merged) pull requests from the **parent repository** `gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala`.

## Files

- **`accepted_prs.txt`**: Output file containing all accepted PRs from the parent repo in the required format
- **`get_accepted_prs.py`**: Python script to list and format accepted PRs by djmahe4

## Format

Each line in `accepted_prs.txt` follows the format:
```
#cl-cybersec-owaspbootcamp<task_id> <pull_request_url>
```

## Usage

### Viewing Accepted PRs

Simply view the `accepted_prs.txt` file:
```bash
cat accepted_prs.txt
```

### Regenerating the List

Run the Python script to regenerate the list of accepted PRs:
```bash
python3 get_accepted_prs.py > accepted_prs.txt
```

## Current Accepted PRs

As of November 2025, the following PRs have been merged to the parent repository:

- **PR #12**: Add my contribution file (Task 1)
  - Merged: 2025-07-10
  - URL: https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/12

- **PR #70**: Add my contribution file (Task 2)
  - Merged: 2025-07-17
  - URL: https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/70

- **PR #205**: Added task3 (Task 3)
  - Merged: 2025-08-09
  - URL: https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/205

- **PR #315**: Added tasks 4 and 5 (Tasks 4 & 5)
  - Merged: 2025-08-29
  - URL: https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/315

- **PR #426**: Added Tasks 6-9 (Tasks 6, 7, 8 & 9)
  - Merged: 2025-11-01
  - URL: https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/426

## Requirements

- Python 3.x
- No external dependencies required
