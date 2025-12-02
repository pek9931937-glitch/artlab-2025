// 작품 카드 클릭 시 팝업으로 크게 보여주는 스크립트
document.addEventListener("DOMContentLoaded", () => {
  const popup = document.getElementById("artwork-popup");
  if (!popup) return; // 메인 페이지에서는 실행 안 함

  const popupImageLabel = document.getElementById("popup-image-label");
  const popupText = document.getElementById("popup-text");
  const closeBtn = popup.querySelector(".popup-close");

  const cards = document.querySelectorAll(".artwork-card");
  const dataList = window.artworksData || [];

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const idx = parseInt(card.dataset.artworkIndex, 10) || 0;
      const data = dataList[idx] || null;

      if (data) {
        const label =
          data.placeholder_label ||
          (data.no ? data.no + "번 작품 (이미지 자리)" : "작품 이미지");

        popupImageLabel.textContent = label;
        popupText.textContent = data.description || "";
      } else {
        popupImageLabel.textContent = "작품 이미지";
        popupText.textContent = "";
      }

      popup.classList.add("open");
    });
  });

  const closePopup = () => popup.classList.remove("open");

  if (closeBtn) {
    closeBtn.addEventListener("click", closePopup);
  }

  popup.addEventListener("click", (e) => {
    if (e.target === popup) {
      closePopup();
    }
  });
});
