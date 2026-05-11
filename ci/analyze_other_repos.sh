#!/usr/bin/env bash
set -e
# repos to analyze
REPOS=(
  "https://github.com/tapas100/flexgate-proxy"
  "https://github.com/tapas100/forgeops"
)
for repo in "${REPOS[@]}"; do
  echo "Analyzing $repo"
  python3 /home/forgeops/tools/repo-analyze.py "$repo" --mem --send || echo "Failed to analyze $repo"
done
