# UADER_ISII_ROUDE1
# Trabajo práctico 1 
## GITHUB
### Taller gestión de la configuración

A continuación comentaré los pasos realizados según los puntos del trabajo práctico:

### **Punto 1:**

Cree el repositorio UADER_ISII_ROUDE1 en github. 
Seguí los siguientes comandos: 
1. git init "UADER_ISII_ROUDE1"
2. git add . 
3. git commit -m "Primer commit" 
4. git branch -M main 
5. git remote add origin git@github.com:marisaroude/UADER_ISII_ROUDE1.git

### **Punto 2:**

Cree las carpetas desde la consola:
1. Mkdir Python
2. Mkdir bin
3. Mkdir bash
4. Mkdir images
5. Mkdir docs

### **Punto 3:**

Luego de esto agregue en la carpeta de Python el archivo de primos.py

### **Punto 4:**

Para ejecutar el achivo _*primos.py*_ desde la consola me posicione en la carpeta de python e ingrese lo siguiente
python primos.py 

### **Punto 5:**

Hice git add . , commit y cuando quise realizar el push me dio un error de autenticación.
Por lo tanto tuve que autenticarme, cree una clave SSH y la asocie a github. 
Luego al intentar hacer el push me dio el siguiente error:
![Image_error](../main/images/push-error.png)

Este error me dio porque cree el repositorio incluyendo el README. Y lo tenia en el repositorio local, por lo tanto borre el readme del repositorio local e hice los siguientes comandos:
- git pull --rebase origin main
- git log
- git push -u origin main

### **Punto 6:**
Borre el archivo primos.py y lo comprobé por consola con el comando git status de la siguiente manera:
![Image_borrado](../main/images/archivo-borrado.png)

Para recuperar el archivo primos.py utilicé el comando git checkout primos.py

**Punto 7:**

Ejecuto primos.py desde la consola de la siguiente manera:

Python primos.py

Para leer las constantes desde la consola me guié del siguiente link:

https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion7/entrada_salida.html

Luego que dejé el archivo primos.py listo ejecute:
- git add . 
- git commit 
- git push

### **Punto 8 y 9:**

Instalé el módulo Textblob que se utiliza para traducir los print.

### **Punto 10:**

Utilicé el módulo time para imprimir la fecha y hora actual en la consola.











