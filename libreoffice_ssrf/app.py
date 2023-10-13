from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return """docx,xlsx文件ole对象ssrf</br><form action="/upload" method="POST" enctype="multipart/form-data">
       <input type="file" name="file">
       <input type="submit" value="上传">
   </form>"""

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        # 保存上传的文件
        file.save(file.filename)

        if file.filename.endswith(('.xlsx', '.docx')):
            # 将文件转换为PDF
            output_pdf_path = os.path.splitext(file.filename)[0] + '.pdf'
            subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', file.filename])

            # 显示成功消息
            message = '文件上传成功！'
            return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
