import httpx

async def fetch_repo_stats(repo_url: str, token: str | None = None):
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]

        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        async with httpx.AsyncClient() as client:
            repo_details = await client.get(
                f"https://api.github.com/repos/{owner}/{repo}",
                headers=headers,
            )

            if repo_details.status_code != 200:
                return None

            repo_json = repo_details.json()
            stars = repo_json.get("stargazers_count", 0)
            forks = repo_json.get("forks_count", 0)

            pulls = await client.get(
                f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all",
                headers=headers,
            )
            prs = len(pulls.json()) if pulls.status_code == 200 else 0

            issues_resp = await client.get(
                f"https://api.github.com/repos/{owner}/{repo}/issues?state=all",
                headers=headers,
            )
            issues = len(issues_resp.json()) if issues_resp.status_code == 200 else 0

            commits_resp = await client.get(
                f"https://api.github.com/repos/{owner}/{repo}/commits",
                headers=headers,
            )
            commits = len(commits_resp.json()) if commits_resp.status_code == 200 else 0

            return {
                "stars": stars,
                "forks": forks,
                "prs": prs,
                "issues": issues,
                "commits": commits,
            }

    except:
        return None