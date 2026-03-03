const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const previewBtn = document.getElementById("previewBtn");
const imageBox = document.getElementById("imageBox");

previewBtn.addEventListener("click", function(){

    if (!imageInput.files.length) {
        alert("Please upload an image first");
        return;
    }

    const file = imageInput.files[0];

    preview.src = URL.createObjectURL(file);
    imageBox.style.display = "block";
});