-- Crear el usuario del servidor MySQL 'user_0d_1'
-- con todos los permisos  &&  no debe fallar si ya existe
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILIEGES ON * . * TO 'user_0d_1'@'localhost';
