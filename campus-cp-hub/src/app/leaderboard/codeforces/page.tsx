"use client";

import { useEffect, useState } from "react";

type User = {
  rank: number;
  user_id: number;
  name: string;
  rating: number;
  year: number;
};

export default function Page() {
  const [data, setData] = useState<User[]>([]);

  useEffect(() => {
    fetch("/api/leaderboard/codeforces")
      .then(res => res.json())
      .then(setData);
  }, []);

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        Codeforces Leaderboard
      </h1>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-200">
            <th>Rank</th>
            <th>Name</th>
            <th>Rating</th>
            <th>Year</th>
          </tr>
        </thead>

        <tbody>
          {data.map((u) => (
            <tr key={u.user_id}>
              <td>{u.rank}</td>
              <td>{u.name}</td>
              <td>{u.rating}</td>
              <td>{u.year}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
