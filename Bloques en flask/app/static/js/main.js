document.addEventListener("DOMContentLoaded", function() {
    const formulario = document.querySelector("form");
    const botonEjecutar = document.querySelector(".btn-success");

    // Detalle 2: Estado de Carga en Botones
    if (formulario && botonEjecutar) {
        formulario.addEventListener("submit", function() {
            botonEjecutar.disabled = true;
            botonEjecutar.innerHTML = `<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Procesando Objetos en Servidor...`;
        });
    }

    // Detalle 3: Guardar y restaurar la posición del Scroll del Sidebar de bloques
    const sidebar = document.querySelector(".sidebar-docs");
    if (sidebar) {
        // Al hacer click en una unidad, guardamos en memoria dónde estaba el scroll
        const enlaces = document.querySelectorAll(".enlace-sidebar");
        enlaces.forEach(enlace => {
            enlace.addEventListener("click", function() {
                localStorage.setItem("sidebar-scroll", sidebar.scrollTop);
            });
        });

        // Al cargar la página, recuperamos la posición exacta
        const posicionGuardada = localStorage.getItem("sidebar-scroll");
        if (posicionGuardada) {
            sidebar.scrollTop = posicionGuardada;
        }
    }
});