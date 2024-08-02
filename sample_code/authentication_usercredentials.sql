-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2024 at 10:11 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthmanagementdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `authentication_usercredentials`
--

CREATE TABLE `authentication_usercredentials` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `authentication_usercredentials`
--

INSERT INTO `authentication_usercredentials` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`) VALUES
(8, 'pbkdf2_sha256$720000$8Qim4lJWFYokTbJZbYSzrl$9RmFKuRzQDqZEG4fJtI7heiay1806jXeWiVPVJGDjHQ=', '2024-07-30 08:06:39.596820', 0, 'ponnar', '', '', 0, 1, '2024-07-29 08:52:08.175254', 'ponnar@gmail.com'),
(9, 'pbkdf2_sha256$720000$f1ek1GOjtzFmjy4dG6hNLL$O287ovAs/0s3/V63QsBc4eH8OcNZF0Le1PGtZzOpvV8=', '2024-07-30 08:08:37.453799', 0, 'Koodalarasan', '', '', 0, 1, '2024-07-29 08:53:30.826565', 'koodal1998@gmail.com'),
(10, 'pbkdf2_sha256$720000$4O8qX6CMq4OyMnc0tb35o8$MiP0s9zviiRYEmyHMI+DK80vgN5wARL6I0a9ddAs5ak=', '2024-07-30 08:00:52.089633', 0, 'praganes', '', '', 0, 1, '2024-07-30 07:45:47.024666', 'praga@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authentication_usercredentials`
--
ALTER TABLE `authentication_usercredentials`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authentication_usercredentials`
--
ALTER TABLE `authentication_usercredentials`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
