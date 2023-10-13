# 使用基础映像
FROM python:3.9

# 在容器中创建一个工作目录
WORKDIR /app

# 复制文件到工作目录
COPY . /app

# 安装依赖项
RUN pip install flask requests

# 暴露端口
EXPOSE 80

# 定义容器的入口点
CMD ["python", "app.py"]