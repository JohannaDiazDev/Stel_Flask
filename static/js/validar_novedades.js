document.addEventListener("DOMContentLoaded", () => {
    const formularios = document.querySelectorAll(".form-novedad");

    const expresionAsunto = /^.{5,100}$/;
    const expresionDescripcion = /^.{10,500}$/;

    formularios.forEach(form => {
        const trabajador = form.querySelector(".input-trabajador");
        const fecha = form.querySelector(".input-fecha");
        const tipo = form.querySelector(".input-tipo");
        const asunto = form.querySelector(".input-asunto");
        const descripcion = form.querySelector(".input-descripcion");
        const estado = form.querySelector(".input-estado");

        const errorTrabajador = form.querySelector(".error-trabajador");
        const errorFecha = form.querySelector(".error-fecha");
        const errorTipo = form.querySelector(".error-tipo");
        const errorAsunto = form.querySelector(".error-asunto");
        const errorDescripcion = form.querySelector(".error-descripcion");
        const errorEstado = form.querySelector(".error-estado");

        form.addEventListener("submit", e => {
            let valido = true;

            // Limpiar estilos previos
            [trabajador, fecha, tipo, asunto, descripcion, estado].forEach(el => {
                if (el) el.classList.remove("border-red-500");
            });
            [errorTrabajador, errorFecha, errorTipo, errorAsunto, errorDescripcion, errorEstado].forEach(el => {
                if (el) el.classList.add("hidden");
            });

            if (trabajador && !trabajador.value) {
                errorTrabajador.classList.remove("hidden");
                trabajador.classList.add("border-red-500");
                valido = false;
            }

            if (!fecha.value) {
                errorFecha.classList.remove("hidden");
                fecha.classList.add("border-red-500");
                valido = false;
            }

            if (!tipo.value || !["Solicitud", "Queja", "Reporte"].includes(tipo.value)) {
                errorTipo.classList.remove("hidden");
                tipo.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionAsunto.test(asunto.value.trim())) {
                errorAsunto.classList.remove("hidden");
                asunto.classList.add("border-red-500");
                valido = false;
            }

            if (!expresionDescripcion.test(descripcion.value.trim())) {
                errorDescripcion.classList.remove("hidden");
                descripcion.classList.add("border-red-500");
                valido = false;
            }

            if (!estado.value || !["Pendiente", "Proceso", "Resuelto"].includes(estado.value)) {
                errorEstado.classList.remove("hidden");
                estado.classList.add("border-red-500");
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
            }
        });

        // Validaciones en vivo
        if (trabajador) {
            trabajador.addEventListener("change", () => {
                if (!trabajador.value) {
                    errorTrabajador.classList.remove("hidden");
                    trabajador.classList.add("border-red-500");
                } else {
                    errorTrabajador.classList.add("hidden");
                    trabajador.classList.remove("border-red-500");
                }
            });
        }

        fecha.addEventListener("change", () => {
            if (!fecha.value) {
                errorFecha.classList.remove("hidden");
                fecha.classList.add("border-red-500");
            } else {
                errorFecha.classList.add("hidden");
                fecha.classList.remove("border-red-500");
            }
        });

        tipo.addEventListener("change", () => {
            if (!["Solicitud", "Queja", "Reporte"].includes(tipo.value)) {
                errorTipo.classList.remove("hidden");
                tipo.classList.add("border-red-500");
            } else {
                errorTipo.classList.add("hidden");
                tipo.classList.remove("border-red-500");
            }
        });

        asunto.addEventListener("input", () => {
            if (!expresionAsunto.test(asunto.value.trim())) {
                errorAsunto.classList.remove("hidden");
                asunto.classList.add("border-red-500");
            } else {
                errorAsunto.classList.add("hidden");
                asunto.classList.remove("border-red-500");
            }
        });

        descripcion.addEventListener("input", () => {
            if (!expresionDescripcion.test(descripcion.value.trim())) {
                errorDescripcion.classList.remove("hidden");
                descripcion.classList.add("border-red-500");
            } else {
                errorDescripcion.classList.add("hidden");
                descripcion.classList.remove("border-red-500");
            }
        });

        estado.addEventListener("change", () => {
            if (!["Pendiente", "Proceso", "Resuelto"].includes(estado.value)) {
                errorEstado.classList.remove("hidden");
                estado.classList.add("border-red-500");
            } else {
                errorEstado.classList.add("hidden");
                estado.classList.remove("border-red-500");
            }
        });
    });
});
