import sqlite3

DATABASE_NAME = 'farmacia.db'


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    tables = [
        """CREATE TABLE Inventario (
            idProducto INTEGER PRIMARY KEY,
            Nombre VARCHAR(45),
            Id_presentacion INTEGER,
            Id_laboratorio INTEGER,
            Concentracion INTEGER,
            Existencia_minima INTEGER,
            idPrescripcion INTEGER
        )""",
        """CREATE TABLE Ventas (
            idVenta INTEGER PRIMARY KEY,
            Id_Producto INTEGER,
            Cantidad INTEGER,
            Precio FLOAT,
            Descuento FLOAT,
            Total_importe FLOAT,
            Fecha DATE,
            Hora TIME,
            Id_empleado INTEGER,
            idEstado INTEGER,
            idLote VARCHAR(25),
            FOREIGN KEY (Id_Producto) REFERENCES Inventario(idProducto),
            FOREIGN KEY (idEstado) REFERENCES Estado_Ventas(idEstadoVenta)
        )""",
        """CREATE TABLE Lotes (
            idLote VARCHAR(25) PRIMARY KEY,
            Fecha_vencimiento DATE
        )""",
        """CREATE TABLE Compras (
            idCompra INTEGER PRIMARY KEY,
            Id_Proveedor INTEGER,
            No_factura VARCHAR(25),
            Fecha DATE
        )""",
        """CREATE TABLE Ajustes (
            idAjuste INTEGER PRIMARY KEY,
            IdProducto INTEGER,
            Motivo INTEGER,
            Cantidad INTEGER,
            Fecha DATE,
            Tipo VARCHAR(30),
            idLote VARCHAR(25),
            FOREIGN KEY (IdProducto) REFERENCES Inventario(idProducto),
            FOREIGN KEY (idLote) REFERENCES Lotes(idLote)
        )""",
        """CREATE TABLE BitExistenciaInicial (
            idBitExistenciaInicial INTEGER PRIMARY KEY,
            idProducto INTEGER,
            idLote VARCHAR(25),
            Cantidad INTEGER,
            FOREIGN KEY (idProducto) REFERENCES Inventario(idProducto),
            FOREIGN KEY (idLote) REFERENCES Lotes(idLote)
        )""",
        """CREATE TABLE Estado_Ventas (
            idEstadoVenta INTEGER PRIMARY KEY,
            Descripcion VARCHAR(60)
        )""",
        """CREATE TABLE Detalle_Lote (
            idProducto INTEGER,
            idLote VARCHAR(25),
            FechaIngreso DATE,
            Cantidad INTEGER,
            Precio_Compra FLOAT,
            Porcentaje_Ganancia INTEGER,
            Porcentaje_Descuento INTEGER,
            Precio_Venta FLOAT,
            PRIMARY KEY (idProducto, idLote),
            FOREIGN KEY (idProducto) REFERENCES Inventario(idProducto),
            FOREIGN KEY (idLote) REFERENCES Lotes(idLote)
        )""",
        """CREATE TABLE Devoluciones (
            idDevolucion INTEGER PRIMARY KEY,
            idVenta INTEGER,
            Cantidad INTEGER,
            Fecha DATE,
            Hora TIME,
            idEmpleado INTEGER,
            FOREIGN KEY (idVenta) REFERENCES Ventas(idVenta)
        )""",
        """CREATE TABLE Detalle_Compra (
            Id_compra INTEGER,
            Id_producto INTEGER,
            Cantidad INTEGER,
            Precio_compra FLOAT,
            idLote VARCHAR(25),
            PRIMARY KEY (Id_compra, Id_producto),
            FOREIGN KEY (Id_compra) REFERENCES Compras(idCompra),
            FOREIGN KEY (Id_producto) REFERENCES Inventario(idProducto),
            FOREIGN KEY (idLote) REFERENCES Lotes(idLote)
        )"""
    ]

    try:
        db = get_db()
        cursor = db.cursor()
        for table in tables:
            cursor.execute(table)
        db.commit()
    except sqlite3.Error as e:
        print(f"Error en la creación de tablas: {e}")
    finally:
        db.close()

create_tables()
