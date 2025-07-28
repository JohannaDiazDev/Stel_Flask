document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('formParqueo');
    if (!form) return;

    const cupo = form.querySelector("input[name='cupo']");
    const estado = form.querySelector("select[name='estado']");
    const fecha = form.querySelector("input[name='fecha']"); 
    const tipo = form.querySelector("select[name='tipo']");
    const placa = form.querySelector("input[name='placa']");
    const residente = form.querySelector("select[name='residente_id']");
    const visitante = form.querySelector("select[name='visitante_id']");
    
    const errorCupo = document.getElementById('error-cupo');
    const errorEstado = document.getElementById('error-estado');
    const errorFecha = document.getElementById('error-fecha');
    const errorTipo = document.getElementById('error-tipo');
    const errorPlaca = document.getElementById('error-placa'); 
    const errorPersona = document.getElementById('error-persona');

    tipo.addEventListener('change', () => {
        if (tipo.value && (tipo.value === 'carro' || tipo.value === 'moto' )) {
            tipo.classList.remove('border-red-500');
            tipo.classList.add('border-[#1E4C40]');
            errorTipo.classList.add('hidden');
        }
        validarCupo();
    });

    cupo.addEventListener('input', () => {
        validarCupo();
    });

    function validarCupo() {
        const valor = parseInt(cupo.value);
        const tipoValor = tipo.value;
        let valido = false;

        if (tipoValor === 'carro') {
            valido = valor >= 1 && valor <= 55;
        } else if (tipoValor === 'moto') {
            valido = valor >= 1 && valor <= 35;
        }

        if (valido) {
            cupo.classList.remove('border-red-500');
            cupo.classList.add('border-[#1E4C40]');
            errorCupo.classList.add('hidden');
        } else {
            cupo.classList.add('border-red-500');
            cupo.classList.remove('border-[#1E4C40]');
            errorCupo.classList.remove('hidden');
        }

        return valido;
    }

    estado.addEventListener('change', () => {
        if (estado.value === 'disponible' || estado.value === 'ocupado') {
            estado.classList.remove('border-red-500');
            estado.classList.add('border-[#1E4C40]');
            errorEstado.classList.add('hidden');
        }
    });

    fecha.addEventListener('input', () => {
        if (fecha.value) {
            fecha.classList.remove('border-red-500');
            fecha.classList.add('border-[#1E4C40]');
            errorFecha.classList.add('hidden');
        }
    });

    placa.addEventListener('input', () => {
        const valor = placa.value.trim();
        if (valor.length >= 6 && valor.length <= 7) {
            placa.classList.remove('border-red-500');
            placa.classList.add('border-[#1E4C40]');
            errorPlaca.classList.add('hidden');
        }
    });

    function validarPersona() {
        if (residente.value || visitante.value) {
            errorPersona.classList.add('hidden');
            residente.classList.remove('border-red-500');
            visitante.classList.remove('border-red-500');
        } else {
            errorPersona.classList.remove('hidden');
            residente.classList.add('border-red-500');
            visitante.classList.add('border-red-500');
        }
    }

    residente.addEventListener('change', validarPersona);
    visitante.addEventListener('change', validarPersona);

    form.addEventListener('submit', (e) => {
        let valido = true;

        [cupo, tipo, estado, fecha, placa, residente, visitante].forEach(el => {
            el.classList.remove('border-red-500');
            el.classList.add('border-[#1E4C40]');
        });

        [errorCupo, errorTipo, errorEstado, errorFecha, errorPlaca, errorPersona].forEach(el => {
            el.classList.add('hidden');
        });

        if (!tipo.value || !['carro', 'moto'].includes(tipo.value)) {
            tipo.classList.add('border-red-500');
            tipo.classList.remove('border-[#1E4C40]');
            errorTipo.classList.remove('hidden');
            valido = false;
        }

        if (!validarCupo()) {
            valido = false;
        }

        if (!estado.value || !['disponible', 'ocupado'].includes(estado.value)) {
            estado.classList.add('border-red-500');
            estado.classList.remove('border-[#1E4C40]');
            errorEstado.classList.remove('hidden');
            valido = false;
        }

        if (!fecha.value) {
            fecha.classList.add('border-red-500');
            fecha.classList.remove('border-[#1E4C40]');
            errorFecha.classList.remove('hidden');
            valido = false;
        }

        const placaVal = placa.value.trim();
        if (placaVal.length < 6 || placaVal.length > 7) {
            placa.classList.add('border-red-500');
            placa.classList.remove('border-[#1E4C40]');
            errorPlaca.classList.remove('hidden');
            valido = false;
        }

        if (!residente.value && !visitante.value) {
            errorPersona.classList.remove('hidden');
            residente.classList.add('border-red-500');
            visitante.classList.add('border-red-500');
            valido = false;
        } else {
            errorPersona.classList.add('hidden');
            residente.classList.remove('border-red-500');
            visitante.classList.remove('border-red-500');
        }

        if (!valido) {
            e.preventDefault();
        }

    }); 
});

// Validaciones editar parqueadero

