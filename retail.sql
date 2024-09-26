-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: retail
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add goods',7,'add_goods'),(26,'Can change goods',7,'change_goods'),(27,'Can delete goods',7,'delete_goods'),(28,'Can view goods',7,'view_goods'),(29,'Can add mail',8,'add_mail'),(30,'Can change mail',8,'change_mail'),(31,'Can delete mail',8,'delete_mail'),(32,'Can view mail',8,'view_mail'),(33,'Can add manager',9,'add_manager'),(34,'Can change manager',9,'change_manager'),(35,'Can delete manager',9,'delete_manager'),(36,'Can view manager',9,'view_manager'),(37,'Can add order_record',10,'add_order_record'),(38,'Can change order_record',10,'change_order_record'),(39,'Can delete order_record',10,'delete_order_record'),(40,'Can view order_record',10,'view_order_record'),(41,'Can add remain',11,'add_remain'),(42,'Can change remain',11,'change_remain'),(43,'Can delete remain',11,'delete_remain'),(44,'Can view remain',11,'view_remain'),(45,'Can add sale_record',12,'add_sale_record'),(46,'Can change sale_record',12,'change_sale_record'),(47,'Can delete sale_record',12,'delete_sale_record'),(48,'Can view sale_record',12,'view_sale_record'),(49,'Can add 商店',13,'add_shop'),(50,'Can change 商店',13,'change_shop'),(51,'Can delete 商店',13,'delete_shop'),(52,'Can view 商店',13,'view_shop'),(53,'Can add 供应商',14,'add_supplier'),(54,'Can change 供应商',14,'change_supplier'),(55,'Can delete 供应商',14,'delete_supplier'),(56,'Can view 供应商',14,'view_supplier'),(57,'Can add cost',15,'add_cost'),(58,'Can change cost',15,'change_cost'),(59,'Can delete cost',15,'delete_cost'),(60,'Can view cost',15,'view_cost'),(61,'Can add salesman',16,'add_salesman'),(62,'Can change salesman',16,'change_salesman'),(63,'Can delete salesman',16,'delete_salesman'),(64,'Can view salesman',16,'view_salesman');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'manager','cost'),(7,'manager','goods'),(8,'manager','mail'),(9,'manager','manager'),(10,'manager','order_record'),(11,'manager','remain'),(12,'manager','sale_record'),(13,'manager','shop'),(14,'manager','supplier'),(6,'sessions','session'),(16,'staff','salesman');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-06-08 21:29:09.392503'),(2,'auth','0001_initial','2024-06-08 21:29:09.805758'),(3,'admin','0001_initial','2024-06-08 21:29:09.913345'),(4,'admin','0002_logentry_remove_auto_add','2024-06-08 21:29:09.921348'),(5,'admin','0003_logentry_add_action_flag_choices','2024-06-08 21:29:09.929649'),(6,'contenttypes','0002_remove_content_type_name','2024-06-08 21:29:10.025495'),(7,'auth','0002_alter_permission_name_max_length','2024-06-08 21:29:10.076490'),(8,'auth','0003_alter_user_email_max_length','2024-06-08 21:29:10.095328'),(9,'auth','0004_alter_user_username_opts','2024-06-08 21:29:10.104114'),(10,'auth','0005_alter_user_last_login_null','2024-06-08 21:29:10.151286'),(11,'auth','0006_require_contenttypes_0002','2024-06-08 21:29:10.154212'),(12,'auth','0007_alter_validators_add_error_messages','2024-06-08 21:29:10.162311'),(13,'auth','0008_alter_user_username_max_length','2024-06-08 21:29:10.213835'),(14,'auth','0009_alter_user_last_name_max_length','2024-06-08 21:29:10.270299'),(15,'auth','0010_alter_group_name_max_length','2024-06-08 21:29:10.287521'),(16,'auth','0011_update_proxy_permissions','2024-06-08 21:29:10.297402'),(17,'auth','0012_alter_user_first_name_max_length','2024-06-08 21:29:10.351031'),(18,'manager','0001_initial','2024-06-08 21:29:10.528468'),(19,'manager','0002_alter_order_record_order_time','2024-06-08 21:29:10.562132'),(20,'manager','0003_rename_telephone_1_shop_telephone_and_more','2024-06-08 21:29:10.591468'),(21,'manager','0004_rename_telephone_1_supplier_telephone_and_more','2024-06-08 21:29:10.617297'),(22,'manager','0005_shop_location_specific_alter_shop_location','2024-06-08 21:29:10.677454'),(23,'sessions','0001_initial','2024-06-08 21:29:10.707674'),(24,'staff','0001_initial','2024-06-08 21:29:10.766062'),(25,'manager','0006_manager_is_admin_manager_last_login','2024-06-09 13:38:38.913150'),(26,'manager','0007_remove_manager_is_admin_remove_manager_last_login_and_more','2024-06-09 13:38:39.028341'),(27,'manager','0008_alter_sale_record_turnover','2024-06-09 13:38:39.078628');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bz9qf0x74qufdx54zo4ertonr6wbgobj','eyJpZCI6IjEiLCJuYW1lIjoiXHU5MWQxXHU3ZjE4XHU1YjlkIiwicGVyIjoibWFuYWdlciJ9:1sV77U:QHuxdPuCws9hxNSIipgbQCxEy7jqtu8RJ30PYjZT8p8','2024-08-03 18:15:16.705835'),('ls5tz6yiayya75gvok78t8g3yseiufkm','eyJpZCI6IjEiLCJuYW1lIjoiXHU5MWQxXHU3ZjE4XHU1YjlkIiwic2hvcF9pZCI6MX0:1rxKWJ:763F92fQzyrTEsAuA_64ham_moWsFaMOQC9UGsIWTuU','2024-07-02 13:41:15.622570'),('r9ft0n5lr7t2imm579fg41auf8qcl92q','eyJpZCI6IjEiLCJuYW1lIjoiXHU5MWQxXHU3ZjE4XHU1YjlkIiwic2hvcF9pZCI6MX0:1ruBkY:C3ISCV2rdNn_qKM7p4LEEsIG00x0Ut4nl-TufXDrZ88','2024-06-23 21:42:58.890670'),('x6jawtv2v0y9v6wt6cxpw22cd6mlb688','eyJpZCI6IjEiLCJuYW1lIjoiXHU5MWQxXHU3ZjE4XHU1YjlkIiwicGVyIjoibWFuYWdlciJ9:1s5ns2:vSdzKpzMu5QPBYiiDsC4-p-Fe7bm2F3vFs8x25canxA','2024-07-25 22:38:42.214601');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_cost`
--

