CREATE DATABASE Farmacia

USE Farmacia
GO

CREATE TABLE farmaceutico (
	id_farma INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL
);

CREATE TABLE proveedor (
	id_proveedor INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	nombre_responsable VARCHAR(50) NOT NULL
);

CREATE TABLE cliente (
	id_cliente INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	telefono VARCHAR(15) NOT NULL,
	direccion VARCHAR(100)
);

CREATE TABLE categoria(
	id_categoria INT IDENTITY(1,1) PRIMARY KEY,
	categoria VARCHAR(100) NOT NULL
);

CREATE TABLE producto (
	id_producto INT IDENTITY(1,1) PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	unidades_stock INT NOT NULL,
	id_categoria INT NOT NULL,
	id_proveedor INT NOT NULL
);


CREATE TABLE factura(
	id_factura INT IDENTITY(1,1) PRIMARY KEY,
	descripcion VARCHAR(100) NOT NULL,
	fecha DATE NOT NULL,
	cantidad INT NOT NULL,
	total DECIMAL NOT NULL,
	id_farma INT NOT NULL,
	id_cliente INT NOT NULL,
	id_producto INT NOT NULL
);

ALTER TABLE producto ADD FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
ALTER TABLE producto ADD FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor)
ALTER TABLE factura ADD FOREIGN KEY (id_farma) REFERENCES farmaceutico(id_farma)
ALTER TABLE factura ADD FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
ALTER TABLE factura ADD FOREIGN KEY (id_producto) REFERENCES producto(id_producto)