CREATE DATABASE citiesData;
use citiesData;

CREATE TABLE IF NOT EXISTS tblCitiesImport (
    "Index" INT(11),
    "Living Space (sq ft)" DECIMAL(10, 2),
    "Beds" DECIMAL(10, 2),
    "Baths" DECIMAL(10, 2),
    "Zip" DECIMAL(10, 2),
    "Year" DECIMAL(10, 2),
    "List Price ($)" DECIMAL(10, 2)
    PRIMARY KEY ("Index")
);
INSERT INTO tblCitiesImport VALUES
(1, 2222, 3, 3.5, 32312, 1981, 250000);
(2, 1628, 3, 2, 32308, 2009, 185000);
(3, 3824, 5, 4, 32312, 1954, 399000);
(4, 1137, 3, 2, 32309, 1993, 150000);
(7, 3631, 4, 3, 32309, 1996, 649000);
(8, 2483, 4, 3, 32312, 2016, 399000);
(9, 2400, 4, 4, 32312, 2002, 613000);
(10, 1997, 3, 3, 32311, 2006, 295000);