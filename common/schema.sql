SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema garmin_menopause
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `garmin_menopause` ;

-- -----------------------------------------------------
-- Schema garmin_menopause
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `garmin_menopause` DEFAULT CHARACTER SET utf8 ;
USE `garmin_menopause` ;

-- -----------------------------------------------------
-- Table `garmin_menopause`.`story`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `garmin_menopause`.`fittowork_player_scores` ;

CREATE TABLE IF NOT EXISTS `garmin_menopause`.`fittowork_player_scores` (
  `id`  INT NOT NULL AUTO_INCREMENT,
  `player_id` VARCHAR(36) NOT NULL,
  `solo_score` INT NULL,
  `team_score` INT NOT NULL,
  `team_p1_id` VARCHAR(36) NOT NULL,
  `team_p1_score` INT NOT NULL,
  `team_p2_id` VARCHAR(36) NOT NULL,
  `team_p2_score` INT NOT NULL,
  `team_p3_id` VARCHAR(36) NOT NULL,
  `team_p3_score` INT NOT NULL,
  `comp_score` INT NOT NULL,
  `comp_p1_id` VARCHAR(36) NOT NULL,
  `comp_p1_score` INT NOT NULL,
  `comp_p2_id` VARCHAR(36) NOT NULL,
  `comp_p2_score` INT NOT NULL,
  `comp_p3_id` VARCHAR(36) NOT NULL,
  `comp_p3_score` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;

CREATE INDEX `topic_idx` ON `garmin_menopause`.`fittowork_player_scores` (`player_id` ASC) VISIBLE;