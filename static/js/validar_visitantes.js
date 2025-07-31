document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("visitanteForm");
    if (form) {
        const fecha = form.querySelector("input[name='fecha']");
        const inmueble = form.querySelector("select[name='inmueble_id']");
        const autorizado = form.querySelector("select[name='autorizado']");
        const nombre = form.querySelector("input[name='nombre']");
        const cedula = form.querySelector("input[name='cedula']");
        const ingresaCarro = form.querySelector("select[name='ingresa_carro']");

        const errorFecha = document.getElementById("error-fecha");
        const errorInmueble = document.getElementById("error-inmueble");
        const errorAutorizado = document.getElementById("error-autorizado");
        const errorNombre = document.getElementById("error-nombre");
        const errorCedula = document.getElementById("error-cedula");
        const errorCarro = document.getElementById("error-carro");

        
        const expresionNombre = /^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$/;
        const expresionCedula = /^\d{4,10}$/;

        // Validación en vivo
        
        fecha.addEventListener('input', () => {
            if (fecha.value) {
                fecha.classList.remove('border-red-500');
                fecha.classList.add('border-[#1E4C40]');
                errorFecha.classList.add('hidden');
            }
        });

        inmueble.addEventListener("change", () => {
            if (inmueble.value) {
                errorInmueble.classList.add("hidden");
                inmueble.classList.remove("border-red-500");
                inmueble.classList.add("border-[#1E4C40]");
            }
        });

        autorizado.addEventListener("change", () => {
            if (autorizado.value) {
                errorAutorizado.classList.add("hidden");
                autorizado.classList.remove("border-red-500");
                autorizado.classList.add("border-[#1E4C40]");
            }
        });

        nombre.addEventListener("input", () => {
            if (expresionNombre.test(nombre.value.trim())) {
                errorNombre.classList.add("hidden");
                nombre.classList.remove("border-red-500");
                nombre.classList.add("border-[#1E4C40]");
            }
        });

        cedula.addEventListener("input", () => {
            if (expresionCedula.test(cedula.value.trim())) {
                errorCedula.classList.add("hidden");
                cedula.classList.remove("border-red-500");
                cedula.classList.add("border-[#1E4C40]");
            }
        });

        ingresaCarro.addEventListener("change", () => {
            if (ingresaCarro.value) {
                errorCarro.classList.add("hidden");
                ingresaCarro.classList.remove("border-red-500");
                ingresaCarro.classList.add("border-[#1E4C40]");
            }
        });

        // Validación al enviar
        form.addEventListener("submit", (e) => {
            let valido = true;
            const hoy = new Date().toISOString().split("T")[0];
            const valorFecha = fecha.value.split("T")[0];

            [errorFecha, errorInmueble, errorAutorizado, errorNombre, errorCedula, errorCarro].forEach(err => err.classList.add("hidden"));
            [fecha, inmueble, autorizado, nombre, cedula, ingresaCarro].forEach(campo => {
                campo.classList.remove("border-red-500");
                campo.classList.add("border-[#1E4C40]");
            });

            if (!fecha.value) {
                fecha.classList.add('border-red-500');
                fecha.classList.remove('border-[#1E4C40]');
                errorFecha.classList.remove('hidden');
                valido = false;
            }

            if (!inmueble.value) {
                errorInmueble.classList.remove("hidden");
                inmueble.classList.add("border-red-500");
                inmueble.classList.remove("border-[#1E4C40]");
                valido = false;
            }

            if (!autorizado.value) {
                errorAutorizado.classList.remove("hidden");
                autorizado.classList.add("border-red-500");
                autorizado.classList.remove("border-[#1E4C40]");
                valido = false;
            }

            if (!expresionNombre.test(nombre.value.trim())) {
                errorNombre.classList.remove("hidden");
                nombre.classList.add("border-red-500");
                nombre.classList.remove("border-[#1E4C40]");
                valido = false;
            }

            if (!expresionCedula.test(cedula.value.trim())) {
                errorCedula.classList.remove("hidden");
                cedula.classList.add("border-red-500");
                cedula.classList.remove("border-[#1E4C40]");
                valido = false;
            }

            if (!ingresaCarro.value) {
                errorCarro.classList.remove("hidden");
                ingresaCarro.classList.add("border-red-500");
                ingresaCarro.classList.remove("border-[#1E4C40]");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });
    }
});
