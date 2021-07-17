

window.addEventListener("DOMContentLoaded", ()=> {
    const btnSubmit = document.getElementById("btnSubmit");
    btnSubmit.addEventListener("click", ()=> {
        const guessVal = document.getElementById("txtGuess").value;
        // alert(guessVal);
        // Send HTTP request
        fetch('http://localhost:5000/guess/' + guessVal, {'method':'POST'})
        .then(function (response) {
            // console.log(response)
            if (response.status === 201) console.log('%cConnected to backend!', 'color: green');
            return response.json(); // convert body to JSON and return this value.
        })
        .then(function (json) {
            // console.log(json)
            alert(json.message);
        })
        .catch(function (error) {
            console.error('Failed to connect to backend! Error: ', error);
        }); // End of fetch fn
    }); // End of "click" event fn
}); // End of "load" event fun
