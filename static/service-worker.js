self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('restaurant-v1').then((cache) => {
            return cache.addAll([
                '/',
                '/static/styles.css',
                '/static/images/header-bg.jpg'
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});