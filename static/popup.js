document.addEventListener("DOMContentLoaded", () => {
    const popup = document.getElementById("popup");
    const popupImg = document.getElementById("popup-img");
    const popupText = document.getElementById("popup-text");

    /* ======================
       1. 선생님 사진 팝업
       ====================== */
    const teacher = document.getElementById("teacher-photo");
    if (teacher && popup && popupImg && popupText) {
        teacher.addEventListener("click", () => {
            popupImg.style.display = "block";
            popupImg.src = teacher.src;
            popupText.textContent = "지도교사 한지민 선생님입니다.";
            popup.style.display = "flex";
        });
    }

    /* ======================
       2. 작품 클릭 팝업
          - 이미지 영역(.art-img) 클릭
          - 제목/설명 크게 보기
       ====================== */
    const artImgs = document.querySelectorAll(".art-img");
    artImgs.forEach((box) => {
        box.addEventListener("click", () => {
            const card = box.closest(".art-card");
            if (!card) return;

            const titleEl = card.querySelector(".art-title");
            const descEl = card.querySelector(".art-desc");

            const title = titleEl ? titleEl.textContent.trim() : "";
            const desc = descEl ? descEl.textContent.trim() : "";

            // 작품은 실제 이미지가 아직 없으므로, 텍스트 중심으로 표시
            popupImg.style.display = "none";  // 이미지 영역 숨김
            popupImg.src = "";
            popupText.textContent = `${title}\n\n${desc}`;
            popup.style.display = "flex";
        });
    });

    /* ======================
       3. 팝업 닫기
          - 배경 클릭
          - ESC 키
       ====================== */
    if (popup) {
        popup.addEventListener("click", (e) => {
            if (e.target === popup) {
                popup.style.display = "none";
            }
        });

        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") {
                popup.style.display = "none";
            }
        });
    }

    /* ======================
       4. 좋아요 버튼 토글
          - 처음 클릭: +1
          - 다시 클릭: -1
       ====================== */
    const likeButtons = document.querySelectorAll(".like-btn");
    likeButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const liked = btn.getAttribute("data-liked") === "true";

            // 버튼 텍스트에서 숫자 읽기
            const text = btn.textContent;
            const match = text.match(/(\d+)/);
            let count = match ? parseInt(match[1], 10) : 0;

            if (!liked) {
                count += 1;
                btn.setAttribute("data-liked", "true");
            } else {
                count = Math.max(0, count - 1);
                btn.setAttribute("data-liked", "false");
            }

            btn.textContent = `❤️ 좋아요 ${count}`;
        });
    });
});
