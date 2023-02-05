function CreateSession() {

    let _message = document.getElementById('message');
    
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    if (username.length < 4 || password.length < 4) {
        
        return _message.innerHTML = "Error";
    }

    let hash = sha512(password)
    
    fetch('/auth/create-session', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }, body: JSON.stringify({
            'username': username,
            'password': hash
        })
    }).then((t) => window.location.href = '/')
}