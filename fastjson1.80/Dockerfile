# 使用基础镜像，例如OpenJDK
FROM openjdk:11-jdk-slim

# 设置工作目录
WORKDIR /app

# 将JAR文件复制到工作目录
COPY fastjson1.80.jar /app/fastjson1.80.jar

# 暴露应用程序的端口
EXPOSE 80

# 启动应用程序
CMD ["java", "-jar", "/app/fastjson1.80.jar"]