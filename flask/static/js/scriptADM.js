//Login ADM -------------------------

// document.getElementById('admin-login-form').addEventListener('submit', function(e) {
//   e.preventDefault();

//   const login = document.getElementById('admin-login').value;
//   const password = document.getElementById('admin-password').value;

//   // Verifique as credenciais adm e senha123
//   const correctLogin = 'adm';
//   const correctPassword = 'senha123';

//   if (login === correctLogin && password === correctPassword) {
//       alert('Login realizado com sucesso!');
//       window.location.href = './templates/controlebanco.html';; // Redireciona para a página desejada 

//   } else {
//       alert('Login ou senha incorretos. Tente novamente.');
//   }
// });

// Manipuladores para divs dentro de #noticias
document.querySelectorAll('#noticias .FotosNoticias').forEach(div => {
  div.addEventListener('click', function() {
      const url = this.getAttribute('data-url'); // Corrigido para data-url
      if (url) {
          window.location.href = url;
      }
  });
});