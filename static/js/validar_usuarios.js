document.addEventListener("DOMContentLoaded", () => {
    const formularios = document.querySelectorAll(".form-usuario");

    const expresionNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$/;
    const expresionCedula = /^\d{4,10}$/;
    const expresionCorreo = /^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$/;
    const expresionCelular = /^3\d{9}$/
    const expresionContraseña = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=<>?{}[\]~]).{8,}$/;

    formularios.forEach(form => {
        const nombre = form.querySelector(".input-nombre");
        const cedula = form.querySelector(".input-cedula");
        const celular = form.querySelector(".input-celular");
        const correo = form.querySelector(".input-correo");
        const contraseña = form.querySelector(".input-contraseña");
        const rol = form.querySelector(".input-rol");

        const errorNombre = form.querySelector(".error-nombre");
        const errorCedula = form.querySelector(".error-cedula");
        const errorCelular = form.querySelector(".error-celular");
        const errorCorreo = form.querySelector(".error-correo");
        const errorContraseña = form.querySelector(".error-contraseña");
        const errorRol = form.querySelector(".error-rol");
        form.addEventListener("submit", e => {
            let valido = true;

            [nombre, cedula, celular, correo, contraseña, rol].forEach(el => {
                if (el) el.classList.remove("border-red-500");
            });

            // Limpiar errores anteriores
            [errorNombre, errorCedula, errorCelular, errorCorreo, errorContraseña, errorRol].forEach(el => { 
                if (el) el.classList.add("hidden");
            });

            if (!expresionNombre.test(nombre.value.trim())) {
                errorNombre.classList.remove("hidden");
                nombre.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionCedula.test(cedula.value.trim())) {
                errorCedula.classList.remove("hidden");
                cedula.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionCelular.test(celular.value.trim())) {
                errorCelular.classList.remove("hidden");
                celular.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionCorreo.test(correo.value.trim())) {
                errorCorreo.classList.remove("hidden");
                correo.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionContraseña.test(contraseña.value.trim())) {
                errorContraseña.classList.remove("hidden");
                contraseña.classList.add("border-red-500");
                valido = false;
            }

            if (!rol.value) {
                errorRol.classList.remove("hidden");
                rol.classList.add("border-red-500");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });

        nombre.addEventListener("input", () => {
            if (!nombre.test(nombre.value.trim())) {
                errorNombre.classList.remove("hidden");
                nombre.classList.add("border-red-500");
            } else {
                errorNombre.classList.add("hidden");
                nombre.classList.remove("border-red-500");
            }
        });

        cedula.addEventListener("input", () => {
            if (!cedula.test(cedula.value.trim())) {
                errorCedula.classList.remove("hidden");
                cedula.classList.add("border-red-500");
            } else {
                errorCedula.classList.add("hidden");
                cedula.classList.remove("border-red-500");
            }
        });
        
        celular.addEventListener("input", () => {
            if (!celular.test(celular.value.trim())) {
                errorCelular.classList.remove("hidden");
                celular.classList.add("border-red-500");
            } else {
                errorCelular.classList.add("hidden");
                celular.classList.remove("border-red-500");
            }
        });

        correo.addEventListener("input", () => {
            if (!correo.test(correo.value.trim())) {
                errorCorreo.classList.remove("hidden");
                correo.classList.add("border-red-500");
            } else {
                errorCorreo.classList.add("hidden");
                correo.classList.remove("border-red-500");
            }
        });

        contraseña.addEventListener("input", () => {
            if (!contraseña.test(contraseña.value.trim())) {
                errorContraseña.classList.remove("hidden");
                contraseña.classList.add("border-red-500");
            } else {
                errorContraseña.classList.add("hidden");
                contraseña.classList.remove("border-red-500");
            }
        });

        if (rol) {
            rol.addEventListener("change", () => {
                if (!rol.value) {
                    errorRol.classList.remove("hidden");
                    rol.classList.add("border-red-500");
                } else {
                    errorRol.classList.add("hidden");
                    rol.classList.remove("border-red-500");
                }
            });
        }
    });
});

document.querySelectorAll(".form-editar-usuario").forEach(form => {
    let id = form.dataset.id;

    let nombre = document.getElementById("nombre-editar" + id);
    let errorNombre = document.getElementById("error-nombre-editar" + id);

    let cedula = document.getElementById("cedula-editar" + id);
    let errorCedula = document.getElementById("error-cedula-editar" + id);

    let celular = document.getElementById("celular-editar" + id);
    let errorCelular = document.getElementById("error-celular-editar" + id);

    let correo = document.getElementById("correo-editar" + id);
    let errorCorreo = document.getElementById("error-correo-editar" + id);

    let contraseña = document.getElementById("contraseña-editar" + id);
    let errorContraseña = document.getElementById("error-contraseña-editar" + id);

    let rol = document.getElementById("rol" + id);
    let errorRol = document.getElementById("error-rol-editar" + id);

    nombre.addEventListener("input", () => {
        if (nombre.value) errorNombre.classList.add("hidden");
    });

    cedula.addEventListener("input", () => {
        if (cedula.value) errorCedula.classList.add("hidden");
    });

    celular.addEventListener("input", () => {
        if (celular.value) errorCelular.classList.add("hidden");
    });

    correo.addEventListener("input", () => {
        if (correo.value) errorCorreo.classList.add("hidden");
    });

    contraseña.addEventListener("input", () => {
        if (contraseña.value) errorContraseña.classList.add("hidden");
    });

    rol.addEventListener("change", () => {
        if (rol.value) errorRol.classList.add("hidden");
    });

    form.addEventListener("submit", function (e) {
        let valido = true;

        if (!nombre.value) {
            errorNombre.classList.remove("hidden");
            valido = false;
        }

        if (!cedula.value) {
            errorCedula.classList.remove("hidden");
            valido = false;
        }

        if (!celular.value) {
            errorCelular.classList.remove("hidden");
            valido = false;
        }

        if (!correo.value) {
            errorCorreo.classList.remove("hidden");
            valido = false;
        }

        if (!contraseña.value) {
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