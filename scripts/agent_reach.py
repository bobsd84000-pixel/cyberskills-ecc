#!/usr/bin/env python3
"""Agent Reach — search GitHub live with token."""
import argparse
import os
import json
import urllib.request
import urllib.parse
import sys


def search_github(query, limit=10):
    """Search GitHub API with optional token."""
    token = os.environ.get("GITHUB_TOKEN")
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.github.com/search/repositories?q={encoded_query}&per_page={limit}&sort=stars"

    results = []
    try:
        req = urllib.request.Request(url)
        if token:
            req.add_header("Authorization", f"token {token}")
        req.add_header("Accept", "application/vnd.github.v3+json")

        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            for repo in data.get("items", []):
                results.append({
                    "title": repo["full_name"],
                    "url": repo["html_url"],
                    "stars": repo["stargazers_count"],
                    "lang": repo.get("language", "Unknown"),
                })
    except urllib.error.HTTPError as e:
        print(f"GitHub API error ({e.code}): {e.reason}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

    return results


def main():
    parser = argparse.ArgumentParser(description="Agent Reach - search GitHub")
    parser.add_argument("query", help="search keyword")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    results = search_github(args.query, args.limit)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print(f"\n{'='*60}")
    print(f"Agent Reach: {args.query}")
    print(f"{'='*60}\n")

    print("📌 GITHUB")
    print("-" * 60)
    if results:
        for item in results:
            print(f"[{item['stars']:>6}★] {item['lang']}")
            print(f"    {item['title']}")
            print(f"    → {item['url']}\n")
    else:
        print("No results found.\n")


if __name__ == "__main__":
    main()
