-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-04-2025 a las 04:44:05
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `stel`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cartera`
--

CREATE TABLE `cartera` (
  `pkidestado` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `fecha_actual` datetime NOT NULL,
  `saldo` decimal(10,2) NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `correspondencia`
--

CREATE TABLE `correspondencia` (
  `pkidcorrespondencia` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `fecha_recibido` datetime NOT NULL,
  `fecha_entrega` datetime DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  `tipo` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inmueble`
--

CREATE TABLE `inmueble` (
  `pkidinmueble` int(11) NOT NULL,
  `numeroinmueble` varchar(20) NOT NULL,
  `anden` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inmueble`
--

INSERT INTO `inmueble` (`pkidinmueble`, `numeroinmueble`, `anden`) VALUES
(1, '1', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `multa`
--

CREATE TABLE `multa` (
  `pkidmulta` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `fecha_pago` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `multa`
--

INSERT INTO `multa` (`pkidmulta`, `fecha`, `inmueble_id`, `tipo`, `valor`, `trabajador_id`, `fecha_pago`) VALUES
(1, '2025-04-16 23:56:24', 1, 'Estacionamiento indebido', 170000.00, 1, NULL),
(2, '2025-04-16 23:27:00', 1, 'Ruido Excesivo', 160000.00, 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `novedades`
--

CREATE TABLE `novedades` (
  `pkidnovedad` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `asunto` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parqueadero`
--

CREATE TABLE `parqueadero` (
  `pkidparqueadero` int(11) NOT NULL,
  `cupo` int(11) NOT NULL,
  `tarifa` decimal(10,2) NOT NULL,
  `residente_id` int(11) DEFAULT NULL,
  `visitante_id` int(11) DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  `fecha` datetime NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `placa` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `residente`
--

CREATE TABLE `residente` (
  `pkidresidente` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `residente`
--

INSERT INTO `residente` (`pkidresidente`, `usuario_id`, `inmueble_id`, `rol_id`) VALUES
(1, 2, 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `pkidrol` int(11) NOT NULL,
  `nombrerol` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`pkidrol`, `nombrerol`) VALUES
(1, 'Administrador'),
(2, 'Residente'),
(3, 'Trabajador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `trabajador`
--

CREATE TABLE `trabajador` (
  `pkidtrabajador` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `cargo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `trabajador`
--

INSERT INTO `trabajador` (`pkidtrabajador`, `usuario_id`, `rol_id`, `empresa`, `cargo`) VALUES
(1, 1, 1, 'Administradores Col', 'Administrador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `pkidturno` int(11) NOT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`pkidturno`, `usuario_id`, `fecha`, `hora_inicio`, `hora_fin`) VALUES
(10, 3, '2025-04-22', '06:00:00', '18:00:00'),
(11, 4, '2025-04-22', '18:00:00', '06:00:00'),
(12, 3, '2025-04-23', '06:00:00', '18:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `pkiduser` int(11) NOT NULL,
  `rol_id` int(11) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `celular` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`pkiduser`, `rol_id`, `cedula`, `correo`, `contraseña`, `celular`, `nombre`) VALUES
(1, 1, '14896542', 'alba_am@gmail.com', '$2b$12$/FPCCWf2v6/RsYqpppA1Y.Md4GLcz9V2nmbk4BdKauy6l9hfLQ7QG', '3104987985', 'Alba Amaya'),
(2, 2, '1047965406', 'danr@gmail.com', '$2b$12$9Z7/6NNzRCFG9Bka8JhO4uMIiIiFUYpUxsBdEC9LxwNeMWdRCMh0u', '3114987098', 'Daniel Reynolds'),
(3, 3, '56789012', 'juandelgado@gmail.com', '$2b$12$NCShdIVJvYu2/RiPg.3s5OwRfnNnvcFm5FdOXu2sRAqJBYXWHnf3y', '3219546650', 'Juan Delgado'),
(4, 3, '1014321659', 'isa_gar@gmail.com', 'I5@gr', '3151123080', 'Isabella García');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitante`
--

CREATE TABLE `visitante` (
  `pkidvisitante` int(11) NOT NULL,
  `ingresa_carro` tinyint(1) NOT NULL,
  `fecha` datetime NOT NULL,
  `autorizado` tinyint(1) NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `residente_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `cedula` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cartera`
--
ALTER TABLE `cartera`
  ADD PRIMARY KEY (`pkidestado`),
  ADD KEY `trabajador_id` (`trabajador_id`),
  ADD KEY `inmueble_id` (`inmueble_id`);

--
-- Indices de la tabla `correspondencia`
--
ALTER TABLE `correspondencia`
  ADD PRIMARY KEY (`pkidcorrespondencia`),
  ADD KEY `trabajador_id` (`trabajador_id`),
  ADD KEY `inmueble_id` (`inmueble_id`);

--
-- Indices de la tabla `inmueble`
--
ALTER TABLE `inmueble`
  ADD PRIMARY KEY (`pkidinmueble`);

--
-- Indices de la tabla `multa`
--
ALTER TABLE `multa`
  ADD PRIMARY KEY (`pkidmulta`),
  ADD KEY `trabajador_id` (`trabajador_id`),
  ADD KEY `inmueble_id` (`inmueble_id`);

--
-- Indices de la tabla `novedades`
--
ALTER TABLE `novedades`
  ADD PRIMARY KEY (`pkidnovedad`),
  ADD KEY `trabajador_id` (`trabajador_id`),
  ADD KEY `inmueble_id` (`inmueble_id`);

--
-- Indices de la tabla `parqueadero`
--
ALTER TABLE `parqueadero`
  ADD PRIMARY KEY (`pkidparqueadero`),
  ADD KEY `residente_id` (`residente_id`),
  ADD KEY `visitante_id` (`visitante_id`);

--
-- Indices de la tabla `residente`
--
ALTER TABLE `residente`
  ADD PRIMARY KEY (`pkidresidente`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `inmueble_id` (`inmueble_id`),
  ADD KEY `rol_id` (`rol_id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`pkidrol`);

--
-- Indices de la tabla `trabajador`
--
ALTER TABLE `trabajador`
  ADD PRIMARY KEY (`pkidtrabajador`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `rol_id` (`rol_id`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`pkidturno`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`pkiduser`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `rol_id` (`rol_id`);

--
-- Indices de la tabla `visitante`
--
ALTER TABLE `visitante`
  ADD PRIMARY KEY (`pkidvisitante`),
  ADD UNIQUE KEY `cedula` (`cedula`),
  ADD KEY `inmueble_id` (`inmueble_id`),
  ADD KEY `residente_id` (`residente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cartera`
--
ALTER TABLE `cartera`
  MODIFY `pkidestado` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `correspondencia`
--
ALTER TABLE `correspondencia`
  MODIFY `pkidcorrespondencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inmueble`
--
ALTER TABLE `inmueble`
  MODIFY `pkidinmueble` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `multa`
--
ALTER TABLE `multa`
  MODIFY `pkidmulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `novedades`
--
ALTER TABLE `novedades`
  MODIFY `pkidnovedad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `parqueadero`
--
ALTER TABLE `parqueadero`
  MODIFY `pkidparqueadero` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `residente`
--
ALTER TABLE `residente`
  MODIFY `pkidresidente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `pkidrol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `trabajador`
--
ALTER TABLE `trabajador`
  MODIFY `pkidtrabajador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `pkidturno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `pkiduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `visitante`
--
ALTER TABLE `visitante`
  MODIFY `pkidvisitante` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cartera`
--
ALTER TABLE `cartera`
  ADD CONSTRAINT `cartera_ibfk_1` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`pkidtrabajador`),
  ADD CONSTRAINT `cartera_ibfk_2` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`);

--
-- Filtros para la tabla `correspondencia`
--
ALTER TABLE `correspondencia`
  ADD CONSTRAINT `correspondencia_ibfk_1` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`pkidtrabajador`),
  ADD CONSTRAINT `correspondencia_ibfk_2` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`);

--
-- Filtros para la tabla `multa`
--
ALTER TABLE `multa`
  ADD CONSTRAINT `multa_ibfk_1` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`pkidtrabajador`),
  ADD CONSTRAINT `multa_ibfk_2` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`);

--
-- Filtros para la tabla `novedades`
--
ALTER TABLE `novedades`
  ADD CONSTRAINT `novedades_ibfk_1` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador` (`pkidtrabajador`),
  ADD CONSTRAINT `novedades_ibfk_2` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`);

--
-- Filtros para la tabla `parqueadero`
--
ALTER TABLE `parqueadero`
  ADD CONSTRAINT `parqueadero_ibfk_1` FOREIGN KEY (`residente_id`) REFERENCES `residente` (`pkidresidente`),
  ADD CONSTRAINT `parqueadero_ibfk_2` FOREIGN KEY (`visitante_id`) REFERENCES `visitante` (`pkidvisitante`);

--
-- Filtros para la tabla `residente`
--
ALTER TABLE `residente`
  ADD CONSTRAINT `residente_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`pkiduser`),
  ADD CONSTRAINT `residente_ibfk_2` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`),
  ADD CONSTRAINT `residente_ibfk_3` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`pkidrol`);

--
-- Filtros para la tabla `trabajador`
--
ALTER TABLE `trabajador`
  ADD CONSTRAINT `trabajador_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`pkiduser`),
  ADD CONSTRAINT `trabajador_ibfk_2` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`pkidrol`);

--
-- Filtros para la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `turnos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`pkiduser`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`pkidrol`);

--
-- Filtros para la tabla `visitante`
--
ALTER TABLE `visitante`
  ADD CONSTRAINT `visitante_ibfk_1` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`),
  ADD CONSTRAINT `visitante_ibfk_2` FOREIGN KEY (`residente_id`) REFERENCES `residente` (`pkidresidente`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
