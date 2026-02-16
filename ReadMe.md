# Campus CP Hub

Competitive programming tracker.

Features:
- LeetCode ratings
- Codeforces ratings
- Rating history storage

Run scraper:
cd scraper
python update_ratings.py



// Done till 


<!-- # ✅ Campus CP Hub — Phase-1 Completion Checklist

## 🟢 Database (Supabase)

* [x] Supabase project created
* [x] PostgreSQL connected successfully
* [x] Using pooler connection string (port 6543)
* [x] Tables created: `users`, `handles`, `ratings`
* [x] Foreign keys working
* [x] Data can be inserted & read
* [x] GitHub Actions can connect to DB

---

## 🟢 Scraper System

* [x] LeetCode scraper working
* [x] Codeforces scraper working
* [x] CodeChef scraper working
* [x] `update_ratings.py` runs all scrapers
* [x] Ratings stored in DB
* [x] Multiple users supported

Folder structure:

```
scraper/
 ├─ db.py
 ├─ leetcode.py
 ├─ codeforces.py
 ├─ codechef.py
 └─ update_ratings.py
```

---

## 🟢 Environment & Security

* [x] `.env` works locally
* [x] `.env` in `.gitignore`
* [x] `DATABASE_URL` stored in GitHub Secrets
* [x] Secrets not exposed in repo
* [x] requirements.txt working

---

## 🟢 GitHub Actions Automation

* [x] `.github/workflows/scraper.yml` created
* [x] Workflow runs successfully
* [x] Can run manually
* [x] Scraper runs in cloud
* [x] DB updates from GitHub Actions
* [x] No errors remaining

---

## 🟢 GitHub Repo Setup

* [x] Repo initialized
* [x] Code pushed
* [x] `.gitignore` configured
* [x] Clean folder structure
* [x] Secrets safe

---

# 🏁 PHASE-1 STATUS: COMPLETE

You now have:

* Cloud scraper
* Auto rating updates
* Database storage
* Multi-platform tracking
* Production-ready backend engine -->

/////////////////////////////////////////////////////////////////





//////////////////////////////////////////////////////////////////
 Next 

===============================
CAMPUS CP HUB — REMAINING WORK
FROM CURRENT STATE → FULL DEPLOY
===============================

CURRENT STATUS (ALREADY DONE)
- CF scraper done
- LC scraper done
- CodeChef scraper done
- Postgres DB connected
- ratings table storing history
- handles table working
- GitHub cron running daily
- Multi-platform rating updates working

You are AFTER Phase-2 backend.
Now remaining = visible product + deploy.

---------------------------------
PHASE 2 (FINAL) — LEADERBOARDS
---------------------------------
GOAL: Live multi-platform leaderboard pages

BACKEND
- Query latest rating per user per platform
- Calculate ranks
- Build APIs:
  /api/leaderboard/codeforces
  /api/leaderboard/leetcode
  /api/leaderboard/codechef
- Add filters:
  ?year=1
  ?search=name

FRONTEND
- Pages:
  /leaderboard/codeforces
  /leaderboard/leetcode
  /leaderboard/codechef
- Table columns:
  rank | name | rating | year
- Search bar
- Year filter dropdown

DONE WHEN:
Opening site shows real leaderboard from DB.

---------------------------------
PHASE 3 — PROFILE SYSTEM
---------------------------------
GOAL: Public user profiles

BACKEND
- API:
  /api/profile/[userId]
- Fetch:
  CF rating
  LC rating
  CC rating
  max rating
  rank
  handles

FRONTEND
- Page:
  /profile/[username]
- Show:
  ratings
  handles
  rank
  year

OPTIONAL (STRONG FOR RESUME)
- rating history graph
- stats cards

ALSO BUILD
- /dashboard page
User can:
  edit handles
  update year

---------------------------------
PHASE 4 — CONTEST CALENDAR
---------------------------------
GOAL: Show upcoming contests

BACKEND
- Fetch CF contests (API)
- Fetch LC contests
- Scrape CodeChef contests
- Store in contests table
- Cron every 6 hours

FRONTEND
- Page:
  /contests
- Show:
  upcoming contests list
  start time
  countdown

HOMEPAGE WIDGET
- Next contest countdown

---------------------------------
PHASE 5 — WEEKLY STATS
---------------------------------
GOAL: Top performers system

BACKEND
- Use rating history table
- Compute weekly rating gain
- Query top gainers

FRONTEND
- Homepage section:
  “Top Weekly Gainers”
- Show top 5 students

---------------------------------
PHASE 6 — YEAR FILTER + COLLEGE RANK
---------------------------------
GOAL: Batch competition

BACKEND
- Filter leaderboard by year
- Rank within year

FRONTEND
- Dropdown filter: 1st/2nd/3rd/4th year
- Show badge on profile:
  “Rank #3 in College”

---------------------------------
PHASE 7 — AUTH + JOIN FLOW
---------------------------------
GOAL: Users join CP club

BACKEND
- Google login
- email login
- save user record
- save handles
- validate handles
- prevent duplicates

FRONTEND
- Landing page
- Join form
- After login → /join
- Dashboard edit handles

---------------------------------
PHASE 8 — UI POLISH
---------------------------------
GOAL: Recruiter-ready UI

BUILD
- Landing page hero
- Features section
- leaderboard preview
- contest preview
- dark theme
- mobile responsive

---------------------------------
PHASE 9 — DEPLOYMENT
---------------------------------
GOAL: Public website

