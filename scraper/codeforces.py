import requests

def get_cf_rating(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"

    try:
        res = requests.get(url, timeout=10)
        data = res.json()
    except Exception as e:
        print("API error:", e)
        return None

    if data.get("status") != "OK":
        return None

    user = data["result"][0]

    rating = user.get("rating", 0)
    max_rating = user.get("maxRating", rating)

    return rating, max_rating
    