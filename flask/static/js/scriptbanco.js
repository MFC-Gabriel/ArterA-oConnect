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