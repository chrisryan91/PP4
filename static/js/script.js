document.addEventListener('DOMContentLoaded', function() {
    var cardDivs = document.querySelectorAll('.card');

    cardDivs.forEach(function(cardDiv) {
        cardDiv.addEventListener('mouseover', function(event) {
            var label = cardDiv.querySelector('.text').textContent;
            var url = cardDiv.querySelector('a[href]').getAttribute('href');

            sessionStorage.setItem('modalLabel', label);
            sessionStorage.setItem('modalURL', url);
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var label2 = sessionStorage.getItem('modalLabel');
    var url2 = sessionStorage.getItem('modalURL');
    var titleElement = document.getElementById('title');

    if (label2 && titleElement) {
        titleElement.textContent = label2;
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Check if the script should run on the current page
    if (window.location.pathname === '/submit_review/') {
        var urlInput = document.getElementById("id_url");
        var labelInput = document.getElementById("id_title");
        var storedUrl = sessionStorage.getItem("modalURL");
        var storedLabel = sessionStorage.getItem("modalLabel");

        if (urlInput && storedUrl) {
            urlInput.value = storedUrl;
        }

        if (labelInput && storedLabel) {
            labelInput.value = storedLabel;
        }
    }
});