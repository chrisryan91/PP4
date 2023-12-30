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
    var url2 = sessionStorage.getItem('modalURL');
    var titleElement = document.getElementById('recipe');

    if (label2 && titleElement) {
        titleElement.textContent = label2;
    }
});

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.pathname === '/submit_review/') {
        var urlInput = document.getElementById("id_url");
        var labelInput = document.getElementById("id_recipe");
        var storedUrl = sessionStorage.getItem("modalURL");
        var storedLabel = sessionStorage.getItem("modalLabel");
        var ingredientsArray = sessionStorage.getItem("wholeRecipe");

        if (urlInput && storedUrl) {
            urlInput.value = storedUrl;
        }

        if (labelInput && storedLabel) {
            labelInput.value = storedLabel;
        }
        
        const ingredientsList = document.getElementById("ingredients");
        ingredientsList.innerText = ingredientsArray.slice(0, -1) 
    }
});

$(document).ready(function () {
    $('#id_ingredients').select2();
    $('#id_utensils').select2();
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