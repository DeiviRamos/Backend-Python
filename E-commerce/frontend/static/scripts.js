const lottieScript = document.createElement('script');
lottieScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.12.0/lottie.min.js';
document.head.appendChild(lottieScript);

lottieScript.onload = () => {
    lottie.loadAnimation({
        container: document.getElementById('lottie-animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'static/animation.json'
    });
};