<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script id="cookieyes" type="text/javascript"
        src="https://cdn-cookieyes.com/client_data/9f0569a235dfe95c90b4dd96/script.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"
        rel="stylesheet">
    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', 'G-4KZJ2XHGQB');
    </script>
    <x-seo::meta />

    @vite('resources/css/app.css')
    @vite('resources/js/app.js')
</head>

<body class="bg-gray-50 min-h-screen>
    @include('layout.header')

    <main>
        @yield('content')
    </main>
    @include('layout.footer')
</body>

</html>
