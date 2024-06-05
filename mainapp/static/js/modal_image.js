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


// Modal comments
const btnModalComments = document.querySelectorAll('.modalComments'),
      modalComments = document.querySelectorAll('.wrapper-modal_comment'),
      btnCloseModal = document.querySelector('.btn_close_comment');


btnModalComments.forEach(function(btn) {
    btn.addEventListener('click', function () {
        const commentId = btn.getAttribute('data-comment-id'),
              modalComment = document.getElementById(commentId);
        
        if (modalComment) {
            modalComment.style.display = 'block';
        }
    });
});

modalComments.forEach(function(modal) {
    const btnCloseModal = modal.querySelector('.btn_close_comment');
    if (btnCloseModal) {
        btnCloseModal.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }
});


// Modal comments
document.addEventListener('DOMContentLoaded', function() {
    const rejectButtons = document.querySelectorAll('.btn__valid_reports');

    rejectButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const operationId = button.getAttribute('data-operation-id');
            const modal = document.getElementById(`modal-comment-${operationId}`);
            if (modal) {
                modal.style.display = 'flex';
            }
        });
    });

    const closeModalButtons = document.querySelectorAll('.close-modal');

    closeModalButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const modal = button.closest('.wrapper-comment');
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });

    window.onclick = function(event) {
        const modals = document.querySelectorAll('.wrapper-comment');
        modals.forEach(function(modal) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    }
});
