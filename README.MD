# Hygiene Py Bot

## Requerimientos
Python 3.10.0  
Dependencias detalladas en requirements.txt, para instalarlas ejecutar `pip install -r requirements.txt`

## Configurar ENV
Se debe crear un archivo llamado .env y dentro del mismo establecer la url del webhook en la variable: DAILY_HOOK_URL.

Para obtener la url del webhook debemos seguir las instrucciones detalladas en la documentación de microsoft: [Create Incoming Webhooks](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

## Puntos a tener en cuenta
- Cualquier cambio realizado en el branch main activara el deploy automático en Heroku.