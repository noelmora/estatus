# 🌐 Checador

**Checador** es una aplicación elegante y práctica para monitorear en tiempo real el estado de diversos endpoints HTTP. Gracias a su interfaz gráfica sencilla y moderna en Python con Tkinter, puedes visualizar fácilmente el estado de tus servicios, detectar errores, medir tiempos de respuesta y realizar pruebas rápidas con un servidor HTTP local integrado.

---

## 🚀 Características Principales

* ✅ **Interfaz amigable:** Vista clara y cómoda para visualizar resultados.
* ⏱️ **Chequeos automáticos:** Usa multihilos para no bloquear la interfaz.
* ⚙️ **Configuración dinámica:** Ajusta el intervalo de monitoreo directamente desde la aplicación.
* 🎨 **Colores intuitivos:** Estado indicado con colores (verde, amarillo, rojo).
* 🛠️ **Servidor local incluido:** Facilita pruebas rápidas y efectivas.

---

## 📋 Requisitos

* **Python** 3.6 o superior
* **Tkinter** (generalmente incluido con Python)
* Biblioteca **requests** (`pip install requests`)

---

## 📥 Instalación y Uso

### 🔧 Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/noelmora/estatus.git
   cd estatus
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

### 🖥️ Ejecuta el servidor local (opcional para pruebas)

```bash
python servidor.py
```

Esto levantará un servidor en `http://localhost:8000/servidor`.

### 🚀 Ejecuta la aplicación

Edita el archivo `checador.py` para agregar o cambiar los endpoints si lo necesitas.

```bash
python checador.py
```

---

## 🎯 Cómo usar Checador

* Observa la tabla principal para ver el estado actual de tus endpoints.
* Ajusta fácilmente el **intervalo de chequeo** desde la interfaz.
* Cierra la ventana cuando desees finalizar el monitoreo.

---

## 📂 Estructura del Proyecto

```
checador/
├── checador.py         # Aplicación principal con GUI
├── servidor.py         # Servidor HTTP simple para pruebas locales
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación
```

---

## 🖌️ Personalización

* **Endpoints:** Modifica directamente la lista de `endpoints` en el archivo `checador.py`.
* **Estilo y diseño:** Ajusta fuentes, colores y tamaños en `_configura_estilos()` dentro de `checador.py`.

---

## 🤝 Imagenes

![image](https://github.com/user-attachments/assets/b6912e2e-0af6-4e61-a863-753be128b13c)
![image](https://github.com/user-attachments/assets/c64b9909-c392-4b76-8666-679f00da2d31)



