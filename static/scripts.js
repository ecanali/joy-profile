// greets the user based on the input given
function greet() {
    const userEmail = document.querySelector('#email').value
    if (userEmail === '') {
        document.querySelector('#result').innerHTML = "Please, let's be friends!"
        return false
    } else {
        document.querySelector('#result').innerHTML = `Nice! I'll contact you by your ${userEmail} email`
    }
}