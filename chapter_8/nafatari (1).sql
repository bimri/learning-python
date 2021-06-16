-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2021 at 04:35 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nafatari`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`) VALUES
('admin@admin.com', 'admin'),
('kiki@gmail.com', 'kiki'),
('kiki@kikima.com', 'popeyeblue'),
('mugo@malvin.com', 'popeyeblue');

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `appointment_no` int(30) NOT NULL,
  `patient_id` int(30) NOT NULL,
  `speciality` varchar(30) NOT NULL,
  `medical_condition` text DEFAULT NULL,
  `doctors_suggestion` varchar(30) DEFAULT NULL,
  `payment_amount` int(199) DEFAULT NULL,
  `case_closed` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` (`appointment_no`, `patient_id`, `speciality`, `medical_condition`, `doctors_suggestion`, `payment_amount`, `case_closed`) VALUES
(59, 85, 'Audiologist', 'eardrum puncture', '', NULL, 'no'),
(60, 86, 'Dentist', 'amalgam', 'suggestion', NULL, 'no'),
(61, 87, 'Oncologist', 'prostrate', NULL, NULL, 'no'),
(62, 88, 'urinologist', 'UTI', NULL, NULL, 'no'),
(63, 89, 'ENT', 'tinitus', NULL, NULL, 'no'),
(64, 90, 'Cardiologist', 'angina', NULL, NULL, 'no'),
(65, 91, 'Dermatologist', 'eczema', NULL, NULL, 'no'),
(66, 92, 'Gynaecologist', 'fibroids', NULL, NULL, 'no');

-- --------------------------------------------------------

--
-- Table structure for table `clerks`
--

CREATE TABLE `clerks` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `fullname` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='stores information about clerk';

--
-- Dumping data for table `clerks`
--

INSERT INTO `clerks` (`email`, `password`, `fullname`) VALUES
('hope@yahoo.com', 'ewaa', 'Matu Kina'),
('juju@ju.com', 'oppo', 'Jojo Ahari');

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `fullname` varchar(30) NOT NULL,
  `speciality` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`email`, `password`, `fullname`, `speciality`) VALUES
('misfar@yahoo.com', 'admin', 'Swaleh Misfar', 'Oncologist'),
('omondi@gmail.com', 'yeye', 'Ogutu Omondi             ', 'Cardiologist'),
('paulina@outlook.com', '136172', 'Sonia Mbithi', 'urinologist'),
('thandi@gmail.com', 'thandi', 'Thandi Tanda', 'Dentist'),
('yusuf@gmail.com', 'yusufu', 'Yusuf Guled', 'Audiologist'),
('zuhura@outlook.com', 'pepeoo', 'Zuhura Ebe', 'Gynecologist');

-- --------------------------------------------------------

--
-- Table structure for table `patient_info`
--

CREATE TABLE `patient_info` (
  `patientId` int(10) NOT NULL,
  `full_name` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `weight` int(8) NOT NULL,
  `phone_no` varchar(30) NOT NULL,
  `Location` varchar(260) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='patient';

--
-- Dumping data for table `patient_info`
--

INSERT INTO `patient_info` (`patientId`, `full_name`, `DOB`, `weight`, `phone_no`, `Location`) VALUES
(85, 'Abduba Abdalla ', '1975-01-12', 47, '57473422', 'Sinai'),
(87, 'Tendi Amber', '2000-10-21', 52, '072122177', 'Ngong'),
(88, 'Brian Gachoka', '1956-03-25', 52, '011176354', 'Lavington'),
(89, 'Chima Ade', '1987-06-14', 50, '071812342', 'Makadara'),
(90, 'Chris Omondi', '1976-05-01', 54, '01236542', 'Syokimau'),
(91, 'Yaya Ebena', '2012-01-01', 70, '0710992503', 'Mwiki'),
(92, 'Zoya Gigi', '2013-07-07', 53, '078362673', 'Eka'),
(93, 'Foi Grassa ', '1977-12-13', 76, '079123456', 'Ruiru'),
(94, 'JOY', '1995-11-22', 65, '011197653', 'Kilimani'),
(95, 'Kaira Aliyah ', '1984-09-09', 87, '07886767', 'Eastleigh'),
(96, 'Saul Maina ', '1955-02-15', 101, '0674321', 'Kasarani'),
(97, 'Mwangi Mana ', '2005-04-17', 97, '046738373', 'South C'),
(98, 'Mark Eli ', '2001-08-15', 64, '474755731', 'South C'),
(99, 'Zahara Maya ', '2003-03-03', 56, '78324782', 'Thika'),
(100, 'Muteti Mutai ', '2004-10-04', 83, '65437642', 'Wangige'),
(102, 'Kada Pombe ', '1988-12-25', 77, '2654628', 'Kikuyu'),
(103, 'Ziki Bijou ', '1999-09-09', 55, '465653878', 'Westlands'),
(104, 'Tracy Likana', '1994-05-17', 78, '78563288', 'Ruaka'),
(105, 'Shayne Terra ', '2006-01-17', 99, '43578543', 'Karen'),
(106, 'Titus Mogaka ', '2007-03-02', 63, '9996653', 'Satellite'),
(107, 'Wawira Kimau ', '2006-12-15', 43, '87425782', 'Dandora'),
(108, 'Kenneth Wekesa ', '1943-01-22', 70, '01217638', 'Riruta'),
(109, 'Kevin Keso ', '1966-08-25', 56, '203573107', 'Embakasi'),
(110, 'Yugesh verma ', '1992-07-14', 95, '27382764', 'Milimani');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `fullname` varchar(30) NOT NULL,
  `patient_Id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `password`, `fullname`, `patient_Id`) VALUES
