const chatArea = document.getElementById("chatArea");

// 🎤 Start voice input
function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    const audioChunks = [];

    addBubble("🎙 Listening...", "bot");

    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/webm" });
      const formData = new FormData();
      formData.append("audio", audioBlob, "recording.webm");

      fetch("/api/ask", {
        method: "POST",
        body: formData
      })
        .then(res => res.json())
        .then(data => {
          if (data.transcript) addBubble(data.transcript.trim(), "user");
          if (data.reply) addBubble(data.reply.trim(), "bot");
          if (data.audio_url) new Audio(data.audio_url).play();
        })
        .catch(() => {
          addBubble("❌ Could not connect to assistant.", "bot");
        });
    };

    mediaRecorder.start();
    setTimeout(() => mediaRecorder.stop(), 4000);
  }).catch(() => {
    addBubble("❌ Microphone access denied", "bot");
  });
}

// 🧾 Create chat bubbles
function addBubble(message, type) {
  const bubble = document.createElement("div");
  bubble.className = "chat-bubble " + type;
  bubble.innerHTML = `<strong>${type === "user" ? "You" : "SathiSwar"}:</strong> ${message}`;
  chatArea.appendChild(bubble);
  chatArea.scrollTop = chatArea.scrollHeight;
}

// 🌙 Dark/Light theme toggle
const themeSwitcher = document.getElementById("themeSwitcher");
const root = document.documentElement;

const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
  root.setAttribute("data-theme", savedTheme);
  themeSwitcher.checked = savedTheme === "dark";
} else {
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  root.setAttribute("data-theme", prefersDark ? "dark" : "light");
  themeSwitcher.checked = prefersDark;
}

themeSwitcher.addEventListener("change", () => {
  const newTheme = themeSwitcher.checked ? "dark" : "light";
  root.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme);
});
