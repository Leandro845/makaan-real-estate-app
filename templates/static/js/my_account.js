const uploadButton = document.getElementById('update-image-button');
const uploadInput = document.getElementById('profile-image-upload');

uploadButton.addEventListener('click', () => {
    uploadInput.click();
});

$(document).ready(function() {
    $("#togglePassword").click(function() {
        var passwordField = $("#password");
        if (passwordField.attr("type") === "password") {
            passwordField.attr("type", "text");
            $(this).html('<i class="fas fa-eye-slash"></i>'); // Change icon to slashed eye
        } else {
            passwordField.attr("type", "password");
            $(this).html('<i class="fas fa-eye"></i>'); // Change icon back to eye
        }
    });
});

/** *
$(document).ready(function() {
    $("#update-image-button").click(function() {
      $("#profile-image-upload").click(); // Abre o input de arquivo
    });
  
    $("#profile-form").submit(function() {
      // Verifica se uma imagem foi selecionada
      if ($("#profile-image-upload")[0].files.length === 0) {
        //alert("Por favor, selecione uma imagem para fazer upload.");
        return false; // Impede o envio do formulário
      } 
      // Caso contrário, o formulário será enviado normalmente
    });
}); */

$(document).ready(function() {
    $("#update-image-button").click(function() {
      $("#profile-image-upload").click(); 
  
      if ($("#profile-image-upload")[0].files.length > 0) {
        $("#save-changes").prop("disabled", false); 
      } else {
        $("#profile-image-upload").on("change", function() {
          $("#save-changes").prop("disabled", false); 
        });
      }
    });
  
    $("#profile-form").submit(function() {
      if ($("#profile-form").data("dirty") || $("#profile-image-upload")[0].files.length > 0) {
        return true; 
      } else {
        return false; 
      }
    });
  
    $(document).on("change", 'input, select, textarea', function() {
      $("#profile-form").data("dirty", true);
    });
});