('abduba@gmail.com', 'welli', 'Abduba Abdalla', 85),
('aden122@gmail.com', 'fitur', 'Aden Abdalla', 86),
('amber@outlook.com', 'aero', 'Tendi Amber', 87),
('Brian@yahoo.com', 'brayo', 'Brian Gachoka', 88),
('chima@gmail.com', '123456', 'Chima Ade', 89),
('Chris @outlook.com', 'ero', 'Chris Omondi', 90),
('ebena@yahoo.com', 'yahura', 'Yaya Ebena', 91),
('gizi@outlook.com', 'emba', 'Zoya Gigi', 92),
('grassa32@outlook.com', 'grassavile', 'Foi Grassa', 93),
('joy@joy.com', 'joy', 'JOY', 94),
('Kaira@gmail.com', 'ejaud', 'Kaira Aliyah', 95),
('mamish@yahoo.com', 'mamisha', 'Saul Maina', 96),
('mana@yahoo.com', 'sessu', 'Mwangi Mana', 97),
('mark@gmail.com', 'mark', 'Mark Eli', 98),
('Maya@gmail.com', 'maya', 'Zahara Maya', 99),
('muteti@gmail.com', '123456', 'Muteti Mutai', 100),
('pombe@outlook.com', 'padlock', 'Kada Pombe', 102),
('riziki@gmail.com', 'bibabi', 'Ziki Bijou', 103),
('Tarcy@gmail.com', 'didi', 'Tracy Lkana', 104),
('terra45@gmail.com', 'rear', 'Shayne Terra ', 105),
('titus@gmail.com', 'okoko', 'Titus Mogaka', 106),
('wawira@gmail.com', 'wawesh', 'Wawira Kimau', 107),
('wekulu@gmail.com', 'wekesa', 'Kenneth Wekesa', 108),
('yarake@gmail.com', 'yarab', 'Kevin Keso', 109),
('yugeshverma32@gmail.com', '123456', 'Yugesh verma', 110);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`appointment_no`);

--
-- Indexes for table `clerks`
--
ALTER TABLE `clerks`
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `patient_info`
--
ALTER TABLE `patient_info`
  ADD PRIMARY KEY (`patientId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`patient_Id`),
  ADD UNIQUE KEY `username` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `appointment_no` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `patient_info`
--
ALTER TABLE `patient_info`
  MODIFY `patientId` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
