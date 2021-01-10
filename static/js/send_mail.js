<script>
    let form = document.getElementById('form')
    from.addEventListener('submit', function(event){
        event.preventDefault()
        let name = document.getElementById('name').value
        let email = document.getElementById('email').value

    })
    var formData = new FormData();
    formData.append('from_email', this.email)
    formData.append('message', this.name)
    var request = new XMLHttpRequest();

    request.open("POST", 'http://127.0.0.1:8000/main/contact/');
    request.send(formData);
</script>