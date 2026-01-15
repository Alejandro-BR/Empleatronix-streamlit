# 🏢 Empleatronix

Aplicación web interactiva construida con **Streamlit** para visualizar y explorar datos de empleados, mostrando sus sueldos mediante una gráfica de barras horizontales interactiva.

[Demo en Streamlit 🔗](https://empleatronix-alejandrobr.streamlit.app/)

## 📂 Estructura del proyecto

```
.
├── data/
│   └── employees.csv
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 📊 Datos

La aplicación utiliza el archivo:

```
data/employees.csv
```

| Columna     | Tipo de dato         | Descripción                     |
| ----------- | -------------------- | ------------------------------- |
| `full name` | `string` (texto)     | Nombre completo del empleado    |
| `salary`    | `int` (entero)       | Sueldo del empleado en euros    |
| `gender`    | `string` (categoría) | Género del empleado             |
| `email`     | `string` (texto)     | Correo electrónico del empleado |

## 🐳 Ejecutar con Docker

### 1. Construir y levantar el contenedor

```bash
docker-compose up --build
```

### 2. Abrir en el navegador

```
http://localhost:8501
```

## ✍️ Créditos

**Alejandro Barrionuevo Rosado**

Máster de FP en Inteligencia Artificial y Big Data - CPIFP Alan Turing
