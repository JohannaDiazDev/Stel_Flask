document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('multaForm');
    if (form) {
        const fecha = form.querySelector("input[name='fecha']");
        const inmueble = form.querySelector("select[name='inmueble_id']");
        const tipo = form.querySelector("select[name='tipo']");
        const valor = form.querySelector("input[name='valor']");
        const trabajador = form.querySelector("select[name='trabajador_id']");
        const fechaPago = form.querySelector("input[name='fecha_pago']");

        const errorFecha = document.getElementById('error-fecha');
        const errorValor = document.getElementById('error-valor');
        const errorTipo = document.getElementById('error-tipo');
        const errorInmueble = document.getElementById('error-inmueble');
        const errorTrabajador = document.getElementById('error-trabajador');
        const errorFechaPago = document.getElementById('error-fecha-pago');


        // Validaciones en vivo
        fecha.addEventListener('input', () => {
            if (fecha.value) {
                errorFecha.classList.add('hidden');
                fecha.classList.remove('border-red-500');
                fecha.classList.add('border-[#1E4C40]');
            }
        });

        valor.addEventListener('input', () => {
            const num = parseFloat(valor.value);
            if (!isNaN(num) && num >= 50000 && num <= 250000) {
                errorValor.classList.add('hidden');
                valor.classList.remove('border-red-500');
                valor.classList.add('border-[#1E4C40]');
            }
        });

        tipo.addEventListener('change', () => {
            if (tipo.value) {
                errorTipo.classList.add('hidden');
                tipo.classList.remove('border-red-500');
                tipo.classList.add('border-[#1E4C40]');
            }
        });

        inmueble.addEventListener('change', () => {
            if (inmueble.value) {
                errorInmueble.classList.add('hidden');
                inmueble.classList.remove('border-red-500');
                inmueble.classList.add('border-[#1E4C40]');
            }
        });

        trabajador.addEventListener('change', () => {
            if (trabajador.value) {
                errorTrabajador.classList.add('hidden');
                trabajador.classList.remove('border-red-500');
                trabajador.classList.add('border-[#1E4C40]');
            }
        });

        // Validación al enviar
        form.addEventListener('submit', (e) => {
            let valido = true;

            [fecha, valor, tipo, inmueble, trabajador, fechaPago].forEach(el => {
                el.classList.remove('border-red-500');
                el.classList.add('border-[#1E4C40]');
            });

            [errorFecha, errorValor, errorTipo, errorInmueble, errorTrabajador, errorFechaPago].forEach(el => {
                el.classList.add('hidden');
            });

            if (!tipo.value) {
                tipo.classList.add('border-red-500');
                tipo.classList.remove('border-[#1E4C40]');
                errorTipo.classList.remove('hidden');
                valido = false;
            }

            if (!fecha.value) {
                fecha.classList.add('border-red-500');
                fecha.classList.remove('border-[#1E4C40]');
                errorFecha.classList.remove('hidden');
                valido = false;
            } 

            const valorNum = parseFloat(valor.value);
            if (!valor.value || isNaN(valorNum) || valorNum < 50000 || valorNum > 250000) {
                valor.classList.add('border-red-500');
                valor.classList.remove('border-[#1E4C40]');
                errorValor.classList.remove('hidden');
                valido = false;
            }

            if (!inmueble.value) {
                inmueble.classList.add('border-red-500');
                inmueble.classList.remove('border-[#1E4C40]');
                errorInmueble.classList.remove('hidden');
                valido = false;
            }

            if (!trabajador.value) {
                trabajador.classList.add('border-red-500');
                trabajador.classList.remove('border-[#1E4C40]');
                errorTrabajador.classList.remove('hidden');
                valido = false;
            }

            if (fechaPago && fechaPago.value) {
                const f = new Date(fecha.value);
                const fp = new Date(fechaPago.value);
                if (fp < f) { // no puede ser antes de la multa
                    fechaPago.classList.add('border-red-500');
                    fechaPago.classList.remove('border-[#1E4C40]');
                    errorFechaPago.classList.remove('hidden');
                    valido = false;
                }
            }

            if (!valido) e.preventDefault();
        });
    }

    // Formularios de editar (puede haber varios)
    document.querySelectorAll('.form-editar-multa').forEach(form => {
        const id = form.dataset.id;

        const fecha = form.querySelector(`#fecha-editar${id}`);
        const valor = form.querySelector(`#valor-editar${id}`);
        const tipo = form.querySelector(`#tipo-editar${id}`);
        const inmueble = form.querySelector(`#inmueble-editar${id}`);
        const trabajador = form.querySelector(`#trabajador-editar${id}`);
        const fechaPago = form.querySelector(`#fecha-pago-editar${id}`); // campo extra

        const errorFecha = form.querySelector(`#error-fecha-editar${id}`);
        const errorValor = form.querySelector(`#error-valor-editar${id}`);
        const errorTipo = form.querySelector(`#error-tipo-editar${id}`);
        const errorInmueble = form.querySelector(`#error-inmueble-editar${id}`);
        const errorTrabajador = form.querySelector(`#error-trabajador-editar${id}`);
        const errorFechaPago = form.querySelector(`#error-fecha-pago-editar${id}`);

        const today = new Date().toISOString().split('T')[0];

        // Envío
        form.addEventListener('submit', (e) => {
            let valido = true;

            [fecha, valor, tipo, inmueble, trabajador, fechaPago].forEach(el => {
                el.classList.remove('border-red-500');
                el.classList.add('border-[#1E4C40]');
            });

            [errorFecha, errorValor, errorTipo, errorInmueble, errorTrabajador, errorFechaPago].forEach(el => {
                el.classList.add('hidden');
            });

            if (!tipo.value) {
                tipo.classList.add('border-red-500');
                tipo.classList.remove('border-[#1E4C40]');
                errorTipo.classList.remove('hidden');
                valido = false;
            }

            if (!fecha.value) {
                fecha.classList.add('border-red-500');
                fecha.classList.remove('border-[#1E4C40]');
                errorFecha.classList.remove('hidden');
                valido = false;
            } 

            const valorNum = parseFloat(valor.value);
            if (!valor.value || isNaN(valorNum) || valorNum < 50000 || valorNum > 250000) {
                valor.classList.add('border-red-500');
                valor.classList.remove('border-[#1E4C40]');
                errorValor.classList.remove('hidden');
                valido = false;
            }

            if (!inmueble.value) {
                inmueble.classList.add('border-red-500');
                inmueble.classList.remove('border-[#1E4C40]');
                errorInmueble.classList.remove('hidden');
                valido = false;
            }

            if (!trabajador.value) {
                trabajador.classList.add('border-red-500');
                trabajador.classList.remove('border-[#1E4C40]');
                errorTrabajador.classList.remove('hidden');
                valido = false;
            }

            if (fechaPago.value) {
                const f = new Date(fecha.value);
                const fp = new Date(fechaPago.value);
                if (fp <= f) {
                    fechaPago.classList.add('border-red-500');
                    fechaPago.classList.remove('border-[#1E4C40]');
                    errorFechaPago.classList.remove('hidden');
                    valido = false;
                }
            }
 
            if (!valido) e.preventDefault();
        });
    });
});
