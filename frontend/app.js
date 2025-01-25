const socket = io("http://localhost:5000");

const video = document.getElementById("stream");

// Receive video stream
socket.on("video", (data) => {
    const blob = new Blob([data], { type: "video/webm" });
    video.srcObject = URL.createObjectURL(blob);
});

// Send user input
document.addEventListener("keydown", (e) => {
    socket.emit("input", { type: "keydown", key: e.key });
});
