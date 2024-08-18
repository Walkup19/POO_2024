from conexionDB import *
import datetime

class Proveedores():
    def __init__(self, nombre, direccion, telefono, email, productos_suministrados, contacto_principal, notas):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.productos_suministrados = productos_suministrados
        self.contacto_principal = contacto_principal
        self.notas = notas

    def crear_proveedor(self):
        try:
            #Insertar en proveedores
            fecha_registro = datetime.datetime.now()
            cursor.execute(
                "INSERT INTO proveedores(nombre, direccion, telefono, email, productos_suministrados, contacto_principal, fecha_registro, notas) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.nombre, self.direccion, self.telefono, self.email, self.productos_suministrados, self.contacto_principal, fecha_registro, self.notas)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Error al crear el proveedor. ", excepcion)
            return False
        
    @classmethod
    def mostrar_proveedor(self):
        try:
            cursor.execute(
                "SELECT * FROM proveedores"
            )
            registros = cursor.fetchall()
            return registros
        
        except Exception as excepcion:
            print("Error al mostrar productos. ", excepcion)
            return []

    def actualizar_proveedor(self, id_prov):
        try:
            #Actualizar proveedores
            cursor.execute(
                "UPDATE proveedores SET nombre = %s, direccion = %s, telefono = %s, email = %s, productos_suministrados = %s, contacto_principal = %s, notas = %s WHERE id_proveedor = %s",
                (self.nombre, self.direccion, self.telefono, self.email, self.productos_suministrados, self.contacto_principal, self.notas, id_prov)
            )
            
            conexion.commit()
            return True
        except Exception as exp:
            print("Ha ocurrido un error. ", exp)
            return False
        
    def borrar_proveedor(self, id_prov):
        try:
            #Borrar en tabla proveedores
            cursor.execute(
                "DELETE FROM proveedores WHERE id_proveedor = %s",
                (id_prov,)
            )

            conexion.commit()
            return True
        except Exception as excepcion:
            print("Ocurrio un error al borrar el registro. ", excepcion)
            return False