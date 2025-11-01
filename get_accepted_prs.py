#!/usr/bin/env python3
"""
Script to fetch all accepted (merged) pull requests from the repository
and format them in the required format: #cl-cybersec-owaspbootcamp<task_id> <pull_request_url>

This script can work in two modes:
1. With GitHub CLI (gh) if GH_TOKEN is set
2. Manual mode using pre-fetched data
"""

import json
import re
import sys
import subprocess
import os


def fetch_pull_requests_gh(owner, repo):
    """Fetch all pull requests from the repository using GitHub CLI"""
    try:
        # Use gh CLI to fetch PRs
        result = subprocess.run(
            ['gh', 'pr', 'list', '--repo', f'{owner}/{repo}', '--state', 'all', '--json', 
             'number,title,body,url,mergedAt', '--limit', '100'],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"GitHub CLI not available or not authenticated: {e}", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        return None


def get_manual_pr_data():
    """Return manually collected PR data"""
    # This data was collected from GitHub API
    return [
        {
            "number": 1,
            "title": "Add README.md for Maheshwar Anup bootcamp submissions",
            "body": """Creates a README.md for the "Maheshwar Anup" directory documenting all 9 muLearn x OWASP Kerala Cybersecurity Bootcamp task submissions.

## Changes
- Added README.md with task descriptions, hashtags, karma points, and PDF links for all 9 tasks
- Linked to existing task PDFs: `file.pdf` (Task 1), `task2.pdf` through `task9.pdf`, and `Task_5.pdf` (Task 5)
- Included external resource links for tasks 4, 6, and 9
- Total karma documented: 2,250 points

Task 1 - Hashtag: #cl-cybersec-owaspbootcamp1
Task 2 - Hashtag: #cl-cybersec-owaspbootcamp2
Task 3 - Hashtag: #cl-cybersec-owaspbootcamp3
Task 4 - Hashtag: #cl-cybersec-owaspbootcamp4
Task 5 - Hashtag: #cl-cybersec-owaspbootcamp5
Task 6 - Hashtag: #cl-cybersec-owaspbootcamp6
Task 7 - Hashtag: #cl-cybersec-owaspbootcamp7
Task 8 - Hashtag: #cl-cybersec-owaspbootcamp8
Task 9 - Hashtag: #cl-cybersec-owaspbootcamp9
""",
            "url": "https://github.com/djmahe4/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/1",
            "mergedAt": "2025-10-27T18:09:41Z"
        }
    ]


def extract_task_ids_from_text(text):
    """Extract task IDs from hashtags in the text"""
    if not text:
        return []
    
    # Pattern to match hashtags like #cl-cybersec-owaspbootcamp1, #cl-cybersec-owaspbootcamp2, etc.
    pattern = r'#cl-cybersec-owaspbootcamp(\d+)'
    matches = re.findall(pattern, text)
    return sorted(set(matches), key=int)


def main():
    owner = "djmahe4"
    repo = "Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala"
    
    print("Fetching pull requests...", file=sys.stderr)
    
    # Try GitHub CLI first if available
    prs = fetch_pull_requests_gh(owner, repo)
    
    # Fall back to manual data if GitHub CLI is not available
    if prs is None:
        print("Using manually collected PR data...", file=sys.stderr)
        prs = get_manual_pr_data()
    
    if not prs:
        print("No pull requests found.", file=sys.stderr)
        return
    
    print(f"Found {len(prs)} pull requests total", file=sys.stderr)
    
    # Filter for merged/accepted PRs and extract task information
    results = []
    
    for pr in prs:
        # Check if PR is merged (accepted)
        if pr.get('mergedAt'):
            pr_url = pr.get('url')
            pr_title = pr.get('title', '')
            pr_body = pr.get('body', '')
            pr_number = pr.get('number')
            
            # Extract task IDs from title and body
            task_ids = extract_task_ids_from_text(pr_title + ' ' + pr_body)
            
            if task_ids:
                for task_id in task_ids:
                    results.append(f"#cl-cybersec-owaspbootcamp{task_id} {pr_url}")
            else:
                # If no specific task ID found, report the PR anyway
                print(f"Warning: PR #{pr_number} has no task ID hashtags", file=sys.stderr)
    
    # Sort results by task ID
    results.sort(key=lambda x: int(re.search(r'owaspbootcamp(\d+)', x).group(1)))
    
    # Print results
    print("\n=== Accepted Pull Requests ===", file=sys.stderr)
    for result in results:
        print(result)
    
    print(f"\nTotal accepted PRs with task IDs: {len(results)}", file=sys.stderr)


if __name__ == "__main__":
    main()