document.querySelectorAll('.form-editar-parqueo').forEach(form => {
    const id = form.dataset.id;

    const cupo = form.querySelector(`#cupo-editar${id}`);
    const tipo = form.querySelector(`#tipo-editar${id}`);
    const estado = form.querySelector(`#estado-editar${id}`);
    const fecha = form.querySelector(`#fecha-editar${id}`);
    const horaSalida = form.querySelector(`#hora-salida-editar${id}`);
    const placa = form.querySelector(`#placa-editar${id}`);
    const residente = form.querySelector(`#residente-editar${id}`);
    const visitante = form.querySelector(`#visitante-editar${id}`); 

    const errorCupo = form.querySelector(`#error-cupo-editar${id}`);
    const errorTipo = form.querySelector(`#error-tipo-editar${id}`);
    const errorEstado = form.querySelector(`#error-estado-editar${id}`);
    const errorFecha = form.querySelector(`#error-fecha-editar${id}`);
    const errorHoraSalida = form.querySelector(`#error-hora-salida-editar${id}`);
    const errorPlaca = form.querySelector(`#error-placa-editar${id}`);
    const errorPersona = form.querySelector(`#error-persona-editar${id}`);

    function validarCupoEdicion() {
        const valor = parseInt(cupo.value);
        const tipoValor = tipo.value;
        let valido = false;

        if (tipoValor === 'carro') {
            valido = valor >= 1 && valor <= 55;
        } else if (tipoValor === 'moto') {
            valido = valor >= 1 && valor <= 35;
        }

        if (valido) {
            cupo.classList.remove('border-red-500');
            cupo.classList.add('border-[#1E4C40]');
            errorCupo.classList.add('hidden');
        } else {
            cupo.classList.add('border-red-500');
            cupo.classList.remove('border-[#1E4C40]');
            errorCupo.classList.remove('hidden');
        }
        return valido;
    }

    tipo.addEventListener('change', () => {
        if (['carro', 'moto'].includes(tipo.value)) {
            tipo.classList.remove('border-red-500');
            tipo.classList.add('border-[#1E4C40]');
            errorTipo.classList.add('hidden');
        }
        validarCupoEdicion();
    });

    cupo.addEventListener('input', validarCupoEdicion);

    function validarPersonaEdicion() {
        if (residente.value || visitante.value) {
            errorPersona.classList.add('hidden');
            residente.classList.remove('border-red-500');
            visitante.classList.remove('border-red-500');
        } else {
            errorPersona.classList.remove('hidden');
            residente.classList.add('border-red-500');
            visitante.classList.add('border-red-500');
        }
    }

    residente.addEventListener('change', validarPersonaEdicion);
    visitante.addEventListener('change', validarPersonaEdicion);

    fecha.addEventListener('input', () => {
        if (fecha.value) {
            fecha.classList.remove('border-red-500');
            fecha.classList.add('border-[#1E4C40]');
            errorFecha.classList.add('hidden');
        }
    });

    placa.addEventListener('input', () => {
        if (placa.value.trim().length < 6 || placa.value.trim().length > 7) {
            placa.classList.remove('border-red-500');
            placa.classList.add('border-[#1E4C40]');
            errorPlaca.classList.add('hidden');
        }
    });

    estado.addEventListener('change', () => {
        if (['disponible', 'ocupado'].includes(estado.value)) {
            estado.classList.remove('border-red-500');
            estado.classList.add('border-[#1E4C40]');
            errorEstado.classList.add('hidden');
        }
    });
    if (horaSalida) {
        horaSalida.addEventListener("input", () => {
            if (fecha.value && horaSalida.value) {
                const fechaVal = new Date(fecha.value);
                const salidaVal = new Date(horaSalida.value);

                if (salidaVal > fechaVal) {
                    errorHoraSalida.classList.add("hidden");
                    horaSalida.classList.remove("border-red-500");
                    horaSalida.classList.add("border-[#1E4C40]");
                }
            }
        });
    }

    form.addEventListener('submit', e => {
        let valido = true;

        [cupo, tipo, estado, fecha, placa, residente, visitante].forEach(el => {
            el.classList.remove('border-red-500');
            el.classList.add('border-[#1E4C40]');
        });

        [errorCupo, errorTipo, errorEstado, errorFecha, errorPlaca, errorPersona].forEach(el => {
            el.classList.add('hidden');
        });

        if (!['carro', 'moto'].includes(tipo.value)) {
            tipo.classList.add('border-red-500');
            tipo.classList.remove('border-[#1E4C40]');
            errorTipo.classList.remove('hidden');
            valido = false;
        }

        if (!validarCupoEdicion()) {
            valido = false;
        }

        if (!['disponible', 'ocupado'].includes(estado.value)) {
            estado.classList.add('border-red-500');
            estado.classList.remove('border-[#1E4C40]');
            errorEstado.classList.remove('hidden');
            valido = false;
        }

        if (!fecha.value) {
            fecha.classList.add('border-red-500');
            fecha.classList.remove('border-[#1E4C40]');
            errorFecha.classList.remove('hidden');
            valido = false;
        }


        if (horaSalida && fecha && horaSalida.value && fecha.value) {
            const fechaVal = new Date(fecha.value);
            const salidaVal = new Date(horaSalida.value);

            if (salidaVal <= fechaVal) {
                errorHoraSalida.classList.remove("hidden");
                horaSalida.classList.add("border-red-500");
                horaSalida.classList.remove("border-[#1E4C40]");
                valido = false;
            } else {
                errorHoraSalida.classList.add("hidden");
                horaSalida.classList.remove("border-red-500");
                horaSalida.classList.add("border-[#1E4C40]");
            }
        }

        if (placa.value.trim().length < 6 || placa.value.trim() > 7) {
            placa.classList.add('border-red-500');
            placa.classList.remove('border-[#1E4C40]');
            errorPlaca.classList.remove('hidden');
            valido = false;
        }

        if (!residente.value && !visitante.value) {
            errorPersona.classList.remove('hidden');
            residente.classList.add('border-red-500');
            visitante.classList.add('border-red-500');
            valido = false;
        } else {
            errorPersona.classList.add('hidden');
            residente.classList.remove('border-red-500');
            visitante.classList.remove('border-red-500');
        }

        if (!valido) {
            e.preventDefault();
        }
    });
});