// 지도교사 사진 클릭 시 팝업 열기
document.addEventListener("DOMContentLoaded", () => {
  const teacherBox = document.querySelector(".teacher-box");
  const popup = document.getElementById("teacher-popup");
  if (!teacherBox || !popup) return;

  const closeBtn = popup.querySelector(".popup-close");

  const open = () => popup.classList.add("open");
  const close = () => popup.classList.remove("open");

  teacherBox.addEventListener("click", open);

  if (closeBtn) {
    closeBtn.addEventListener("click", close);
  }

  // 바깥(어두운 영역) 클릭 시 닫기
  popup.addEventListener("click", (e) => {
    if (e.target === popup) {
      close();
    }
  });
});

