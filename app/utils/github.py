import httpx

async def fetch_latest_commit(repo_url: str, token: str | None = None):
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]

        api_url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"

        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        async with httpx.AsyncClient() as client:
            r = await client.get(api_url, headers=headers)

        if r.status_code != 200:
            return None

        data = r.json()[0]

        return {
            "message": data["commit"]["message"],
            "sha": data["sha"],
            "url": data["html_url"],
        }

    except:
        return None