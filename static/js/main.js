const msgPositive = document.querySelector('.alert-success');

if (msgPositive || msgPositive) {
    setTimeout(() =>  {
        msgPositive.style.display = 'none';
    }, 4000);
}


// Hover input auth
const inputAuth = document.querySelectorAll(".form-control"),
      btnSubmit = document.querySelector(".btn_submit");
    
inputAuth.forEach((el) => {
  el.addEventListener("input", () => {
    if (el.value.trim() !== "") {
      el.style.border = "2px solid var(--main_color)";
    } else {
      el.style.border = "2px solid var(--warning)";
    }
    el.style.transitionDuration = "0.1s";
  });
});


// Mobile menu
const mobileMenu = document.getElementById('mobileMenu'),
      headerModal = document.getElementById('header');

mobileMenu.addEventListener('click', () => {
  headerModal.classList.add('active_modile_icon')
})

document.addEventListener('click', (event) => {
  const isClickInsideHeader = headerModal.contains(event.target),
        isClickInsideMobileMenu = mobileMenu.contains(event.target);
      
  if (!isClickInsideHeader && !isClickInsideMobileMenu) {
      headerModal.classList.remove('active_modile_icon');
  }
});