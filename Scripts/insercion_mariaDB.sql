LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/farmaceutico.csv'
INTO TABLE farmaceutico
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/proveedor.csv'
INTO TABLE proveedor
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/cliente.csv'
INTO TABLE cliente
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;

LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/categoria.csv'
INTO TABLE categoria
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;


LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/producto.csv'
INTO TABLE producto
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;


LOAD DATA
INFILE 'C:/xampp/dataset/CreacionRegistros/factura.csv'
INTO TABLE factura
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS;