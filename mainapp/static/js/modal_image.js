// Modal images
const imageReports = document.querySelectorAll('.image_reports'),
      modalImage = document.querySelector('.modal_images');

imageReports.forEach(function(imageReport) {
    imageReport.addEventListener('click', function() {
        const imageUrl = this.getAttribute('data-image'),
              modalImg = document.getElementById('modalImage');
        modalImg.src = imageUrl;
        modalImage.style.display = 'flex';
    });
});

modalImage.addEventListener('click', function(event) {
    if (event.target === modalImage) {
        modalImage.style.display = 'none';
    }
});

document.querySelectorAll(".report_form").forEach(function(form) {
    form.addEventListener("submit", function() {
            document.querySelector(".modal_loading").style.display = "flex";
    });
});
