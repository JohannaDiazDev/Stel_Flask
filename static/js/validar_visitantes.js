document.addEventListener("DOMContentLoaded", () => {
    const formularios = document.querySelectorAll(".form-visitante");

    const expresionNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$/;
    const expresionCedula = /^\d{4,10}$/;

    formularios.forEach(form => {
        const fecha = form.querySelector(".input-fecha");
        const inmueble = form.querySelector(".input-inmueble");
        const autorizado = form.querySelector(".input-autorizado");
        const nombre = form.querySelector(".input-nombre");
        const cedula = form.querySelector(".input-cedula");
        const carro = form.querySelector(".input-carro");

        const errorFecha = form.querySelector(".error-fecha");
        const errorInmueble = form.querySelector(".error-inmueble");
        const errorAutorizado = form.querySelector(".error-autorizado");
        const errorNombre = form.querySelector(".error-nombre");
        const errorCedula = form.querySelector(".error-cedula");
        const errorCarro = form.querySelector(".error-carro");

        form.addEventListener("submit", e => {

            let valido = true;
            const hoy = new Date().toISOString().split("T")[0];
            const valorFecha = fecha.value.split("T")[0];

            [fecha, inmueble, autorizado, nombre, cedula, carro].forEach(el => { 
                if (el) el.classList.remove("border-red-500");
            });
            [errorFecha, errorInmueble, errorAutorizado, errorNombre, errorCedula, errorCarro].forEach(el => { 
                if (el) el.classList.add("hidden");
            });
            
            if (!fecha.value) {
                errorFecha.classList.remove('hidden');
                fecha.classList.add('border-red-500');
                valido = false;
            }

            if (!inmueble.value) {
                errorInmueble.classList.remove("hidden");
                inmueble.classList.add("border-red-500");
                valido = false;
            }

            if (!autorizado.value) {
                errorAutorizado.classList.remove("hidden");
                autorizado.classList.add("border-red-500");
                valido = false;
            }

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

            if (!carro.value) {
                errorCarro.classList.remove("hidden");
                carro.classList.add("border-red-500");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });

        fecha.addEventListener('input', () => {
            if (fecha.value) {
                errorFecha.classList.add("hidden");
                fecha.classList.remove('border-red-500');
            }
        });

        inmueble.addEventListener("change", () => {
            if (inmueble.value) {
                errorInmueble.classList.add("hidden");
                inmueble.classList.remove("border-red-500");
            } else {
                errorInmueble.classList.add("hidden");
                inmueble.classList.remove("border-red-500");
            } 
        });

        autorizado.addEventListener("change", () => {
            if (autorizado.value) {
                errorAutorizado.classList.add("hidden");
                autorizado.classList.remove("border-red-500");
            } else {
                errorAutorizado.classList.add("hidden");
                autorizado.classList.remove("border-red-500");
            }
        });

        nombre.addEventListener("input", () => {
            if (expresionNombre.test(nombre.value.trim())) {
                errorNombre.classList.add("hidden");
                nombre.classList.remove("border-red-500");
            } else {
                errorNombre.classList.add("hidden");
                nombre.classList.remove("border-red-500");
            }
        });

        cedula.addEventListener("input", () => {
            if (expresionCedula.test(cedula.value.trim())) {
                errorCedula.classList.add("hidden");
                cedula.classList.remove("border-red-500");
            } else {
                errorCedula.classList.add("hidden");
                cedula.classList.remove("border-red-500");
            }
        });

        carro.addEventListener("change", () => {
            if (carro.value) {
                errorCarro.classList.add("hidden");
                carro.classList.remove("border-red-500");
            } else {
                errorCarro.classList.add("hidden");
                carro.classList.remove("border-red-500");
            }
        });
    });
});

