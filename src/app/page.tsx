import React from "react";

export default function HomePage() {
  return (
    <div className="space-y-6">
      <section className="rounded-lg border p-6 bg-white shadow-sm">
        <h2 className="text-2xl font-semibold">Welcome to Vedhify</h2>
        <p className="mt-2 text-neutral-700">
          This is a small frontend shell built to run with your repository files.
          It uses the Next.js App Router and TailwindCSS (configured).
        </p>
      </section>

      <section className="grid gap-4 sm:grid-cols-2">
        <div className="rounded-lg border p-4 bg-white">
          <h3 className="font-medium">Quick actions</h3>
          <ul className="mt-3 space-y-2 text-neutral-700">
            <li>• Run the dev server: npm run dev</li>
            <li>• Open: http://localhost:3000</li>
          </ul>
        </div>

        <div className="rounded-lg border p-4 bg-white">
          <h3 className="font-medium">Notes</h3>
          <p className="mt-2 text-neutral-700">
            The loader referenced in next.config.ts is present as a simple
            passthrough. If you add more features or component libraries, add
            their files under src/ and export them from components or ui
            folders as needed.
          </p>
        </div>
      </section>
    </div>
  );
}