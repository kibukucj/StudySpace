// Get references to HTML elements
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.getElementById('chat-messages');

// Function to add a message to the chat
function addMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatMessages.appendChild(messageElement);
}

// Event listener for send button click
sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    // Send the message to the server (using WebSocket)
    // Display the message in the chat
    addMessage(message);
    // Clear the message input field
    messageInput.value = '';
});
