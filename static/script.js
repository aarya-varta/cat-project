async function getCat() {
    const response = await fetch("/random-cat");
    const data = await response.json();

    document.getElementById("fact").innerText = data.fact;

    const img = document.getElementById("cat-img");
    img.src = data.image + "?t=" + new Date().getTime(); // avoid caching
    
}