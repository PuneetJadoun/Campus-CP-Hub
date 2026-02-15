from db import get_connection
from leetcode import get_leetcode_rating

def update_leetcode():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id, handle FROM handles WHERE platform='leetcode'")
    users = cur.fetchall()

    for user_id, handle in users:
        print(f"Fetching {handle}")

        result = get_leetcode_rating(handle)
        if not result:
            print("No rating found")
            continue

        rating, max_rating = result

        # check last stored rating
        cur.execute("""
            SELECT rating FROM ratings
            WHERE user_id=%s AND platform='leetcode'
            ORDER BY fetched_at DESC LIMIT 1
        """, (user_id,))
        last = cur.fetchone()

        if last and last[0] == rating:
            print("No change in rating")
            continue

        cur.execute("""
            INSERT INTO ratings (user_id, platform, rating, max_rating)
            VALUES (%s, %s, %s, %s)
        """, (user_id, "leetcode", rating, max_rating))

        print(f"Saved new rating {rating}")

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    update_leetcode()
