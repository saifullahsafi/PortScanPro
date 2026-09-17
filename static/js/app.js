document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const button = document.querySelector("button[type='submit']");

    if (form && button) {

        form.addEventListener("submit", function () {

            const startPort = parseInt(
                document.querySelector("input[name='start_port']").value
            );

            const endPort = parseInt(
                document.querySelector("input[name='end_port']").value
            );

            if (startPort > endPort) {
                alert("Start port must be less than end port.");
                return;
            }

            button.disabled = true;
            button.textContent = "SCANNING...";
        });
    }

});