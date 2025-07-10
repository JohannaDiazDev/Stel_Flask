-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-07-2025 a las 06:15:52
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
  `fecha_actual` datetime NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `saldo` decimal(10,2) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cartera`
--

INSERT INTO `cartera` (`pkidestado`, `fecha_actual`, `inmueble_id`, `estado`, `saldo`, `trabajador_id`, `observaciones`) VALUES
(1, '2025-04-24 18:41:00', 1, 'Paz y Salvo', 0.00, 1, ''),
(4, '2025-04-29 17:57:00', 2, 'Moroso', 150000.00, 1, '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `correspondencia`
--

CREATE TABLE `correspondencia` (
  `pkidcorrespondencia` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `inmueble_id` int(11) DEFAULT NULL,
  `fecha_recibido` datetime NOT NULL,
  `fecha_entrega` datetime DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `tipo` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `correspondencia`
--

INSERT INTO `correspondencia` (`pkidcorrespondencia`, `trabajador_id`, `inmueble_id`, `fecha_recibido`, `fecha_entrega`, `descripcion`, `tipo`, `estado`) VALUES
(1, 1, NULL, '2025-05-29 00:00:00', NULL, '<p class=\"text-center\"><strong>CONJUNTO RESIDENCIAL</strong></p>\r\n            <p class=\"text-center\"><strong>QUINTAS DEL RECREO ETAPA 1 P.H.</strong></p>\r\n            <p class=\"text-center\"><strong>Nit. 830132858-1</strong></p>\r\n            <p><strong>CONVOCATORIA ASAMBLEA GENERAL ORDINARIA DE COPROPIETARIOS</strong></p>\r\n            <p><strong>Señor(a)</strong></p>\r\n            <p><strong>COPROPIETARIO(A)</strong></p>\r\n            <p><strong>CONJUNTO RESIDENCIAL QUINTAS DEL RECREO ETAPA 1</strong></p>\r\n            <p><strong>CIUDAD</strong></p>\r\n            <p><strong>Asamblea: <u>General</u></strong></p>\r\n            <p><strong>Fecha: 15 de mayo de 2025</strong></p><p><strong><strong></strong>Hora: <u>10:00 am</u></strong></p><strong>\r\n            <p><strong></strong>Medio: Presencial</p><br><br>\r\n            <p>En mi calidad de Administradora y Representante Legal del <strong>Conjunto Residencial Quintas Del Recreo Etapa I Propiedad Horizontal</strong></p>en cumplimiento de las funciones Legales y Estatutarias consagradas en el reglamento de propiedad horizontal artículo 39 de la Ley 675 de 2001,<p></p>\r\n            <p>me permito convocar a todos los copropietarios a la celebración de la <strong>ASAMBLEA GENERAL ORDINARIA,</strong> la cual se llevará a cabo el <u>15 de mayo a las 10 am</u>, en el <u>parqueadero</u></p>    \r\n            <p>Atentamente,<br><br><strong>Administración.</strong></p></strong>', 'Carta Administración', 'generado'),
(2, 1, NULL, '2025-05-29 00:00:00', NULL, '<p><strong>Reunión Andén</strong></p>\r\n            <p><strong>Señores Copropietarios del andén <u>__5_</u>:</strong></p>\r\n            <p>Se le convoca a una reunión para tratar temas relacionados con su andén, el día <u>03 de junio</u> a las <u>07: pm</u>.</p>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración', 'generado'),
(3, 1, NULL, '2025-05-29 00:00:00', NULL, '<p><strong>Reunión Andén</strong></p>\r\n            <p><strong>Señores Copropietarios del andén <u>__5_</u>:</strong></p>\r\n            <p>Se le convoca a una reunión para tratar temas relacionados con su andén, el día <u>03 de junio</u> a las <u>07: pm</u>.</p>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración', 'generado'),
(4, 1, NULL, '2025-05-29 00:00:00', NULL, '<p><strong>Reunión Andén</strong></p>\r\n            <p><strong>Señores Copropietarios del andén <u>__5_</u>:</strong></p>\r\n            <p>Se le convoca a una reunión para tratar temas relacionados con su andén, el día <u>03 de junio</u> a las <u>07: pm</u>.</p>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración', 'generado'),
(5, 1, NULL, '2025-05-29 00:00:00', NULL, '<p><strong>Reunión de Parqueadero</strong></p>\r\n            <p><strong>Señor(a) Copropietario(a)</strong></p>\r\n            <p>Me permito convocarlo a una reunión sobre el uso y organización del parqueadero, el día <u>24 de junio</u> a las <u>07:00pm</u>.</p>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración', 'generado'),
(6, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(7, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(8, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(9, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(10, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(11, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(12, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(13, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(14, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(15, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(16, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(17, 1, NULL, '2025-05-29 00:00:00', NULL, '\r\n            <div class=\"bg-[#FFF6E5] p-6 rounded-xl border-2 border-[#A65B00] shadow-md relative\">\r\n                <div class=\"absolute -top-4 left-4 bg-[#A65B00] text-white px-3 py-1 rounded-full text-sm flex items-center gap-2 shadow\">\r\n                    <i class=\"bi bi-stars\"></i> Evento Especial\r\n                </div>\r\n                <h1 class=\"text-center text-2xl font-bold text-[#A65B00] mb-4\"><u>__________</u></h1>\r\n                <p class=\"mb-2\">Queridos <u>niños</u>&nbsp;del conjunto,</p>\r\n                <p class=\"mb-2\">Con mucho cariño los invitamos a celebrar su día en una tarde llena de amor, alegría y gratitud.</p>\r\n                <p class=\"mb-2 font-semibold text-center text-[#A65B00]\">¡Los esperamos!</p>\r\n                <p class=\"mb-2 text-center\"><strong>El día 15 de junio&nbsp;a las <u>3:00 pm</u></strong></p>\r\n                <p class=\"mb-4 text-center\"><strong>En el parque<u>______</u> del Conjunto.</strong></p>\r\n                <p class=\"text-right\">Atentamente,<br><strong>Administración</strong></p>\r\n            </div>', 'Carta Administración', 'generado'),
(18, 1, NULL, '2025-06-04 00:00:00', NULL, '<p class=\"text-center\"><strong>CONJUNTO RESIDENCIAL</strong></p>\r\n            <p class=\"text-center\"><strong>QUINTAS DEL RECREO ETAPA 1 P.H.</strong></p>\r\n            <p class=\"text-center\"><strong>Nit. 830132858-1</strong></p><br>\r\n            <p><strong>CONVOCATORIA ASAMBLEA GENERAL ORDINARIA DE COPROPIETARIOS</strong></p>\r\n            <p><strong>Señor(a)</strong></p>\r\n            <p><strong>COPROPIETARIO(A)</strong></p>\r\n            <p><strong>CONJUNTO RESIDENCIAL QUINTAS DEL RECREO ETAPA 1</strong></p>\r\n            <p><strong>CIUDAD</strong></p>\r\n            <p><strong>Asamblea: <u>__________</u></strong></p>\r\n            <p><strong>Fecha: \r\n            </strong></p><p><strong><strong></strong>Hora: <u>_____</u></strong></p><strong>\r\n            <p><strong></strong>Medio: Presencial</p><br><br>\r\n            <p>En mi calidad de Administradora y Representante Legal del <strong>Conjunto Residencial Quintas Del Recreo Etapa I Propiedad Horizontal</strong></p>en cumplimiento de las funciones Legales y Estatutarias consagradas en el reglamento de propiedad horizontal artículo 39 de la Ley 675 de 2001,<p></p>\r\n            <p>me permito convocar a todos los copropietarios a la celebración de la <strong>ASAMBLEA GENERAL ORDINARIA,</strong> la cual se llevará a cabo el <u>_____</u>, en el <u>____</u></p><br>    \r\n            <p>Atentamente,<br><strong>Administración.</strong></p></strong>', 'Carta Administración - Asamblea', 'generado'),
(19, 1, NULL, '2025-06-04 00:00:00', NULL, '<p class=\"text-center\"><strong>CONJUNTO RESIDENCIAL</strong></p>\r\n            <p class=\"text-center\"><strong>QUINTAS DEL RECREO ETAPA 1 P.H.</strong></p>\r\n            <p class=\"text-center\"><strong>Nit. 830132858-1</strong></p>\r\n            <p><strong>Reunión Andén</strong></p>\r\n            <p><strong>Señores Copropietarios del andén <u>_5__</u>:</strong></p>\r\n            <p>Se le convoca a una reunión para tratar temas relacionados con su andén, el día 04 de junio <u>___</u> a las <u>_07:00 pm en el salón comunal del conjunto___</u>.</p><br>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración - Anden', 'generado'),
(20, 1, NULL, '2025-06-04 00:00:00', NULL, '<p class=\"text-center\"><strong>CONJUNTO RESIDENCIAL</strong></p>\r\n            <p class=\"text-center\"><strong>QUINTAS DEL RECREO ETAPA 1 P.H.</strong></p>\r\n            <p class=\"text-center\"><strong>Nit. 830132858-1</strong></p>\r\n            <p><strong>Reunión Andén</strong></p>\r\n            <p><strong>Señores Copropietarios del andén <u>_5__</u>:</strong></p>\r\n            <p>Se le convoca a una reunión para tratar temas relacionados con su andén, el día 04 de junio <u>___</u> a las <u>_07:00 pm en el salón comunal del conjunto___</u>.</p><br>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración - Anden', 'generado'),
(21, 1, NULL, '2025-06-04 00:00:00', NULL, '<p class=\"text-center\"><strong>CONJUNTO RESIDENCIAL</strong></p>\r\n            <p class=\"text-center\"><strong>QUINTAS DEL RECREO ETAPA 1 P.H.</strong></p>\r\n            <p class=\"text-center\"><strong>Nit. 830132858-1</strong></p>\r\n            <p><strong>Reunión de Parqueadero</strong></p>\r\n            <p><strong>Señor(a) Copropietario(a)</strong></p>\r\n            <p>Me permito convocarlo a una reunión sobre el uso y organización del parqueadero, el día <u>_20 de junio __</u> a las <u>_07:00 pm__</u>.</p>\r\n            <p>Atentamente,<br><strong>Administración</strong></p>', 'Carta Administración - Parqueadero', 'generado'),
(31, 2, 4, '2025-06-19 22:18:35', '2025-06-20 21:50:00', 'caja', 'paquete', 'Entregado'),
(32, 2, NULL, '2025-06-20 19:13:27', NULL, 'Recibo del Agua', 'agua', 'Recibido'),
(33, 2, NULL, '2025-06-20 19:14:22', NULL, 'Recibo del Agua', 'agua', 'Recibido'),
(34, 2, NULL, '2025-06-20 19:15:48', NULL, 'Recibo del Gas', 'gas', 'Recibido'),
(35, 2, 1, '2025-06-20 19:16:22', NULL, 'sobre', 'paquete', 'Recibido'),
(36, 2, 3, '2025-06-20 19:16:48', NULL, 'sobre', 'paquete', 'Recibido'),
(37, 2, NULL, '2025-06-20 19:17:08', NULL, 'Recibo del Agua', 'agua', 'Recibido'),
(38, 2, 1, '2025-06-20 21:51:50', NULL, 'caja', 'paquete', 'Recibido');

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
(1, '1', '1'),
(2, '2', '1'),
(3, '3', '1'),
(4, '4', '1'),
(5, '5', '1'),
(6, '6', '1'),
(7, '7', '1'),
(8, '8', '1'),
(9, '9', '1'),
(10, '10', '1'),
(11, '11', '1'),
(12, '12', '1'),
(13, '13', '1'),
(14, '14', '1'),
(15, '15', '1'),
(16, '16', '1'),
(17, '17', '1'),
(18, '18', '1'),
(19, '19', '1'),
(20, '20', '1'),
(21, '21', '1'),
(22, '22', '1'),
(23, '23', '1'),
(24, '24', '1'),
(25, '25', '1'),
(26, '26', '1'),
(27, '27', '1'),
(28, '28', '1'),
(29, '29', '1'),
(30, '30', '1'),
(31, '31', '1');

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
(3, '2025-04-21 21:53:00', 1, 'Mascota sin correa', 180010.00, 1, '2025-04-23 11:13:00'),
(4, '2025-04-23 13:10:00', 2, 'Ruido excesivo', 50000.00, 1, '2025-04-23 20:10:00'),
(5, '2025-04-16 20:11:00', 1, 'Daños a zonas comunes', 280000.00, 1, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `novedades`
--

CREATE TABLE `novedades` (
  `pkidnovedad` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `inmueble_id` int(11) DEFAULT NULL,
  `tipo` varchar(50) NOT NULL,
  `asunto` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `estado` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `novedades`
--

INSERT INTO `novedades` (`pkidnovedad`, `trabajador_id`, `fecha`, `inmueble_id`, `tipo`, `asunto`, `descripcion`, `estado`) VALUES
(1, 1, '2025-05-31 04:59:33', NULL, 'Solicitud', 'el anden 4 no tiene iluminación', 'Llamar al técnico', 'Pendiente'),
(3, 1, '2025-06-06 00:00:00', NULL, 'Recomendación', 'cortes programados ', '', 'Resuelto'),
(4, 1, '2025-06-23 19:28:00', NULL, 'Recomendación', 'Chips portería', 'Chips fallando revisar', 'pendiente'),
(5, 2, '2025-06-23 19:40:00', 3, 'Queja', 'Ruido excesivo', 'El inmueble omite las solicitud de reducir el ruido', 'pendiente'),
(6, 2, '2025-06-23 19:49:00', 5, 'Queja', 'Ruido excesivo', 'el inmueble no atiende a la solicitud', 'Pendiente'),
(7, 2, '2025-06-23 20:14:00', NULL, 'Recomendación', 'Inseguridad', ' No dejar entrar personas extrañas', 'Pendiente'),
(8, 2, '2025-06-23 20:24:00', 2, 'Queja', 'Rayón carro', 'El residente del inmueble 2 rayo el carro del cupo 5', 'Pendiente'),
(9, 2, '2025-06-23 20:34:00', NULL, 'Solicitud', 'el anden 5 no tiene iluminación', 'programar revisión', 'Proceso'),
(10, 1, '2025-06-23 20:36:00', NULL, 'Recomendación', 'cortes programados ', 'Habrán cortes de agua', 'proceso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parqueadero`
--

