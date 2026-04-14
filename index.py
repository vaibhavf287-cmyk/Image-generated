<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>X Gen - Premium AI</title>
<link
href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap"
rel="stylesheet">
<style>
/* --- PREMIUM CSS VARIABLES --- */
:root {
--bg-color: #050505;
--card-bg: rgba(30, 30, 35, 0.7);
--accent: #00f2ff; /* Cyber Cyan */
--accent-glow: rgba(0, 242, 255, 0.4);
--text-main: #ffffff;
--text-sec: #aaaaaa;
--glass: rgba(255, 255, 255, 0.05);
--border: rgba(255, 255, 255, 0.1);
}
* { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
body {
background-color: var(--bg-color);
background-image: radial-gradient(circle at 50% -20%, #1a1a2e, #000000);
color: var(--text-main);
font-family: 'Outfit', sans-serif;
min-height: 100vh;
display: flex;
flex-direction: column;
align-items: center;
padding-bottom: 60px; /* Space for footer */
}
/* --- HEADER & TABS --- */
.header {

width: 100%;
padding: 20px;
text-align: center;
background: rgba(0,0,0,0.5);
backdrop-filter: blur(10px);
position: sticky;
top: 0;
z-index: 100;
border-bottom: 1px solid var(--border);
}
h1 {
font-weight: 700;
letter-spacing: 1px;
background: linear-gradient(90deg, #fff, var(--accent));
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom: 15px;
font-size: 1.8rem;
}
/* Telegram Button (Floating Pill) */
.tg-btn {
background: linear-gradient(45deg, #0088cc, #005f8f);
color: white;
text-decoration: none;
padding: 8px 20px;
border-radius: 20px;
font-size: 0.9rem;
font-weight: 500;
box-shadow: 0 4px 15px rgba(0,136,204,0.3);
display: inline-block;
margin-bottom: 15px;
transition: transform 0.2s;
}
.tg-btn:active { transform: scale(0.95); }
/* Custom Tabs */
.tabs {
display: flex;
background: var(--glass);
border-radius: 50px;
padding: 5px;
width: 90%;

max-width: 400px;
margin: 0 auto;
border: 1px solid var(--border);
}
.tab {
flex: 1;
padding: 10px;
text-align: center;
border-radius: 40px;
cursor: pointer;
transition: all 0.3s ease;
font-weight: 500;
color: var(--text-sec);
}
.tab.active {
background: var(--accent);
color: #000;
box-shadow: 0 0 15px var(--accent-glow);
font-weight: 700;
}
/* --- MAIN CONTENT AREA --- */
.container {
width: 90%;
max-width: 600px;
margin-top: 20px;
flex: 1;
}
/* --- CREATOR TAB --- */
#creatorTab { display: block; }
.prompt-box {
background: var(--card-bg);
border: 1px solid var(--border);
border-radius: 20px;
padding: 20px;
backdrop-filter: blur(10px);
box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
textarea {

width: 100%;
background: rgba(0,0,0,0.3);
border: 1px solid var(--border);
border-radius: 12px;
padding: 15px;
color: #fff;
font-family: inherit;
font-size: 1rem;
resize: none;
outline: none;
transition: border 0.3s;
}
textarea:focus { border-color: var(--accent); }
.controls {
display: flex;
gap: 10px;
margin-top: 15px;
}
select {
background: rgba(0,0,0,0.3);
color: #fff;
border: 1px solid var(--border);
padding: 12px;
border-radius: 10px;
flex: 1;
outline: none;
}
.gen-btn {
background: var(--accent);
color: #000;
border: none;
padding: 12px 25px;
border-radius: 10px;
font-weight: 700;
cursor: pointer;
flex: 2;
box-shadow: 0 0 20px var(--accent-glow);
transition: 0.3s;
}
.gen-btn:hover { box-shadow: 0 0 30px var(--accent-glow); }
.gen-btn:active { transform: scale(0.98); }

/* Image Result */
.result-area {
margin-top: 20px;
min-height: 300px;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
position: relative;
}
.main-img {
width: 100%;
border-radius: 15px;
display: none;
box-shadow: 0 10px 40px rgba(0,0,0,0.6);
border: 1px solid var(--border);
}
.loading {
width: 40px;
height: 40px;
border: 4px solid rgba(255,255,255,0.1);
border-top: 4px solid var(--accent);
border-radius: 50%;
animation: spin 1s infinite linear;
display: none;
}
.download-btn {
margin-top: 15px;
background: #fff;
color: #000;
padding: 10px 20px;
border-radius: 50px;
font-weight: 600;
text-decoration: none;
display: none; /* Hidden until image generates */
box-shadow: 0 5px 15px rgba(255,255,255,0.2);
}
/* --- GALLERY TAB (History) --- */
#galleryTab { display: none; }

.gallery-grid {
display: grid;
grid-template-columns: repeat(2, 1fr);
gap: 15px;
padding-bottom: 20px;
}
.gallery-item {
position: relative;
border-radius: 12px;
overflow: hidden;
aspect-ratio: 1;
border: 1px solid var(--border);
background: var(--card-bg);
}
.gallery-item img {
width: 100%;
height: 100%;
object-fit: cover;
}
.empty-msg {
text-align: center;
color: var(--text-sec);
margin-top: 50px;
font-size: 0.9rem;
}
/* --- FOOTER --- */
.footer {
position: fixed;
bottom: 0;
width: 100%;
text-align: center;
padding: 15px;
background: linear-gradient(to top, #000, transparent);
font-weight: 900;
letter-spacing: 2px;
font-size: 1.2rem;
color: #fff;
text-shadow: 0 0 10px var(--accent);
pointer-events: none;

}
@keyframes spin { 100% { transform: rotate(360deg); } }
</style>
</head>
<body>
<div class="header">
<a href="https://t.me/aihindiagency" target="_blank" class="tg-btn">Join Telegram ✈️</a>
<h1>X GEN AI</h1>
<div class="tabs">
<div class="tab active" onclick="switchTab('creator')">Creator</div>
<div class="tab" onclick="switchTab('gallery')">Gallery</div>
</div>
</div>
<div class="container">
<div id="creatorTab">
<div class="prompt-box">
<textarea id="prompt" rows="3" placeholder="What do you want to create
today?"></textarea>
<div class="controls">
<select id="ratio">
<option value="1:1">Square (1:1)</option>
<option value="16:9">YouTube (16:9)</option>
<option value="9:16">Mobile (9:16)</option>
<option value="3:4">Portrait (3:4)</option>
</select>
<button class="gen-btn" onclick="generateArt()">GENERATE ✨</button>
</div>
</div>
<div class="result-area">
<div class="loading" id="loader"></div>
<img id="resultImage" class="main-img" src="" alt="AI Art">
<a href="#" id="dlBtn" class="download-btn" onclick="downloadCurrent()">Download
HD ⬇️</a>
</div>
</div>
<div id="galleryTab">

<div class="gallery-grid" id="galleryGrid">
</div>
<div id="emptyMsg" class="empty-msg">No images yet. Create something
amazing!</div>
</div>
</div>
<div class="footer">AI HINDI AGENCY</div>
<script>
// --- LOGIC ---
const loader = document.getElementById('loader');
const resultImg = document.getElementById('resultImage');
const dlBtn = document.getElementById('dlBtn');
const galleryGrid = document.getElementById('galleryGrid');
const emptyMsg = document.getElementById('emptyMsg');
// Current State
let currentUrl = '';
// Switch Tabs
function switchTab(tabName) {
document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
if (tabName === 'creator') {
document.querySelector('.tabs .tab:nth-child(1)').classList.add('active');
document.getElementById('creatorTab').style.display = 'block';
document.getElementById('galleryTab').style.display = 'none';
} else {
document.querySelector('.tabs .tab:nth-child(2)').classList.add('active');
document.getElementById('creatorTab').style.display = 'none';
document.getElementById('galleryTab').style.display = 'block';
loadHistory(); // Refresh history grid
}
}
// Generate Image
function generateArt() {
const prompt = document.getElementById('prompt').value.trim();
const ratio = document.getElementById('ratio').value;
if (!prompt) return alert("Please type a prompt first!");

// UI Updates
loader.style.display = 'block';
resultImg.style.display = 'none';
dlBtn.style.display = 'none';
// Calculate Dimensions
let w = 1024, h = 1024;
if (ratio === '16:9') { w = 1280; h = 720; }
else if (ratio === '9:16') { w = 720; h = 1280; }
else if (ratio === '3:4') { w = 768; h = 1024; }
const seed = Math.floor(Math.random() * 1000000);
// Pollinations API URL
const url =
`https://image.pollinations.ai/prompt/${encodeURIComponent(prompt)}?width=${w}&height=${h}
&seed=${seed}&nologo=true`;
// Preload Image
const img = new Image();
img.src = url;
img.onload = () => {
loader.style.display = 'none';
resultImg.src = url;
resultImg.style.display = 'block';
dlBtn.style.display = 'inline-block';
currentUrl = url;
// Save to History automatically
saveToHistory(url, prompt);
};
}
// Download Function
function downloadCurrent() {
if(!currentUrl) return;
const link = document.createElement('a');
link.href = currentUrl;
link.target = '_blank';
link.download = 'AI-Art-' + Date.now();
link.click();
}
// Local Storage History

function saveToHistory(url, prompt) {
let history = JSON.parse(localStorage.getItem('xhistory')) || [];
// Add new to start
history.unshift({ url: url, prompt: prompt });
// Keep only last 20
if (history.length > 20) history.pop();
localStorage.setItem('xhistory', JSON.stringify(history));
}
function loadHistory() {
let history = JSON.parse(localStorage.getItem('xhistory')) || [];
galleryGrid.innerHTML = '';
if (history.length === 0) {
emptyMsg.style.display = 'block';
return;
} else {
emptyMsg.style.display = 'none';
}
history.forEach(item => {
const div = document.createElement('div');
div.className = 'gallery-item';
div.innerHTML = `<img src="${item.url}" onclick="viewImage('${item.url}')">`;
galleryGrid.appendChild(div);
});
}
function viewImage(url) {
// Click history to bring back to creator tab
switchTab('creator');
resultImg.src = url;
resultImg.style.display = 'block';
currentUrl = url;
dlBtn.style.display = 'inline-block';
}
</script>
</body>
</html>
