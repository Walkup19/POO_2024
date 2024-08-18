from conexionDB import *

class Productos():
    def __init__(self, nombre, categoria, cantidad, precio_unitario, descripcion):
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.descripcion = descripcion

class Maquinaria(Productos):
    def __init__(self, nombre, categoria, cantidad, precio_unitario, descripcion, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria):
        super().__init__(nombre, categoria, cantidad, precio_unitario, descripcion)
        self.tipo_maquinaria = tipo_maquinaria
        self.marca_maquinaria = marca_maquinaria
        self.modelo_maquinaria = modelo_maquinaria
        self.anio_fabricacion = anio_fabricacion
        self.num_serie = num_serie
        self.estado_maquinaria = estado_maquinaria

    def crear(self):
        try:
            #Insertar en productos
            cursor.execute(
                "INSERT INTO productos(nombre, categoria, cantidad, precio_unitario, descripcion) VALUES(%s, %s, %s, %s, %s)",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion)
            )

            #Obtener el ID del producto recién insertado
            id_producto = cursor.lastrowid

            #Insertar en materiales
            cursor.execute(
                "INSERT INTO maquinaria(id_maquinaria, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                (id_producto, self.tipo_maquinaria, self.marca_maquinaria, self.modelo_maquinaria, self.anio_fabricacion, self.num_serie, self.estado_maquinaria)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Error al crear el producto. ", excepcion)
            return False


    @classmethod
    def mostrar(self):
        try:
            cursor.execute(
                "SELECT productos.id_producto, productos.nombre, productos.categoria, productos.cantidad, productos.precio_unitario, productos.descripcion, "
                "maquinaria.tipo_maquinaria, maquinaria.marca_maquinaria, maquinaria.modelo_maquinaria, maquinaria.anio_fabricacion, maquinaria.num_serie, maquinaria.estado_maquinaria "
                "FROM productos "
                "INNER JOIN maquinaria ON productos.id_producto = maquinaria.id_maquinaria"
            )
            registros = cursor.fetchall()
            return registros
        except Exception as excepcion:
            print("Error al mostrar productos. ", excepcion)
            return []

        
    def actualizar(self, id_producto):
        try:
            #Actualizar tabla productos
            cursor.execute(
                "UPDATE productos SET nombre = %s, categoria = %s, cantidad = %s, precio_unitario = %s, descripcion = %s WHERE id_producto = %s",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion, id_producto)
            )

            #Actualizar tabla maquinaria
            cursor.execute(
                "UPDATE maquinaria SET tipo_maquinaria = %s, marca_maquinaria = %s, modelo_maquinaria = %s, anio_fabricacion = %s, num_serie = %s, estado_maquinaria = %s WHERE id_maquinaria = %s",
                (self.tipo_maquinaria, self.marca_maquinaria, self.modelo_maquinaria, self.anio_fabricacion, self.num_serie, self.estado_maquinaria, id_producto)
            )

            conexion.commit()
            return True
        
        except Exception as excepcion:
            print("Error al actualizar productos. ", excepcion)
            return False
    
    def borrar(self, id_producto):
        try:
            #borrar en tabla maquinaria
            cursor.execute(
                "DELETE FROM maquinaria WHERE id_maquinaria = %s",
                (id_producto,)
            )

            cursor.execute(
                "DELETE FROM productos WHERE id_producto = %s",
                (id_producto,)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Ocurrio un error al borrar el registro. ", excepcion)
            return False

class Herramientas(Productos):
    def __init__(self, nombre, categoria, cantidad, precio_unitario, descripcion, tipo_herramienta, marca_herramienta, modelo_herramienta):
        super().__init__(nombre, categoria, cantidad, precio_unitario, descripcion)
        self.tipo_herramienta = tipo_herramienta
        self.marca_herramienta = marca_herramienta
        self.modelo_herramienta = modelo_herramienta

    def crear(self):
        try:
            #Insertar en productos
            cursor.execute(
                "INSERT INTO productos(nombre, categoria, cantidad, precio_unitario, descripcion) VALUES(%s, %s, %s, %s, %s)",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion)
            )

            #Obtener el ID del producto recién insertado
            id_producto = cursor.lastrowid

            #Insertar en herramientas
            cursor.execute(
                "INSERT INTO herramientas(id_herramienta, tipo_herramienta, marca_herramienta, modelo_herramienta) VALUES(%s, %s, %s, %s)",
                (id_producto, self.tipo_herramienta, self.marca_herramienta, self.modelo_herramienta)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Error al crear el producto. ", excepcion)
            return False
        
    @classmethod
    def mostrar(self):
        try:
            cursor.execute(
                "SELECT productos.id_producto, productos.nombre, productos.categoria, productos.cantidad, productos.precio_unitario, productos.descripcion, " "herramientas.tipo_herramienta, herramientas.marca_herramienta, herramientas.modelo_herramienta " "FROM productos" " INNER JOIN herramientas ON productos.id_producto = herramientas.id_herramienta"
            )
            registros = cursor.fetchall()
            return registros
        except Exception as excepcion:
            print("Error al mostrar productos. ", excepcion)
            return []

    def actualizar(self, id_producto):
        try:
            #Actualizar tabla productos
            cursor.execute(
                "UPDATE productos SET nombre = %s, categoria = %s, cantidad = %s, precio_unitario = %s, descripcion = %s WHERE id_producto = %s",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion, id_producto)
            )

            #Actualizar tabla herramientas
            cursor.execute(
                "UPDATE herramientas SET tipo_herramienta = %s, marca_herramienta = %s, modelo_herramienta = %s WHERE id_herramienta = %s",
                (self.tipo_herramienta, self.marca_herramienta, self.modelo_herramienta, id_producto)
            )

            conexion.commit()
            return True
        
        except Exception as excepcion:
            print("Error al actualizar productos. ", excepcion)
            return False
        
    def borrar(self, id_producto):
        try:
            #Borrar en tabla herramientas
            cursor.execute(
                "DELETE FROM herramientas WHERE id_herramienta = %s",
                (id_producto,)
            )

            #Borrar en tabla productos
            cursor.execute(
                "DELETE FROM productos WHERE id_producto = %s",
                (id_producto,)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Ocurrio un error al borrar el registro. ", excepcion)
            return False

class Materiales(Productos):
    def __init__(self, nombre, categoria, cantidad, precio_unitario, descripcion, tipo_material, unidad_medida):
        super().__init__(nombre, categoria, cantidad, precio_unitario, descripcion)
        self.tipo_material = tipo_material
        self.unidad_medida = unidad_medida

    def crear(self):
        try:
            #Insertar en productos
            cursor.execute(
                "INSERT INTO productos(nombre, categoria, cantidad, precio_unitario, descripcion) VALUES(%s, %s, %s, %s, %s)",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion)
            )

            #Obtener el ID del producto recién insertado
            id_producto = cursor.lastrowid

            #Insertar en materiales
            cursor.execute(
                "INSERT INTO materiales(id_material, tipo_material, unidad_medida) VALUES(%s, %s, %s)",
                (id_producto, self.tipo_material, self.unidad_medida)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Error al crear el producto. ", excepcion)
            return False
        
    @classmethod
    def mostrar(self):
        try:
            cursor.execute(
                "SELECT productos.id_producto, productos.nombre, productos.categoria, productos.cantidad, productos.precio_unitario, productos.descripcion, " "materiales.tipo_material, materiales.unidad_medida " "FROM productos" " INNER JOIN materiales ON productos.id_producto = materiales.id_material"
            )
            registros = cursor.fetchall()
            return registros
        except Exception as excepcion:
            print("Error al mostrar productos. ", excepcion)
            return []

    def actualizar(self, id_producto):
        try:
            #Actualizar tabla productos
            cursor.execute(
                "UPDATE productos SET nombre = %s, categoria = %s, cantidad = %s, precio_unitario = %s, descripcion = %s WHERE id_producto = %s",
                (self.nombre, self.categoria, self.cantidad, self.precio_unitario, self.descripcion, id_producto)
            )

            #Actualizar tabla materiales
            cursor.execute(
                "UPDATE materiales SET tipo_material = %s, unidad_medida = %s WHERE id_material = %s",
                (self.tipo_material, self.unidad_medida, id_producto)
            )

            conexion.commit()
            return True
        
        except Exception as excepcion:
            print("Error al actualizar productos. ", excepcion)
            return False
        
    def borrar(self, id_producto):
        try:
            #Borrar en tabla materiales
            cursor.execute(
                "DELETE FROM materiales WHERE id_material = %s",
                (id_producto,)
            )

            #Borrar en tabla productos
            cursor.execute(
                "DELETE FROM productos WHERE id_producto = %s",
                (id_producto,)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Ocurrio un error al borrar el registro. ", excepcion)
            return False
       