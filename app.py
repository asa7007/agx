from flask import Flask, request, jsonify

app = Flask(__name__)

status = 0  # Initial status

@app.route('/')
def index():
    return '''
    <html>
    <body>
        <h1>On/Off Control</h1>
        <button onclick="onButtonPressed()">On</button>
        <button onclick="offButtonPressed()">Off</button>
        <p>Status: <span id="status">0</span></p>
        <button onclick="getStatus()">Get Status</button>
        <script>
            function onButtonPressed() {
                fetch("/status?value=1");
            }

            function offButtonPressed() {
                fetch("/status?value=0");
            }

            function getStatus() {
                fetch("/get_status")
                    .then(response => response.text())
                    .then(status => alert("Current Status: " + status));
            }

            setInterval(function() {
                fetch("/check_status")
                    .then(response => response.text())
                    .then(status => document.getElementById("status").textContent = status);
            }, 1000);
        </script>
    </body>
    </html>
    '''

@app.route('/status', methods=['GET'])
def set_status():
    global status
    status = int(request.args.get('value', 0))
    return "OK"

@app.route('/check_status', methods=['GET'])
def check_status():
    return str(status)

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

