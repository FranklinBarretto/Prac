from flask import Flask, render_template, request
app = Flask(__name__, static_folder="static")


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/read_file', methods=['GET'])
@app.route('/read_file/<string:file_name>', methods=['GET'])
def read_file(file_name="file1.txt"):
    start_line = request.args.get('start_line', default=0, type=int)
    end_line = request.args.get('end_line', default=0, type=int)
    try:
        with open('static/' + file_name, 'r', encoding="utf8", errors='ignore') as f:
            file_content = f.readlines()
            end_line = len(file_content) if end_line <= 0 else end_line + 1
            return render_template('content.html', data=file_content[start_line:end_line])
    except Exception as e:
        error_msg = e.message if hasattr(e, 'message') else e.__str__()
        return render_template('error.html', error=error_msg)


if __name__ == '__main__':
    app.run()
