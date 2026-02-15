import requests

def get_leetcode_rating(username):
    url = "https://leetcode.com/graphql"

    query = """
    query getUser($username: String!) {
      userContestRanking(username: $username) {
        rating
      }
      userContestRankingHistory(username: $username) {
        rating
        attended
      }
    }
    """

    variables = {"username": username}

    res = requests.post(url, json={"query": query, "variables": variables})
    data = res.json()

    ranking = data.get("data", {}).get("userContestRanking")

    if not ranking:
        return None

    rating = int(ranking["rating"])

    history = data["data"]["userContestRankingHistory"]
    max_rating = max([h["rating"] for h in history if h["attended"]], default=rating)

    return rating, int(max_rating)
