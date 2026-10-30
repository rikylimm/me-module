# Study Tracker

A self-contained, single-file study tracker for a 66-week curriculum across 19 modules and 5 problem sets. Everything runs in `study-tracker.html` — no build step, no server, no install.

## What's here

- `index.html` — the landing page.
- `study-tracker.html` — the app. Open it in any modern browser.
- `sync.html` — cloud sync (carry your progress between devices).
- `favicon.svg` — the site icon.
- `module-01` … `module-19` — the reading modules (PDF).
- `problems-01` … `problems-05` — the problem sets (PDF).
- `problem-data/` — CSV data files and the answer key the problems rely on.
- `lookup-workbook.xlsx`, `reading-list-by-tier.pdf`, `reading-map-by-week.pdf`, `curriculum-66-weeks-56-problems.pdf` — quick-reference materials.
- `setup-multi-device.pdf` — the original setup guide.

## Quick start (one device)

1. Download or clone this repo.
2. Open `study-tracker.html` in your browser.
3. Keep every file in the same folder (including `problem-data/`) and all the links work as-is.

Your ticks/progress are stored in that browser's local storage. They stay on that device unless you back them up (see below).

## Access from several devices (anywhere)

The tracker is already wired for this. Host this folder once and point every device at it:

1. Host the folder (this repo has GitHub Pages enabled).
2. Open the hosted site: `https://<your-user>.github.io/<repo>/` (it shows a landing page).
3. The PDF links resolve relative to the page, so they load from the same address on every device.

## Cloud sync (carry progress between devices)

Progress is stored by each browser separately. To move it between devices, open `sync.html` (or click **Cloud sync** on the landing page) and choose one backend:

- **Secret gist** — simplest. Generate a fine-grained GitHub token with only **Gists: Read and write**, paste it into `sync.html`, and click **Create a secret gist for me**. Then **Sync and open tracker**.
- **Private repository** — genuinely private. Create a private repo (e.g. `me-sync`), grant the token **Contents: Read and write** on that repo only, enter `owner/repo` in `sync.html`, then sync.

The sync page merges two devices' state safely (later edits win per field). Use **Force push/pull** only when you're sure one side should win.

> You can still use **Export backup / Import backup** at the foot of the tracker as a manual fallback.

## Privacy note

This repo is public so GitHub Pages can serve the files for free and from any device. That means the modules and the answer key in `problem-data/ANSWERS_do_not_open_first.json` are publicly viewable by anyone with the link. If you'd rather keep them private, you'll need a paid GitHub plan (GitHub Pages on a private repo), or keep the folder local and share it only with your own devices.
