const form = document.getElementById("registerForm");

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {

        const response = await fetch("http://127.0.0.1:8000/register", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        document.getElementById("message").textContent =
            JSON.stringify(data);

    } catch (error) {

        document.getElementById("message").textContent =
            "Error: " + error;

    }

});