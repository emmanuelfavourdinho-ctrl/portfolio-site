function toggleChat() {
    let box = document.getElementById("chat-box");
    box.style.display = box.style.display === "block" ? "none" : "block";
}
document.getElementById("year").textContent = new Date().getFullYear();