document.addEventListener("DOMContentLoaded", function () {
  // Obtener el div de mensajes de archivo
  const mensajesArchivoDiv = document.getElementById("mensajes-archivo");

  // Mostrar los mensajes de archivo
  mensajesArchivoDiv.classList.remove("d-none");

  // Ocultar los mensajes después de 3 segundos (3000 milisegundos)
  setTimeout(() => {
    mensajesArchivoDiv.classList.add("d-none");
  }, 3000);

  function limpiarFormulario() {
    $("#contrato").val("");
    $("#archivo").val("");
    $("#inputGroupSelect02").val("");
  }

  // Ejecutar la función al cargar la página
  limpiarFormulario();
});
