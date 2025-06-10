document.getElementById('logbtn').addEventListener('click', () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;


    if(username && password){
        window.location.href = 'index2.html';
    } else {
        alert('아이디와 비밀번호를 입력하세요.');
    }
});


