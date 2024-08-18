import tkinter as tk
from tkinter import messagebox
from productos import productos
from proveedores import proveedores


def borrar_herramienta():
    # Crear una nueva ventana para borrar material
    borrar_herramienta_window = tk.Toplevel(productos_window)
    borrar_herramienta_window.title("Borrar Herramienta")

    # Solicitar el ID del producto a borrar
    tk.Label(borrar_herramienta_window, text="ID de la herramienta:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(borrar_herramienta_window)
    entry_id_producto.grid(row=0, column=1)

    def submit_borrar_herramienta():
        try:
            id_herramienta = int(entry_id_producto.get())
            # Objeto vacío
            obj_herramienta = productos.Herramientas("", "", 0, 0.0, "", "", "", "")

            # Llamar a la función borrar
            resultado = obj_herramienta.borrar(id_herramienta)

            if resultado:
                messagebox.showinfo("Éxito", "Herramienta borrada con éxito.")
            else:
                messagebox.showerror("Error", "Ha ocurrido un error al borrar la herramienta.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(borrar_herramienta_window, text="Borrar", command=submit_borrar_herramienta).grid(row=1, column=0, columnspan=2)

def borrar_maquinaria():
    # Crear una nueva ventana para borrar maquinaria
    borrar_maquinaria_window = tk.Toplevel(productos_window)
    borrar_maquinaria_window.title("Borrar Herramienta")

    # Solicitar el ID del producto a actualizar
    tk.Label(borrar_maquinaria_window, text="ID de la maquinaria:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(borrar_maquinaria_window)
    entry_id_producto.grid(row=0, column=1)

    def submit_borrar_maquinaria():
        try:
            id_maquinaria = int(entry_id_producto.get())
            # Objeto vacío
            obj_maquinaria = productos.Maquinaria("", "", 0, 0.0, "", "", "", "", 0, 0, "")

            # Llamar a la función borrar
            resultado = obj_maquinaria.borrar(id_maquinaria)

            if resultado:
                messagebox.showinfo("Éxito", "Maquinaria borrada con éxito.")
            else:
                messagebox.showerror("Error", "Ha ocurrido un error al borrar la maquinaria.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(borrar_maquinaria_window, text="Borrar", command=submit_borrar_maquinaria).grid(row=1, column=0, columnspan=2)

def borrar_material():
    # Crear una nueva ventana para borrar material
    borrar_herramienta_window = tk.Toplevel(productos_window)
    borrar_herramienta_window.title("Borrar material")

    # Solicitar el ID del producto a actualizar
    tk.Label(borrar_herramienta_window, text="ID de la maquinaria:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(borrar_herramienta_window)
    entry_id_producto.grid(row=0, column=1)

    def submit_borrar_material():
        try:
            id_material = int(entry_id_producto.get())
            # Objeto vacío
            obj_material = productos.Materiales("", "", 0, 0.0, "", "", "")

            # Llamar a la función borrar
            resultado = obj_material.borrar(id_material)

            if resultado:
                messagebox.showinfo("Éxito", "Material borrado con éxito.")
            else:
                messagebox.showerror("Error", "Ha ocurrido un error al borrar el material.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(borrar_herramienta_window, text="Borrar", command=submit_borrar_material).grid(row=1, column=0, columnspan=2)

def actualizar_herramienta():
    # Crear una nueva ventana para actualizar herramienta
    actualizar_herramienta_window = tk.Toplevel(productos_window)
    actualizar_herramienta_window.title("Actualizar Herramienta")

    # Solicitar el ID del producto a actualizar
    tk.Label(actualizar_herramienta_window, text="ID de la herramienta:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(actualizar_herramienta_window)
    entry_id_producto.grid(row=0, column=1)

    def solicitar_datos():
        try:
            id_producto = int(entry_id_producto.get())
            # Aquí podrías agregar una verificación para asegurarte de que el ID existe en la base de datos
            # Si el ID es válido, mostrar los campos para actualizar los datos

            # Cerrar la ventana de solicitud de ID
            actualizar_herramienta_window.destroy()

            # Crear una nueva ventana para actualizar los datos
            actualizar_datos_window = tk.Toplevel(productos_window)
            actualizar_datos_window.title("Actualizar Datos de la herramienta")

            # Solicitar datos nuevos
            tk.Label(actualizar_datos_window, text="Nombre:").grid(row=0, column=0)
            entry_nombre = tk.Entry(actualizar_datos_window)
            entry_nombre.grid(row=0, column=1)

            tk.Label(actualizar_datos_window, text="Categoría:").grid(row=1, column=0)
            entry_categoria = tk.Entry(actualizar_datos_window)
            entry_categoria.grid(row=1, column=1)

            tk.Label(actualizar_datos_window, text="Cantidad:").grid(row=2, column=0)
            entry_cantidad = tk.Entry(actualizar_datos_window)
            entry_cantidad.grid(row=2, column=1)

            tk.Label(actualizar_datos_window, text="Precio unitario:").grid(row=3, column=0)
            entry_precio_unitario = tk.Entry(actualizar_datos_window)
            entry_precio_unitario.grid(row=3, column=1)

            tk.Label(actualizar_datos_window, text="Uso:").grid(row=4, column=0)
            entry_descripcion = tk.Entry(actualizar_datos_window)
            entry_descripcion.grid(row=4, column=1)

            tk.Label(actualizar_datos_window, text="Tipo de herramienta:").grid(row=5, column=0)
            entry_tipo_herramienta = tk.Entry(actualizar_datos_window)
            entry_tipo_herramienta.grid(row=5, column=1)

            tk.Label(actualizar_datos_window, text="Marca de herramienta:").grid(row=6, column=0)
            entry_marca_herramienta = tk.Entry(actualizar_datos_window)
            entry_marca_herramienta.grid(row=6, column=1)

            tk.Label(actualizar_datos_window, text="Modelo de herramienta:").grid(row=7, column=0)
            entry_modelo_herramienta = tk.Entry(actualizar_datos_window)
            entry_modelo_herramienta.grid(row=7, column=1)

            def submit_actualizar_herramienta():
                try:
                    nombre = entry_nombre.get()
                    categoria = entry_categoria.get()
                    cantidad = int(entry_cantidad.get())
                    precio_unitario = float(entry_precio_unitario.get())
                    descripcion = entry_descripcion.get()
                    tipo_herramienta = entry_tipo_herramienta.get()
                    marca_herramienta = entry_marca_herramienta.get()
                    modelo_herramienta = entry_modelo_herramienta.get()

                    # Crear objeto con los datos nuevos
                    obj_herramienta = productos.Herramientas(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_herramienta, marca_herramienta, modelo_herramienta)

                    # Llamar a la función actualizar
                    resultado = obj_herramienta.actualizar(id_producto)

                    if resultado:
                        messagebox.showinfo("Éxito", "Herramienta actualizada con éxito.")
                    else:
                        messagebox.showerror("Error", "Fallo al actualizar la herramienta.")
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

            tk.Button(actualizar_datos_window, text="Actualizar", command=submit_actualizar_herramienta).grid(row=8, column=0, columnspan=2)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(actualizar_herramienta_window, text="Siguiente", command=solicitar_datos).grid(row=1, column=0, columnspan=2)
def actualizar_maquinaria():
    # Crear una nueva ventana para actualizar maquinaria
    actualizar_maquinaria_window = tk.Toplevel(productos_window)
    actualizar_maquinaria_window.title("Actualizar Material")

    # Solicitar el ID del producto a actualizar
    tk.Label(actualizar_maquinaria_window, text="ID del material:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(actualizar_maquinaria_window)
    entry_id_producto.grid(row=0, column=1)

    def solicitar_datos():
        try:
            id_producto = int(entry_id_producto.get())
            # Aquí podrías agregar una verificación para asegurarte de que el ID existe en la base de datos
            # Si el ID es válido, mostrar los campos para actualizar los datos

            # Cerrar la ventana de solicitud de ID
            actualizar_maquinaria_window.destroy()

            # Crear una nueva ventana para actualizar los datos
            actualizar_datos_window = tk.Toplevel(productos_window)
            actualizar_datos_window.title("Actualizar Datos de la maquinaria")

            # Solicitar datos nuevos
            tk.Label(actualizar_datos_window, text="Nombre:").grid(row=0, column=0)
            entry_nombre = tk.Entry(actualizar_datos_window)
            entry_nombre.grid(row=0, column=1)

            tk.Label(actualizar_datos_window, text="Categoría:").grid(row=1, column=0)
            entry_categoria = tk.Entry(actualizar_datos_window)
            entry_categoria.grid(row=1, column=1)

            tk.Label(actualizar_datos_window, text="Cantidad:").grid(row=2, column=0)
            entry_cantidad = tk.Entry(actualizar_datos_window)
            entry_cantidad.grid(row=2, column=1)

            tk.Label(actualizar_datos_window, text="Precio unitario:").grid(row=3, column=0)
            entry_precio_unitario = tk.Entry(actualizar_datos_window)
            entry_precio_unitario.grid(row=3, column=1)

            tk.Label(actualizar_datos_window, text="Uso:").grid(row=4, column=0)
            entry_descripcion = tk.Entry(actualizar_datos_window)
            entry_descripcion.grid(row=4, column=1)

            tk.Label(actualizar_datos_window, text="Tipo de maquinaria:").grid(row=5, column=0)
            entry_tipo_maquinaria = tk.Entry(actualizar_datos_window)
            entry_tipo_maquinaria.grid(row=5, column=1)

            tk.Label(actualizar_datos_window, text="Marca de maquinaria:").grid(row=6, column=0)
            entry_marca_maquinaria = tk.Entry(actualizar_datos_window)
            entry_marca_maquinaria.grid(row=6, column=1)

            tk.Label(actualizar_datos_window, text="Modelo de maquinaria:").grid(row=7, column=0)
            entry_modelo_maquinaria = tk.Entry(actualizar_datos_window)
            entry_modelo_maquinaria.grid(row=7, column=1)

            tk.Label(actualizar_datos_window, text="Anio de fabricacion:").grid(row=8, column=0)
            entry_anio_fabricacion = tk.Entry(actualizar_datos_window)
            entry_anio_fabricacion.grid(row=8, column=1)

            tk.Label(actualizar_datos_window, text="Numero de serie:").grid(row=9, column=0)
            entry_num_serie = tk.Entry(actualizar_datos_window)
            entry_num_serie.grid(row=9, column=1)

            tk.Label(actualizar_datos_window, text="Estado de maquinaria:").grid(row=10, column=0)
            entry_estado_maquinaria = tk.Entry(actualizar_datos_window)
            entry_estado_maquinaria.grid(row=10, column=1)


            def submit_actualizar_material():
                try:
                    nombre = entry_nombre.get()
                    categoria = entry_categoria.get()
                    cantidad = int(entry_cantidad.get())
                    precio_unitario = float(entry_precio_unitario.get())
                    descripcion = entry_descripcion.get()
                    tipo_maquinaria = entry_tipo_maquinaria.get()
                    marca_maquinaria = entry_marca_maquinaria.get()
                    modelo_maquinaria = entry_modelo_maquinaria.get()
                    anio_fabricacion = int(entry_anio_fabricacion.get())
                    num_serie = int(entry_num_serie.get())
                    estado_maquinaria = entry_estado_maquinaria.get()

                    # Crear objeto con los datos nuevos
                    obj_maquinaria = productos.Maquinaria(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria)

                    # Llamar a la función actualizar
                    resultado = obj_maquinaria.actualizar(id_producto)

                    if resultado:
                        messagebox.showinfo("Éxito", "Maquinaria actualizada con éxito.")
                    else:
                        messagebox.showerror("Error", "Fallo al actualizar la maquinaria.")
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

            tk.Button(actualizar_datos_window, text="Actualizar", command=submit_actualizar_material).grid(row=11, column=0, columnspan=2)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(actualizar_maquinaria_window, text="Siguiente", command=solicitar_datos).grid(row=1, column=0, columnspan=2)

def actualizar_material():
    # Crear una nueva ventana para actualizar material
    actualizar_material_window = tk.Toplevel(productos_window)
    actualizar_material_window.title("Actualizar Material")

    # Solicitar el ID del producto a actualizar
    tk.Label(actualizar_material_window, text="ID del material:").grid(row=0, column=0)
    entry_id_producto = tk.Entry(actualizar_material_window)
    entry_id_producto.grid(row=0, column=1)

    def solicitar_datos():
        try:
            id_producto = int(entry_id_producto.get())
            # Aquí podrías agregar una verificación para asegurarte de que el ID existe en la base de datos
            # Si el ID es válido, mostrar los campos para actualizar los datos

            # Cerrar la ventana de solicitud de ID
            actualizar_material_window.destroy()

            # Crear una nueva ventana para actualizar los datos
            actualizar_datos_window = tk.Toplevel(productos_window)
            actualizar_datos_window.title("Actualizar Datos del Material")

            # Solicitar datos nuevos
            tk.Label(actualizar_datos_window, text="Nombre:").grid(row=0, column=0)
            entry_nombre = tk.Entry(actualizar_datos_window)
            entry_nombre.grid(row=0, column=1)

            tk.Label(actualizar_datos_window, text="Categoría:").grid(row=1, column=0)
            entry_categoria = tk.Entry(actualizar_datos_window)
            entry_categoria.grid(row=1, column=1)

            tk.Label(actualizar_datos_window, text="Cantidad:").grid(row=2, column=0)
            entry_cantidad = tk.Entry(actualizar_datos_window)
            entry_cantidad.grid(row=2, column=1)

            tk.Label(actualizar_datos_window, text="Precio unitario:").grid(row=3, column=0)
            entry_precio_unitario = tk.Entry(actualizar_datos_window)
            entry_precio_unitario.grid(row=3, column=1)

            tk.Label(actualizar_datos_window, text="Descripción:").grid(row=4, column=0)
            entry_descripcion = tk.Entry(actualizar_datos_window)
            entry_descripcion.grid(row=4, column=1)

            tk.Label(actualizar_datos_window, text="Tipo de material:").grid(row=5, column=0)
            entry_tipo_material = tk.Entry(actualizar_datos_window)
            entry_tipo_material.grid(row=5, column=1)

            tk.Label(actualizar_datos_window, text="Unidad de medida del material:").grid(row=6, column=0)
            entry_unidad_medida = tk.Entry(actualizar_datos_window)
            entry_unidad_medida.grid(row=6, column=1)

            def submit_actualizar_material():
                try:
                    nombre = entry_nombre.get()
                    categoria = entry_categoria.get()
                    cantidad = int(entry_cantidad.get())
                    precio_unitario = float(entry_precio_unitario.get())
                    descripcion = entry_descripcion.get()
                    tipo_material = entry_tipo_material.get()
                    unidad_medida = entry_unidad_medida.get()

                    # Crear objeto con los datos nuevos
                    obj_material = productos.Materiales(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_material, unidad_medida)

                    # Llamar a la función actualizar
                    resultado = obj_material.actualizar(id_producto)

                    if resultado:
                        messagebox.showinfo("Éxito", "Material actualizado con éxito.")
                    else:
                        messagebox.showerror("Error", "Fallo al actualizar el material.")
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

            tk.Button(actualizar_datos_window, text="Actualizar", command=submit_actualizar_material).grid(row=7, column=0, columnspan=2)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(actualizar_material_window, text="Siguiente", command=solicitar_datos).grid(row=1, column=0, columnspan=2)

def volver_borrar_productos():
    borrar_productos_window.destroy()

def volver_actualizar_productos():
    actualizar_productos_window.destroy()

def volver_mostrar_productos():
    mostrar_productos_window.destroy()

def mostrar_herramienta():
    registros = productos.Herramientas.mostrar()
    mostrar_registros_herramientas("Herramientas", registros)

def mostrar_maquinaria():
    registros = productos.Maquinaria.mostrar()
    mostrar_registros_maquinaria("Maquinaria", registros)

def mostrar_material():
    registros = productos.Materiales.mostrar()
    mostrar_registros_materiales("Materiales", registros)

def mostrar_registros_materiales(titulo, registros):
    mostrar_registros_window = tk.Toplevel(productos_window)
    mostrar_registros_window.title(f"Mostrar {titulo}")

    for i, registro in enumerate(registros):
        texto = (f"ID: {registro[0]}, \nNombre: {registro[1]}, \nCategoria: {registro[2]}, \nCantidad: {registro[3]}, "
                 f"\nPrecio unitario: {registro[4]}, \nDescripcion: {registro[5]}, \nTipo: {registro[6]}, "
                 f"\nUnidad de medida: {registro[7]}\n")
        tk.Label(mostrar_registros_window, text=texto, justify=tk.LEFT).grid(row=i, column=0, sticky="w")

    tk.Button(mostrar_registros_window, text="Cerrar", command=mostrar_registros_window.destroy).grid(row=len(registros), column=0)

def mostrar_registros_herramientas(titulo, registros):
    mostrar_registros_window = tk.Toplevel(productos_window)
    mostrar_registros_window.title(f"Mostrar {titulo}")

    for i, registro in enumerate(registros):
        texto = (f"ID: {registro[0]}, \nNombre: {registro[1]}, \nCategoria: {registro[2]}, \nCantidad: {registro[3]}, "
                 f"\nPrecio unitario: {registro[4]}, \nDescripcion: {registro[5]}, \nTipo: {registro[6]}, "
                 f"\nMarca: {registro[7]}, \nModelo: {registro[8]}\n")
        tk.Label(mostrar_registros_window, text=texto, justify=tk.LEFT).grid(row=i, column=0, sticky="w")

    tk.Button(mostrar_registros_window, text="Cerrar", command=mostrar_registros_window.destroy).grid(row=len(registros), column=0)


def mostrar_registros_maquinaria(titulo, registros):
    mostrar_registros_window = tk.Toplevel(productos_window)
    mostrar_registros_window.title(f"Mostrar {titulo}")

    for i, registro in enumerate(registros):
        texto = (f"ID: {registro[0]}, \nNombre: {registro[1]}, \nCategoria: {registro[2]}, \nCantidad: {registro[3]}, "
                 f"\nPrecio unitario: {registro[4]}, \nUso: {registro[5]}, \nTipo: {registro[6]}, "
                 f"\nMarca: {registro[7]}, \nModelo: {registro[8]}, \nAño: {registro[9]}, "
                 f"\nNumero de serie: {registro[10]}, \nEstado: {registro[11]}\n")
        tk.Label(mostrar_registros_window, text=texto, justify=tk.LEFT).grid(row=i, column=0, sticky="w")

    tk.Button(mostrar_registros_window, text="Cerrar", command=mostrar_registros_window.destroy).grid(row=len(registros), column=0)


def crear_herramienta():
    def submit_herramienta():
        nombre = entry_nombre.get()
        categoria = entry_categoria.get()
        cantidad = int(entry_cantidad.get())
        precio_unitario = float(entry_precio_unitario.get())
        descripcion = entry_descripcion.get()
        tipo_herramienta = entry_tipo_herramienta.get()
        marca_herramienta = entry_marca_herramienta.get()
        modelo_herramienta = entry_modelo_herramienta.get()

        obj_herramienta = productos.Herramientas(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_herramienta, marca_herramienta, modelo_herramienta)
        resultado = obj_herramienta.crear()

        if resultado:
            messagebox.showinfo("Éxito", "Producto creado con éxito.")
        else:
            messagebox.showerror("Error", "Fallo al crear el producto.")

    crear_herramienta_window = tk.Toplevel(crear_productos_window)
    crear_herramienta_window.title("Crear Herramienta")

    tk.Label(crear_herramienta_window, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(crear_herramienta_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(crear_herramienta_window, text="Categoría:").grid(row=1, column=0)
    entry_categoria = tk.Entry(crear_herramienta_window)
    entry_categoria.grid(row=1, column=1)

    tk.Label(crear_herramienta_window, text="Cantidad:").grid(row=2, column=0)
    entry_cantidad = tk.Entry(crear_herramienta_window)
    entry_cantidad.grid(row=2, column=1)

    tk.Label(crear_herramienta_window, text="Precio unitario:").grid(row=3, column=0)
    entry_precio_unitario = tk.Entry(crear_herramienta_window)
    entry_precio_unitario.grid(row=3, column=1)

    tk.Label(crear_herramienta_window, text="Descripción:").grid(row=4, column=0)
    entry_descripcion = tk.Entry(crear_herramienta_window)
    entry_descripcion.grid(row=4, column=1)

    tk.Label(crear_herramienta_window, text="Tipo de herramienta:").grid(row=5, column=0)
    entry_tipo_herramienta = tk.Entry(crear_herramienta_window)
    entry_tipo_herramienta.grid(row=5, column=1)

    tk.Label(crear_herramienta_window, text="Marca de herramienta:").grid(row=6, column=0)
    entry_marca_herramienta = tk.Entry(crear_herramienta_window)
    entry_marca_herramienta.grid(row=6, column=1)

    tk.Label(crear_herramienta_window, text="Modelo:").grid(row=7, column=0)
    entry_modelo_herramienta = tk.Entry(crear_herramienta_window)
    entry_modelo_herramienta.grid(row=7, column=1)

    tk.Button(crear_herramienta_window, text="Crear", command=submit_herramienta).grid(row=8, column=0, columnspan=2)

def crear_maquinaria():
    def submit_maquinaria():
        nombre = entry_nombre.get()
        categoria = entry_categoria.get()
        cantidad = int(entry_cantidad.get())
        precio_unitario = float(entry_precio_unitario.get())
        descripcion = entry_descripcion.get()
        tipo_maquinaria = entry_tipo_maquinaria.get()
        marca_maquinaria = entry_marca_maquinaria.get()
        modelo_maquinaria = entry_modelo_maquinaria.get()
        anio_fabricacion = int(entry_anio_fabricacion.get())
        num_serie = int(entry_num_serie.get())
        estado_maquinaria = entry_estado_maquinaria.get()

        obj_maquinaria = productos.Maquinaria(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria)
        resultado = obj_maquinaria.crear()

        if resultado:
            messagebox.showinfo("Éxito", "Producto creado con éxito.")
        else:
            messagebox.showerror("Error", "Fallo al crear el producto.")

    crear_maquinaria_window = tk.Toplevel(crear_productos_window)
    crear_maquinaria_window.title("Crear Maquinaria")

    tk.Label(crear_maquinaria_window, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(crear_maquinaria_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(crear_maquinaria_window, text="Categoría:").grid(row=1, column=0)
    entry_categoria = tk.Entry(crear_maquinaria_window)
    entry_categoria.grid(row=1, column=1)

    tk.Label(crear_maquinaria_window, text="Cantidad:").grid(row=2, column=0)
    entry_cantidad = tk.Entry(crear_maquinaria_window)
    entry_cantidad.grid(row=2, column=1)

    tk.Label(crear_maquinaria_window, text="Precio unitario:").grid(row=3, column=0)
    entry_precio_unitario = tk.Entry(crear_maquinaria_window)
    entry_precio_unitario.grid(row=3, column=1)

    tk.Label(crear_maquinaria_window, text="Descripción:").grid(row=4, column=0)
    entry_descripcion = tk.Entry(crear_maquinaria_window)
    entry_descripcion.grid(row=4, column=1)

    tk.Label(crear_maquinaria_window, text="Tipo de maquinaria:").grid(row=5, column=0)
    entry_tipo_maquinaria = tk.Entry(crear_maquinaria_window)
    entry_tipo_maquinaria.grid(row=5, column=1)

    tk.Label(crear_maquinaria_window, text="Marca de maquinaria:").grid(row=6, column=0)
    entry_marca_maquinaria = tk.Entry(crear_maquinaria_window)
    entry_marca_maquinaria.grid(row=6, column=1)

    tk.Label(crear_maquinaria_window, text="Modelo de maquinaria:").grid(row=7, column=0)
    entry_modelo_maquinaria = tk.Entry(crear_maquinaria_window)
    entry_modelo_maquinaria.grid(row=7, column=1)

    tk.Label(crear_maquinaria_window, text="Anio de fabricacion:").grid(row=8, column=0)
    entry_anio_fabricacion = tk.Entry(crear_maquinaria_window)
    entry_anio_fabricacion.grid(row=8, column=1)

    tk.Label(crear_maquinaria_window, text="Numero de serie:").grid(row=9, column=0)
    entry_num_serie = tk.Entry(crear_maquinaria_window)
    entry_num_serie.grid(row=9, column=1)

    tk.Label(crear_maquinaria_window, text="Estado de maquinaria:").grid(row=10, column=0)
    entry_estado_maquinaria = tk.Entry(crear_maquinaria_window)
    entry_estado_maquinaria.grid(row=10, column=1)

    tk.Button(crear_maquinaria_window, text="Crear", command=submit_maquinaria).grid(row=11, column=0, columnspan=2)

def crear_material():
    def submit_material():
        nombre = entry_nombre.get()
        categoria = entry_categoria.get()
        cantidad = int(entry_cantidad.get())
        precio_unitario = float(entry_precio_unitario.get())
        descripcion = entry_descripcion.get()
        tipo_material = entry_tipo_material.get()
        unidad_medida = entry_unidad_medida.get()

        obj_material = productos.Materiales(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_material, unidad_medida)
        resultado = obj_material.crear()

        if resultado:
            messagebox.showinfo("Éxito", "Producto creado con éxito.")
        else:
            messagebox.showerror("Error", "Fallo al crear el producto.")

    crear_material_window = tk.Toplevel(crear_productos_window)
    crear_material_window.title("Crear Herramienta")

    tk.Label(crear_material_window, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(crear_material_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(crear_material_window, text="Categoría:").grid(row=1, column=0)
    entry_categoria = tk.Entry(crear_material_window)
    entry_categoria.grid(row=1, column=1)

    tk.Label(crear_material_window, text="Cantidad:").grid(row=2, column=0)
    entry_cantidad = tk.Entry(crear_material_window)
    entry_cantidad.grid(row=2, column=1)

    tk.Label(crear_material_window, text="Precio unitario:").grid(row=3, column=0)
    entry_precio_unitario = tk.Entry(crear_material_window)
    entry_precio_unitario.grid(row=3, column=1)

    tk.Label(crear_material_window, text="Descripción:").grid(row=4, column=0)
    entry_descripcion = tk.Entry(crear_material_window)
    entry_descripcion.grid(row=4, column=1)

    tk.Label(crear_material_window, text="Tipo de material:").grid(row=5, column=0)
    entry_tipo_material = tk.Entry(crear_material_window)
    entry_tipo_material.grid(row=5, column=1)

    tk.Label(crear_material_window, text="Unidad de medida del material:").grid(row=6, column=0)
    entry_unidad_medida = tk.Entry(crear_material_window)
    entry_unidad_medida.grid(row=6, column=1)


    tk.Button(crear_material_window, text="Crear", command=submit_material).grid(row=7, column=0, columnspan=2)

def volver_crear_productos():
    crear_productos_window.destroy()

def crear_producto():
    global crear_productos_window
    crear_productos_window = tk.Toplevel(productos_window)
    crear_productos_window.title("Crear Producto")

    label = tk.Label(crear_productos_window, text=".:::     SELECCIONA PRODUCTO A CREAR     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_herramienta = tk.Button(crear_productos_window, text="1. HERRAMIENTA", command=crear_herramienta)
    btn_herramienta.pack(pady=5)

    btn_maquinaria = tk.Button(crear_productos_window, text="2. MAQUINARIA", command=crear_maquinaria)
    btn_maquinaria.pack(pady=5)

    btn_material = tk.Button(crear_productos_window, text="3. MATERIAL", command=crear_material)
    btn_material.pack(pady=5)

    btn_volver = tk.Button(crear_productos_window, text="4. VOLVER AL MENU ANTERIOR", command=volver_crear_productos)
    btn_volver.pack(pady=5)

def mostrar_productos():
    global mostrar_productos_window
    mostrar_productos_window = tk.Toplevel(productos_window)
    mostrar_productos_window.title("Mostrar Producto")

    label = tk.Label(mostrar_productos_window, text=".:::     SELECCIONA PRODUCTO A MOSTRAR     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_herramienta = tk.Button(mostrar_productos_window, text="1. HERRAMIENTA", command=mostrar_herramienta)
    btn_herramienta.pack(pady=5)

    btn_maquinaria = tk.Button(mostrar_productos_window, text="2. MAQUINARIA", command=mostrar_maquinaria)
    btn_maquinaria.pack(pady=5)

    btn_material = tk.Button(mostrar_productos_window, text="3. MATERIAL", command=mostrar_material)
    btn_material.pack(pady=5)

    btn_volver = tk.Button(mostrar_productos_window, text="4. VOLVER AL MENU ANTERIOR", command=volver_mostrar_productos)
    btn_volver.pack(pady=5)

def actualizar_producto():
    global actualizar_productos_window
    actualizar_productos_window = tk.Toplevel(productos_window)
    actualizar_productos_window.title("Actualizar Producto")

    label = tk.Label(actualizar_productos_window, text=".:::     SELECCIONA PRODUCTO A ACTUALIZAR     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_herramienta = tk.Button(actualizar_productos_window, text="1. HERRAMIENTA", command=actualizar_herramienta)
    btn_herramienta.pack(pady=5)

    btn_maquinaria = tk.Button(actualizar_productos_window, text="2. MAQUINARIA", command=actualizar_maquinaria)
    btn_maquinaria.pack(pady=5)

    btn_material = tk.Button(actualizar_productos_window, text="3. MATERIAL", command=actualizar_material)
    btn_material.pack(pady=5)

    btn_volver = tk.Button(actualizar_productos_window, text="4. VOLVER AL MENU ANTERIOR", command=volver_actualizar_productos)
    btn_volver.pack(pady=5)

def borrar_producto():
    global borrar_productos_window
    borrar_productos_window = tk.Toplevel(productos_window)
    borrar_productos_window.title("Borrar Producto")

    label = tk.Label(borrar_productos_window, text=".:::     SELECCIONA PRODUCTO A BORRAR     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_herramienta = tk.Button(borrar_productos_window, text="1. HERRAMIENTA", command=borrar_herramienta)
    btn_herramienta.pack(pady=5)

    btn_maquinaria = tk.Button(borrar_productos_window, text="2. MAQUINARIA", command=borrar_maquinaria)
    btn_maquinaria.pack(pady=5)

    btn_material = tk.Button(borrar_productos_window, text="3. MATERIAL", command=borrar_material)
    btn_material.pack(pady=5)

    btn_volver = tk.Button(borrar_productos_window, text="4. VOLVER AL MENU ANTERIOR", command=volver_borrar_productos)
    btn_volver.pack(pady=5)

def crear_proveedor():
    def submit_proveedor():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        productos_suministrados = entry_productos_suministrados.get()
        contacto_principal = entry_contacto_principal.get()
        notas = entry_notas.get()

        obj_proveedor = proveedores.Proveedores(nombre, direccion, telefono, email, productos_suministrados, contacto_principal, notas)
        resultado = obj_proveedor.crear_proveedor()

        if resultado:
            messagebox.showinfo("Éxito", "Proveedor creado con éxito.")
        else:
            messagebox.showerror("Error", "Fallo al crear el proveedor.")

    crear_proveedor_window = tk.Toplevel(proveedores_window)
    crear_proveedor_window.title("Crear Proveedor")

    tk.Label(crear_proveedor_window, text="Nombre del proveedor:").grid(row=0, column=0)
    entry_nombre = tk.Entry(crear_proveedor_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(crear_proveedor_window, text="Direccion del proveedor:").grid(row=1, column=0)
    entry_direccion = tk.Entry(crear_proveedor_window)
    entry_direccion.grid(row=1, column=1)

    tk.Label(crear_proveedor_window, text="Telefono del proveedor:").grid(row=2, column=0)
    entry_telefono = tk.Entry(crear_proveedor_window)
    entry_telefono.grid(row=2, column=1)

    tk.Label(crear_proveedor_window, text="Correo electronico del proveedor:").grid(row=3, column=0)
    entry_email = tk.Entry(crear_proveedor_window)
    entry_email.grid(row=3, column=1)

    tk.Label(crear_proveedor_window, text="Productos suministrados por el proveedor:").grid(row=4, column=0)
    entry_productos_suministrados = tk.Entry(crear_proveedor_window)
    entry_productos_suministrados.grid(row=4, column=1)

    tk.Label(crear_proveedor_window, text="Contacto principal del proveedor:").grid(row=5, column=0)
    entry_contacto_principal = tk.Entry(crear_proveedor_window)
    entry_contacto_principal.grid(row=5, column=1)

    tk.Label(crear_proveedor_window, text="Ingresa alguna nota sobre el proveedor:").grid(row=6, column=0)
    entry_notas = tk.Entry(crear_proveedor_window)
    entry_notas.grid(row=6, column=1)

    tk.Button(crear_proveedor_window, text="Crear", command=submit_proveedor).grid(row=7, column=0, columnspan=2)

def mostrar_proveedor():
    registros = proveedores.Proveedores.mostrar_proveedor()
    mostrar_registros_proveedores("Proveedores", registros)

def mostrar_registros_proveedores(titulo, registros):
    mostrar_registros_window = tk.Toplevel(proveedores_window)
    mostrar_registros_window.title(f"Mostrar {titulo}")

    for i, registro in enumerate(registros):
        texto = (f"ID: {registro[0]}, \nNombre: {registro[1]}, \nDireccion: {registro[2]}, \nTelefono: {registro[3]}, \nCorreo electronico: {registro[4]}, \nProductos suministrados: {registro[5]}, \nContacto principal: {registro[6]}, \nFecha de registro: {registro[7]}, \nNotas: {registro[8]}\n")
        tk.Label(mostrar_registros_window, text=texto, justify=tk.LEFT).grid(row=i, column=0, sticky="w")

def actualizar_proveedor():
    # Crear una nueva ventana para actualizar el proveedor
    actualizar_proveedor_window = tk.Toplevel(proveedores_window)
    actualizar_proveedor_window.title("Actualizar Proveedor")

    # Solicitar el ID del producto a actualizar
    tk.Label(actualizar_proveedor_window, text="ID del proveedor:").grid(row=0, column=0)
    entry_id_prov = tk.Entry(actualizar_proveedor_window)
    entry_id_prov.grid(row=0, column=1)

    def solicitar_datos():
        try:
            id_prov = int(entry_id_prov.get())
            # Aquí podrías agregar una verificación para asegurarte de que el ID existe en la base de datos
            # Si el ID es válido, mostrar los campos para actualizar los datos

            # Cerrar la ventana de solicitud de ID
            actualizar_proveedor_window.destroy()

            # Crear una nueva ventana para actualizar los datos
            actualizar_datos_window = tk.Toplevel(proveedores_window)
            actualizar_datos_window.title("Actualizar Datos del Proveedor")

            # Solicitar datos nuevos
            tk.Label(actualizar_datos_window, text="Nombre:").grid(row=0, column=0)
            entry_nombre = tk.Entry(actualizar_datos_window)
            entry_nombre.grid(row=0, column=1)

            tk.Label(actualizar_datos_window, text="Direccion del proveedor:").grid(row=1, column=0)
            entry_direccion = tk.Entry(actualizar_datos_window)
            entry_direccion.grid(row=1, column=1)

            tk.Label(actualizar_datos_window, text="Telefono del proveedor:").grid(row=2, column=0)
            entry_telefono = tk.Entry(actualizar_datos_window)
            entry_telefono.grid(row=2, column=1)

            tk.Label(actualizar_datos_window, text="Correo electronico del proveedor:").grid(row=3, column=0)
            entry_email = tk.Entry(actualizar_datos_window)
            entry_email.grid(row=3, column=1)

            tk.Label(actualizar_datos_window, text="Productos suministrados por el proveedor:").grid(row=4, column=0)
            entry_productos_suministrados = tk.Entry(actualizar_datos_window)
            entry_productos_suministrados.grid(row=4, column=1)

            tk.Label(actualizar_datos_window, text="Contacto principal del proveedor:").grid(row=5, column=0)
            entry_contacto_principal = tk.Entry(actualizar_datos_window)
            entry_contacto_principal.grid(row=5, column=1)

            tk.Label(actualizar_datos_window, text="Ingresa alguna nota sobre el proveedor:").grid(row=6, column=0)
            entry_notas = tk.Entry(actualizar_datos_window)
            entry_notas.grid(row=6, column=1)


            def submit_actualizar_proveedor():
                try:
                    nombre = entry_nombre.get()
                    direccion = entry_direccion.get()
                    telefono = entry_telefono.get()
                    email = entry_email.get()
                    productos_suministrados = entry_productos_suministrados.get()
                    contacto_principal = entry_contacto_principal.get()
                    notas = entry_notas.get()

                    # Crear objeto con los datos nuevos
                    obj_proveedor = proveedores.Proveedores(nombre, direccion, telefono, email, productos_suministrados, contacto_principal, notas)

                    # Llamar a la función actualizar
                    resultado = obj_proveedor.actualizar_proveedor(id_prov)

                    if resultado:
                        messagebox.showinfo("Éxito", "Proveedor actualizado con éxito.")
                    else:
                        messagebox.showerror("Error", "Fallo al actualizar el proveedor.")
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

            tk.Button(actualizar_datos_window, text="Actualizar", command=submit_actualizar_proveedor).grid(row=7, column=0, columnspan=2)

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(actualizar_proveedor_window, text="Siguiente", command=solicitar_datos).grid(row=1, column=0, columnspan=2)

def borrar_proveedor():
    # Crear una nueva ventana para borrar proveedor
    borrar_proveedor_window = tk.Toplevel(proveedores_window)
    borrar_proveedor_window.title("Borrar proveedor")

    # Solicitar el ID del producto a actualizar
    tk.Label(borrar_proveedor_window, text="ID del proveedor:").grid(row=0, column=0)
    entry_id_prov = tk.Entry(borrar_proveedor_window)
    entry_id_prov.grid(row=0, column=1)

    def submit_borrar_proveedor():
        try:
            id_prov = int(entry_id_prov.get())
            # Objeto vacío
            obj_proveedor = proveedores.Proveedores("", "", "", "", "", "", "")

            # Llamar a la función borrar
            resultado = obj_proveedor.borrar_proveedor(id_prov)

            if resultado:
                messagebox.showinfo("Éxito", "Proveedor borrado con éxito.")
            else:
                messagebox.showerror("Error", "Ha ocurrido un error al borrar el proveedor.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un ID válido.")

    tk.Button(borrar_proveedor_window, text="Borrar", command=submit_borrar_proveedor).grid(row=1, column=0, columnspan=2)

def volver_proveedores_menu_principal():
    proveedores_window.destroy()

def volver_productos_menu_principal():
    productos_window.destroy()

def gestion_productos():
    global productos_window
    productos_window = tk.Toplevel(root)
    productos_window.title("Gestión de Productos")

    label = tk.Label(productos_window, text=".:::     GESTION DE PRODUCTOS     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_crear = tk.Button(productos_window, text="1. CREAR PRODUCTO", command=crear_producto)
    btn_crear.pack(pady=5)

    btn_mostrar = tk.Button(productos_window, text="2. MOSTRAR PRODUCTOS", command=mostrar_productos)
    btn_mostrar.pack(pady=5)

    btn_actualizar = tk.Button(productos_window, text="3. ACTUALIZAR PRODUCTO", command=actualizar_producto)
    btn_actualizar.pack(pady=5)

    btn_borrar = tk.Button(productos_window, text="4. BORRAR PRODUCTO", command=borrar_producto)
    btn_borrar.pack(pady=5)

    btn_volver = tk.Button(productos_window, text="5. VOLVER AL MENU PRINCIPAL", command=volver_menu_principal)
    btn_volver.pack(pady=5)

def gestion_proveedores():
    global proveedores_window
    proveedores_window = tk.Toplevel(root)
    proveedores_window.title("Gestión de Proveedores")

    label = tk.Label(proveedores_window, text=".:::     GESTION DE PROVEEDORES     :::.", font=("Helvetica", 16))
    label.pack(pady=10)

    btn_crear = tk.Button(proveedores_window, text="1. CREAR PROVEEDOR", command=crear_proveedor)
    btn_crear.pack(pady=5)

    btn_mostrar = tk.Button(proveedores_window, text="2. MOSTRAR PROVEEDORES", command=mostrar_proveedor)
    btn_mostrar.pack(pady=5)

    btn_actualizar = tk.Button(proveedores_window, text="3. ACTUALIZAR PROVEEDOR", command=actualizar_proveedor)
    btn_actualizar.pack(pady=5)

    btn_borrar = tk.Button(proveedores_window, text="4. BORRAR PROVEEDOR", command=borrar_proveedor)
    btn_borrar.pack(pady=5)

    btn_volver = tk.Button(proveedores_window, text="5. VOLVER AL MENU PRINCIPAL", command=volver_proveedores_menu_principal)
    btn_volver.pack(pady=5)

def salir():
    root.destroy()

root = tk.Tk()
root.title("Menu Principal")

label = tk.Label(root, text=".:::     MENU PRINCIPAL     :::.", font=("Helvetica", 16))
label.pack(pady=10)

btn_productos = tk.Button(root, text="1. GESTION DE PRODUCTOS", command=gestion_productos)
btn_productos.pack(pady=5)

btn_proveedores = tk.Button(root, text="2. GESTION DE PROVEEDORES", command=gestion_proveedores)
btn_proveedores.pack(pady=5)

btn_salir = tk.Button(root, text="3. SALIR", command=salir)
btn_salir.pack(pady=5)

root.mainloop()
