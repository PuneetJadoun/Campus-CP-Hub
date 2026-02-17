import { fetchLeaderboard } from "@/models/leaderboardModel";

export async function getLeaderboard(platform: string) {
  const data = await fetchLeaderboard(platform);

  return data.map((u: any, i: number) => ({
    rank: i + 1,
    ...u,
  }));
}
