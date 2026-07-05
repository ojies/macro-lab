import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "macro-lab · dashboard",
  description:
    "Five poles of the debt cycle — Nigeria, US, Europe, China, Japan. Live from the macro-lab models.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
