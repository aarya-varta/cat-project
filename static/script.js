const btn = document.getElementById("cat-btn");
const card = document.getElementById("card");

btn.addEventListener("click", async () => {
    btn.innerText = "Loading... 😼";
    btn.disabled = true;

    try {
        const res = await fetch("/random-cat");
        const data = await res.json();

        document.getElementById("fact").innerText = data.fact;

        const img = document.getElementById("cat-img");
        img.src = data.image + "?t=" + new Date().getTime();

        card.classList.remove("hidden");

    } catch (err) {
        alert("Something broke 😿");
    }

    btn.innerText = "Another one 😺";
    btn.disabled = false;
});