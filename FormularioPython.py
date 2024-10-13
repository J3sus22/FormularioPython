import tkinter as tk
from tkinter import messagebox
import re
import mysql.connector

def insertar_en_bd(nombres, apellidos, edad, estatura, telefono, genero):
     try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3306",
            database="programacion_a",
            user="root",
            password="TobbyM4tias280"
        )
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO registros (Nombre, Apellidos, Edad, Estatura, Telefono, Genero)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (nombres, apellidos, edad, estatura, telefono, genero))
        connection.commit()

        cursor.close()
        connection.close()

     except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al insertar en la base de datos: {error}")

# Definición de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellido.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)

def borrar():
    limpiar_campos()

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellido.get()
    edads = tbEdad.get()
    estaturas = tbEstatura.get()
    telefonos = tbTelefono.get()
    
    # Obtener el género de los RadioButtons
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"
    
    datos = f"Nombre: {nombres}\nApellido: {apellidos}\nEdad: {edads}\nEstatura: {estaturas}\nTelefono: {telefonos}\nGenero: {genero}"
    
    insertar_en_bd(nombres, apellidos, edads, estaturas, telefonos, genero)    
    messagebox.showinfo("Informacion", f"Datos guardados con exito:\n\n{datos}")
    limpiar_campos()

def validar_edad(event):
    if not entero_valido(tbEdad.get()):
        messagebox.showerror("Error", "Por favor, ingrese una edad valida.")
        tbEdad.delete(0, tk.END)

def validar_estatura(event):
    if not decimal_valido(tbEstatura.get()):
        messagebox.showerror("Error", "Por favor, ingrese una estatura valida.")
        tbEstatura.delete(0, tk.END)

def validar_telefono(event):
    if not entero_valido_de_10_digitos(tbTelefono.get()):
        messagebox.showerror("Error telefono", "Ingrese un telefono de 10 digitos.")

def validar_nombre(event):
    if not texto_valido(tbNombre.get()):
        messagebox.showerror("Error", "Por favor, ingrese un nombre valido.")

def validar_apellido(event):
    if not texto_valido(tbApellido.get()):
        messagebox.showerror("Error", "Por favor, ingrese un apellido valido.")

def entero_valido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

def decimal_valido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def entero_valido_de_10_digitos(valor):
    return valor.isdigit() and len(valor) == 10

def texto_valido(valor):
    return bool(re.match(r'^[a-zA-Z\s]+$', valor))

# Configuracion de la ventana principal
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Formulario Vr.01")

# Variable para Radiobutton
var_genero = tk.IntVar()

# Creación de widgets
lbNombre = tk.Label(ventana, text="Nombre:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()
tbNombre.bind("<KeyRelease>", validar_nombre)

lbApellido = tk.Label(ventana, text="Apellido:")
lbApellido.pack()
tbApellido = tk.Entry(ventana)
tbApellido.pack()
tbApellido.bind("<KeyRelease>", validar_apellido)

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()
tbEdad.bind("<KeyRelease>", validar_edad)

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()
tbEstatura.bind("<KeyRelease>", validar_estatura)

lbTelefono = tk.Label(ventana, text="Telefono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()
tbTelefono.bind("<FocusOut>", validar_telefono)

lbGenero = tk.Label(ventana, text="Genero:")
lbGenero.pack()
rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()
rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

# Creación de botones
btnBorrar = tk.Button(ventana, text="Borrar", command=borrar)
btnBorrar.pack()
btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()
ventana.mainloop()