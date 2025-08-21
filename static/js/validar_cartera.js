document.addEventListener('DOMContentLoaded', () => {
    // Todos los formularios que tengan validación
    const forms = document.querySelectorAll('.form-cartera');

    forms.forEach(form => {
        const fechaActual = form.querySelector(".input-fecha");
        const inmueble = form.querySelector(".input-inmueble");
        const estado = form.querySelector(".input-estado");
        const saldo = form.querySelector(".input-saldo");
        const trabajador = form.querySelector(".input-trabajador");
        const observaciones = form.querySelector(".input-observaciones");

        const errorFecha = form.querySelector(".error-fecha");
        const errorInmueble = form.querySelector(".error-inmueble");
        const errorEstado = form.querySelector(".error-estado");
        const errorSaldo = form.querySelector(".error-saldo");
        const errorTrabajador = form.querySelector(".error-trabajador");
        const errorObservaciones = form.querySelector(".error-observaciones");

        
        const estadosValidos = ['Paz y Salvo', 'Moroso', 'Acuerdo de Pago', 'Cobro Juridico'];

        // Eventos individuales
        fechaActual.addEventListener("input", () => {
            if (fechaActual.value) {
                errorFecha.classList.add("hidden");
                fechaActual.classList.remove("border-red-500");
                fechaActual.classList.add("border-[#1E4C40]");
            }
        });

        inmueble.addEventListener("change", () => {
            if (inmueble.value) {
                errorInmueble.classList.add("hidden");
                inmueble.classList.remove("border-red-500");
                inmueble.classList.add("border-[#1E4C40]");
            }
        });

        estado.addEventListener('change', () => {
            if (!estadosValidos.includes(estado.value.trim())) {
                errorEstado.textContent = 'Estado inválido.';
                errorEstado.classList.remove("hidden");
                estado.classList.add('border-red-500');
                estado.classList.remove('border-[#1E4C40]');
            } else {
                errorEstado.classList.add("hidden");
                estado.classList.remove('border-red-500');
                estado.classList.add('border-[#1E4C40]');
            }
        });

        saldo.addEventListener("input", () => {
            const num = parseFloat(saldo.value);
            if (!isNaN(num) && num >= 0) {
                errorSaldo.classList.add("hidden");
                saldo.classList.remove("border-red-500");
                saldo.classList.add("border-[#1E4C40]");
            }
        });

        trabajador.addEventListener("change", () => {
            if (trabajador.value) {
                errorTrabajador.classList.add("hidden");
                trabajador.classList.remove("border-red-500");
                trabajador.classList.add("border-[#1E4C40]");
            }
        });

        // Validación al enviar
        form.addEventListener("submit", (e) => {
            let valido = true;

            if (!fechaActual.value) {
                errorFecha.textContent = "La fecha es obligatoria.";
                errorFecha.classList.remove("hidden");
                fechaActual.classList.add("border-red-500");
                valido = false;
            } else {
                errorFecha.classList.add("hidden");
            }

            if (!inmueble.value) {
                errorInmueble.textContent = "Debe seleccionar un inmueble.";
                errorInmueble.classList.remove("hidden");
                inmueble.classList.add("border-red-500");
                valido = false;
            } else {
                errorInmueble.classList.add("hidden");
            }

            if (!estadosValidos.includes(estado.value.trim())) {
                errorEstado.textContent = "Estado inválido.";
                errorEstado.classList.remove("hidden");
                estado.classList.add("border-red-500");
                valido = false;
            } else {
                errorEstado.classList.add("hidden");
            }

            const saldoNum = parseFloat(saldo.value);
            if (isNaN(saldoNum) || saldoNum < 0) {
                errorSaldo.textContent = "El saldo debe ser un número positivo.";
                errorSaldo.classList.remove("hidden");
                saldo.classList.add("border-red-500");
                valido = false;
            } else {
                errorSaldo.classList.add("hidden");
            }

            if (!trabajador.value) {
                errorTrabajador.textContent = "Debe seleccionar un trabajador.";
                errorTrabajador.classList.remove("hidden");
                trabajador.classList.add("border-red-500");
                valido = false;
            } else {
                errorTrabajador.classList.add("hidden");
            }

            if (observaciones.value.length > 200) {
                errorObservaciones.textContent = "Las observaciones no deben superar los 200 caracteres.";
                errorObservaciones.classList.remove("hidden");
                observaciones.classList.add("border-red-500");
                valido = false;
            } else {
                errorObservaciones.classList.add("hidden");
            }

            if (!valido) {
                e.preventDefault();
            } 
        });
    });
});

// Editar con dataset id
document.querySelectorAll(".form-editar-cartera").forEach(form => {
    let id = form.dataset.id;

    let fecha = document.getElementById("fecha-editar" + id);
    let errorFecha = document.getElementById("error-fecha-editar" + id);

    let inmueble = document.getElementById("inmueble-editar" + id);
    let errorInmueble = document.getElementById("error-inmueble-editar" + id);

    let estado = document.getElementById("estado-editar" + id);
    let errorEstado = document.getElementById("error-estado-editar" + id);

    let saldo = document.getElementById("saldo-editar" + id);
    let errorSaldo = document.getElementById("error-saldo-editar" + id);

    let trabajador = document.getElementById("trabajador-editar" + id);
    let errorTrabajador = document.getElementById("error-trabajador-editar" + id);

    let observaciones = document.getElementById("observaciones-editar" + id);
    let errorObservaciones = document.getElementById("error-observaciones-editar" + id);

    // 🔹 Validación en vivo
    fecha.addEventListener("input", () => {
        if (fecha.value) errorFecha.classList.add("hidden");
    });

    inmueble.addEventListener("change", () => {
        if (inmueble.value) errorInmueble.classList.add("hidden");
    });

    estado.addEventListener("change", () => {
        if (estado.value) errorEstado.classList.add("hidden");
    });

    saldo.addEventListener("input", () => {
        let s = parseFloat(saldo.value);
        if (saldo.value && !isNaN(s) && s >= 0) {
            errorSaldo.classList.add("hidden");
        }
    });

    trabajador.addEventListener("change", () => {
        if (trabajador.value) errorTrabajador.classList.add("hidden");
    });

    observaciones.addEventListener("input", () => {
        if (observaciones.value.length <= 200) {
            errorObservaciones.classList.add("hidden");
        }
    });

    // 🔹 Validación en submit
    form.addEventListener("submit", function(e) {
        let valido = true;

        if (!fecha.value) {
            errorFecha.classList.remove("hidden");
            valido = false;
        }
        if (!inmueble.value) {
            errorInmueble.classList.remove("hidden");
            valido = false;
        }
        if (!estado.value) {
            errorEstado.classList.remove("hidden");
            valido = false;
        }
        let saldoNum = parseFloat(saldo.value);
        if (!saldo.value || isNaN(saldoNum) || saldoNum < 0) {
            errorSaldo.classList.remove("hidden");
            valido = false;
        }
        if (!trabajador.value) {
            errorTrabajador.classList.remove("hidden");
            valido = false;
        }
        if (observaciones.value.length > 200) {
            errorObservaciones.classList.remove("hidden");
            valido = false;
        }

        if (!valido) {
            e.preventDefault();
        }
    });
});
