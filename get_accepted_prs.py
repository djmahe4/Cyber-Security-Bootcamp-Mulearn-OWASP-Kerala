#!/usr/bin/env python3
"""
Script to list accepted PRs from the parent repository in the required format.
This version uses hardcoded data collected from the GitHub API.
"""

import re

# PR data collected from gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala
# These are all merged PRs by djmahe4
prs_data = [
    {
        "number": 426,
        "title": "Added Tasks 6-9",
        "url": "https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/426",
        "merged_at": "2025-11-01T15:10:31Z",
        # Based on title, this PR contains tasks 6, 7, 8, and 9
        "tasks": [6, 7, 8, 9]
    },
    {
        "number": 315,
        "title": "Added tasks 4 and 5",
        "url": "https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/315",
        "merged_at": "2025-08-29T17:42:30Z",
        # Based on title, this PR contains tasks 4 and 5
        "tasks": [4, 5]
    },
    {
        "number": 205,
        "title": "Added task3",
        "url": "https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/205",
        "merged_at": "2025-08-09T17:32:35Z",
        # Based on title, this PR contains task 3
        "tasks": [3]
    },
    {
        "number": 70,
        "title": "Add my contribution file",
        "url": "https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/70",
        "merged_at": "2025-07-17T15:06:20Z",
        # Based on title, this PR contains task 2 (need to verify)
        "tasks": [2]
    },
    {
        "number": 12,
        "title": "Add my contribution file",
        "url": "https://github.com/gtech-mulearn/Cyber-Security-Bootcamp-Mulearn-OWASP-Kerala/pull/12",
        "merged_at": "2025-07-10T06:25:11Z",
        # Based on title, this PR contains task 1 (first contribution)
        "tasks": [1]
    }
]

def main():
    results = []
    
    # Process each PR and generate output for each task
    for pr in prs_data:
        pr_url = pr["url"]
        tasks = pr["tasks"]
        
        for task_id in tasks:
            results.append(f"#cl-cybersec-owaspbootcamp{task_id} {pr_url}")
    
    # Sort results by task ID
    results.sort(key=lambda x: int(re.search(r'owaspbootcamp(\d+)', x).group(1)))
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