DROP TABLE IF EXISTS `manager_cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_cost` (
  `id` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(20) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `cost_unit` decimal(8,2) NOT NULL,
  `status` varchar(3) NOT NULL,
  `compare` smallint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `manager_cost_supplier_name_goods_name_f8000700_uniq` (`supplier_name`,`goods_name`),
  KEY `manager_cost_goods_name_d7563216` (`goods_name`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_cost`
--

LOCK TABLES `manager_cost` WRITE;
/*!40000 ALTER TABLE `manager_cost` DISABLE KEYS */;
INSERT INTO `manager_cost` VALUES (1,'蒙牛','牛奶',2.00,'已进货',1),(2,'格力','空调',100.00,'已进货',1),(3,'晨光','橡皮',5.00,'已进货',2),(4,'耐克','篮球鞋',100.00,'已进货',3),(5,'李宁','跑步鞋',100.00,'已进货',1),(6,'华为','耳机',1000.00,'已进货',2),(7,'华为','电脑',100.00,'已进货',3),(8,'蒙牛','返老还童丹',1.25,'已进货',1),(9,'李宁','风火轮',4.00,'已进货',2),(10,'华为','照妖镜',10.00,'已进货',2),(11,'华为','金刚钻',10.00,'已进货',2),(12,'格力','量子计算机',20000.00,'已进货',2),(13,'李宁','青龙偃月刀',100.10,'已进货',2),(14,'蒙牛','奶酪',100.00,'已进货',3),(19,'华为','金箍棒',50.00,'已进货',1),(20,'蒙牛','西瓜',10.00,'预订购',2),(21,'耐克','扫把',10.00,'已进货',2),(22,'光明','牛奶',15.00,'已进货',3),(23,'伊利','牛奶',10.00,'已进货',2),(24,'格力','冰箱',1000.00,'已进货',2),(25,'华为','手套',10.00,'预订购',2),(26,'蒙牛','草莓',2.00,'已进货',2),(27,'华为','手机',4.00,'已进货',1),(28,'华为','自行车',200.00,'预订购',2),(29,'华为','梨子',2.00,'已进货',2),(30,'华为','测试mouse',20.00,'预订购',2),(31,'伊利','香蕉',2.00,'已进货',2),(32,'华为','鼠标',20.00,'预订购',2),(33,'蒙牛','测试菠萝',2.00,'已进货',2),(34,'华为','鼠标（测试用）',20.00,'预订购',2),(35,'光明','菠萝',2.00,'已进货',2),(36,'华为','芯片',20000.00,'预订购',2),(37,'光明','荔枝',2.00,'已进货',2),(38,'光明','龙岩',2.00,'已进货',2),(39,'蒙牛','酸奶',2.00,'已进货',2),(40,'华为','风火轮',100.00,'已进货',2),(41,'光明','蜂蜜',2.00,'已进货',2);
/*!40000 ALTER TABLE `manager_cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_goods`
--

DROP TABLE IF EXISTS `manager_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_goods` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` smallint NOT NULL,
  `name` varchar(20) NOT NULL,
  `unit_sale` decimal(8,2) NOT NULL,
  `measurement` varchar(5) NOT NULL,
  `status` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_goods`
--

LOCK TABLES `manager_goods` WRITE;
/*!40000 ALTER TABLE `manager_goods` DISABLE KEYS */;
INSERT INTO `manager_goods` VALUES (1,1,'牛奶',20.00,'盒','已确认'),(2,2,'空调',3000.00,'台','已确认'),(3,5,'橡皮',2.00,'个','已确认'),(4,3,'篮球鞋',1000.00,'双','已确认'),(5,3,'跑步鞋',1999.00,'双','已确认'),(6,4,'耳机',2500.00,'对','已确认'),(7,4,'电脑',1000.00,'台','未确认'),(8,1,'返老还童丹',9999.00,'颗','已确认'),(9,3,'风火轮',2000.00,'对','已确认'),(10,5,'照妖镜',9999.00,'面','已确认'),(11,2,'金刚钻',2000.00,'个','已确认'),(12,4,'量子计算机',10000.00,'台','已确认'),(13,2,'青龙偃月刀',500.00,'把','已确认'),(21,1,'金箍棒',555.00,'个','已确认'),(22,1,'奶酪',15.00,'块','已确认'),(23,2,'扫把',15.00,'个','已确认'),(24,1,'冰箱',2100.00,'台','已确认'),(25,1,'草莓',2.50,'个','已确认'),(26,1,'梨子',2.50,'个','已确认'),(27,1,'香蕉',2.50,'个','已确认'),(28,1,'测试菠萝',2.25,'个','已确认'),(29,1,'菠萝',2.20,'个','未确认'),(30,1,'荔枝',2.50,'个','已确认'),(31,1,'龙岩',2.20,'个','未确认'),(32,1,'酸奶',2.50,'个','已确认'),(33,4,'手机',6666.00,'部','已确认'),(34,1,'蜂蜜',10.00,'个','已确认');
/*!40000 ALTER TABLE `manager_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_mail`
--

DROP TABLE IF EXISTS `manager_mail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_mail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` varchar(80) NOT NULL,
  `time` datetime(6) NOT NULL,
  `type` smallint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_mail`
--

LOCK TABLES `manager_mail` WRITE;
/*!40000 ALTER TABLE `manager_mail` DISABLE KEYS */;
INSERT INTO `manager_mail` VALUES (1,'新建了<b>蒙牛</b>供应的<b>牛奶</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-08 22:02:42.685218',2),(2,'新建了<b>格力</b>供应的<b>空调</b>单价信息，进货单价为2000.0元，请及时到商品单价界面查看！','2024-06-08 22:03:33.090953',2),(3,'新建了<b>晨光</b>供应的<b>橡皮</b>单价信息，进货单价为5.0元，请及时到商品单价界面查看！','2024-06-08 22:04:08.003038',2),(4,'新建了<b>耐克</b>供应的<b>篮球鞋</b>单价信息，进货单价为2000.0元，请及时到商品单价界面查看！','2024-06-08 22:05:46.027207',2),(5,'新建了<b>李宁</b>供应的<b>跑步鞋</b>单价信息，进货单价为400.0元，请及时到商品单价界面查看！','2024-06-08 22:07:04.105623',2),(6,'新建了<b>华为</b>供应的<b>耳机</b>单价信息，进货单价为1000.0元，请及时到商品单价界面查看！','2024-06-08 22:09:00.410737',2),(7,'商品名称为<b>牛奶</b>的商品信息发生了改动！','2024-06-08 22:10:31.705884',3),(8,'商品名称为<b>空调</b>的商品信息发生了改动！','2024-06-08 22:10:46.478085',3),(9,'商品名称为<b>橡皮</b>的商品信息发生了改动！','2024-06-08 22:11:02.654295',3),(10,'商品名称为<b>篮球鞋</b>的商品信息发生了改动！','2024-06-08 22:11:16.457546',3),(11,'商品名称为<b>跑步鞋</b>的商品信息发生了改动！','2024-06-08 22:11:40.806321',3),(12,'商品名称为<b>耳机</b>的商品信息发生了改动！','2024-06-08 22:12:02.199637',3),(13,'新建了<b>华为</b>供应的<b>电脑</b>单价信息，进货单价为20.0元，请及时到商品单价界面查看！','2024-06-08 22:16:31.824276',2),(14,'商品名称为<b>电脑</b>的商品信息发生了改动！','2024-06-08 22:17:07.829016',3),(15,'新建了<b>蒙牛</b>供应的<b>返老还童丹</b>单价信息，进货单价为4.0元，请及时到商品单价界面查看！','2024-06-08 22:30:36.011520',2),(16,'商品名称为<b>返老还童丹</b>的商品信息发生了改动！','2024-06-08 22:30:54.594959',3),(17,'新建了<b>李宁</b>供应的<b>风火轮</b>单价信息，进货单价为4.0元，请及时到商品单价界面查看！','2024-06-08 22:40:41.960701',2),(18,'商品名称为<b>风火轮</b>的商品信息发生了改动！','2024-06-08 22:41:14.579552',3),(19,'商品名称为<b>风火轮</b>的商品信息发生了改动！','2024-06-08 22:43:32.977188',3),(20,'新建了<b>华为</b>供应的<b>照妖镜</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-08 22:46:40.685564',2),(21,'商品名称为<b>照妖镜</b>的商品信息发生了改动！','2024-06-08 22:46:58.042530',3),(22,'商品名称为<b>照妖镜</b>的商品信息发生了改动！','2024-06-08 22:47:09.976772',3),(23,'商品名称为<b>照妖镜</b>的商品信息发生了改动！','2024-06-08 22:47:34.275453',3),(24,'商品名称为<b>篮球鞋</b>的商品信息发生了改动！','2024-06-08 22:49:06.046267',3),(25,'<b>蒙牛</b>供应的<b>返老还童丹</b>单价由原来的4.00元变为1.25元。','2024-06-08 22:50:33.655617',1),(26,'商品名称为<b>返老还童丹</b>的商品信息发生了改动！','2024-06-08 22:50:54.862086',3),(27,'商品名称为<b>牛奶</b>的商品信息发生了改动！','2024-06-08 22:51:04.328996',3),(28,'新建了<b>华为</b>供应的<b>金刚钻</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-08 23:03:37.883135',2),(29,'商品名称为<b>金刚钻</b>的商品信息发生了改动！','2024-06-08 23:03:58.838756',3),(30,'商品名称为<b>金刚钻</b>的商品信息发生了改动！','2024-06-08 23:04:33.286980',3),(31,'新建了<b>格力</b>供应的<b>量子计算机</b>单价信息，进货单价为20000.0元，请及时到商品单价界面查看！','2024-06-08 23:06:26.041587',2),(32,'商品名称为<b>量子计算机</b>的商品信息发生了改动！','2024-06-08 23:07:21.070990',3),(33,'新建了<b>李宁</b>供应的<b>青龙偃月刀</b>单价信息，进货单价为100.09909909909909元，请及时到商品单价界面查看！','2024-06-08 23:13:55.464035',2),(34,'商品名称为<b>青龙偃月刀</b>的商品信息发生了改动！','2024-06-08 23:16:35.393176',3),(35,'<b>华为</b>供应的<b>电脑</b>单价由原来的20.00元变为100.0元。','2024-06-09 10:22:03.805218',1),(36,'商品名称为<b>电脑</b>的商品信息发生了改动！','2024-06-09 10:23:24.283435',3),(37,'<b>蒙牛</b>供应的<b>牛奶</b>单价由原来的10.00元变为12.0元。','2024-06-09 10:59:08.382353',1),(38,'<b>蒙牛</b>供应的<b>牛奶</b>单价由原来的12.00元变为9.0元。','2024-06-09 10:59:51.581511',1),(39,'<b>耐克</b>供应的<b>篮球鞋</b>单价由原来的2000.00元变为50.0元。','2024-06-09 11:00:23.401391',1),(40,'<b>格力</b>供应的<b>空调</b>单价由原来的2000.00元变为100.0元。','2024-06-09 11:06:53.229481',1),(48,'新建了<b>华为</b>供应的<b>金箍棒</b>单价信息，进货单价为50.0元，请及时到商品单价界面查看！','2024-06-09 11:24:15.756341',2),(49,'新建了<b>蒙牛</b>供应的<b>奶酪</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-09 11:24:50.316214',2),(50,'商品名称为<b>牛奶</b>的商品信息发生了改动！','2024-06-09 12:15:59.142450',3),(51,'商品名称为<b>空调</b>的商品信息发生了改动！','2024-06-09 12:16:04.617970',3),(52,'商品名称为<b>篮球鞋</b>的商品信息发生了改动！','2024-06-09 12:16:11.096016',3),(53,'商品名称为<b>橡皮</b>的商品信息发生了改动！','2024-06-09 12:16:19.034493',3),(54,'商品名称为<b>金箍棒</b>的商品信息发生了改动！','2024-06-09 12:16:46.070610',3),(55,'商品名称为<b>奶酪</b>的商品信息发生了改动！','2024-06-09 12:16:52.184876',3),(56,'<b>蒙牛</b>供应的<b>奶酪</b>单价由原来的10.00元变为100.0元。','2024-06-09 21:33:39.879737',1),(57,'新建了<b>耐克</b>供应的<b>扫把</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-09 21:39:37.562123',2),(58,'商品名称为<b>扫把</b>的商品信息发生了改动！','2024-06-09 21:42:00.407188',3),(59,'新建了<b>光明</b>供应的<b>牛奶</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-09 21:57:56.612687',2),(60,'新建了<b>伊利</b>供应的<b>牛奶</b>单价信息，进货单价为10.0元，请及时到商品单价界面查看！','2024-06-09 21:58:53.971760',2),(61,'<b>光明</b>供应的<b>牛奶</b>单价由原来的10.00元变为15.0元。','2024-06-13 11:17:39.319513',1),(62,'新建了<b>格力</b>供应的<b>冰箱</b>单价信息，进货单价为1000.0元，请及时到商品单价界面查看！','2024-06-13 14:23:55.949917',2),(63,'<b>耐克</b>供应的<b>篮球鞋</b>单价由原来的50.00元变为45.0元。','2024-06-13 14:26:28.629375',1),(64,'<b>李宁</b>供应的<b>跑步鞋</b>单价由原来的400.00元变为420.0元。','2024-06-13 14:26:36.508756',1),(65,'商品名称为<b>奶酪</b>的商品信息发生了改动！','2024-06-13 14:28:38.040183',3),(66,'商品名称为<b>冰箱</b>的商品信息发生了改动！','2024-06-13 14:33:31.369192',3),(67,'新建了<b>蒙牛</b>供应的<b>草莓</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-14 09:53:25.784077',2),(68,'商品名称为<b>草莓</b>的商品信息发生了改动！','2024-06-14 09:54:40.482212',3),(69,'新建了<b>华为</b>供应的<b>梨子</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-14 19:06:51.970237',2),(70,'商品名称为<b>梨子</b>的商品信息发生了改动！','2024-06-14 19:07:37.394248',3),(71,'<b>华为</b>供应的<b>电脑</b>单价由原来的100.00元变为10.0元。','2024-06-18 08:44:02.091923',1),(72,'<b>华为</b>供应的<b>电脑</b>单价由原来的10.00元变为100.0元。','2024-06-18 08:44:53.522771',1),(73,'新建了<b>伊利</b>供应的<b>香蕉</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 08:48:27.656413',2),(74,'商品名称为<b>香蕉</b>的商品信息发生了改动！','2024-06-18 08:49:35.009487',3),(75,'新建了<b>蒙牛</b>供应的<b>测试菠萝</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 09:03:07.933214',2),(76,'商品名称为<b>测试菠萝</b>的商品信息发生了改动！','2024-06-18 09:04:09.970745',3),(77,'新建了<b>光明</b>供应的<b>菠萝</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 09:17:39.323441',2),(78,'新建了<b>光明</b>供应的<b>荔枝</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 13:44:03.542218',2),(79,'商品名称为<b>荔枝</b>的商品信息发生了改动！','2024-06-18 13:44:44.639102',3),(80,'新建了<b>光明</b>供应的<b>龙岩</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 13:47:03.205249',2),(81,'新建了<b>蒙牛</b>供应的<b>酸奶</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-06-18 13:48:35.066961',2),(82,'商品名称为<b>酸奶</b>的商品信息发生了改动！','2024-06-18 13:49:31.174555',3),(83,'新建了<b>华为</b>供应的<b>手机</b>单价信息，进货单价为4.0元，请及时到商品单价界面查看！','2024-07-10 16:12:45.458087',2),(84,'商品名称为<b>手机</b>的商品信息发生了改动！','2024-07-10 16:13:38.629903',3),(85,'<b>蒙牛</b>供应的<b>牛奶</b>单价由原来的9.00元变为2.0元。','2024-07-10 16:14:06.167630',1),(86,'商品名称为<b>牛奶</b>的商品信息发生了改动！','2024-07-10 16:14:16.242118',3),(87,'新建了<b>华为</b>供应的<b>风火轮</b>单价信息，进货单价为100.0元，请及时到商品单价界面查看！','2024-07-10 16:14:43.371988',2),(88,'商品名称为<b>风火轮</b>的商品信息发生了改动！','2024-07-10 16:15:07.214673',3),(89,'<b>耐克</b>供应的<b>篮球鞋</b>单价由原来的45.00元变为100.0元。','2024-07-10 16:19:49.112992',1),(90,'<b>李宁</b>供应的<b>跑步鞋</b>单价由原来的420.00元变为100.0元。','2024-07-10 16:20:07.622134',1),(91,'商品名称为<b>篮球鞋</b>的商品信息发生了改动！','2024-07-10 16:20:14.841678',3),(92,'商品名称为<b>跑步鞋</b>的商品信息发生了改动！','2024-07-10 16:20:18.703546',3),(93,'新建了<b>光明</b>供应的<b>蜂蜜</b>单价信息，进货单价为2.0元，请及时到商品单价界面查看！','2024-07-10 17:44:40.759039',2),(94,'商品名称为<b>蜂蜜</b>的商品信息发生了改动！','2024-07-10 17:45:05.074975',3);
/*!40000 ALTER TABLE `manager_mail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_manager`
--

DROP TABLE IF EXISTS `manager_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_manager` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(20) NOT NULL,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_manager`
--

LOCK TABLES `manager_manager` WRITE;
/*!40000 ALTER TABLE `manager_manager` DISABLE KEYS */;
INSERT INTO `manager_manager` VALUES (1,'123','金缘宝');
/*!40000 ALTER TABLE `manager_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_order_record`
--

DROP TABLE IF EXISTS `manager_order_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_order_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(20) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `goods_order_num` smallint NOT NULL,
  `cost_money` decimal(12,2) NOT NULL,
  `shop_name` varchar(20) NOT NULL,
  `order_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_order_record_goods_name_c4ba0d3b` (`goods_name`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_order_record`
--

LOCK TABLES `manager_order_record` WRITE;
/*!40000 ALTER TABLE `manager_order_record` DISABLE KEYS */;
INSERT INTO `manager_order_record` VALUES (1,'蒙牛','牛奶',1000,10000.00,'邯郸分店','2024-03-19 22:02:42.689987'),(2,'蒙牛','牛奶',1000,10000.00,'交大分店','2024-03-19 22:03:00.912344'),(3,'格力','空调',100,200000.00,'北大分店','2024-03-29 22:03:33.091165'),(4,'晨光','橡皮',2000,10000.00,'南大分店','2024-06-08 22:04:08.003038'),(5,'晨光','橡皮',1000,5000.00,'厦大分店','2024-06-08 22:04:37.944723'),(6,'耐克','篮球鞋',50,100000.00,'同济分店','2024-04-08 22:05:46.029268'),(7,'李宁','跑步鞋',50,20000.00,'上财分店','2024-04-08 22:07:04.105623'),(8,'华为','耳机',100,100000.00,'邯郸分店','2024-04-18 22:09:00.413718'),(9,'华为','电脑',100,2000.00,'北大分店','2024-02-29 22:16:31.824276'),(10,'蒙牛','返老还童丹',200,800.00,'厦大分店','2024-05-14 22:30:36.014493'),(11,'李宁','风火轮',500,2000.00,'南大分店','2024-03-19 22:40:41.960701'),(12,'华为','照妖镜',100,1000.00,'川大分店','2024-03-19 22:46:40.685564'),(13,'蒙牛','返老还童丹',20,25.00,'厦大分店','2024-05-14 22:50:33.655617'),(14,'华为','金刚钻',1000,10000.00,'浙大分店','2024-03-19 23:03:37.883135'),(15,'格力','量子计算机',50,1000000.00,'交大分店','2024-03-09 23:06:26.041587'),(16,'李宁','青龙偃月刀',666,66666.00,'郑州分店','2024-03-16 23:13:55.464035'),(17,'华为','电脑',500,50000.00,'南大分店','2024-06-09 10:22:03.805218'),(18,'蒙牛','牛奶',1000,9000.00,'浙大分店','2024-06-09 10:59:51.581511'),(19,'耐克','篮球鞋',2000,100000.00,'郑州分店','2024-06-09 11:00:23.401391'),(20,'格力','空调',20,2000.00,'邯郸分店','2024-06-09 11:06:53.229481'),(21,'华为','金箍棒',10,500.00,'浙大分店','2024-06-09 11:24:15.758080'),(22,'蒙牛','奶酪',520,5200.00,'浙大分店','2024-06-09 11:24:50.316214'),(23,'蒙牛','奶酪',500,5000.00,'同济分店','2024-06-09 11:33:00.047649'),(24,'蒙牛','奶酪',10,1000.00,'厦大分店','2024-06-09 21:33:39.880737'),(25,'华为','电脑',500,50000.00,'南大分店','2024-06-09 21:35:22.811207'),(26,'耐克','扫把',10,100.00,'邯郸分店','2024-06-09 21:39:37.566124'),(27,'光明','牛奶',10,100.00,'浙大分店','2024-06-09 21:57:56.613686'),(28,'伊利','牛奶',100,1000.00,'川大分店','2024-06-09 21:58:53.972760'),(29,'光明','牛奶',200,3000.00,'郑州分店','2024-06-13 11:17:39.319513'),(30,'华为','电脑',500,50000.00,'南大分店','2024-06-13 11:46:12.356930'),(31,'格力','冰箱',20,20000.00,'北大分店','2024-06-13 14:23:55.951584'),(32,'华为','电脑',500,50000.00,'南大分店','2024-06-14 09:50:00.790833'),(33,'蒙牛','草莓',100,200.00,'邯郸分店','2024-06-14 09:53:25.784077'),(34,'华为','电脑',500,50000.00,'南大分店','2024-06-14 18:51:49.814502'),(35,'华为','电脑',500,50000.00,'南大分店','2024-06-14 18:55:35.571781'),(36,'华为','电脑',500,50000.00,'南大分店','2024-06-14 19:03:46.249717'),(37,'华为','梨子',10,20.00,'邯郸分店','2024-06-14 19:06:51.972232'),(38,'华为','电脑',500,50000.00,'南大分店','2024-06-18 08:44:53.526825'),(39,'伊利','香蕉',10,20.00,'邯郸分店','2024-06-18 08:48:27.659944'),(40,'华为','电脑',500,50000.00,'南大分店','2024-06-18 08:59:49.449588'),(41,'蒙牛','测试菠萝',10,20.00,'邯郸分店','2024-06-18 09:03:07.945928'),(42,'华为','电脑',500,50000.00,'南大分店','2024-06-18 09:13:57.423879'),(43,'光明','菠萝',10,20.00,'邯郸分店','2024-06-18 09:17:39.323441'),(44,'华为','电脑',500,50000.00,'南大分店','2024-06-18 13:37:35.523175'),(45,'光明','荔枝',10,20.00,'邯郸分店','2024-06-18 13:44:03.549797'),(46,'光明','龙岩',10,20.00,'邯郸分店','2024-06-18 13:47:03.205249'),(47,'蒙牛','酸奶',10,20.00,'邯郸分店','2024-06-18 13:48:35.082094'),(48,'华为','手机',500,2000.00,'交大分店','2024-07-10 16:12:45.458087'),(49,'蒙牛','牛奶',2000,4000.00,'交大分店','2024-07-10 16:14:06.167630'),(50,'华为','风火轮',50,5000.00,'交大分店','2024-07-10 16:14:43.371988'),(51,'耐克','篮球鞋',200,20000.00,'交大分店','2024-07-10 16:19:49.112992'),(52,'李宁','跑步鞋',200,20000.00,'交大分店','2024-07-10 16:20:07.622134'),(53,'华为','电脑',500,50000.00,'南大分店','2024-07-10 17:41:16.103801'),(54,'光明','蜂蜜',10,20.00,'交大分店','2024-07-10 17:44:40.763032'),(55,'华为','金箍棒',10,500.00,'华师大分店','2024-07-11 22:33:47.648540');
/*!40000 ALTER TABLE `manager_order_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_remain`
--

DROP TABLE IF EXISTS `manager_remain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_remain` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(20) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `goods_remain` smallint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_remain_goods_name_f491ad46` (`goods_name`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_remain`
--

LOCK TABLES `manager_remain` WRITE;
/*!40000 ALTER TABLE `manager_remain` DISABLE KEYS */;
INSERT INTO `manager_remain` VALUES (1,'邯郸分店','牛奶',638),(2,'交大分店','牛奶',2212),(3,'北大分店','空调',20),(4,'南大分店','橡皮',2000),(5,'厦大分店','橡皮',250),(6,'同济分店','篮球鞋',50),(7,'上财分店','跑步鞋',50),(8,'邯郸分店','耳机',53),(9,'北大分店','电脑',30),(10,'厦大分店','返老还童丹',125),(11,'南大分店','风火轮',466),(12,'川大分店','照妖镜',15),(13,'浙大分店','金刚钻',820),(14,'交大分店','量子计算机',2),(15,'郑州分店','青龙偃月刀',316),(16,'南大分店','电脑',6000),(17,'浙大分店','牛奶',1010),(18,'郑州分店','篮球鞋',2000),(19,'邯郸分店','空调',20),(27,'浙大分店','金箍棒',0),(28,'浙大分店','奶酪',520),(29,'同济分店','奶酪',500),(30,'厦大分店','奶酪',10),(31,'邯郸分店','扫把',9),(32,'川大分店','牛奶',100),(33,'郑州分店','牛奶',200),(34,'北大分店','冰箱',20),(35,'邯郸分店','草莓',100),(36,'邯郸分店','梨子',10),(37,'邯郸分店','香蕉',10),(38,'邯郸分店','测试菠萝',10),(39,'邯郸分店','菠萝',10),(40,'邯郸分店','荔枝',10),(41,'邯郸分店','龙岩',10),(42,'邯郸分店','酸奶',10),(43,'交大分店','手机',480),(44,'交大分店','风火轮',50),(45,'交大分店','篮球鞋',180),(46,'交大分店','跑步鞋',160),(47,'交大分店','蜂蜜',10),(48,'华师大分店','金箍棒',10);
/*!40000 ALTER TABLE `manager_remain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_sale_record`
--

DROP TABLE IF EXISTS `manager_sale_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_sale_record` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(20) NOT NULL,
  `goods_name` varchar(20) NOT NULL,
  `goods_sale_num` smallint NOT NULL,
  `turnover` decimal(10,2) NOT NULL,
  `sale_time` datetime(6) NOT NULL,
  `sale_man_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `manager_sale_record_goods_name_68c7e492` (`goods_name`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_sale_record`
--

LOCK TABLES `manager_sale_record` WRITE;
/*!40000 ALTER TABLE `manager_sale_record` DISABLE KEYS */;
INSERT INTO `manager_sale_record` VALUES (1,'邯郸分店','耳机',1,2500.00,'2024-06-07 22:13:42.801717',1),(2,'邯郸分店','耳机',1,2500.00,'2024-05-25 22:13:46.245982',1),(3,'邯郸分店','耳机',5,12500.00,'2024-05-21 22:13:49.147165',1),(4,'邯郸分店','牛奶',200,4000.00,'2024-04-21 22:13:53.480694',1),(5,'邯郸分店','耳机',25,62500.00,'2024-06-07 22:13:58.401740',1),(6,'邯郸分店','牛奶',150,3000.00,'2024-04-01 22:14:03.279503',1),(7,'北大分店','电脑',20,400000.00,'2024-04-21 22:17:53.713574',3),(8,'北大分店','电脑',20,400000.00,'2024-05-01 22:17:57.226202',3),(9,'北大分店','空调',20,80000.00,'2024-04-14 22:18:00.836441',3),(10,'北大分店','空调',20,80000.00,'2024-05-15 22:18:03.679847',3),(11,'北大分店','空调',20,80000.00,'2024-05-17 22:18:07.835748',3),(12,'北大分店','空调',20,80000.00,'2024-04-27 22:18:11.180455',3),(13,'北大分店','电脑',10,200000.00,'2024-05-01 22:25:31.858216',3),(14,'北大分店','电脑',10,200000.00,'2024-06-05 22:25:36.058608',3),(15,'北大分店','电脑',10,200000.00,'2024-04-27 22:25:40.524903',3),(16,'厦大分店','橡皮',500,4250.00,'2024-06-08 22:28:09.759275',8),(17,'厦大分店','橡皮',250,2125.00,'2024-06-08 22:28:14.080679',8),(18,'厦大分店','返老还童丹',5,50000.00,'2024-05-25 22:33:13.069841',8),(19,'厦大分店','返老还童丹',5,50000.00,'2024-05-22 22:33:18.847762',8),(20,'厦大分店','返老还童丹',5,50000.00,'2024-05-24 22:33:22.059131',8),(21,'厦大分店','返老还童丹',10,100000.00,'2024-05-30 22:33:25.503214',8),(22,'厦大分店','返老还童丹',10,100000.00,'2024-05-19 22:33:28.670098',8),(23,'南大分店','风火轮',2,40000.00,'2024-05-24 22:41:56.015180',5),(24,'南大分店','风火轮',2,40000.00,'2024-05-15 22:41:59.370950',5),(25,'南大分店','风火轮',5,100000.00,'2024-06-12 22:42:02.592757',5),(26,'南大分店','风火轮',5,100000.00,'2024-04-24 22:42:05.292599',5),(27,'南大分店','风火轮',10,200000.00,'2024-05-13 22:42:08.329151',5),(28,'南大分店','风火轮',10,200000.00,'2024-04-02 22:42:11.759406',5),(29,'川大分店','照妖镜',5,49995.00,'2024-05-01 22:47:48.538126',9),(30,'川大分店','照妖镜',10,99990.00,'2024-04-20 22:47:51.804543',9),(31,'川大分店','照妖镜',20,199980.00,'2024-04-26 22:47:54.893479',9),(32,'川大分店','照妖镜',50,499950.00,'2024-06-04 22:47:58.260888',9),(33,'厦大分店','返老还童丹',20,199980.00,'2024-05-28 22:52:11.805087',8),(34,'厦大分店','返老还童丹',20,199980.00,'2024-06-08 22:52:15.404890',8),(35,'厦大分店','返老还童丹',20,199980.00,'2024-05-30 22:52:18.415840',8),(36,'浙大分店','金刚钻',20,40000.00,'2024-05-15 23:04:54.494502',10),(37,'浙大分店','金刚钻',20,40000.00,'2024-05-11 23:04:59.716589',10),(38,'浙大分店','金刚钻',20,40000.00,'2024-05-07 23:05:03.516978',10),(39,'浙大分店','金刚钻',20,40000.00,'2024-04-29 23:05:06.638894',10),(40,'浙大分店','金刚钻',50,100000.00,'2024-04-04 23:05:09.561644',10),(41,'浙大分店','金刚钻',50,100000.00,'2024-04-12 23:05:12.506056',10),(42,'交大分店','量子计算机',20,200000.00,'2024-04-15 23:07:48.717221',7),(43,'交大分店','量子计算机',15,150000.00,'2024-04-29 23:07:51.872558',7),(44,'交大分店','牛奶',500,10000.00,'2024-05-04 23:15:11.347471',7),(45,'交大分店','牛奶',288,5760.00,'2024-04-05 23:15:15.628441',7),(46,'交大分店','量子计算机',10,100000.00,'2024-05-02 23:15:31.406363',7),(47,'郑州分店','青龙偃月刀',50,25000.00,'2024-05-21 23:16:51.584462',11),(48,'郑州分店','青龙偃月刀',66,33000.00,'2024-05-19 23:16:54.895489',11),(49,'郑州分店','青龙偃月刀',74,37000.00,'2024-05-18 23:16:57.740379',11),(50,'郑州分店','青龙偃月刀',35,17500.00,'2024-05-18 23:17:00.519793',11),(51,'郑州分店','青龙偃月刀',25,12500.00,'2024-05-29 23:17:04.595056',11),(52,'郑州分店','青龙偃月刀',100,50000.00,'2024-05-25 23:17:07.950894',11),(53,'邯郸分店','牛奶',2,40.00,'2024-06-09 12:31:53.910088',1),(54,'邯郸分店','牛奶',10,200.00,'2024-06-09 21:38:18.072291',1),(55,'邯郸分店','扫把',1,15.00,'2024-06-13 12:19:36.774799',1),(56,'邯郸分店','耳机',2,5000.00,'2024-06-14 09:51:58.434735',1),(57,'邯郸分店','耳机',2,5000.00,'2024-06-14 19:05:40.698191',1),(58,'邯郸分店','耳机',2,5000.00,'2024-06-18 08:46:39.755990',1),(59,'邯郸分店','耳机',2,5000.00,'2024-06-18 09:01:26.730874',1),(60,'邯郸分店','耳机',2,5000.00,'2024-06-18 09:15:58.307859',1),(61,'邯郸分店','耳机',5,12500.00,'2024-06-18 13:40:12.636011',1),(62,'交大分店','篮球鞋',20,20000.00,'2024-07-10 16:20:58.190981',7),(63,'交大分店','跑步鞋',40,79960.00,'2024-07-10 16:21:01.827784',7),(64,'交大分店','手机',20,133320.00,'2024-07-10 16:21:05.635920',7),(65,'交大分店','量子计算机',2,20000.00,'2024-07-10 16:21:12.307400',7),(66,'交大分店','量子计算机',1,10000.00,'2024-07-10 17:43:09.876780',7),(67,'浙大分店','金箍棒',10,5550.00,'2024-07-11 22:35:22.844842',10);
/*!40000 ALTER TABLE `manager_sale_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_shop`
--

DROP TABLE IF EXISTS `manager_shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_shop` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `location` varchar(15) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `salesman_name` varchar(10) NOT NULL,
  `status` smallint NOT NULL,
  `location_specific` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `telephone_1` (`telephone`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_shop`
--

LOCK TABLES `manager_shop` WRITE;
/*!40000 ALTER TABLE `manager_shop` DISABLE KEYS */;
INSERT INTO `manager_shop` VALUES (1,'邯郸分店','上海市-杨浦区','18276951268','钱糖浆',1,'邯郸路220号'),(2,'北大分店','北京市-海淀区','13376951268','郝运来',1,'颐和园路5号'),(3,'同济分店','上海市-杨浦区','18274251268','黄朴姜',1,'四平路1239号'),(4,'南大分店','江苏省-南京市','18276951299','郑器水',1,'栖霞区仙林大道163号'),(5,'上财分店','上海市-杨浦区','13328567755','石芬渺',1,'国定路777号'),(6,'交大分店','上海市-闵行区','13376950968','白芊万',1,'东川路800号'),(7,'厦大分店','福建省-厦门市','18276651209','陈秦表',1,'思明南路422号'),(8,'川大分店','四川省-成都市','13622224487','孙乌空',1,'望江路19号'),(9,'浙大分店','浙江省-杭州市','18896585124','宝舰品',1,'玉古路154号'),(10,'郑州分店','河南省-郑州市','18599632145','辛篇樟',1,'黄河东路129号'),(11,'华师大分店','上海市-闵行区','18585967416','易生君',1,'东川路500号');
/*!40000 ALTER TABLE `manager_shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_supplier`
--

DROP TABLE IF EXISTS `manager_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager_supplier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `telephone_1` (`telephone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_supplier`
--

LOCK TABLES `manager_supplier` WRITE;
/*!40000 ALTER TABLE `manager_supplier` DISABLE KEYS */;
INSERT INTO `manager_supplier` VALUES (1,'蒙牛','13376951268','mengniu@163.com'),(2,'格力','18276951299','geli@gmail.com'),(3,'晨光','18874159657','chenguang@qq.com'),(4,'耐克','15696325632','nike@126.com'),(5,'李宁','18356897152','lining@oxford.com'),(6,'华为','17745125699','huawei@hw.com'),(7,'光明','19982938473','guangming@gm.com'),(8,'伊利','13349495857','yili@yl.com');
/*!40000 ALTER TABLE `manager_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff_salesman`
--

DROP TABLE IF EXISTS `staff_salesman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff_salesman` (
  `id` int NOT NULL AUTO_INCREMENT,
  `salesman_password` varchar(20) NOT NULL,
  `salesman_name` varchar(10) NOT NULL,
  `shop_id_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `staff_salesman_shop_id_id_b28bc9ca_fk_manager_shop_id` (`shop_id_id`),
  CONSTRAINT `staff_salesman_shop_id_id_b28bc9ca_fk_manager_shop_id` FOREIGN KEY (`shop_id_id`) REFERENCES `manager_shop` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff_salesman`
--

LOCK TABLES `staff_salesman` WRITE;
/*!40000 ALTER TABLE `staff_salesman` DISABLE KEYS */;
INSERT INTO `staff_salesman` VALUES (1,'KKkk1111','钱糖浆',1),(2,'KKkk2222','金翠兰',1),(3,'KKkk3333','郝运来',2),(4,'KKkk4444','黄朴姜',3),(5,'KKkk5555','郑器水',4),(6,'KKkk6666','石芬渺',5),(7,'KKkk7777','白芊万',6),(8,'KKkk8888','陈秦表',7),(9,'KKkk9999','孙乌空',8),(10,'KKkk1111','宝舰品',9),(11,'KKkk1111','辛篇樟',10),(12,'KKkk6666','易生君',11);
/*!40000 ALTER TABLE `staff_salesman` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-20 18:22:25
