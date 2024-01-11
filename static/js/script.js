/*jshint esversion: 6 */
/*jshint esversion: 6, jquery: true */
/*jshint esversion: 6, browser: true */
/*global bootstrap:false */

document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname === '/search/')  {
        var cardDivs = document.querySelectorAll('.card');
    
        cardDivs.forEach(function(cardDiv) {
            cardDiv.addEventListener('mouseover', function(event) {
                var label = cardDiv.querySelector('.text').textContent;
                var url = cardDiv.querySelector('a[href]').getAttribute('href');
                var image = cardDiv.querySelector('img').getAttribute('src');
    
    
                sessionStorage.setItem('modalLabel', label);
                sessionStorage.setItem('modalURL', url);
                sessionStorage.setItem('modalImg', image);
            });
        });
    }
});


document.addEventListener('DOMContentLoaded', function() {
    if (window.location.pathname === '/search/')  {
        var label2 = sessionStorage.getItem('modalLabel');
        var titleElement = document.getElementById('recipe');

        if (label2 && titleElement) {
            titleElement.textContent = label2;
        }
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/submit_review/') {
        var urlInput = document.getElementById("id_url");
        var labelInput = document.getElementById("id_recipe");
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

$(document).ready(function () {
        $('#id_ingredients').select2();

        $('#id_utensils').select2();

        $('#id_cuisine_type').select2();
});

$(document).ready(function() {
        $('#ingredientInput').select2({
            tags: true,
            tokenSeparators: [','],
            placeholder: 'Enter ingredients',
        });

        $('form').submit(function() {
            var selectedIngredients = $('#ingredientInput').val();
            $('#ingredientQuery').val(selectedIngredients.join(','));
        });
});

setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 1500);