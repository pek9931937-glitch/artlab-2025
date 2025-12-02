document.addEventListener("DOMContentLoaded", () => {
    /* 1. 선생님 사진 팝업 */
    const teacher = document.getElementById("teacher-photo");
    const popup = document.getElementById("popup");
    const popupImg = document.getElementById("popup-img");

    if (teacher && popup && popupImg) {
        teacher.addEventListener("click", () => {
            popup.style.display = "flex";
            popupImg.src = teacher.src;
        });

        popup.addEventListener("click", () => {
            popup.style.display = "none";
        });
    }

    /* 2. 좋아요 버튼 토글 */
    const likeButtons = document.querySelectorAll(".like-btn");
    likeButtons.forEach((btn) => {
        btn.addEventListener("click", (event) => {
            event.stopPropagation(); // 카드 클릭 이벤트와 분리
            const countSpan = btn.querySelector(".like-count");
            let count = parseInt(countSpan.textContent, 10);
            const liked = btn.getAttribute("data-liked") === "true";

            if (liked) {
                count -= 1;
                btn.setAttribute("data-liked", "false");
                btn.classList.remove("liked");
            } else {
                count += 1;
                btn.setAttribute("data-liked", "true");
                btn.classList.add("liked");
            }
            countSpan.textContent = String(count);
        });
    });

    /* 3. 작품 클릭 시 큰 팝업 (이미지 + 설명) */
    const artCards = document.querySelectorAll(".art-card");
    const artPopup = document.getElementById("art-popup");
    const artPopupImg = document.getElementById("art-popup-img");
    const artPopupTitle = document.getElementById("art-popup-title");
    const artPopupDesc = document.getElementById("art-popup-desc");

    if (artPopup && artPopupImg && artPopupTitle && artPopupDesc) {
        artCards.forEach((card) => {
            const imgBox = card.querySelector(".art-img");

            if (!imgBox) return;

            imgBox.addEventListener("click", () => {
                const artText = card.getAttribute("data-art") || imgBox.textContent;
                const titleText = card.getAttribute("data-title") || "";
                const descText = card.getAttribute("data-desc") || "";

                artPopupImg.textContent = artText;
                artPopupTitle.textContent = titleText;
                artPopupDesc.textContent = descText;

                artPopup.style.display = "flex";
            });
        });

        artPopup.addEventListener("click", () => {
            artPopup.style.display = "none";
        });
    }
});