CREATE TABLE `parqueadero` (
  `pkidparqueadero` int(11) NOT NULL,
  `cupo` int(11) NOT NULL,
  `tarifa` int(11) NOT NULL,
  `residente_id` int(11) DEFAULT NULL,
  `visitante_id` int(11) DEFAULT NULL,
  `estado` varchar(50) NOT NULL,
  `fecha` datetime NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `placa` varchar(20) NOT NULL,
  `hora_salida` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `parqueadero`
--

INSERT INTO `parqueadero` (`pkidparqueadero`, `cupo`, `tarifa`, `residente_id`, `visitante_id`, `estado`, `fecha`, `tipo`, `placa`, `hora_salida`) VALUES
(1, 1, 62000, 1, NULL, 'disponible', '2025-05-06 05:33:00', 'carro', 'LDF-687', '2025-05-16 23:40:00'),
(7, 5, 24000, NULL, 4, 'disponible', '2025-06-17 18:02:00', 'moto', 'HS-123S', '2025-06-18 10:00:00'),
(10, 6, 62000, 1, NULL, 'disponible', '2025-06-17 23:54:00', 'carro', 'LDA-562', '2025-06-18 00:55:00'),
(11, 4, 6000, NULL, 3, 'ocupado', '2025-06-18 17:59:00', 'carro', 'HSD-953', '2025-06-18 22:00:23'),
(12, 2, 31500, NULL, 3, 'ocupado', '2025-06-18 20:20:00', 'carro', 'PAS-943', '2025-06-19 17:21:17');

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
(1, 2, 1, 2),
(2, 5, 2, 2);

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
(1, 1, 1, 'Administradores Col', 'Administrador'),
(2, 3, 3, 'Vigias Colombia', 'Guarda');

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
(3, 3, '56789012', 'juandelgado@gmail.com', '$2b$12$LSQnpO7i6S3ONTYGgwRXV.IS9ABzqwhFt51waJ2LQBMGyXn79Gh22', '3219546650', 'Juan Delgado'),
(4, 3, '1014321659', 'isa_gar@gmail.com', '$2b$12$VzE1bhwNvasg1.8DWwSXCevfvgm.D7yasevzvRcNM0FXb/dFh8/Bu', '3151123080', 'Isabella García'),
(5, 2, '1113468097', 'lorenzoro@gmail.com', '$2b$12$RlT5tmKBmprbGNKDEwViMeUVx4gqJjfgwjS7kemK/PuAZoI8Mjjlm', '3101123654', 'Lorenzo Rodriguez');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `visitante`
--

CREATE TABLE `visitante` (
  `pkidvisitante` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `inmueble_id` int(11) NOT NULL,
  `autorizado` tinyint(1) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `cedula` varchar(20) NOT NULL,
  `ingresa_carro` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `visitante`
--

INSERT INTO `visitante` (`pkidvisitante`, `fecha`, `inmueble_id`, `autorizado`, `nombre`, `cedula`, `ingresa_carro`) VALUES
(2, '2025-04-15 17:39:00', 1, 1, 'Dan', '213745805', 0),
(3, '2025-04-29 17:44:00', 1, 2, 'Rafael Blas', '513654454', 1),
(4, '2025-06-12 22:51:00', 3, 1, 'Santiago Padilla', '1046231064', 0);

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
  ADD KEY `inmueble_id` (`inmueble_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cartera`
--
ALTER TABLE `cartera`
  MODIFY `pkidestado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `correspondencia`
--
ALTER TABLE `correspondencia`
  MODIFY `pkidcorrespondencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `inmueble`
--
ALTER TABLE `inmueble`
  MODIFY `pkidinmueble` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `multa`
--
ALTER TABLE `multa`
  MODIFY `pkidmulta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `novedades`
--
ALTER TABLE `novedades`
  MODIFY `pkidnovedad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `parqueadero`
--
ALTER TABLE `parqueadero`
  MODIFY `pkidparqueadero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `residente`
--
ALTER TABLE `residente`
  MODIFY `pkidresidente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `pkidrol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `trabajador`
--
ALTER TABLE `trabajador`
  MODIFY `pkidtrabajador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `pkidturno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `pkiduser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `visitante`
--
ALTER TABLE `visitante`
  MODIFY `pkidvisitante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
  ADD CONSTRAINT `visitante_ibfk_1` FOREIGN KEY (`inmueble_id`) REFERENCES `inmueble` (`pkidinmueble`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
