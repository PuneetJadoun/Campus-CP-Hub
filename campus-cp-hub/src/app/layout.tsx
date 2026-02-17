import type { Metadata } from "next";
import "../styles/global.css";

export const metadata: Metadata = {
  title: "Campus CP Hub",
  description: "Campus Competitive Programming Hub",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
