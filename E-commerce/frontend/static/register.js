document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault(); 

    const name = document.getElementById('name').value;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, username, password }),
        });

        if (response.ok) {
            
            Swal.fire({
                title: 'Registration Successful!',
                text: 'Your account has been created successfully.',
                icon: 'success',
                confirmButtonText: 'Go to Login',
            }).then(() => {
                window.location.href = 'index.html'; 
            });
        } else {
            const errorData = await response.json();
    
            Swal.fire({
                title: 'Registration Failed',
                text: errorData.detail || 'We could not complete your registration. Please try again.',
                icon: 'error',
                confirmButtonText: 'Try Again',
            });
        }
    } catch (error) {

        Swal.fire({
            title: 'Unexpected Error',
            text: 'There was a problem connecting to the server. Please try again later.',
            icon: 'error',
            confirmButtonText: 'Try Again',
        });
    }
});
