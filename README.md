# 🤖 Auditor-IA Costos Tercerizados TigoUNE

Plataforma corporativa automatizada para la auditoría, cruce masivo y validación de costos tercerizados frente a facturación en la operación de TigoUNE. Diseñada e implementada para Casalimpia S.A. bajo sus lineamientos de marca e identidad corporativa.

---

## 📌 Descripción General

El Auditor-IA automatiza la conciliación financiera y técnica entre los registros contables internos de Novasoft, las reversiones del cliente TigoUNE, las facturas registradas en la DIAN y el Cuadro Control operacional.

Sustituye procesos manuales complejos y propensos a error por un procesamiento veloz en segundos utilizando Python (Pandas), desplegando un dashboard analítico interactivo en Streamlit.

---

## ✨ Características Principales

* 🚀 **Procesamiento Ultra-Rápido:** Conciliación masiva de 6 bases de datos en segundos.

* 🎨 **Interfaz Corporativa:** Dashboard ejecutivo ajustado a la paleta institucional (Azul `#1179bf` y Verde `#83b431`) y tipografía oficial Montserrat de Casalimpia S.A.

* 📊 **Tarjetas KPI Ejecutivas:** Visualización clara de los montos evaluados ($ COP) y conteo de registros por estado operacional.

* 🔎 **Filtros & Buscador Universal:** Búsqueda en tiempo real por NIT, Proveedor, Número de Factura, Requerimiento (RQ), entre otros.

* ⚡ **Validación de Alertas DIAN:** Identificación de inconsistencias electrónicas tributarias en las facturas de proveedores.

* 📥 **Exportación Personalizada:** Descarga en Excel (.xlsx) que respeta dinámicamente los filtros y búsquedas aplicadas en pantalla.

---

## 📋 Reglas de Clasificación Operacional (OBS_2)

El motor de auditoría evalúa cada registro y lo clasifica automáticamente en uno de los 4 estados institucionales:

* **Gestión correcta:** Requerimiento numérico válido con utilidad positiva tras el cruce.

* **Facturación del proveedor sin cobro al cliente:** Registro con costo pero con factura en 0 o sin facturar al cliente.

* **Facturación del proveedor con pérdida:** Registros donde la utilidad resulta negativa o menor/igual a cero.

* **Facturación del proveedor sin requerimientos identificados:** Registros cuyo Requerimiento (RQ) viene vacío, en 0 o contiene texto no numérico.

---

## 📁 Archivos Requeridos para el Cruce

La aplicación requiere la carga de 6 archivos Excel (.xlsx):

1. **BBDD Costos Novasoft:** Generado desde el módulo Contabilidad NIF Novasoft.
2. **BBDD Reversiones:** Archivo unificado de reversiones TigoUNE (RQ, Valor Facturado, EA, FV, Mes).
3. **BBDD F-100:** Reporte enviado por el área de Facturación.
4. **Cuadro-control:** Documento enviado por TigoUNE hasta la columna Provisión.
5. **Facturas NOVA:** Consulta CXP generada desde el módulo Contabilidad NIF Novasoft.
6. **Facturas DIAN:** Reporte oficial generado desde la plataforma DIAN.

> 💡 **Nota de flexibilidad:** Los usuarios pueden cargar los archivos con cualquier nombre; el sistema procesa la estructura interna de los libros de manera automática.

---

## 🛠️ Requisitos e Instalación

### Prerrequisitos
* Python 3.9 o superior instalado en el sistema.

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU-USUARIO/auditor-ia-costos-tigoune.git](https://github.com/TU-USUARIO/auditor-ia-costos-tigoune.git)
cd auditor-ia-costos-tigoune
