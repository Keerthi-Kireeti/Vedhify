import "./globals.css";
import React from "react";

export const metadata = {
  title: "Vedhify",
  description: "Vedhify — Frontend",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-50 text-neutral-900">
        <header className="border-b bg-white/60 backdrop-blur sticky top-0 z-50">
          <div className="mx-auto max-w-4xl px-4 py-3">
            <h1 className="text-xl font-semibold">Vedhify</h1>
          </div>
        </header>
        <main className="mx-auto max-w-4xl px-4 py-8">{children}</main>
        <footer className="mx-auto max-w-4xl px-4 py-8 text-sm text-neutral-600">
          Built with Next.js
        </footer>
      </body>
    </html>
  );
}