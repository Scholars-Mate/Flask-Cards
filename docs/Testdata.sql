-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: flaskcards
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Create database
--

DROP DATABASE IF EXISTS flaskcards;
CREATE DATABASE flaskcards;
USE flaskcards;

--
-- Table structure for table `Cards`
--

DROP TABLE IF EXISTS `Cards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cards` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `setid` int(11) NOT NULL,
  `front` varchar(1023) DEFAULT '',
  `back` varchar(1023) DEFAULT '',
  `indicator` tinyint(1) DEFAULT NULL,
  `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `setid` (`setid`),
  CONSTRAINT `Cards_ibfk_1` FOREIGN KEY (`setid`) REFERENCES `Sets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cards`
--

LOCK TABLES `Cards` WRITE;
/*!40000 ALTER TABLE `Cards` DISABLE KEYS */;
INSERT INTO `Cards` VALUES (1,1,'What is the three leter abbreviation for Alanine?','Ala',NULL,'2017-11-29 22:03:16'),(2,1,'What is the three leter abbreviation for Arginine?','Arg',NULL,'2017-11-29 22:03:17'),(3,1,'What is the three leter abbreviation for Asparagine?','Asn',NULL,'2017-11-29 22:03:17'),(4,1,'What is the three leter abbreviation for Aspartic acid?','Asp',NULL,'2017-11-29 22:03:17'),(5,1,'What is the three leter abbreviation for Cysteine?','Cys',NULL,'2017-11-29 22:03:17'),(6,1,'What is the three leter abbreviation for Glutamic acid?','Glu',NULL,'2017-11-29 22:03:17'),(7,1,'What is the three leter abbreviation for Glutamine?','Gln',NULL,'2017-11-29 22:03:17'),(8,1,'What is the three leter abbreviation for Glycine?','Gly',NULL,'2017-11-29 22:03:17'),(9,1,'What is the three leter abbreviation for Histidine?','His',NULL,'2017-11-29 22:03:17'),(10,1,'What is the three leter abbreviation for Isoleucine?','Ile',NULL,'2017-11-29 22:03:17'),(11,1,'What is the three leter abbreviation for Leucine?','Leu',NULL,'2017-11-29 22:03:17'),(12,1,'What is the three leter abbreviation for Lysine?','Lys',NULL,'2017-11-29 22:03:17'),(13,1,'What is the three leter abbreviation for Methionine?','Met',NULL,'2017-11-29 22:03:18'),(14,1,'What is the three leter abbreviation for Phenylalanine?','Phe',NULL,'2017-11-29 22:03:18'),(15,1,'What is the three leter abbreviation for Proline?','Pro',NULL,'2017-11-29 22:03:18'),(16,1,'What is the three leter abbreviation for Serine?','Ser',NULL,'2017-11-29 22:03:18'),(17,1,'What is the three leter abbreviation for Threonine?','Thr',NULL,'2017-11-29 22:03:18'),(18,1,'What is the three leter abbreviation for Tryptophan?','Trp',NULL,'2017-11-29 22:03:18'),(19,1,'What is the three leter abbreviation for Tyrosine?','Tyr',NULL,'2017-11-29 22:03:18'),(20,1,'What is the three leter abbreviation for Valine?','Val',NULL,'2017-11-29 22:03:18'),(21,2,'What is signal transduction?','A conversion of information to a chemical change.',NULL,'2017-11-29 22:03:18'),(22,2,'How is specificity acheived in signal transduction?','By precise molecular complementarity between the signal and receptor molecules.',NULL,'2017-11-29 22:03:18'),(23,2,'What is aplification in signal transduction?','When an enzyme associated with a signal receptor is activated and in turn activates many molecules of a second enzyme, which activates many molecules of a third and so on.',NULL,'2017-11-29 22:03:19'),(24,3,'What is experimenter bias?','When a researcher\'s expectation or preference about the outcomes of a study influence the results obtained.',NULL,'2017-11-29 22:03:19'),(25,3,'What is a response set?','A tendency to respond to questions in a particular way that is unrelated to the content of the question.',NULL,'2017-11-29 22:03:19'),(26,3,'What is social desirability bias?','The tendency to give socially approved answers to questions about oneself.',NULL,'2017-11-29 22:03:19'),(27,4,'What is the efficiency of heap sort?','nlog(n)',NULL,'2017-11-29 22:03:19'),(28,4,'What is the efficiency of merge sort?','nlog(n)',NULL,'2017-11-29 22:03:19'),(29,4,'What is the efficiency of heapify()?','log(n)',NULL,'2017-11-29 22:03:19'),(30,5,'How do you avoid SQL Injection attacks?','Escape your input, or use prepared statements.',NULL,'2017-11-29 22:03:19'),(31,5,'Parameters in the URL are which method?','GET',NULL,'2017-11-29 22:03:19'),(32,5,'What does CRUD stand for?','Create, read, update, and delete.',NULL,'2017-11-29 22:03:19');
/*!40000 ALTER TABLE `Cards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `Category_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Category`
--

LOCK TABLES `Category` WRITE;
/*!40000 ALTER TABLE `Category` DISABLE KEYS */;
INSERT INTO `Category` VALUES (1,1,'Biochemistry'),(2,1,'Psychology'),(3,2,'Computer Science');
/*!40000 ALTER TABLE `Category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Sets`
--

DROP TABLE IF EXISTS `Sets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Sets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT 'Unamed Set',
  `categoryid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `createdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `categoryid` (`categoryid`),
  KEY `userid` (`userid`),
  CONSTRAINT `Sets_ibfk_1` FOREIGN KEY (`categoryid`) REFERENCES `Category` (`id`),
  CONSTRAINT `Sets_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sets`
--

LOCK TABLES `Sets` WRITE;
/*!40000 ALTER TABLE `Sets` DISABLE KEYS */;
INSERT INTO `Sets` VALUES (1,'Amino Acids',1,1,'2017-11-29 22:03:16'),(2,'Biosignaling',1,1,'2017-11-29 22:03:16'),(3,'Terms',2,1,'2017-11-29 22:03:16'),(4,'Algorithms',3,2,'2017-11-29 22:03:16'),(5,'Databases',3,2,'2017-11-29 22:03:16');
/*!40000 ALTER TABLE `Sets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  `password` char(94) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'johndoe','John Doe','pbkdf2:sha256:50000$oS0uZS51$64b66780c6705d2c08511caa0b8fefada9c6d0930a6cbc4a817cb6b57681072e'),(2,'janedoe','Jane Doe','pbkdf2:sha256:50000$neuvHhnZ$c91d93be49a059c6ef5ecca3ac01a7e7a674f61a80176fd4be7e48c552da79b3');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-29 16:04:13
