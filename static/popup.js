document.addEventListener("DOMContentLoaded", () => {
    const teacher = document.getElementById("teacher-photo");
    const popup = document.getElementById("popup");
    const popupImg = document.getElementById("popup-img");

    teacher.addEventListener("click", () => {
        popup.style.display = "flex";
        popupImg.src = teacher.src;
    });

    popup.addEventListener("click", () => {
        popup.style.display = "none";
    });
});

