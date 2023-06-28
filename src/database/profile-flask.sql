-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2023 a las 18:43:17
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `profile-flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(10) NOT NULL,
  `NDI` int(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `Direccion` varchar(30) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Empresa` varchar(35) NOT NULL,
  `Cargo` varchar(25) NOT NULL,
  `Area_locativa` varchar(30) NOT NULL,
  `Email` varchar(35) NOT NULL,
  `Fecha_nacimiento` date DEFAULT NULL,
  `Rol` int(2) NOT NULL,
  `Nombre-img` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id_user`, `NDI`, `password`, `fullname`, `Direccion`, `Telefono`, `Empresa`, `Cargo`, `Area_locativa`, `Email`, `Fecha_nacimiento`, `Rol`, `Nombre-img`) VALUES
(1, 1010166424, 'pbkdf2:sha256:600000$4KEC0m5pbovSRyDe$2a3cc99f49180b6c63acfa1126ef7ced7c8554ad9112f1aff2a58ded9b25000c', 'deivid bautista', 'calle siempre viva109', 31212287, 'Americana de servicios L.T.D.A', 'Aprendiz', 'Oficina', 'debautist15@gmail.com', '2023-05-02', 0, ''),
(2, 12345678, 'pbkdf2:sha256:600000$RmJkvDljtnXNGrSM$8c36155079b871e820f0d70c83458edaacaa9535fca958fcfb3fbfb0639ffeba', 'Jonatthan Florez', '', 0, '', '', '', '', NULL, 0, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
