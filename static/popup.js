// 작품 카드 클릭 시 팝업으로 크게 보여주는 스크립트
document.addEventListener("DOMContentLoaded", () => {
  const popup = document.getElementById("artwork-popup");
  if (!popup) return; // 이 페이지에 팝업이 없으면 종료

  const popupImageBox = popup.querySelector(".popup-image-box");
  const popupImageLabel = document.getElementById("popup-image-label");
  const popupText = document.getElementById("popup-text");
  const closeBtn = popup.querySelector(".popup-close");

  // 학생 페이지에서 넘겨준 작품 데이터
  const dataList = window.artworksData || [];

  // 작품 카드들
  const cards = document.querySelectorAll(".artwork-card");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      const idx = parseInt(card.dataset.artworkIndex, 10) || 0;
      const data = dataList[idx] || null;

      if (!data) {
        popupImageLabel.textContent = "작품 이미지";
        popupText.textContent = "";
      } else {
        // 이미지 파일을 이후에 사용하고 싶으면 여기에서 <img> 생성해서 붙이면 됨
        const label =
          data.placeholder_label ||
          (data.no ? data.no + "번 작품 (이미지 자리)" : "작품 이미지");

        // 현재는 이미지 대신 텍스트 라벨만 표시
        popupImageLabel.textContent = label;
        popupText.textContent = data.description || "";
      }

      popup.classList.add("open");
    });
  });

  const closePopup = () => {
    popup.classList.remove("open");
  };

  // 닫기 버튼
  if (closeBtn) {
    closeBtn.addEventListener("click", closePopup);
  }

  // 오버레이 클릭 시 닫기
  popup.addEventListener("click", (e) => {
    if (e.target === popup) {
      closePopup();
    }
  });
});
