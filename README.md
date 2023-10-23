# 个人漏洞复现学习记录
为方便各位师傅，都做成了docker文件

在对应的Dockerfile目录下执行
```
docker build -t test .
```

全部都在容器里开的是80端口，执行
```
docker run test -p 80:80
```
访问机器80端口即可开始复现
