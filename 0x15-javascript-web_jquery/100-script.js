// Script que actulalice el color del header cuando se carga el dom (evento)
// capturamos el momento en el que el DOM esta listo
document.addEventListener('DOMContentLoaded', function () {
  // obtengo el header
  document.querySelector('header').style.background = '#FF0000';
});
