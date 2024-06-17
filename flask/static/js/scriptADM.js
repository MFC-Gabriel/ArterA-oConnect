//Login ADM -------------------------

document.getElementById('admin-login-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const login = document.getElementById('admin-login').value;
    const password = document.getElementById('admin-password').value;
  
    // Verifique as credenciais adm e senha12
    const correctLogin = 'adm';
    const correctPassword = 'senha123';
  
  
    if (login === correctLogin && password === correctPassword) {
      alert('Login foi')
      window.location.href = 'controlebanco.html';
    } else {
      alert('Login ou senha incorretos. Tente novamente.');
    }
  });