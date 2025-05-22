function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userMessage = input.value.trim();
  if (!userMessage) return;

  addMessage("You", userMessage, "user");

  // Simulate pet response
  setTimeout(() => {
    const petReply = getPetReply(userMessage);
    addMessage("Pet", petReply, "pet");
  }, 500);

  input.value = "";
}

function addMessage(sender, text, type) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", type);
  messageDiv.textContent = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function getPetReply(message) {
  // Simple AI for now (can be replaced with GPT backend)
  const replies = [
    "Woof woof! 🐶",
    "Meow~ 🐱",
    "I'm hungry! 🍖",
    "Let's play! 🎾",
    "Nap time! 💤",
    "I love you! ❤️"
  ];
  return replies[Math.floor(Math.random() * replies.length)];
}
