let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    
    // Check if the input is empty
    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
        return;
    }

    // Create a new XMLHttpRequest to make the API call
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        // Check if the request is complete and successful
        if (this.readyState == 4 && this.status == 200) {
            // Parse the JSON response
            let response = JSON.parse(xhttp.responseText);
            
            // Check if the response contains a message or a valid result
            if (response.message) {
                document.getElementById("system_response").innerHTML = response.message;
            } else {
                document.getElementById("system_response").innerHTML = "Error processing the emotion detection. Please try again.";
            }
        }
    };

    // Construct the URL with the query parameter
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
