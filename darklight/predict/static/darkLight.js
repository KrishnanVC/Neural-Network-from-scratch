let canvas = document.querySelector(".color");
let sliderRed = document.querySelector(".slider#red");
let sliderGreen = document.querySelector(".slider#green");
let sliderBlue = document.querySelector(".slider#blue");


sliderRed.addEventListener('input', () => {
    setColor();
});

sliderGreen.addEventListener('input', () => {
    setColor();
});

sliderBlue.addEventListener('input', () => {
    setColor();
});

function setColor() {
    fetch(`http://127.0.0.1:8000/predict/prediction?red=${sliderRed.value}&blue=${sliderBlue.value}&green=${sliderGreen.value}`)
        .then((res) => res.json())
        .then(res => {
            let color = res['val'];
            canvas.style.color = color == 1? "black" : "white";
        });
    canvas.style.backgroundColor = `rgb(${sliderRed.value},${sliderGreen.value},${sliderBlue.value})`;
}

// 1 - Dark
// 0 - Light
