const cityFilter = document.querySelector("#cityFilter");

if (cityFilter) {
    cityFilter.addEventListener("change", function () {
        cityFilter.form.submit();
    });
}
