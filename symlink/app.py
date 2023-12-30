from flask import Flask, request, send_from_directory, jsonify,render_template
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 上传文件存放的文件夹

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        file_list = unzip(file_path)  # 调用解压函数
        return jsonify({'message': '文件上传成功并解压缩完成！', 'files': file_list})
    else:
        return '未选择文件！'

def unzip(file_path):
    extract_path = os.path.splitext(file_path)[0]  # 使用原文件名作为解压后的文件夹名
    os.makedirs(extract_path, exist_ok=True)
    command = f'unzip {file_path} -d {extract_path}'
    subprocess.run(command, shell=True)
    os.remove(file_path)  # 删除上传的zip文件

    file_list = []
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    
    return file_list

@app.route('/download/<path:filename>')
def download(filename):
    print(app.config['UPLOAD_FOLDER'])
    return send_from_directory('./', filename)

if __name__ == '__main__':
    app.run(port=80,debug=True)