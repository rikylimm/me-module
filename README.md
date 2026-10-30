# Study Tracker

A self-contained, single-file study tracker for a 66-week curriculum across 19 modules and 5 problem sets. Everything runs in `study-tracker.html` — no build step, no server, no install.

## What's here

- `study-tracker.html` — the app. Open it in any modern browser.
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
2. Open the hosted `study-tracker.html`.
3. On each device, find the **"Where your files live"** card in the sidebar, and paste the hosted folder address, for example:

   ```
   https://<your-user>.github.io/<repo>/
   ```

   Then every PDF link on every device loads from that address.

### Progress does not sync by itself

Ticks are stored by each browser separately. When you switch devices:

1. On the device you worked on, use **Export backup** at the foot of the page.
2. On the other device, use **Import backup** with that file.

## Privacy note

This repo is public so GitHub Pages can serve the files for free and from any device. That means the modules and the answer key in `problem-data/ANSWERS_do_not_open_first.json` are publicly viewable by anyone with the link. If you'd rather keep them private, you'll need a paid GitHub plan (GitHub Pages on a private repo), or keep the folder local and share it only with your own devices.
