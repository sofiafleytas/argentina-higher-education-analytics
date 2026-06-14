# Argentina Higher Education Analytics

Análisis exploratorio de la educación superior argentina utilizando datos abiertos oficiales del Gobierno Nacional.

## Objetivo

El objetivo de este proyecto es analizar la evolución de la matrícula universitaria, los egresados, las diferencias entre universidades públicas y privadas, y la distribución de estudiantes por áreas de conocimiento entre 2014 y 2023.

Además, se realiza un caso de estudio específico sobre las carreras de Informática para comprender su evolución dentro del sistema universitario argentino.

---

## Dataset

**Fuente oficial**

https://www.argentina.gob.ar/sites/default/files/00._educ_superior_datos.csv

**Período analizado**

2014 - 2023

**Cantidad de registros**

6.074

### Variables principales

| Variable | Descripción |
|-----------|------------|
| ANIO | Año |
| TIPO_UNIV | Universidad Pública o Privada |
| NIVEL_ACADEM | Pregrado, Grado o Posgrado |
| OF_ACADEM | Tipo de oferta académica |
| DISCIP_OCDE | Área de conocimiento OCDE |
| DISCIP_ESPECIF | Disciplina específica |
| TIPO_ALUMNO | Estudiantes o Egresados |
| VALOR | Cantidad de personas |

---

## Arquitectura del Proyecto

```text
argentina-higher-education-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── 01_data_discovery.ipynb
│   ├── 02_data_profiling.ipynb03_business_analysis
    └── 03_business_analysis
│
├── src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── README.md
└── requirements.txt
```


## Pipeline ETL

### Extracción

Se desarrolló un proceso automatizado para descargar el dataset oficial desde el portal de datos abiertos del Gobierno Nacional.

### Transformación

Reglas aplicadas:

- Conversión de la variable `VALOR` a tipo entero.
- Eliminación de la columna `U_MED`.
- Validación de tipos de datos.
- Verificación de valores nulos.
- Verificación de registros duplicados.

### Carga

Preparación de datasets analíticos para consumo posterior en Power BI.


# Análisis Exploratorio de Datos

## KPI 1 - Evolución de Estudiantes

### Resultados

| Año | Estudiantes |
|------|-----------:|
| 2014 | 2.005.469 |
| 2023 | 2.730.800 |

### Hallazgos

- La matrícula universitaria creció un **36,2%** entre 2014 y 2023.
- El mayor crecimiento anual ocurrió en 2020.
- La tendencia general muestra una expansión sostenida del sistema universitario.


## KPI 2 - Evolución de Egresados

### Resultados

| Año | Egresados |
|------|---------:|
| 2014 | 134.234 |
| 2023 | 159.730 |

### Hallazgos

- Los egresados crecieron un **19%** durante el período analizado.
- El crecimiento fue significativamente menor al observado en la matrícula.


## KPI 3 - Relación entre Estudiantes y Egresados

### Hallazgos

| Año | Indicador |
|------|----------:|
| 2014 | 6,69% |
| 2023 | 5,85% |

El crecimiento de la matrícula no estuvo acompañado por un crecimiento proporcional de los egresados.


## KPI 4 - Universidades Públicas vs Privadas

### Indicador de Egresados respecto a Estudiantes

| Tipo de Universidad | Indicador |
|--------------------|----------:|
| Privada | 10,25% |
| Pública | 4,87% |

### Hallazgos

- Las universidades públicas concentran la mayoría de estudiantes y egresados.
- Las universidades privadas presentan una mayor proporción de egresados respecto a su volumen de estudiantes.
- Este indicador no representa una tasa de graduación real, sino una relación agregada entre estudiantes y egresados.


## KPI 5 - Distribución de Estudiantes por Área de Conocimiento

| Disciplina | Participación |
|------------|-------------:|
| Ciencias Sociales | 48,63% |
| Ciencias Médicas | 17,80% |
| Exactas y Naturales | 11,33% |
| Ingeniería y Tecnología | 11,06% |
| Humanidades | 8,29% |
| Ciencias Agrícolas | 2,89% |

### Hallazgos

- Casi la mitad de la matrícula universitaria argentina pertenece al área de Ciencias Sociales.
- Ciencias Médicas ocupa el segundo lugar con el 17,8% de participación.


## KPI 6 - Distribución de Egresados por Área de Conocimiento

| Disciplina | Participación |
|------------|-------------:|
| Ciencias Sociales | 54,39% |
| Ciencias Médicas | 18,55% |
| Ingeniería y Tecnología | 9,93% |
| Exactas y Naturales | 9,01% |
| Humanidades | 5,82% |
| Ciencias Agrícolas | 2,30% |

### Hallazgos

- Más de la mitad de los egresados pertenecen al área de Ciencias Sociales.
- Ingeniería y Exactas presentan una menor participación relativa en egresados que en estudiantes.


# Caso de Estudio: Informática

## Evolución de Estudiantes

| Año | Estudiantes |
|------|-----------:|
| 2014 | 79.916 |
| 2023 | 177.525 |

### Hallazgo

La matrícula en Informática creció un **122%**, más de tres veces por encima del crecimiento del sistema universitario en general.


## Evolución de Egresados

| Año | Egresados |
|------|---------:|
| 2014 | 3.899 |
| 2023 | 3.883 |

### Hallazgo

La cantidad de egresados se mantuvo prácticamente estable durante toda la década.


## Relación entre Estudiantes y Egresados

| Año | Indicador |
|------|----------:|
| 2014 | 4,88% |
| 2023 | 2,19% |

### Hallazgo Principal

La demanda por carreras de Informática creció aceleradamente, especialmente a partir de 2020. Sin embargo, dicho crecimiento no se tradujo en un aumento proporcional de egresados.


## Ranking Nacional

### Estudiantes

Informática ocupa el puesto:

**#9 de 37 disciplinas específicas**

Participación:

**4,66%** del total de estudiantes universitarios.

### Hallazgo

Informática se encuentra entre las diez disciplinas con mayor cantidad de estudiantes del país.


# Tecnologías Utilizadas

- Python
- Pandas
- Jupyter Notebook
- Git
- GitHub
- Power BI


# Próximos Pasos

- Construcción del dashboard interactivo en Power BI.
- Visualización de tendencias de matrícula y egreso.
- Comparación entre universidades públicas y privadas.
- Análisis específico de carreras tecnológicas.
- Publicación como proyecto de portfolio.

