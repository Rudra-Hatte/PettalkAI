// script.js

let mediaRecorder, audioChunks = [];
const recordBtn = document.getElementById('record-btn');
const stopBtn   = document.getElementById('stop-btn');
const chatBox   = document.getElementById('chat-box');

recordBtn.addEventListener('click', async () => {
  // ask for mic permission and start recording
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  audioChunks = [];

  mediaRecorder.addEventListener('dataavailable', e => {
    audioChunks.push(e.data);
  });
  mediaRecorder.start();

  recordBtn.disabled = true;
  stopBtn.disabled   = false;
  addMessage('System', 'Recording…', 'system');
});

stopBtn.addEventListener('click', () => {
  mediaRecorder.stop();
  recordBtn.disabled = false;
  stopBtn.disabled   = true;

  mediaRecorder.addEventListener('stop', async () => {
    // assemble audio blob
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    sendAudioToServer(audioBlob);
  });
});

function addMessage(sender, text, cls) {
  const msg = document.createElement('div');
  msg.classList.add('message', cls);
  msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendAudioToServer(blob) {
  addMessage('You', '[audio recording]', 'user');
  const form = new FormData();
  form.append('audio', blob, 'pet.wav');

  try {
    const res  = await fetch('/api/pet-talk', {
      method: 'POST',
      body: form
    });
    const json = await res.json();
    if (json.reply) {
      addMessage('PetTalkAI', json.reply, 'pet');
    } else {
      addMessage('Error', json.error || 'No reply.', 'error');
    }
  } catch (err) {
    addMessage('Error', err.message, 'error');
  }
}