SETUP
- Vercel deploy frontend
- Backend API deploy (Next.js API or server)
- Supabase DB
- Env variables
- Domain
- GitHub cron already running

TEST
- Add user
- Cron updates
- Leaderboard updates
- Profile visible
- Contest page working

---------------------------------
FINAL PRODUCT WILL HAVE
---------------------------------
- Login + join system
- CF/LC/CC leaderboards
- Profiles
- Contest calendar
- Weekly gainers
- Year filters
- Rank badges
- Live deployed site

---------------------------------
REALISTIC TIMELINE
---------------------------------
Phase-2 finish: 3-4 days
Phase-3 profiles: 5 days
Phase-4 contests: 4 days
Phase-5 weekly stats: 3 days
Phase-6 filters: 2 days
Phase-7 auth: 3 days
UI polish: 4 days
Deploy: 2 days

TOTAL:
~25 days normal pace
~14 days intense mode

---------------------------------
WHAT YOU SHOULD BUILD NEXT
---------------------------------
START HERE:
Leaderboard API + Leaderboard UI

This completes Phase-2 officially.
Then move to profiles.


///////////////////////////////


========================================
PHASE-2 (FINAL) — PLATFORM LEADERBOARDS
========================================
Source: Project feature plan PDFs
Phase-2 = LC + CC ratings + leaderboard system fully working

You already completed:
- CF/LC/CC scrapers
- Cron updates
- Ratings stored in DB

So Phase-2 LEFT = visible leaderboard system

Goal of Phase-2 completion:
Live multi-platform leaderboard pages using stored ratings.

When Phase-2 is DONE you must have:
/leaderboard/codeforces
/leaderboard/leetcode
/leaderboard/codechef

========================================
STEP 1 — DATABASE CHECK (MANDATORY)
========================================
Ensure tables exist:

users
- id
- name
- email
- year

handles
- user_id
- platform (codeforces/leetcode/codechef)
- handle

ratings
- user_id
- platform
- rating
- max_rating
- fetched_at (timestamp)

IMPORTANT:
ratings must store history.
Do NOT overwrite old rows.

========================================
STEP 2 — LATEST RATING QUERY ENGINE
========================================
We need latest rating per user.

SQL logic:
For each user + platform → get latest row.

Pseudo query:
SELECT DISTINCT ON (user_id)
user_id, rating, max_rating
FROM ratings
WHERE platform='codeforces'
ORDER BY user_id, fetched_at DESC;

Then join with users table:
name, year.

Do this for:
- codeforces
- leetcode
- codechef

Create reusable function:
getLeaderboard(platform)

It should return:
rank, name, rating, year, user_id

Ranking logic:
Sort by rating DESC
Assign rank numbers

========================================
STEP 3 — LEADERBOARD API
========================================
Create API routes:

GET /api/leaderboard/codeforces
GET /api/leaderboard/leetcode
GET /api/leaderboard/codechef

Each returns:
[
 { rank:1, name:"Puneet", rating:1800, year:2 },
 { rank:2, name:"Rahul", rating:1700, year:3 }
]

Optional query params:
?year=2
?search=puneet

So final API supports:
- full leaderboard
- year filtered leaderboard
- search by name

========================================
STEP 4 — RANK CALCULATION
========================================
After fetching sorted users:

rank = index + 1

Store in response only.
Do NOT store rank in DB.

========================================
STEP 5 — FRONTEND PAGES
========================================
Create pages:

/leaderboard/codeforces
/leaderboard/leetcode
/leaderboard/codechef

Each page:
- calls API
- renders table

TABLE UI:
Rank | Name | Rating | Year

Add:
search input
year filter dropdown

Click name → go to profile page (Phase-3)

========================================
STEP 6 — HOMEPAGE PREVIEW
========================================
Homepage must show:

Top 5 CF
Top 5 LC
Top 5 CC

Also show:
“Join CP Club” button

This is required by feature doc.

========================================
STEP 7 — HANDLE VALIDATION API
========================================
When user adds handle:

validate before saving:
- CF handle exists
- LC handle exists
- CC handle exists

Reject invalid handles.

Prevents garbage data.

========================================
STEP 8 — CRON HARDENING
========================================
Your cron works.
Now make it production-safe:

Add try/except around each user.
If one fails → continue.

Add logs:
print(platform, handle, rating)

Skip insert if rating unchanged (already done)

========================================
STEP 9 — ERROR STATES
========================================
If user has no rating:
show "Unrated" in leaderboard.

If handle missing:
skip user.

========================================
STEP 10 — PHASE-2 COMPLETION CHECK
========================================
Phase-2 is DONE when:

1. Cron updates ratings daily
2. DB stores rating history
3. Leaderboard API works
4. Leaderboard UI visible
5. Multi-platform pages working
6. Filters working
7. Homepage preview exists

When all above done → Phase-2 complete.

========================================
EXPECTED OUTPUT OF PHASE-2
========================================
A visitor can open your site and see:

- Codeforces leaderboard
- LeetCode leaderboard
- CodeChef leaderboard
- Search users
- Filter by year
- View rankings

This matches:
Feature-2 Platform Leaderboards from PDF.

========================================
ESTIMATED TIME
========================================
DB queries + API: 1 day
Frontend leaderboard pages: 2 days
Filters + polish: 1 day

Total Phase-2 left: ~4 days

========================================
WHAT YOU SHOULD BUILD NEXT
========================================
Start with:
Leaderboard API → then UI

That officially finishes Phase-2.
========================================
