console.log("El archivo JavaScript está conectado correctamente.");

function validateFile() {
  var fileInput = document.getElementById("archivo");
  var filePath = fileInput.value;
  var allowedExtensions = /(\.jpg|\.png|\.pdf)$/i;

  if (!allowedExtensions.exec(filePath)) {
    document.getElementById("archivo-section").style.display = "none";
    alert(
      "Formato de archivo no válido. Por favor, selecciona un archivo con formato JPG, PNG o PDF."
    );
    fileInput.value = "";
    return false;
  } else {
    document.getElementById("archivo-section").style.display = "block";
  }
}

function agregarCampoArchivo() {
  var container = document.getElementById("archivos-container");
  var input = document.createElement("input");
  input.type = "file";
  input.name = "archivos[]";
  container.appendChild(input);
}

function limpiarFormularios() {
  window.location.href = "http://127.0.0.1:8000/";
}

function obtenerSeleccionTipoDocumento() {
  var tipoDocumentoSelect = document.getElementById("tipo_documento");
  var tipoServicioSeleccionado =
    tipoDocumentoSelect.options[tipoDocumentoSelect.selectedIndex].dataset.id;
  console.log("Tipo de servicio seleccionado:", tipoServicioSeleccionado);

  // Asignar el valor al campo oculto en el formulario
  document.getElementById("tipo_documento_seleccionado").value =
    tipoServicioSeleccionado;
}

function submitTipoDocumento(event) {
  event.preventDefault(); // Evitar que se envíe el formulario de manera predeterminada

  var tipoDocumentoSelect = document.getElementById("tipo_documento");
  var tipoDocumentoSeleccionado =
    tipoDocumentoSelect.options[tipoDocumentoSelect.selectedIndex].dataset.id;

  // Verificar si se ha seleccionado un tipo de documento
  if (tipoDocumentoSeleccionado) {
    // Asignar el valor al campo oculto
    var tipoDocumentoSeleccionadoInput = document.getElementById(
      "tipo_documento_seleccionado"
    );
    tipoDocumentoSeleccionadoInput.value = tipoDocumentoSeleccionado;

    // Enviar el formulario
    document.getElementById("formulario-archivo").submit();
  } else {
    alert("Por favor, selecciona un tipo de documento.");
  }
}
