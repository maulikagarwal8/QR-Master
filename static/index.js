document.addEventListener("DOMContentLoaded", () => {
    const genButton = document.querySelector(".gen1");
    const upButton = document.querySelector(".up1");
    const genForm = document.querySelector(".gen");
    const readQRForm = document.querySelector(".readqr");

    // Hide both forms initially
    genForm.classList.remove("visible");
    readQRForm.classList.remove("visible");

    // Show Generate QR form
    genButton.addEventListener("click", () => {
        genForm.classList.add("visible");
        readQRForm.classList.remove("visible");
    });

    // Show Upload QR form
    upButton.addEventListener("click", () => {
        readQRForm.classList.add("visible");
        genForm.classList.remove("visible");
    });
});
