from db import get_connection
from leetcode import get_leetcode_rating
from codeforces import get_cf_rating

def update_ratings():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id, platform, handle FROM handles")
    users = cur.fetchall()

    for user_id, platform, handle in users:
        print(f"\nFetching {platform} → {handle}")

        if platform == "leetcode":
            result = get_leetcode_rating(handle)

        elif platform == "codeforces":
            result = get_cf_rating(handle)

        else:
            continue

        if not result:
            print("No rating found")
            continue

        rating, max_rating = result

        # check last stored rating
        cur.execute("""
            SELECT rating FROM ratings
            WHERE user_id=%s AND platform=%s
            ORDER BY fetched_at DESC LIMIT 1
        """, (user_id, platform))

        last = cur.fetchone()

        if last and last[0] == rating:
            print("No rating change")
            continue

        cur.execute("""
            INSERT INTO ratings (user_id, platform, rating, max_rating)
            VALUES (%s, %s, %s, %s)
        """, (user_id, platform, rating, max_rating))

        print(f"Saved {platform} rating → {rating}")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    update_ratings()
