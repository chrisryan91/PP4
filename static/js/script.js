document.addEventListener('DOMContentLoaded', function() {
    var cardDivs = document.querySelectorAll('.card');

    cardDivs.forEach(function(cardDiv) {
        cardDiv.addEventListener('mouseover', function(event) {
            var label = cardDiv.querySelector('.text').textContent;
            var wholeRecipe = cardDiv.querySelector('.wholerecipe').textContent;
            var url = cardDiv.querySelector('a[href]').getAttribute('href');
            var image = cardDiv.querySelector('img').getAttribute('src');


            sessionStorage.setItem('modalLabel', label);
            sessionStorage.setItem('wholeRecipe', wholeRecipe);
            sessionStorage.setItem('modalURL', url);
            sessionStorage.setItem('modalImg', image);
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    var label2 = sessionStorage.getItem('modalLabel');
    var titleElement = document.getElementById('recipe');

    if (label2 && titleElement) {
        titleElement.textContent = label2;
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/submit_review/') {
        var urlInput = document.getElementById("id_url");
        var labelInput = document.getElementById("id_recipe");
        var imgInput = document.getElementById('id_featured_image_b');
        var storedUrl = sessionStorage.getItem("modalURL");
        var storedLabel = sessionStorage.getItem("modalLabel");
        var storedImg = sessionStorage.getItem("modalImg");

        if (urlInput && storedUrl) {
            urlInput.value = storedUrl;
        }

        if (labelInput && storedLabel) {
            labelInput.value = storedLabel;
        }

        if (imgInput && storedImg) {
            imgInput.value = storedImg;
        }
    }
});

$(document).ready(function () {
    $('#id_ingredients').select2();
    console.log("consoled")
    $('#id_utensils').select2();
    $('#id_cuisine_type').select2();
});

$(document).ready(function() {
    $('#ingredientInput').select2({
        tags: true,
        tokenSeparators: [','],
        placeholder: 'Enter single ingredient and press enter!',
    });

    $('form').submit(function() {
        var selectedIngredients = $('#ingredientInput').val();
        $('#ingredientQuery').val(selectedIngredients.join(','));
    });
});

$(document).ready(function() {
    $('#id_new_ingredient').select2({
        tags: true,
        tokenSeparators: [','],
        placeholder: 'Enter new ingredient and press enter!',
    });

    $('form').submit(function() {
        var newIngredients = $('#id_new_ingredient').val();
        $('#id_new_ingredient').val(newIngredients.join(','));
    });
});