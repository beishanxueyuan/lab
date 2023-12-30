生成软链接文件：ln -s /etc/passwd symlink.file
压缩：zip -r --symlink symlink.zip symlink.file

```
docker build -t symlink .
```
```
docker run -p 80:80 symlink
```
