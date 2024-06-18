// script.js


//EMAIL

document.getElementById('enviar-email').addEventListener('click', function(event) {
    event.preventDefault();
  
    // Coleta os dados do formulário
    var nome = document.getElementsByName('nome')[0].value;
    var email = document.getElementsByName('email')[0].value;
    var assunto = document.getElementsByName('assunto')[0].value;
    var mensagem = document.getElementsByName('mensagem')[0].value;
  
    console.log("Nome: " + nome);
    console.log("E-mail: " + email);
    console.log("Assunto: " + assunto);
    console.log("Mensagem: " + mensagem);
  
    // Define os parâmetros para enviar o e-mail
    var params = {
      to_name: nome,
      from_name: email,
      reply_to: assunto,
      message: mensagem,
    };
  
    // Envia o e-mail
    emailjs.send("service_59sgiv8", "template_obu06m7", params)
      .then(function(response) {
        alert('E-mail enviado com sucesso!');
      }, function(error) {
        console.error('Ocorreu um erro ao enviar o e-mail:', error);
        alert('Ocorreu um erro ao enviar o e-mail. Por favor, tente novamente.');
      });
  });
  
  // CONDIÇÃO MENOR/MAIOR DE 18 PRO FORMULÁRIO
  
  document.addEventListener('DOMContentLoaded', function () {
    const minorRadio = document.querySelector('input[name="idade"][value="Menor"]');
    const adultRadio = document.querySelector('input[name="idade"][value="Maior"]');
    const respFields = document.querySelectorAll('#register-name-resp, #register-email-resp, #register-cpf-resp, #register-tell-resp, #register-gender-resp');
  
    function toggleRespFields() {
      const isMinor = minorRadio.checked;
      respFields.forEach(field => {
        field.required = isMinor;
        field.closest('.form-group').style.display = isMinor ? 'block' : 'none';
      });
    }
  
    minorRadio.addEventListener('change', toggleRespFields);
    adultRadio.addEventListener('change', toggleRespFields);
  
    // Initialize visibility on page load
    toggleRespFields();
  });
  
  