async function sendMessage() {
  const userInput = document.getElementById('userInput').value.trim();
  const chatBox = document.getElementById('chatBox');

  if (!userInput) return;

  // Show user's message
  chatBox.innerHTML += `<div class="message user"><strong>You:</strong> ${userInput}</div>`;

  // Clear input field
  document.getElementById('userInput').value = '';

  // Call Ollama API
  try {
    const response = await fetch('http://localhost:11434/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: 'llama3',
        messages: [
          { role: 'user', content: userInput }
        ]
      })
    });

    const data = await response.json();

    // Show Llama3's reply
    chatBox.innerHTML += `<div class="message bot"><strong>Llama3:</strong> ${data.message.content}</div>`;

    // Auto-scroll down
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    console.error('Error:', error);
    chatBox.innerHTML += `<div class="message error">❌ Error contacting Llama3.</div>`;
  }
}
