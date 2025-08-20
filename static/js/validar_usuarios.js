document.addEventListener("DOMContentLoaded", () => {
    const formularios = document.querySelectorAll(".form-usuario");

    const expresionNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$/;
    const expresionCedula = /^\d{4,10}$/;
    const expresionCorreo = /^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$/;

    formularios.forEach(form => {
        form.addEventListener("submit", e => {
            let valido = true;

            const nombre = form.querySelector(".input-nombre");
            const cedula = form.querySelector(".input-cedula");
            const celular = form.querySelector(".input-celular");
            const correo = form.querySelector(".input-correo");
            const contraseña = form.querySelector(".input-contraseña");
            const rol = form.querySelector("select[name='rol_id']");

            const errorNombre = form.querySelector(".error-nombre");
            const errorCedula = form.querySelector(".error-cedula");
            const errorCelular = form.querySelector(".error-celular");
            const errorCorreo = form.querySelector(".error-correo");
            const errorContraseña = form.querySelector(".error-contraseña");
            const errorRol = form.querySelector(".error-rol");

            // Limpiar errores anteriores
            [errorNombre, errorCedula, errorCelular, errorCorreo, errorContraseña, errorRol].forEach(p => p?.classList.add("hidden"));

            if (!expresionNombre.test(nombre.value.trim())) {
                errorNombre.classList.remove("hidden");
                valido = false;
            }

            if (!expresionCedula.test(cedula.value.trim())) {
                errorCedula.classList.remove("hidden");
                valido = false;
            }

            if (celular.value.trim().length < 7 || isNaN(celular.value.trim())) {
                errorCelular.classList.remove("hidden");
                valido = false;
            }

            if (!expresionCorreo.test(correo.value.trim())) {
                errorCorreo.classList.remove("hidden");
                valido = false;
            }

            if (!contraseña.value.trim()) {
                errorContraseña.classList.remove("hidden");
                valido = false;
            }

            if (!rol.value) {
                errorRol.classList.remove("hidden");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });
    });
});