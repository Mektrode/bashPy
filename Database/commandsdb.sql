-- MySQL Script generated by MySQL Workbench
-- Tue Oct 29 15:33:29 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema CommandDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema CommandDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `CommandDB` DEFAULT CHARACTER SET utf8 ;
USE `CommandDB` ;

-- -----------------------------------------------------
-- Table `CommandDB`.`list_of_commands`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CommandDB`.`list_of_commands` ;

CREATE TABLE IF NOT EXISTS `CommandDB`.`list_of_commands` (
  `command_id` INT NOT NULL AUTO_INCREMENT,
  `command_name` VARCHAR(100) NULL,
  `description` MEDIUMTEXT NULL,
  PRIMARY KEY (`command_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CommandDB`.`list_of_keywords`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CommandDB`.`list_of_keywords` ;

CREATE TABLE IF NOT EXISTS `CommandDB`.`list_of_keywords` (
  `keyword_id` INT NOT NULL AUTO_INCREMENT,
  `parent_id` INT NOT NULL,
  `keyword` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`keyword_id`),
  CONSTRAINT `fk_list_of_keywords_list_of_commands`
    FOREIGN KEY (`parent_id`)
    REFERENCES `CommandDB`.`list_of_commands` (`command_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_list_of_keywords_list_of_commands_idx` ON `CommandDB`.`list_of_keywords` (`parent_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `CommandDB`.`list_of_short_options`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `CommandDB`.`list_of_short_options` ;

CREATE TABLE IF NOT EXISTS `CommandDB`.`list_of_short_options` (
  `parent_id` INT NOT NULL,
  `option_command_name` VARCHAR(45) NULL,
  `option_description` MEDIUMTEXT NULL,
  PRIMARY KEY (`parent_id`),
  CONSTRAINT `fk_short_option_indices_list_of_commands1`
    FOREIGN KEY (`parent_id`)
    REFERENCES `CommandDB`.`list_of_commands` (`command_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_short_option_indices_list_of_commands1_idx` ON `CommandDB`.`list_of_short_options` (`parent_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
