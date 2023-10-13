# 使用基于Ubuntu的Python镜像
FROM python:3.9-buster

# 安装LibreOffice和一些其他依赖
RUN apt-get update && apt-get install -y libreoffice

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到工作目录
COPY . .

# 安装Python依赖
RUN pip install -r requirements.txt

# 启动Flask服务器
CMD ["python", "app.py"]