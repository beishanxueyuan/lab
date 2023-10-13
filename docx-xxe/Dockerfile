# 使用 php:7.4-apache 镜像作为基础镜像
FROM php:7.4-apache

# 安装所需的依赖和扩展
RUN apt-get update && apt-get install -y \
    libzip-dev \
    && rm -rf /var/lib/apt/lists/*

# 安装 zip 扩展并启用
RUN docker-php-ext-install zip

# 将自定义的 Apache 配置文件复制到容器中的相应路径
COPY ./apache/000-default.conf /etc/apache2/sites-available/000-default.conf

# 启用 Apache rewrite 模块
RUN a2enmod rewrite

# 创建应用代码目录
WORKDIR /var/www/html

# 复制应用代码到容器中
COPY ./www .

# 创建上传目录
RUN mkdir /var/www/html/uploads/

# 修改上传目录权限
RUN chmod -R 777 /var/www/html/uploads/

# 暴露端口
EXPOSE 80

CMD ["--net=host"]