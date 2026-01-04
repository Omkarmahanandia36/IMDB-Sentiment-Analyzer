function analyzeSentiment() {
    const text = document.getElementById("textInput").value;
    const resultDiv = document.getElementById("result");

    if (text.trim() === "") {
        resultDiv.innerHTML = "Please enter some text";
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultDiv.innerHTML = data.error;
        } else {
            resultDiv.innerHTML = `
                <strong>Sentiment:</strong> ${data.sentiment}<br>
                <strong>Confidence:</strong> ${data.confidence}
            `;
        }
    })
    .catch(error => {
        resultDiv.innerHTML = " Error connecting to server";
    });
}
