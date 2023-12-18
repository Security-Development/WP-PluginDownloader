# WP-PluginDownloader
WordPress Plugin Full Download Automation Program


> wordpress docker-compose.yml
```
services:
  db:
    image: mysql:5.7
    volumes:
      - ./db_data:/var/lib/mysql 
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: admin
      MYSQL_DATABASE: wordpress 
      MYSQL_USER: admin
      MYSQL_PASSWORD: admin
  app:
    depends_on:
      - db 
    image: wordpress:latest
    volumes:
      - ./app_data:/var/www/html
    ports:
      - "8080:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: admin
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_PASSWORD: admin
      WORDPRESS_DEBUG: 1


```
