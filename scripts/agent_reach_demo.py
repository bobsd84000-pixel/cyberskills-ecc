#!/usr/bin/env python3
"""Agent Reach demo with mock data showing Reddit/GitHub search results."""
import argparse
import json
from datetime import datetime

REDDIT_RESULTS = {
    "python agent": [
        {"title": "Python AI agent frameworks - comparison 2026", "subreddit": "Python", "score": 1240, "url": "reddit.com/r/Python/comments/abc123"},
        {"title": "Best practices for building autonomous agents", "subreddit": "MachineLearning", "score": 856, "url": "reddit.com/r/MachineLearning/comments/def456"},
        {"title": "Agent-based simulation libraries for Python", "subreddit": "learnprogramming", "score": 423, "url": "reddit.com/r/learnprogramming/comments/ghi789"},
    ],
    "golang concurrency": [
        {"title": "Goroutines vs OS threads - real world performance", "subreddit": "golang", "score": 2100, "url": "reddit.com/r/golang/comments/jkl012"},
        {"title": "Channel patterns for safe concurrent access", "subreddit": "golang", "score": 1890, "url": "reddit.com/r/golang/comments/mno345"},
    ],
    "rust memory": [
        {"title": "Understanding Rust's borrow checker - deep dive", "subreddit": "rust", "score": 3450, "url": "reddit.com/r/rust/comments/pqr678"},
        {"title": "Unsafe Rust - when and how to use it", "subreddit": "rust", "score": 2100, "url": "reddit.com/r/rust/comments/stu901"},
    ],
    "docker security": [
        {"title": "Docker container escape vectors - what to check", "subreddit": "docker", "score": 1780, "url": "reddit.com/r/docker/comments/vwx234"},
        {"title": "Rootless Docker in production - lessons learned", "subreddit": "devops", "score": 990, "url": "reddit.com/r/devops/comments/yza567"},
    ],
}

GITHUB_RESULTS = {
    "python agent": [
        {"title": "anthropics/claude-code", "stars": 12400, "url": "github.com/anthropics/claude-code", "lang": "Python"},
        {"title": "openai/swarm", "stars": 8950, "url": "github.com/openai/swarm", "lang": "Python"},
        {"title": "langchain-ai/langgraph", "stars": 7320, "url": "github.com/langchain-ai/langgraph", "lang": "Python"},
    ],
    "golang concurrency": [
        {"title": "golang/go", "stars": 124000, "url": "github.com/golang/go", "lang": "Go"},
        {"title": "uber-go/zap", "stars": 21500, "url": "github.com/uber-go/zap", "lang": "Go"},
    ],
    "rust memory": [
        {"title": "rust-lang/rust", "stars": 95800, "url": "github.com/rust-lang/rust", "lang": "Rust"},
        {"title": "tokio-rs/tokio", "stars": 27900, "url": "github.com/tokio-rs/tokio", "lang": "Rust"},
    ],
    "docker security": [
        {"title": "docker/docker-bench-security", "stars": 8600, "url": "github.com/docker/docker-bench-security", "lang": "Shell"},
        {"title": "aquasecurity/trivy", "stars": 24100, "url": "github.com/aquasecurity/trivy", "lang": "Go"},
    ],
}

def search(query, limit=10):
    query_lower = query.lower()

    # Match against demo queries
    matched_reddit = REDDIT_RESULTS.get(query_lower, [])[:limit]
    matched_github = GITHUB_RESULTS.get(query_lower, [])[:limit]

    return {
        "query": query,
        "timestamp": datetime.now().isoformat(),
        "reddit": matched_reddit,
        "github": matched_github,
    }

def main():
    parser = argparse.ArgumentParser(description="Agent Reach demo - search Reddit & GitHub")
    parser.add_argument("query", help="search keyword")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="output JSON")
    args = parser.parse_args()

    results = search(args.query, args.limit)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print(f"\n{'='*60}")
    print(f"Agent Reach: {args.query}")
    print(f"{'='*60}\n")

    print("📍 REDDIT")
    print("-" * 60)
    if results["reddit"]:
        for item in results["reddit"]:
            print(f"[{item['score']:>5}↑] r/{item['subreddit']}")
            print(f"    {item['title']}")
            print(f"    → {item['url']}\n")
    else:
        print("No results found.\n")

    print("📌 GITHUB")
    print("-" * 60)
    if results["github"]:
        for item in results["github"]:
            print(f"[{item['stars']:>6}★] {item['lang']}")
            print(f"    {item['title']}")
            print(f"    → {item['url']}\n")
    else:
        print("No results found.\n")

if __name__ == "__main__":
    main()
