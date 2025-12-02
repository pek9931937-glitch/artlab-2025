// 작품 카드 클릭 → 팝업 열고, 설명만 크게 보여주는 스크립트
document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.getElementById("popup-overlay");
  const descEl = document.getElementById("popup-description");
  const closeBtn = document.querySelector(".popup-close");

  // 카드 안 이미지 영역 클릭 시
  document.querySelectorAll(".artwork-image-box").forEach((box) => {
    box.addEventListener("click", () => {
      const artNo = box.dataset.artworkNo;
      if (popupData && popupData[artNo]) {
        descEl.textContent = popupData[artNo];
      } else {
        descEl.textContent = "";
      }
      overlay.classList.add("visible");
    });
  });

  // 닫기 버튼
  closeBtn.addEventListener("click", () => {
    overlay.classList.remove("visible");
  });

  // 배경 클릭 시 닫기
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
      overlay.classList.remove("visible");
    }
  });
});
