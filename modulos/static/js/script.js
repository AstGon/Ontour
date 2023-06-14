window.onload = function () {
  console.log("JavaScript conectado correctamente");
};

window.addEventListener("DOMContentLoaded", () => {
  var contratoInput = document.getElementById("contrato");
  contratoInput.value = "";
});

function cargarArchivo() {
  console.log("Función cargarArchivo() llamada."); // Agregar esta línea

  var fileInput = document.getElementById("inputGroupFile02");
  var file = fileInput.files[0];

  if (file) {
    var fileName = file.name;
    var fileExtension = fileName.split(".").pop().toLowerCase();

    if (
      fileExtension === "pdf" ||
      fileExtension === "jpg" ||
      fileExtension === "png"
    ) {
      var formData = new FormData();
      formData.append("archivo", file);
      formData.append("descripcion", fileName);
      formData.append(
        "tipo",
        document.getElementById("inputGroupSelect02").value
      );
      formData.append("contrato", document.getElementById("contrato").value);

      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/carga_archivos/", true);
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
          console.log("Archivo cargado con éxito.");
        }
      };
      xhr.send(formData);
    } else {
      alert("Formato de archivo no válido. Se permiten solo PDF, JPG y PNG.");
    }
  } else {
    alert("No se ha seleccionado ningún archivo.");
  }
}
