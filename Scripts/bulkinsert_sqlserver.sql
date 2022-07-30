set statistics time on

BULK INSERT 
     farmaceutico
        FROM 'C:\dataset\CreacionRegistros\farmaceutico.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);


BULK INSERT 
     proveedor
        FROM 'C:\dataset\CreacionRegistros\proveedor.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);

BULK INSERT 
     cliente
        FROM 'C:\dataset\CreacionRegistros\cliente.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);

BULK INSERT 
     categoria
        FROM 'C:\dataset\CreacionRegistros\categoria.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);

BULK INSERT 
     producto
        FROM 'C:\dataset\CreacionRegistros\producto.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);

BULK INSERT 
     factura
        FROM 'C:\dataset\CreacionRegistros\factura.csv'
        WITH (
            FIELDTERMINATOR = ';',
            ROWTERMINATOR = '\n',
            FIRSTROW = 2,
            MAXERRORS = 3
);

set statistics time off
