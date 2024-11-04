// script.js

let canvas, context, paint;
let clickX = [], clickY = [], clickDrag = [];

function startCanvas() {
    canvas = document.getElementById("canvas");
    context = canvas.getContext("2d");

    context.strokeStyle = "#000000";
    context.lineJoin = "round";
    context.lineWidth = 8;

    canvas.addEventListener("touchstart", function (e) {
        var touch = e.touches[0];
        var mouseEvent = new MouseEvent("mousedown", {
            clientX: touch.clientX,
            clientY: touch.clientY,
        });
        canvas.dispatchEvent(mouseEvent);
    });

    canvas.addEventListener("touchmove", function (e) {
        var touch = e.touches[0];
        var mouseEvent = new MouseEvent("mousemove", {
            clientX: touch.clientX,
            clientY: touch.clientY,
        });
        canvas.dispatchEvent(mouseEvent);
    });

    canvas.addEventListener("touchend", function (e) {
        var mouseEvent = new MouseEvent("mouseup");
        canvas.dispatchEvent(mouseEvent);
    });

    $('#canvas').mousedown(function (e) {
        paint = true;
        addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, false);
        drawCanvas();
    });

    $('#canvas').mousemove(function (e) {
        if (paint) {
            addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
            drawCanvas();
        }
    });

    $('#canvas').mouseup(function (e) {
        paint = false;
        drawCanvas();
    });

    $('#canvas').mouseleave(function (e) {
        paint = false;
    });
}

function addClick(x, y, dragging) {
    clickX.push(x);
    clickY.push(y);
    clickDrag.push(dragging);
}

function clearCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);
}

function resetCanvas() {
    clickX = [];
    clickY = [];
    clickDrag = [];
    clearCanvas();
}

function drawCanvas() {
    clearCanvas();
    for (let i = 0; i < clickX.length; i++) {
        context.beginPath();
        if (clickDrag[i] && i) {
            context.moveTo(clickX[i - 1], clickY[i - 1]);
        } else {
            context.moveTo(clickX[i] - 1, clickY[i]);
        }
        context.lineTo(clickX[i], clickY[i]);
        context.closePath();
        context.stroke();
    }
}

function getPixels() {
    let rawPixels = context.getImageData(0, 0, canvas.width, canvas.height).data;
    let _pixels = [];
    let pixels = [];

    for (let i = 0; i < rawPixels.length; i += 4) {
        _pixels.push(rawPixels[i + 3]);
    }

    for (let i = 0; i < _pixels.length; i += 800) {
        for (let j = 0; j < 200; j += 4) {
            pixels.push(_pixels[i + j]);
        }
    }

    return pixels;
}

function practiceAction() {
    let pixels = getPixels();

    // Send pixel data via AJAX to server
    $.ajax({
        url: '/your-recognition-endpoint', // Replace with your server endpoint
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ pixels: pixels }),
        success: function(response) {
            // Assuming the server returns recognized characters in a 'text' field
            document.getElementById("recognizedText").textContent = response.text;
        },
        error: function(error) {
            console.error("Error:", error);
        }
    });
}
