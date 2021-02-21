# nepomoika

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```



# Всякое о докере (все команды выполняются в директории проекта)

## Сборка
```
docker build -t vuejs-cookbook/dockerize-vuejs-app .
```

## Запуск
```
docker run -it -p 8080:80 --rm --name dockerize-vuejs-app-1 vuejs-cookbook/dockerize-vuejs-app
```
