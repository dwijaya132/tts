import os
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/tts')
def proxy_tts():
    text = request.args.get('text', 'Halo')
    api_key = "Fohs1y49" 
    
    # URL resmi ResponsiveVoice
    rv_url = f"https://code.responsivevoice.org/getvoice.mp3?t={text}&tl=id&sv=g1&vn=&pitch=0.5&rate=0.5&vol=1&key={apiKey}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://responsivevoice.org/'
    }

    try:
        # Mengambil audio dari ResponsiveVoice
        r = requests.get(rv_url, headers=headers, stream=True, timeout=15)
        
        # Meneruskan data MP3 ke ESP32
        return Response(r.iter_content(chunk_size=1024), content_type='audio/mpeg')
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    # Port harus diambil dari environment variable Koyeb
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
