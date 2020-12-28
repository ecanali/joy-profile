// greets the user based on the input given
function greet() {
    const userEmail = document.querySelector('#email').value
    if (userEmail === '') {
        document.querySelector('#result').innerHTML = "Please, let's be friends!"
        return false
    } else {
        alert(`Nice! I'll contact you by your ${userEmail} email`)
    }
}

// prevents user upload any file except .jpeg/.jpg/.png
const file = document.getElementById('file')
if (file) {
    file.onchange = function(e) {
        const ext = this.value.match(/\.([^\.]+)$/)[1]
        switch (ext) {
            case 'jpg':
            case 'jpeg':
            case 'png':
            break
            default:
            alert('File extension not allowed!')
            this.value = ''
        }
    }
}