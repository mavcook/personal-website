DROP DATABASE IF EXISTS mavcooksite;
CREATE DATABASE mavcooksite;
USE mavcooksite;

CREATE USER IF NOT EXISTS '<user>'@'localhost';
GRANT SELECT ON mavcooksite.* TO '<user>'@'localhost';
ALTER USER '<user>'@'localhost' IDENTIFIED BY '<insertPass>';


CREATE TABLE Project(
    project_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    date DATETIME,
    isfeatured BOOL NOT NULL DEFAULT 0,
    description TEXT,
    thumbnail VARCHAR(255) NOT NULL,
    project_seq TINYINT UNSIGNED NOT NULL,
    type CHAR(3) NOT NULL,

    PRIMARY KEY (project_id)
);

CREATE TABLE PTags(
    ptag_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,

    PRIMARY KEY (ptag_id)
);


CREATE TABLE TagsToProject(
    project_id TINYINT UNSIGNED NOT NULL,
    ptag_id TINYINT UNSIGNED NOT NULL, #tag (graphic design, programming, photography, videography, editing, )

    FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE,
    FOREIGN KEY (ptag_id) REFERENCES PTags(ptag_id) ON DELETE CASCADE
);

CREATE TABLE Media(
    media_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    project_id TINYINT UNSIGNED NOT NULL,
    directoryPath VARCHAR(255) NOT NULL,

    PRIMARY KEY (media_id),
    FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE
);


-- CREATE TABLE Related
-- resumeEntryId
-- project_id
