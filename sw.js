/* Metabolic engineering module service worker — offline shell */
const CACHE = "me-55-v24";
const CORE = [
  "./",
  "./index.html",
  "./start-here.html",
  "./course-ui.css",
  "./course-ui.js",
  "./course-data.js",
  "./diagnostic.html",
  "./metabolic-engineering-tracker.html",
  "./search.html",
  "./search-index.json",
  "./manifest.webmanifest",
  "./favicon.svg",
  "./AUDIT.md",
  "./MASTERY.md",
  "./VALIDATION.md",
  "./practice/README.md"
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE).then((c) => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;

  // HTML: network first, cache fallback. Assets: cache first.
  if (event.request.mode === "navigate" || url.pathname.endsWith(".html")) {
    event.respondWith(
      fetch(event.request)
        .then((r) => {
          const copy = r.clone();
          caches.open(CACHE).then((c) => c.put(event.request, copy));
          return r;
        })
        .catch(() => caches.match(event.request).then((r) => r || caches.match("./index.html")))
    );
  } else {
    event.respondWith(
      caches.match(event.request).then((r) => r || fetch(event.request).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(event.request, copy));
        return res;
      }))
    );
  }
});
