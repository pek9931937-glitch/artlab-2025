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
       2. 작품 클릭 팝업 (제목+설명 크게)
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

            popupImg.style.display = "none";  // 작품 실이미지는 아직 없으므로 텍스트로만
            popupImg.src = "";
            popupText.textContent = `${title}\n\n${desc}`;
            popup.style.display = "flex";
        });
    });

    /* ======================
       3. 팝업 닫기
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
       4. 좋아요 - IP + DB 연동
       ====================== */
    const likeButtons = document.querySelectorAll(".like-btn");
    const studentId = document.body.dataset.studentId;

    // 페이지 로드 시 서버에서 현재 좋아요 상태 가져오기
    if (studentId && likeButtons.length > 0) {
        fetch(`/api/likes/${encodeURIComponent(studentId)}`)
            .then((res) => res.json())
            .then((data) => {
                const counts = data.counts || {};
                const myLikes = data.my_likes || {};
                likeButtons.forEach((btn) => {
                    const artNum = parseInt(btn.dataset.art, 10);
                    const count = counts[artNum] || 0;
                    const liked = !!myLikes[artNum];
                    btn.textContent = `❤️ 좋아요 ${count}`;
                    btn.dataset.liked = liked ? "true" : "false";
                });
            })
            .catch((err) => {
                console.error("like init error", err);
            });
    }

    // 버튼 클릭 시 서버에 토글 요청
    likeButtons.forEach((btn) => {
        btn.addEventListener("click", () => {
            const artNum = btn.dataset.art;
            if (!studentId || !artNum) return;

            fetch("/api/like", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    student_id: studentId,
                    art_num: artNum,
                }),
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.error) {
                        console.error("like error", data.error);
                        return;
                    }
                    const count = data.count ?? 0;
                    const liked = !!data.liked;
                    btn.textContent = `❤️ 좋아요 ${count}`;
                    btn.dataset.liked = liked ? "true" : "false";
                })
                .catch((err) => {
                    console.error("like toggle error", err);
                });
        });
    });
});
