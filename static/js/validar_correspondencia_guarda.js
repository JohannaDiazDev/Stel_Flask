document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('formPaquete');
    if (form) {
        const inmueble = form.querySelector("select[name='inmueble_id']");
        const descripcion = form.querySelector("textarea[name='descripcion']");
        const errorInmueble = document.getElementById('error-inmueble');
        const errorDescripcion = document.getElementById('error-descripcion');

        // Validación en vivo
        descripcion.addEventListener('input', () => {
            const desc = descripcion.value.trim();
            if (desc.length >= 3 && desc.length <= 200) {
                errorDescripcion.classList.add('hidden');
                descripcion.classList.remove('border-red-500');
                descripcion.classList.add('border-[#1E4C40]');
            }
        });

        inmueble.addEventListener('change', () => {
            if (inmueble.value) {
                errorInmueble.classList.add('hidden');
                inmueble.classList.remove('border-red-500');
                inmueble.classList.add('border-[#1E4C40]');
            }
        });

        // Validación al enviar
        form.addEventListener('submit', function (e) {
            let valido = true;

            [errorInmueble, errorDescripcion].forEach(el => el.classList.add('hidden'));
            [inmueble, descripcion].forEach(el => el.classList.remove('border-red-500'));

            const desc = descripcion.value.trim();
            if (!inmueble.value) {
                errorInmueble.classList.remove('hidden');
                inmueble.classList.add('border-red-500');
                inmueble.classList.remove('border-[#1E4C40]');
                valido = false;
            }
            if (!desc || desc.length < 3 || desc.length > 200) {
                errorDescripcion.classList.remove('hidden');
                descripcion.classList.add('border-red-500');
                descripcion.classList.remove('border-[#1E4C40]');
                valido = false;
            }

            if (!valido) e.preventDefault();
        });
    }

    // Validaciones para todos los formularios de editar
    document.querySelectorAll('.form-editar-paquete').forEach(form => {
        const id = form.dataset.id;

        const descripcion = form.querySelector(`#descripcion-editar${id}`);
        const estado = form.querySelector(`#estado-editar${id}`); 
        const fechaEntrega = form.querySelector(`#fecha-entrega-editar${id}`);
        const fechaRecibido = form.querySelector(`#fecha-recibido-editar${id}`);

        const errorDescripcion = form.querySelector(`#error-editar-descripcion${id}`);
        const errorEstado = form.querySelector(`#error-editar-estado${id}`);
        const errorFechaEntrega = form.querySelector(`#error-editar-fecha-entrega${id}`);

        // Validación en vivo - descripción
        descripcion.addEventListener('input', () => {
            const val = descripcion.value.trim();
            if (val.length >= 3 && val.length <= 200) {
                descripcion.classList.remove('border-red-500');
                descripcion.classList.add('border-[#1E4C40]');
                errorDescripcion.classList.add('hidden');
            }
        });

        // Validación en vivo - estado
        estado.addEventListener('change', () => {
            if (['Entregado', 'No Entregado'].includes(estado.value)) {
                estado.classList.remove('border-red-500');
                estado.classList.add('border-[#1E4C40]');
                errorEstado.classList.add('hidden');
            }
        });

        // Validación en vivo - fecha entrega posterior a recibida
        fechaEntrega.addEventListener('input', () => {
            if (fechaEntrega.value && fechaRecibido && fechaRecibido.value) {
                const fEntrega = new Date(fechaEntrega.value);
                const fRecibido = new Date(fechaRecibido.value);

                if (fEntrega >= fRecibido) {
                    fechaEntrega.classList.remove('border-red-500');
                    fechaEntrega.classList.add('border-[#1E4C40]');
                    errorFechaEntrega.classList.add('hidden');
                }
            }
        });

        form.addEventListener('submit', (e) => {
            let valido = true;

            [descripcion, estado, fechaEntrega].forEach(el => {
                el.classList.remove('border-red-500');
                el.classList.add('border-[#1E4C40]');
            });

            [errorDescripcion, errorEstado, errorFechaEntrega].forEach(el => {
                el.classList.add('hidden');
            });

            const descripcionVal = descripcion.value.trim();
            if (descripcionVal.length < 3 || descripcionVal.length > 200) {
                descripcion.classList.add('border-red-500');
                descripcion.classList.remove('border-[#1E4C40]');
                errorDescripcion.classList.remove('hidden');
                valido = false;
            }

            if (!estado.value || !['Entregado', 'No Entregado'].includes(estado.value)) {
                estado.classList.add('border-red-500');
                estado.classList.remove('border-[#1E4C40]');
                errorEstado.classList.remove('hidden');
                valido = false;
            }

            if (fechaEntrega.value && fechaRecibido && fechaRecibido.value) {
                const fEntrega = new Date(fechaEntrega.value);
                const fRecibido = new Date(fechaRecibido.value);

                if (fEntrega < fRecibido) {
                    fechaEntrega.classList.add('border-red-500');
                    fechaEntrega.classList.remove('border-[#1E4C40]');
                    errorFechaEntrega.classList.remove('hidden');
                    valido = false;
                }
            }

            if (!valido) e.preventDefault();
        });
    });
});
