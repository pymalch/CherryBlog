-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 18, 2014 at 11:40 PM
-- Server version: 5.5.35
-- PHP Version: 5.3.10-1ubuntu3.11

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cherryblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `article`
--

CREATE TABLE IF NOT EXISTS `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `title` varchar(32) NOT NULL,
  `statement` varchar(255) NOT NULL,
  `description` text,
  `status` tinyint(2) NOT NULL,
  `priority` int(11) NOT NULL DEFAULT '1',
  `options` varchar(255) DEFAULT NULL,
  `visited` int(11) NOT NULL DEFAULT '0',
  `defaultImage` varchar(32) DEFAULT NULL,
  `cDate` int(11) NOT NULL,
  `uDate` int(11) DEFAULT NULL,
  `lang` varchar(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `status` (`status`),
  KEY `lang` (`lang`),
  KEY `uid` (`uid`),
  KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `keyword`
--

CREATE TABLE IF NOT EXISTS `keyword` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `lang` varchar(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`,`lang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `keyword_item`
--

CREATE TABLE IF NOT EXISTS `keyword_item` (
  `articleId` int(11) NOT NULL,
  `keywordId` int(11) NOT NULL,
  UNIQUE KEY `articleId` (`articleId`,`keywordId`),
  KEY `articleId_2` (`articleId`),
  KEY `keywordId` (`keywordId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(32) DEFAULT NULL,
  `cellphone` varchar(14) DEFAULT NULL,
  `userKey` varchar(128) DEFAULT NULL,
  `firstname` varchar(32) DEFAULT NULL,
  `lastname` varchar(32) DEFAULT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  `birthday` int(11) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `website` varchar(64) DEFAULT NULL,
  `defaultImage` varchar(32) DEFAULT NULL,
  `cDate` int(11) NOT NULL,
  `vDate` int(11) DEFAULT NULL,
  `ip` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `status` (`status`),
  KEY `cellphone` (`cellphone`),
  KEY `email` (`email`),
  KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `article`
--
ALTER TABLE `article`
  ADD CONSTRAINT `article_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `keyword_item`
--
ALTER TABLE `keyword_item`
  ADD CONSTRAINT `keyword_item_ibfk_2` FOREIGN KEY (`keywordId`) REFERENCES `keyword` (`id`),
  ADD CONSTRAINT `keyword_item_ibfk_1` FOREIGN KEY (`articleId`) REFERENCES `article` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
