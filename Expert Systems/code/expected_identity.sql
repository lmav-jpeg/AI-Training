#Instruction : Populate this database with some correct and incorrect data
DROP DATABASE IF EXISTS KnowledgeBase;

CREATE DATABASE KnowledgeBase;
USE KnowledgeBase;

CREATE TABLE bios (
 biosID SMALLINT UNSIGNED AUTO_INCREMENT,
 manufacturer VARCHAR(40) NOT NULL,
 serialNumber VARCHAR(40) NOT NULL,
 version VARCHAR(60) NOT NULL,
 CONSTRAINT bios_pk PRIMARY KEY (biosID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#INSERT INTO bios(manufacturer, serialNumber, version)
#VALUES("","","");

CREATE TABLE computer (
 computerID SMALLINT UNSIGNED AUTO_INCREMENT,
 manufacturer VARCHAR(40) NOT NULL,
 model VARCHAR(40) NOT NULL,
 systemFamily VARCHAR(60) NOT NULL,
 CONSTRAINT computer_pk PRIMARY KEY (computerID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#INSERT INTO computer(manufacturer, model, systemFamily)
#VALUES("","","");

CREATE TABLE motherboard (
 motherboardID SMALLINT UNSIGNED AUTO_INCREMENT,
 manufacturer VARCHAR(40) NOT NULL,
 product VARCHAR(40) NOT NULL,
 serialNumber VARCHAR(60) NOT NULL,
 CONSTRAINT motherboard_pk PRIMARY KEY (motherboardID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#INSERT INTO motherboard(manufacturer, product, serialNumber)
#VALUES("","","");

CREATE TABLE processor (
 processorID VARCHAR(100) UNIQUE NOT NULL ,
 manufacturer VARCHAR(40) NOT NULL,
 name VARCHAR(100) NOT NULL,
 CONSTRAINT processor_pk PRIMARY KEY (processorID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
#INSERT INTO processor(processorID, manufacturer, name)
#VALUES("","","");

CREATE TABLE memory (
 memoryID SMALLINT UNSIGNED AUTO_INCREMENT,
 manufacturer VARCHAR(40) NOT NULL,
 serialNumber VARCHAR(60) NOT NULL,
 capacity BIGINT NOT NULL,
 numberMemory SMALLINT UNSIGNED,
 partNumber VARCHAR(150) NOT NULL,
 CONSTRAINT memory_pk PRIMARY KEY (memoryID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#INSERT INTO memory(manufacturer, serialNumber,capacity,numberMemory, partNumber)
#VALUES("","",, ,"");

CREATE TABLE disks (
 diskID SMALLINT UNSIGNED AUTO_INCREMENT,
 model VARCHAR(40) NOT NULL,
 serialNumber VARCHAR(80) NOT NULL,
 CONSTRAINT disks_pk PRIMARY KEY (diskID)
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#INSERT INTO disks(model, serialNumber)
#VALUES("","");