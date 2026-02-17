import { supabase } from "@/lib/supabase";

export async function fetchLeaderboard(platform: string) {
  const { data, error } = await supabase.rpc("get_leaderboard", {
    p_platform: platform,
  });

  if (error) {
    console.error(error);
    return [];
  }

  return data;
}