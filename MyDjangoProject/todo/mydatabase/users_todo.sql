-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2018 at 07:02 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_django`
--

-- --------------------------------------------------------

--
-- Table structure for table `users_todo`
--

CREATE TABLE `users_todo` (
  `id` int(11) NOT NULL,
  `task` varchar(500) NOT NULL,
  `deadline` varchar(250) NOT NULL,
  `username_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users_todo`
--

INSERT INTO `users_todo` (`id`, `task`, `deadline`, `username_id`) VALUES
(16, 'submit assignment', '2018-06-28', 'viggi'),
(17, 'hello', '2018-06-13', 'viggi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users_todo`
--
ALTER TABLE `users_todo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Users_todo_username_id_076d9f9f_uniq` (`username_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users_todo`
--
ALTER TABLE `users_todo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `users_todo`
--
ALTER TABLE `users_todo`
  ADD CONSTRAINT `Users_todo_username_id_076d9f9f_fk_Users_users_username` FOREIGN KEY (`username_id`) REFERENCES `users_users` (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
