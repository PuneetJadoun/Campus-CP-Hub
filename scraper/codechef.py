import requests
from bs4 import BeautifulSoup

def get_cc_rating(handle):
    url = f"https://www.codechef.com/users/{handle}"

    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(res.text, "html.parser")

        rating_div = soup.find("div", class_="rating-number")
        if not rating_div:
            print("Rating not found")
            return None

        rating = int(rating_div.text.strip())

        # highest rating
        highest = soup.find("small")
        max_rating = rating
        if highest and "Highest Rating" in highest.text:
            try:
                max_rating = int(highest.text.split()[-1].replace(")", ""))
            except:
                pass

        return rating, max_rating

    except Exception as e:
        print("CodeChef error:", e)
        return None
