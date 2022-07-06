-- Crear una database 'hbtn_0d_usa' y la tabla 'states' (in the database)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE, name VARCHAR(256));
