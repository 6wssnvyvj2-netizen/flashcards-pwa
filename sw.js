const CACHE_NAME = "flashcards-brainscape-v1";
const ASSETS = [
  "/",
  "/index.html",
  "/manifest.json",
  "/cards.json" 
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(resp => {
      // Return cached file if found, otherwise fetch from network
      return resp || fetch(event.request);
    })
  );
});
