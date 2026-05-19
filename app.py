import os
import requests
from flask import Flask, request, jsonify, send_file, render_template_string
import io

app = Flask(__name__)

# सबसे भरोसेमंद और हमेशा चालू रहने वाला मॉडल
API_URL = "https://huggingface.co"
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
            
            loading.style.display = 'block';
            img.style.display = 'none';
            
            try {
                // इमेज को सीधे यूआरएल से लोड करना ताकि कोई JSON एरर न आए
                const response = await fetch(`/generate?prompt=${encodeURIComponent(prompt)}`);
                
                if (response.ok) {
                    const blob = await response.blob();
                    img.src = URL.createObjectURL(blob);
                    img.style.display = 'block';
                } else {
                    alert('मॉडल अभी लोड हो रहा है, कृपया 10 सेकंड बाद फिर बटन दबाएं।');
                }
            } catch (error) {
                alert('सर्वर व्यस्त है, कृपया दोबारा प्रयास करें।');
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
        return jsonify({"error": "No Token"}), 500

    try:
        response = requests.post(API_URL, headers=headers, json={"inputs": prompt}, timeout=40)
        
        if response.status_code == 200:
            return send_file(io.BytesIO(response.content), mimetype='image/jpeg')
        else:
            return "Error from Hugging Face", response.status_code
            
    except Exception as e:
        return "Server Error", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    
