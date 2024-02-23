document.addEventListener('DOMContentLoaded', function() {
    let email = "li.liangs@northeastern.edu";
    let number = "617-708-2565"
    document.getElementById('myEmail').textContent = email;
    document.getElementById('myPhoneNumber').textContent = number;
});

function postMessage() {
    var message = document.getElementById('welcomeMessageInput').value;

    fetch('http://127.0.0.1:5000/post_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if(data.success) {
            // Fetch and display messages after posting a new one
            fetchMessages();
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    document.getElementById('welcomeMessageInput').value = '';
}

function fetchMessages() {
    fetch('http://127.0.0.1:5000/get_messages')
    .then(response => response.json())
    .then(messages => {
        var messagesContainer = document.getElementById('messagesContainer');
        messagesContainer.innerHTML = ''; // Clear existing messages
        messages.forEach(function(message) {
            var messageElement = document.createElement('p');
            messageElement.textContent = message.message;
            messagesContainer.appendChild(messageElement);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Fetch and display messages when the page loads
document.addEventListener('DOMContentLoaded', fetchMessages);