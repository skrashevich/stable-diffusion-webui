[![Publish Docker](https://github.com/skrashevich/stable-diffusion-webui/actions/workflows/push.yml/badge.svg?branch=main&event=push)](https://github.com/skrashevich/stable-diffusion-webui/actions/workflows/push.yml)

Source: https://github.com/skrashevich/stable-diffusion-webui

Example docker-compose for SD with UI from AUTOMATIC1111
```
version: '3.9'

volumes:
  sd_data:
    driver: local

services:
  stable-diffusion:
    image: skrashevich/stable-diffusion:auto 
    ports:
      - "7860:7860"
    deploy:
      resources:
        reservations:
          devices:
              - driver: nvidia
                device_ids: ['0']
                capabilities: [gpu]
    volumes:
      - sd_data:/data
    environment:
      - CLI_ARGS=--allow-code --medvram --xformers --enable-insecure-extension-access --api
```

Example docker-compose for SD with invoke WebUI:
```
version: '3.9'

volumes:
  sd_data:
    driver: local

services:
  stable-diffusion:
    image: skrashevich/stable-diffusion:invoke 
    ports:
      - "7860:7860"
    deploy:
      resources:
        reservations:
          devices:
              - driver: nvidia
                device_ids: ['0']
                capabilities: [gpu]
    volumes:
      - sd_data:/data
    environment:
      - PRELOAD=true
```