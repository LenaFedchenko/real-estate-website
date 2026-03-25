
const input = document.querySelector('input[name="images"]');
const preview = document.getElementById('preview');

input.addEventListener('change', () => {
    preview.innerHTML = "";

    Array.from(input.files).forEach(file => {
        if (!file.type.startsWith("image/")) return;

        const reader = new FileReader();

        reader.onload = e => {
            const img = document.createElement("img");
            img.src = e.target.result;
            preview.appendChild(img);
        };

        reader.readAsDataURL(file);
    });
});
