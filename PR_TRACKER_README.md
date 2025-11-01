# Pull Request Tracker

This directory contains tools to track and list all accepted (merged) pull requests from the forked repository.

## Files

- **`accepted_prs.txt`**: Output file containing all accepted PRs in the required format
- **`get_accepted_prs.py`**: Python script to fetch and format accepted PRs

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
python3 get_accepted_prs.py
```

The script will output the formatted list to stdout. To save it to a file:
```bash
python3 get_accepted_prs.py 2>/dev/null > accepted_prs.txt
```

### Script Modes

The script supports two modes:

1. **GitHub CLI Mode** (if `gh` is authenticated):
   - Automatically fetches PRs using `gh pr list`
   - Requires GH_TOKEN environment variable in CI/CD

2. **Manual Mode** (fallback):
   - Uses pre-collected PR data
   - Works without authentication
   - Update `get_manual_pr_data()` function when new PRs are merged

## Current Accepted PRs

As of the last update, the following PRs have been merged:

- **PR #1**: Add README.md for Maheshwar Anup bootcamp submissions
  - Contains all 9 muLearn x OWASP Kerala Cybersecurity Bootcamp tasks
  - Tasks: 1, 2, 3, 4, 5, 6, 7, 8, 9
  - URL: https://github.com/djmahe4/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/1

## Requirements

- Python 3.x
- GitHub CLI (`gh`) - optional, for automatic PR fetching
