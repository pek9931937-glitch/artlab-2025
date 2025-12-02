// 지도교사 사진 클릭 시 팝업 열기
document.addEventListener("DOMContentLoaded", () => {
  const teacherBox = document.querySelector(".teacher-box");
  const popup = document.getElementById("teacher-popup");
  if (!teacherBox || !popup) return;

  const closeBtn = popup.querySelector(".popup-close");

  const open = () => popup.classList.add("open");
  const close = () => popup.classList.remove("open");

  // 지도교사 사진 클릭 → 팝업 열기
  teacherBox.addEventListener("click", (e) => {
    e.stopPropagation();
    open();
  });

  // X 버튼 클릭 → 닫기
  if (closeBtn) {
    closeBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      close();
    });
  }

  // 팝업 전체(배경 + 안쪽 내용) 클릭 → 닫기
  popup.addEventListener("click", () => {
    close();
  });
});
