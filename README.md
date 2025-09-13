# Sentiment Analysis Microservice

Este proyecto es un microservicio de análisis de sentimientos multilingüe construido con FastAPI. Utiliza el modelo de análisis de sentimientos de Hugging Face disponible en [AventIQ-AI/XLMRoBERTa_Multilingual_Sentiment_Analysis](https://huggingface.co/AventIQ-AI/XLMRoBERTa_Multilingual_Sentiment_Analysis).

## Estructura del Proyecto

```
sentiment-analysis-microservice
├── src
│   ├── main.py                # Punto de entrada de la aplicación
│   ├── api                    # Módulo de la API
│   │   ├── routes             # Rutas de la API
│   │   │   └── sentiment.py    # Rutas para el análisis de sentimientos
│   │   └── dependencies.py     # Dependencias de la API
│   ├── core                   # Módulo central
│   │   ├── config.py          # Configuración de la aplicación
│   │   └── logging.py         # Configuración del logging
│   ├── models                 # Modelos de datos
│   │   ├── request.py         # Modelos para las solicitudes
│   │   └── response.py        # Modelos para las respuestas
│   ├── services               # Lógica de negocio
│   │   └── sentiment_service.py # Servicio de análisis de sentimientos
│   └── utils                  # Funciones auxiliares
│       └── helpers.py         # Funciones de ayuda
├── tests                      # Pruebas del proyecto
│   ├── test_api.py           # Pruebas para la API
│   └── test_services.py       # Pruebas para los servicios
├── docker                     # Configuración de Docker
│   ├── Dockerfile             # Dockerfile para la aplicación
│   └── docker-compose.yml     # Configuración de Docker Compose
├── requirements.txt           # Dependencias necesarias para la aplicación
├── requirements-dev.txt       # Dependencias para desarrollo y pruebas
├── .env.example               # Ejemplo de variables de entorno
├── .gitignore                 # Archivos y directorios a ignorar por Git
└── README.md                  # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <url-del-repositorio>
   cd sentiment-analysis-microservice
   ```

2. Crea un entorno virtual y activa:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

Para iniciar el microservicio, ejecuta el siguiente comando:

```
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

El microservicio estará disponible en `http://localhost:8000`.

## Pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```
pytest
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

