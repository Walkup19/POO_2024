from productos import productos
from proveedores import proveedores
from funciones import *

while True:
    print("""
.:::     MENU PRINCIPAL     :::.

    1. GESTION DE PRODUCTOS
    2. GESTION DE PROVEEDORES
    3. SALIR
""")
    
    opc = int(input("Elige una opcion: "))
    match opc:
        case 1:
            while True:
                print("""
.:::     GESTION DE PRODUCTOS     :::.

    1. CREAR PRODUCTO
    2. MOSTRAR PRODUCTOS    
    3. ACTUALIZAR PRODUCTO
    4. BORRAR PRODUCTO
    5. VOLVER AL MENU PRINCIPAL
""")
                
                opc_producto = int(input("Elige una opcion: "))
                match opc_producto:
                    case 1:
                        while True:
                            print("\n \t .:::   CREAR PRODUCTO   :::.")
                            print("""
.:::     SELECCIONA PRODUCTO A CREAR     :::.

    1. HERRAMIENTA
    2. MAQUINARIA
    3. MATERIAL
    4. VOLVER AL MENU ANTERIOR
""")
                            seleccionar_producto = int(input("Elige una opcion: "))
                            match seleccionar_producto:
                                case 1:
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_herramienta = input("\tTipo de herramienta: ")
                                    marca_herramienta = input("\tMarca de herramienta: ")
                                    modelo_herramienta = input("\tModelo: ")

                                    obj_herramienta = productos.Herramientas(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_herramienta, marca_herramienta, modelo_herramienta)
                                    resultado = obj_herramienta.crear()

                                    if resultado:
                                        print("Producto creado con éxito.")
                                    else:
                                        print("Fallo al crear el producto.")
                                case 2:
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_maquinaria = input("\tTipo de maquinaria: ")
                                    marca_maquinaria = input("\tMarca de maquinaria: ")
                                    modelo_maquinaria = input("\tModelo de maquinaria: ")
                                    anio_fabricacion = int(input("\tAnio de fabricacion: "))
                                    num_serie = int(input("\tNumero de serie: "))
                                    estado_maquinaria = input("\tEstado de maquinaria (nuevo, usado, mantenimiento, daniada): ")

                                    obj_maquinaria = productos.Maquinaria(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria)
                                    resultado = obj_maquinaria.crear()

                                    if resultado:
                                        print("Producto creado con éxito.")
                                    else:
                                        print("Fallo al crear el producto.")
                                case 3:
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_material = input("\tTipo de material: ")
                                    unidad_medida = input("\tUnidad de medida del material: ")

                                    obj_material = productos.Materiales(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_material, unidad_medida)
                                    resultado = obj_material.crear()

                                    if resultado:
                                        print("Producto creado con éxito.")
                                    else:
                                        print("Fallo al crear el producto.")
                                case 4:
                                    break  
                                case _:
                                    print("Opcion incorrecta, intenta de nuevo.")
                    case 2:
                        while True:
                            print("\n \t .:::   MOSTRAR PRODUCTOS   :::.")
                            print("""
.:::     SELECCIONA PRODUCTO A MOSTRAR     :::.

    1. HERRAMIENTA
    2. MAQUINARIA
    3. MATERIAL
    4. VOLVER AL MENU ANTERIOR
""")
                            seleccionar_producto = int(input("Elige una opcion: "))
                            match seleccionar_producto:
                                case 1:
                                    productos.Herramientas.mostrar()
                                case 2:
                                    productos.Maquinaria.mostrar()
                                case 3:
                                    productos.Materiales.mostrar()
                                case 4:
                                    break
                                case _:
                                    print("Opcion incorrecta, intenta de nuevo.")
                    case 3:
                        while True:
                            print("\n \t .:::   ACTUALIZAR PRODUCTOS   :::.")
                            print("""
.:::     SELECCIONA PRODUCTO A ACTUALIZAR     :::.

    1. HERRAMIENTA
    2. MAQUINARIA
    3. MATERIAL
    4. VOLVER AL MENU ANTERIOR
""")
                            seleccionar_producto = int(input("Elige una opcion: "))
                            match seleccionar_producto:
                                case 1:
                                    #Solicitar el ID del producto a actualizar
                                    id_producto = int(input("\tIngresa el ID de la herramienta que deseas actualizar: "))

                                    #Solicitar datos nuevos 
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_herramienta = input("\tTipo de herramienta: ")
                                    marca_herramienta = input("\tMarca de herramienta: ")
                                    modelo_herramienta = input("\tModelo de herramienta: ")

                                    #Crear objeto con los datos nuevos
                                    obj_herramienta = productos.Herramientas(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_herramienta, marca_herramienta, modelo_herramienta)

                                    #Llamar a la funcion actualizar
                                    resultado = obj_herramienta.actualizar(id_producto)

                                    if resultado:
                                        print("Herramienta actualizada exitosamente.")
                                    else:
                                        print("Ha ocurrido un error al actualizar la herramienta.")
                                case 2:
                                    #Solicitar el ID del producto a actualizar
                                    id_producto = int(input("\tIngresa el ID de la maquinaria que deseas actualizar: "))

                                    #Solicitar datos nuevos 
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_maquinaria = input("\tTipo de maquinaria: ")
                                    marca_maquinaria = input("\tMarca de maquinaria: ")
                                    modelo_maquinaria = input("\tModelo de maquinaria: ")
                                    anio_fabricacion = int(input("\tAnio de fabricacion:"))
                                    num_serie = int(input("\tNumero de serie: "))
                                    estado_maquinaria = input("\tEstado de maquinaria (nuevo, usado, mantenimiento, daniada): ")

                                    #Crear objeto con los datos nuevos
                                    obj_maquinaria = productos.Maquinaria(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_maquinaria, marca_maquinaria, modelo_maquinaria, anio_fabricacion, num_serie, estado_maquinaria)

                                    #Llamar a la funcion actualizar
                                    resultado = obj_maquinaria.actualizar(id_producto)

                                    if resultado:
                                        print("Maquinaria actualizada exitosamente.")
                                    else:
                                        print("Ha ocurrido un error al actualizar la maquinaria.")
                                case 3:
                                    #Solicitar el ID del producto a actualizar
                                    id_producto = int(input("\tIngresa el ID de la herramienta que deseas actualizar: "))

                                    #Solicitar datos nuevos 
                                    nombre = input("\tNombre: ")
                                    categoria = input("\tCategoria: ")
                                    cantidad = int(input("\tCantidad: "))
                                    precio_unitario = float(input("\tPrecio unitario: "))
                                    descripcion = input("\tDescripcion: ")
                                    tipo_material = input("\tTipo de material: ")
                                    unidad_medida = input("\tUnidad de medida: ")

                                    #Crear objeto con los datos nuevos
                                    obj_material = productos.Materiales(nombre, categoria, cantidad, precio_unitario, descripcion, tipo_material, unidad_medida)

                                    #Llamar a la funcion actualizar
                                    resultado = obj_material.actualizar(id_producto)

                                    if resultado:
                                        print("Material actualizado exitosamente.")
                                    else:
                                        print("Ha ocurrido un error al actualizar el material")
                                case 4:
                                    break
                                case _:
                                    print("Opcion incorrecta, intenta de nuevo.")
                    case 4:
                        while True:
                            print("\n \t .:::   BORRAR PRODUCTOS   :::.")
                            print("""
.:::     SELECCIONA PRODUCTO A BORRAR     :::.

    1. HERRAMIENTA
    2. MAQUINARIA
    3. MATERIAL
    4. VOLVER AL MENU ANTERIOR
""")
                            seleccionar_producto = int(input("Elige una opcion: "))
                            match seleccionar_producto:
                                case 1:
                                    #Solicitar el ID del producto a borrar
                                    id_producto = int(input("\tIngresa el ID de la maquinaria que deseas borrar: "))

                                    #Objeto vacío
                                    obj_herramienta = productos.Herramientas("", "", 0, 0.0, "", "", "", "")

                                    #Llamar a la funcion
                                    resultado = obj_herramienta.borrar(id_producto)

                                    if resultado:
                                        print("Herramienta borrada con exito.")
                                    else:
                                        print("Ha ocurrido un error al borrar la herramienta.")
                                case 2:
                                    #Solicitar el ID del producto a borrar
                                    id_producto = int(input("\tIngresa el ID de la maquinaria que deseas borrar: "))

                                    #Objeto vacío
                                    obj_maquinaria = productos.Maquinaria("", "", 0, 0.0, "", "", "", "", 0, 0, "")

                                    #Llamar a la funcion
                                    resultado = obj_maquinaria.borrar(id_producto)

                                    if resultado:
                                        print("Maquinaria borrada con exito.")
                                    else:
                                        print("Ha ocurrido un error al borrar la maquinaria.")
                                case 3:
                                    #Solicitar el ID del producto a borrar
                                    id_producto = int(input("\tIngresa el ID del material que deseas borrar: "))

                                    #Objeto vacío
                                    obj_material = productos.Materiales("", "", 0, 0.0, "", "", "")

                                    #Llamar a la funcion
                                    resultado = obj_material.borrar(id_producto)

                                    if resultado:
                                        print("Material borrado con exito.")
                                    else:
                                        print("Ha ocurrido un error al borrar el material.")
                                case 4:
                                    break
                                case _:
                                    print("Opcion incorrecta, intenta de nuevo.")
                    case 5:
                        break  
                    case _:
                        print("Opcion incorrecta, intenta de nuevo.")
        case 2:
            borrarPantalla()
            while True:
                print("""
.:::     GESTION DE PROVEEDORES     :::.

    1. CREAR PROVEEDOR
    2. MOSTRAR PROVEEDOR
    3. ACTUALIZAR PROVEEDOR
    4. BORRAR PROVEEDOR
    5. VOLVER AL MENU PRINCIPAL
""")
                
                opc_proveedor = int(input("Elige una opcion: "))
                match opc_proveedor:
                    case 1:
                        nombre = input("\tNombre: ")
                        direccion = input("\tDireccion: ")
                        telefono = input("\tTelefono: ")
                        email = input("\tCorreo Electronico: ")
                        productos_suministrados = input("\tIngresa los productos que suministró el proveedor: ")
                        contacto_principal = input("\tIngresa el nombre completo del contacto principal del proveedor: ")
                        notas = input("\tIngresa alguna nota sobre el proveedor: ")

                        obj_proveedor = proveedores.Proveedores(nombre, direccion, telefono, email, productos_suministrados, contacto_principal, notas)
                        resultado = obj_proveedor.crear_proveedor()

                        if resultado:
                            print("Proveedor creado con éxito.")
                        else:
                            print("Fallo al crear el proveedor.")
                    case 2:
                        proveedores.Proveedores.mostrar_proveedor()
                    case 3:
                        borrarPantalla()
                        #Solicitar el ID del proveedor a actualizar
                        id_prov = int(input("\tIngresa el ID del proveedor que deseas actualizar: "))

                        #Solicitar datos nuevos 
                        nombre = input("\tNombre: ")
                        direccion = input("\tDireccion del proveedor: ")
                        telefono = input("\tNumero de telefono del proveedor: ")
                        email = input("\tCorreo electronico del proveedor: ")
                        productos_suministrados = input("\tProductos suministrados por el proveedor: ")
                        contacto_principal = input("\tContacto principal del proveedor: ")
                        notas = input("\tIngresa alguna nota sobre el proveedor: ")

                        #Crear objeto con los datos nuevos
                        obj_proveedor = proveedores.Proveedores(nombre, direccion, telefono, email, productos_suministrados, contacto_principal, notas)

                        #Llamar a la funcion actualizar
                        resultado = obj_proveedor.actualizar_proveedor(id_prov)

                        if resultado:
                            borrarPantalla()
                            input("Proveedor actualizado exitosamente. Pulsa ENTER para continuar...")
                        else:
                            print("Ha ocurrido un error al actualizar el proveedor")
                    case 4:
                        borrarPantalla()
                        #Solicitar el ID del proveedor a borrar
                        id_prov = int(input("\tIngresa el ID del proveedor que deseas borrar: "))

                        #Objeto vacío
                        obj_proveedor = proveedores.Proveedores("", "", "", "", "", "", "")

                        #Llamar a la funcion
                        resultado = obj_proveedor.borrar_proveedor(id_prov)

                        if resultado:
                            print("Proveedor borrado con exito.")
                        else:
                            print("Ha ocurrido un error al borrar el proveedor.")
                    case 5:
                        borrarPantalla()
                        break  
                    case _:
                        print("Opcion incorrecta, intenta de nuevo.")
        case 3:
            borrarPantalla()
            print("Gracias por utilizar este programa.")
            break
        case _:
            print("Opcion incorrecta, elige de nuevo.")


    
    