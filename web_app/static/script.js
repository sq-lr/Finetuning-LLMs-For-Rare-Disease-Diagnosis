document.getElementById('dis_form').addEventListener('submit', function(e) {
    e.preventDefault();

    document.getElementById('loading').style.display = 'block';
    document.getElementById('output').style.display = 'none';

    fetch('/', {
        method: 'POST',
        body: new FormData(this),
        headers: {
            'Accept': 'application/json'
        }
    })
    .then(response => response.json()) // get json from runpod api called in flask
    .then(data => { // change UI
        document.getElementById('loading').style.display = 'none';
        document.getElementById('output').style.display = 'block';
        document.getElementById('output').textContent = data.output[0].choices[0].tokens[0];
    })
    .catch(error => {
        console.error('Error:', error);
    });
});