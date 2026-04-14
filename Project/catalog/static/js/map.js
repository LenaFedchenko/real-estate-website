document.addEventListener("DOMContentLoaded", function () {
    const frame = document.getElementById("mapFrame");

    if (typeof propertyAddress !== "undefined") {
        // Кодуємо адресу для URL
        const query = encodeURIComponent(propertyAddress);

        // Google Maps embed
        frame.src = `https://www.google.com/maps?q=${query}&output=embed`;
    }
});