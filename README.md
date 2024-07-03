# API-EasyBroker
 En este repo se realizará el codigo que consuma la API de EasyBroker

## Requisitos

- Python 3.x

## Instalación

1. Crea y activa un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

2. Instala las dependencias:

    ```bash
        pip install -r requirements.txt
    ```

## Uso (debe de imprimir los titulos de todas las propiedades)

    ```bash
        python easy_broker_api.py
    ```


## Pruebas unitarias (podra ver en el archivo test_easy_broker_api.py las 3 diferentes que se hicieron)

    ```bash
        python -m unittest test_easy_broker_api.py
    ```