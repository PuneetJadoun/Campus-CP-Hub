"use client";

import { useEffect, useState } from "react";

type User = {
  rank: number;
  user_id: number;
  name: string;
  rating: number;
  year: number;
};

export default function CodechefLeaderboard() {
  const [data, setData] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/leaderboard/codechef")
      .then(res => res.json())
      .then(res => {
        setData(res);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  if (loading) {
    return <div className="p-10 text-xl">Loading CodeChef leaderboard...</div>;
  }

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        CodeChef Leaderboard
      </h1>

      <table className="w-full border border-gray-300">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2 border">Rank</th>
            <th className="p-2 border">Name</th>
            <th className="p-2 border">Rating</th>
            <th className="p-2 border">Year</th>
          </tr>
        </thead>

        <tbody>
          {data.length === 0 ? (
            <tr>
              <td colSpan={4} className="p-4 text-center">
                No users found
              </td>
            </tr>
          ) : (
            data.map((u) => (
              <tr key={u.user_id}>
                <td className="p-2 border">{u.rank}</td>
                <td className="p-2 border">{u.name}</td>
                <td className="p-2 border">{u.rating}</td>
                <td className="p-2 border">{u.year}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
