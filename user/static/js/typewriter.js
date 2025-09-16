document.addEventListener("DOMContentLoaded", function() {
    const el = document.querySelector('.speech-bubble p');
    if (!el) return;
    const text = el.textContent;
    el.textContent = '';
    let i = 0;
    function typeWriter() {
        if (i < text.length) {
            el.textContent += text.charAt(i);
            i++;
            setTimeout(typeWriter, 35);
        }
    }
    typeWriter();
});
