// Script que actulalice el color del header cuando se carga el dom (evento)
// obtengo el header
const header = document.querySelector('header');
// capturamos el momento en el que el DOM esta listo
document.addEventListener('DOMContentLoaded', function () {
  header.style.background = '#FF0000';
});
