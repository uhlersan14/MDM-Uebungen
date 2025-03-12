function reverseText() {
    const inputText = document.getElementById('inputText').value;
    
    fetch('/reverse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputText').textContent = data.reversed;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('outputText').textContent = 'Ein Fehler ist aufgetreten';
    });
}