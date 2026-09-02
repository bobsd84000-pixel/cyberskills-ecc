#!/usr/bin/env python3
"""Scraper Reddit (praw) + GitHub (PyGithub) par mot-cle.

Credentials via variables d'environnement:
  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
  GITHUB_TOKEN
"""
import argparse
import os

import praw
from github import Github


def search_reddit(query, limit=10):
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ.get("REDDIT_USER_AGENT", "agent_reach/1.0"),
    )
    results = []
    for submission in reddit.subreddit("all").search(query, limit=limit):
        results.append({
            "title": submission.title,
            "url": f"https://reddit.com{submission.permalink}",
            "score": submission.score,
            "subreddit": str(submission.subreddit),
        })
    return results


def search_github(query, limit=10):
    token = os.environ.get("GITHUB_TOKEN")
    gh = Github(token) if token else Github()
    results = []
    try:
        for repo in gh.search_repositories(query=query)[:limit]:
            results.append({
                "title": repo.full_name,
                "url": repo.html_url,
                "stars": repo.stargazers_count,
            })
    except Exception as e:
        results.append({"error": str(e)})
    return results


def main():
    parser = argparse.ArgumentParser(description="Recherche Reddit + GitHub")
    parser.add_argument("query", help="mot-cle a rechercher")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    print(f"=== Reddit ({args.query}) ===")
    for item in search_reddit(args.query, args.limit):
        print(f"[{item['score']:>5}] r/{item['subreddit']} - {item['title']}")
        print(f"        {item['url']}")

    print(f"\n=== GitHub ({args.query}) ===")
    for item in search_github(args.query, args.limit):
        print(f"[{item['stars']:>5}★] {item['title']}")
        print(f"        {item['url']}")


if __name__ == "__main__":
    main()
