-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: e_payment
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address` (
  `address_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `address` varchar(50) NOT NULL,
  `address2` varchar(50) DEFAULT NULL,
  `district` varchar(20) NOT NULL,
  `city_id` smallint unsigned NOT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `phone` varchar(20) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `city_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `city` varchar(50) NOT NULL,
  `country_id` smallint unsigned NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `country_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(50) NOT NULL,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `gps_id` int DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE KEY `GPS_EMEI_UNIQUE` (`customer_id`),
  KEY `fk_gps_id` (`gps_id`),
  CONSTRAINT `fk_gps_id` FOREIGN KEY (`gps_id`) REFERENCES `gps` (`gps_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('Mugema','charles','xasalod584@ktasy.com',1,1,'2023-12-11 17:53:06','2023-12-11 17:53:06',NULL),('Mugema','charles','xasalod584@ktasy.com',2,1,'2023-12-11 18:00:17','2023-12-11 18:00:17',NULL),('Mugema','charles','xasalod584@ktasy.com',3,1,'2023-12-11 18:09:10','2023-12-11 18:09:10',NULL),('Mugema','charles','xasalod584@ktasy.com',4,1,'2023-12-12 13:26:24','2023-12-12 13:26:24',NULL),('Mugema','charles','xasalod584@ktasy.com',5,1,'2023-12-12 13:50:07','2023-12-12 13:50:07',NULL),('Mugema','charles','xasalod584@ktasy.com',6,1,'2023-12-12 14:00:06','2023-12-12 14:00:06',NULL),('Mugema','charles','xasalod584@ktasy.com',7,1,'2023-12-12 14:14:19','2023-12-12 14:14:19',NULL),('Mugema','charles','xasalod584@ktasy.com',8,1,'2023-12-12 15:19:35','2023-12-12 15:19:35',NULL),('Mugema','charles','xasalod584@ktasy.com',9,1,'2023-12-12 15:47:22','2023-12-12 15:47:22',NULL),('Kwizera','Yves','yves@gmail.com',10,1,'2023-12-12 16:12:05','2023-12-12 16:12:05',NULL),('Rwema','Peter','ntale@ict.rw',11,1,'2023-12-12 16:17:23','2023-12-12 16:17:23',NULL),('Kubwimana','Fils','ntale@ict.rw',12,1,'2023-12-12 16:47:56','2023-12-12 16:47:56',NULL),('Nkurunziza ','pierre','ntale@gmail.com',13,1,'2023-12-12 17:32:55','2023-12-12 17:32:55',NULL),('Kamana','Vedaste','eric@gmail.com',14,1,'2023-12-12 19:20:59','2023-12-12 19:20:59',NULL),('Uwimana','claude','claude@gmail.com',15,1,'2023-12-12 19:23:04','2023-12-12 19:23:04',NULL),('karasira','Claude','basalod584@ktasy.com',16,1,'2023-12-13 10:03:56','2023-12-13 10:03:56',NULL),('Kalisa','Robertt','ntale@yahoo.fr',17,1,'2023-12-18 09:11:03','2023-12-18 09:11:03',NULL),('Kalisa','Robert','kalisa@gmail.com',18,1,'2023-12-18 10:21:09','2023-12-18 10:21:09',NULL),('Kalisa','Michel','michel@gmail.com',19,1,'2023-12-18 10:38:32','2023-12-18 10:38:32',NULL),('Robert','kanu','kanu@gmail.com',20,1,'2023-12-18 11:01:12','2023-12-18 11:01:12',NULL),('charles','muhire','muhire@yahoo.fr',21,1,'2023-12-18 11:04:22','2023-12-18 11:04:22',NULL),('cip','po','r@f.com',22,1,'2023-12-18 11:33:16','2023-12-18 11:33:16',NULL),('cip','po','r@f.com',23,1,'2023-12-18 11:38:44','2023-12-18 11:38:44',NULL),('alex','rugema','rugema61@gmail.com1',24,1,'2023-12-18 11:43:13','2023-12-18 11:43:13',NULL),('Kalisa','Robert','mjabush@gmail.com',25,1,'2023-12-18 11:48:23','2023-12-18 11:48:23',NULL),('KARANGWA ','Sylvere','sylvere@gmail.com',26,1,'2023-12-19 15:34:01','2023-12-19 15:34:01',NULL),('Kamana','Sylvere','sylvere@gmail.com',27,1,'2023-12-19 16:32:49','2023-12-19 16:32:49',NULL),('Kabutura ','Faustin','faustin@yahoo.com',28,1,'2023-12-19 17:04:46','2023-12-19 17:04:46',NULL),('NSENGIYUMVA','Samson','samson@ict.rw',29,1,'2023-12-19 17:24:34','2023-12-19 17:24:34',NULL),('Jobs','SHUMBUSHO','mjabush@gmail.com',30,1,'2023-12-19 17:32:30','2023-12-19 17:32:30',NULL),('Jobs1','SHUMBUSHO','mjabush@yahoo.fr',31,1,'2023-12-19 18:55:05','2023-12-19 18:55:05',NULL),('Kalisa','obed','obed@gmail.com',32,1,'2023-12-20 12:19:07','2023-12-20 12:19:07',9),('Uwamahoro','wivine','wivine@gmail.com',33,1,'2023-12-25 15:58:42','2023-12-25 15:58:42',6);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gps`
--

DROP TABLE IF EXISTS `gps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gps` (
  `EMEI` bigint DEFAULT NULL,
  `Model_Name` varchar(50) DEFAULT NULL,
  `Activated_date` date DEFAULT NULL,
  `GPS_Experied_date` date DEFAULT NULL,
  `gps_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`gps_id`),
  UNIQUE KEY `EMEI` (`EMEI`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gps`
--

LOCK TABLES `gps` WRITE;
/*!40000 ALTER TABLE `gps` DISABLE KEYS */;
INSERT INTO `gps` VALUES (865080043988944,'TR07','2023-12-13','2024-12-13',1),(865080043990551,'TR07','2023-12-13','2024-12-13',2),(8572580035468,'TR07','2023-12-13','2024-12-13',3),(857800700652364,'TR07','2023-12-13','2024-12-13',4),(857641239854789,'TR07','2023-12-13','2024-12-13',5),(857008009856425,'TR07','2023-12-13','2024-12-13',6),(857458214587965,'TR07','2023-12-13','2024-12-13',7),(856280034275812,'TR07','2023-12-14','2024-12-14',8),(857246325412558,'TR07','2023-12-14','2024-12-14',9),(856800342122525,'TR07','2023-12-14','2024-12-21',10),(854212255666236,'TR07','2023-12-14','2024-12-14',11),(858007006500452,'TR07','2023-12-14','2024-12-14',12),(854125551313125,'TR07','2023-12-14','2024-12-14',13),(8574151212303054,'TR07','2023-12-14','2024-12-14',15),(8576254875122212,'TR07','2023-12-14','2024-12-14',16),(8576254875122213,'TR07','2023-12-14','2024-12-14',18),(8576254875122216,'TR07','2023-12-14','2023-12-14',21),(8576254875122217,'TR07','2023-12-14','2024-12-14',22),(855212132564212,'TR07','2023-12-14','2024-12-14',23),(855212132564218,'TR07','2023-12-14','2024-12-14',24),(855212132564220,'TR07','2023-12-14','2024-12-14',25),(85521213256423,'TR07','2023-12-14','2024-12-14',26),(85521213256424,'TR07','2023-12-14','2024-12-14',27),(85521213256425,'TR07','2023-12-14','2024-12-14',29),(85521213256426,'TR07','2023-12-14','2024-12-14',30),(85521213256427,'TR08','2023-12-14','2024-12-14',31);
/*!40000 ALTER TABLE `gps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moto`
--

DROP TABLE IF EXISTS `moto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moto` (
  `moto_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `plate` varchar(10) DEFAULT NULL,
  `Model` varchar(20) DEFAULT NULL,
  `Chassis_Number` varchar(20) DEFAULT NULL,
  `Engine_Number` varchar(20) DEFAULT NULL,
  `gps_id` int DEFAULT NULL,
  PRIMARY KEY (`moto_id`),
  UNIQUE KEY `moto_id` (`moto_id`),
  KEY `gps_id` (`gps_id`),
  CONSTRAINT `moto_ibfk_1` FOREIGN KEY (`gps_id`) REFERENCES `gps` (`gps_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moto`
--

LOCK TABLES `moto` WRITE;
/*!40000 ALTER TABLE `moto` DISABLE KEYS */;
INSERT INTO `moto` VALUES (1,'RAD274l','Discover','56151515w888','55156515df',10),(2,'RAD274l','Discover','56151515w888','55156515df',10),(3,'RAD274l','Discover','56151515w888','55156515df',11),(4,'RD284U','Discover','56151515w887','55157515dm',13);
/*!40000 ALTER TABLE `moto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `payment_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `customer_id` smallint unsigned NOT NULL,
  `rental_id` int DEFAULT NULL,
  `amount` decimal(5,2) NOT NULL,
  `payment_date` datetime NOT NULL,
  `last_update` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `role` varchar(45) NOT NULL DEFAULT 'user',
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Jobs','SHUMBUSHO','mjabush@yahoo.fr','0788683270','admin','jobs','123'),(2,'alex','rr','rugema@mail.com','0781049931','recovery','rugema3','123'),(3,'NSENGIYUMVA','Esli','esli@ict.rw','0788683276','recovery','esli','123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-30 20:48:29
