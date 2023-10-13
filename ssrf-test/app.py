from flask import Flask,request
import requests
import json

app = Flask(__name__)

@app.route('/ssrf', methods=['GET', 'POST'])
def s_path():
    url = request.args.get('url')
    post_url = request.values.get('url')
    if url:
        response = requests.get(url)
        return f"GET Response: {response.text}"
    elif post_url:
        response = requests.get(post_url)
        return f"POST Response: {response.text}"
    else:
        data = request.get_data()
        data = json.loads(data)
        json_url = data['url']
        response = requests.get(json_url)
        return f"JSON Response: {response.text}"

@app.route('/', methods=['GET'])
def index():
    return '''
    <script>
            function json_ssrf() {
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/ssrf', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        var data = {
            url: document.querySelector('body > input[type=text]').value
        };
        xhr.send(JSON.stringify(data));
    }

        function post_ssrf() {
        document.getElementById('myForm')[0].value=document.querySelector('body > input[type=text]').value;
        document.getElementById('myForm').submit()
    }
    
    </script>
        <form id="myForm" action="/ssrf" method="post">
            <input type="hidden" name="url" value="value1">
        </form>
        <input type="text" name="url" placeholder="输入URL" required>
        <br>
        <button type="submit" name="get_request" onclick="window.open('/ssrf?url='+document.querySelector('body > input[type=text]').value);">GET请求</button>
        <button type="submit" name="post_form_request" onclick="post_ssrf();">POST Form请求</button>
        <button type="submit" name="post_json_request" onclick="json_ssrf();">POST JSON请求</button>
    '''

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)