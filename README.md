
# Emotion Analizer

Este es un proyecto surgio por un proyecto final universitario, se basa en un modelo de IA capaz de transcribir un audio e interpretar el sentimiento del hablante gracias a integracion de NLP.

## Librerias necesarias

Encontraras un archivo con dichas librerias en el archivo requirements

## Features

- Transcribir Texto
- Transcribir Texto y analizar sentimiento

## API Reference

#### Root

```http
  GET /root/
```

#### Get Audio transcription 

```http
  GET /upload-audio
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `audio`      | `file` | **Required**. |


#### Get Text transcription 

```http
  GET /upload-text
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `string`      | `text` | **Required**. |


## Usage/Examples

```javascript
fetch("http://127.0.0.1:8000/upload-audio", {
    method: 'POST',
    body: body
}).then(data => data).then(data => res.json())
.then(res => console.log(res))

function App() {
  return <Component />
}
```

