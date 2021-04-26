CREATE DATABASE fordData;
use fordData;

CREATE TABLE IF NOT EXISTS tblFordImport (
    `id` int AUTO_INCREMENT,
    `year` NUMERIC(4, 4),
    `mileage` NUMERIC(2, 1),
    `price` NUMERIC(7, 4),
    PRIMARY KEY (`id`)
);
INSERT INTO tblFordImport (year,mileage,price) VALUES
(1998, 27, 9991);
(1997, 17, 992500);
(1998, 28, 10491);
(1998, 5, 10990);
(1997, 38, 9493);
(1997, 36, 9991);
(1997, 24, 10490);
(1997, 37, 9491);