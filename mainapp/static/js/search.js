document.addEventListener('DOMContentLoaded', function() {
    var dealInputField = document.getElementById('selectedDeal');
    var dealPopup = document.getElementById('dealPopup');
    var counterpartyInputField = document.getElementById('selectedCounterparty');
    var counterpartyPopup = document.getElementById('counterpartyPopup');

    dealInputField.addEventListener('input', function() {
        var inputValue = dealInputField.value.trim().toLowerCase();
        if (inputValue.length > 0) {
            dealPopup.style.display = 'block';
            filterOptions(inputValue, dealPopup);
        } else {
            dealPopup.style.display = 'none';
        }
    });

    counterpartyInputField.addEventListener('input', function() {
        var inputValue = counterpartyInputField.value.trim().toLowerCase();
        if (inputValue.length > 0) {
            counterpartyPopup.style.display = 'block';
            filterOptions(inputValue, counterpartyPopup);
        } else {
            counterpartyPopup.style.display = 'none';
        }
    });

    function filterOptions(inputValue, popup) {
        var items = popup.getElementsByClassName('popup-item');
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            var value = item.getAttribute('data-value').toLowerCase();
            if (value.includes(inputValue)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        }
    }

    function handlePopupItemClick(target, inputField, popup) {
        if (target.classList.contains('popup-item')) {
            inputField.value = target.getAttribute('data-value');
            popup.style.display = 'none';
        }
    }

    dealPopup.addEventListener('click', function(event) {
        handlePopupItemClick(event.target, dealInputField, dealPopup);
    });

    counterpartyPopup.addEventListener('click', function(event) {
        handlePopupItemClick(event.target, counterpartyInputField, counterpartyPopup);
    });

    function hidePopupOnBlur(inputField, popup) {
        inputField.addEventListener('blur', function() {
            setTimeout(function() {
                popup.style.display = 'none';
            }, 200);
        });
    }

    hidePopupOnBlur(dealInputField, dealPopup);
    hidePopupOnBlur(counterpartyInputField, counterpartyPopup);

    function hidePopupOnEscape(inputField, popup) {
        inputField.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                popup.style.display = 'none';
            }
        });
    }

    hidePopupOnEscape(dealInputField, dealPopup);
    hidePopupOnEscape(counterpartyInputField, counterpartyPopup);
});
