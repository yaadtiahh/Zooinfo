const placeholderText = "Search here!";
const input = document.getElementById("animated-input");
let currentText = "";
let index = 0;

function typePlaceholder() {
    if (index < placeholderText.length) {
        currentText += placeholderText[index];
        input.setAttribute("placeholder", currentText);
        index++;
        setTimeout(typePlaceholder, 100); // Скорость набора текста (в миллисекундах)
    }
}

// Запускаем анимацию при загрузке страницы
typePlaceholder();