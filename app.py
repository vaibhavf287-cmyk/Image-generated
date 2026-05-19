import os
import requests
from flask import Flask, request, jsonify, send_file, render_template_string
import io

app = Flask(__name__)

# हमेशा एक्टिव रहने वाला सबसे स्टेबल मॉडल
API_URL = "https://huggingface.co"

# टोकन को सुरक्षित रूप से Render से उठाना
HF_TOKEN = os.environ.get('HF_API_KEY')
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

HTML_UI = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>मेरा अपना AI इमेज जनरेटर</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #121212; color: white; text-align: center; padding: 20px; }
        .container { max-width: 500px; margin: auto; background: #1e1e1e; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        input[type="text"] { width: 90%; padding: 12px; margin: 10px 0; border: none; border-radius: 5px; font-size: 16px; }
        button { width: 95%; padding: 12px; background-color: #00adb5; border: none; color: white; font-size: 16px; font-weight: bold; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #007a80; }
        #result { margin-top: 20px; }
        img { max-width: 100%; border-radius: 8px; margin-top: 10px; display: none; }
        .loading { display: none; color: #00adb5; font-weight: bold; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎨 My AI Image Generator</h2>
        <input type="text" id="prompt" placeholder="यहाँ लिखें (जैसे: Astronaut riding a horse)...">
        <button onclick="generateImage()">इमेज बनाएं</button>
        <div class="loading" id="loading">AI फोटो बना रहा है, कृपया 10-15 सेकंड रुकें...</div>
        <div id="result">
            <img id="outputImage" src="" alt="Generated Image">
        </div>
    </div>

    <script>
        async function generateImage() {
            const prompt = document.getElementById('prompt').value;
            const loading = document.getElementById('loading');
            const img = document.getElementById('outputImage');
            
            if (!prompt) { return alert('कृपया कुछ टेक्स्ट लिखें!'); }
            
            loading.innerText = 'AI फोटो बना रहा है, कृपया 10-15 सेकंड रुकें...';
            loading.style.display = 'block';
            img.style.display = 'none';
            
            try {
                const response = await fetch(`/generate?prompt=${encodeURIComponent(prompt)}`);
                const data = await response.json().catch(() => null);
                
                if (data && data.error) {
                    alert('Error: ' + data.error);
                } else if (response.ok) {
                    const blob = await response.blob();
                    img.src = URL.createObjectURL(blob);
                    img.style.display = 'block';
                } else {
                    alert('इमेज जनरेट नहीं हो सकी। दोबारा कोशिश करें।');
                }
            } catch (error) {
                alert('सर्वर से संपर्क नहीं हो पाया।');
            } finally {
                loading.style.display = 'none';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_UI)

@app.route('/generate', methods=['GET'])
def generate():
    prompt = request.args.get('prompt')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    if not HF_TOKEN:
        return jsonify({"error": "Render पर HF_API_KEY सेट नहीं है। कृपया चेक करें।"}), 500

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=30)
        
        if response.status_code == 200:
            return send_file(io.BytesIO(response.content), mimetype='image/jpeg')
        else:
            # Hugging Face से आने वाले सटीक एरर मैसेज को पढ़ना
            error_details = response.json()
            error_msg = error_details.get('error', 'Unknown Hugging Face Error')
            return jsonify({"error": f"Hugging Face: {error_msg}"}), response.status_code
            
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
        
