function showModal(label, url) {
    console.log('Showing modal', label);
    console.log(url);
    document.getElementById('id01').style.display = 'block';
    document.getElementById('modalHeader').innerHTML = label;

    var urlElement = document.getElementById('modalURL');
    var linkElement = document.createElement('a');
    linkElement.href = url;
    linkElement.innerHTML = "Visit Recipe";


    sessionStorage.setItem('modalLabel', label);
    sessionStorage.setItem('modalURL', url);


    urlElement.innerHTML = "";
    urlElement.appendChild(linkElement);
}

function hideModal() {
    console.log('Hiding modal');
    document.getElementById('id01').style.display = 'none';
}


document.addEventListener('DOMContentLoaded', function() {
    var label = sessionStorage.getItem('modalLabel');
    var url = sessionStorage.getItem('modalURL');
    var titleElement = document.getElementById('title');

    if (label && titleElement) {
        titleElement.textContent = label;
    }
});

document.addEventListener("DOMContentLoaded", function() {
                var urlInput = document.getElementById("id_url");
                var labelInput = document.getElementById("id_title");
                var storedUrl = sessionStorage.getItem("modalURL");
                var storedLabel = sessionStorage.getItem("modalLabel");
    
                if (storedUrl) {
                    urlInput.value = storedUrl;
                }

                if (storedLabel) {
                    labelInput.value = storedLabel;
                }
            });