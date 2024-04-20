
document.addEventListener('DOMContentLoaded', function() {
    var forms = document.querySelectorAll('.form-operation_group');

    forms.forEach(function(form, index) {
        var selectedDeal = form.querySelector('.selectedDeal');
        var selectedDealNameInput = form.querySelector('[id^=selectedDealName]');
        var dealSearchInput = form.querySelector('[id^=dealSearch]');
        var searchResults = form.querySelector('[id^=searchResults]');

        selectedDeal.addEventListener('change', function() {
            var selectedOption = selectedDeal.options[selectedDeal.selectedIndex];
            var selectedOptionValue = selectedOption.getAttribute('data-option-value');

            selectedDealNameInput.value = selectedOptionValue;
            dealSearchInput.value = selectedOption.innerText;
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
        });

        dealSearchInput.addEventListener('input', function() {
            var searchText = dealSearchInput.value.toLowerCase();
            var options = selectedDeal.options;
            var searchResultsHTML = '';

            for (var i = 0; i < options.length; i++) {
                var optionText = options[i].innerText.toLowerCase();
                if (optionText.includes(searchText)) {
                    searchResultsHTML += '<div class="search-result-option" data-value="' + options[i].value + '">' + options[i].innerText + '</div>';
                }
            }

            if (searchResultsHTML) {
                searchResults.innerHTML = searchResultsHTML;
                searchResults.style.display = 'block';
            } else {
                searchResults.innerHTML = '';
                searchResults.style.display = 'none';
            }
        });

        // Handle click on search results
        searchResults.addEventListener('click', function(event) {
            if (event.target.classList.contains('search-result-option')) {
                var selectedValue = event.target.getAttribute('data-value');
                var selectedOption = selectedDeal.querySelector('option[value="' + selectedValue + '"]');
                var selectedOptionValue = selectedOption.getAttribute('data-option-value');

                selectedDeal.value = selectedValue;
                selectedDealNameInput.value = selectedOptionValue;
                dealSearchInput.value = event.target.innerText;
                searchResults.innerHTML = '';
                searchResults.style.display = 'none';
            }
        });

        // Close modal when clicked outside
        document.addEventListener('click', function(event) {
            var isClickInsideModal = searchResults.contains(event.target);
            var isInputField = event.target === dealSearchInput;
            if (!isClickInsideModal && !isInputField) {
                searchResults.innerHTML = '';
                searchResults.style.display = 'none';
            }
        });
    });
});




document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('counterpartyForm');
    var selectedCounterparty = form.querySelector('.selectedCounterparty');
    var selectedCounterpartyNameInput = form.querySelector('#selectedCounterpartyName');

    selectedCounterparty.addEventListener('change', function() {
        var selectedOption = selectedCounterparty.options[selectedCounterparty.selectedIndex];
        var selectedOptionValue = selectedOption.innerText;

        selectedCounterpartyNameInput.value = selectedOptionValue;
    });
});





// loading
document.getElementById('report_form').addEventListener('submit', function() {
    document.querySelector('.modal_loading').style.display = 'flex';
  })