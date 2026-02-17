import { NextResponse } from "next/server";
import { getLeaderboard } from "@/controllers/leaderboardController";

export async function GET(
  req: Request,
  context: { params: Promise<{ platform: string }> }
) {
  const { platform } = await context.params;

  const data = await getLeaderboard(platform);
  return NextResponse.json(data);
}
