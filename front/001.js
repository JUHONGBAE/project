const API_BASE = "http://localhost:8000";  // 백엔드 주소

// 로그인
document.getElementById('logbtn').addEventListener('click', async () => {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username && password) {
        try {
            const res = await fetch(`${API_BASE}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            });

            const data = await res.json();
            if (res.ok) {
                alert("로그인 성공!");
                window.location.href = "index2.html"; // 로그인 성공 후 이동
            } else {
                alert(data.detail);
            }
        } catch (err) {
            alert("서버 오류 발생!");
        }
    } else {
        alert("아이디와 비밀번호를 입력하세요.");
    }
});

// 회원가입 폼 보이기
document.getElementById('signbtn').addEventListener('click', () => {
    document.querySelector('.signup-wrap').style.display = 'block';
});

// 회원가입
document.getElementById('signup-submit').addEventListener('click', async () => {
    const username = document.getElementById('signup-username').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;

    if (username && email && password) {
        try {
            const res = await fetch(`${API_BASE}/signup`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, email, password })
            });

            const data = await res.json();
            if (res.ok) {
                alert("회원가입 성공! 로그인 해주세요.");
                document.querySelector('.signup-wrap').style.display = 'none';
            } else {
                alert(data.detail);
            }
        } catch (err) {
            alert("서버 오류 발생!");
        }
    } else {
        alert("모든 항목을 입력해주세요.");
    }
});
