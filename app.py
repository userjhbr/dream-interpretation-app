from flask import Flask, request, jsonify

app = Flask(__name__)

# Função de interpretação sem considerar sentimentos
def interpret_freud_and_jung(dream_text):
    freudian_symbols = {
        "casa": "Representa o self e a mente.",
        "água": "Simboliza o inconsciente e emoções.",
        "voar": "Desejos de liberdade e transcendência.",
        "fama": "Desejo de reconhecimento e validação, associado ao ego.",
        "cantor": "Pode representar a expressão do self e criatividade.",
    }
    
    jungian_symbols = {
        "sombra": "Aspectos ocultos do self.",
        "anima": "Aspectos femininos na psique masculina.",
        "herói": "Busca por individuação e auto-realização.",
        "fama": "Busca de individuação e auto-realização.",
        "cantor": "Símbolo de auto-expressão e a busca de um caminho de vida autêntico.",
    }
    
    interpretation = []
    
    for word in dream_text.split():
        if word in freudian_symbols:
            interpretation.append(f"Freud: {freudian_symbols[word]}")
        if word in jungian_symbols:
            interpretation.append(f"Jung: {jungian_symbols[word]}")
    
    return " ".join(interpretation)

# Função de interpretação considerando sentimentos
def interpret_with_feelings(dream_text, feelings):
    interpretation = []
    
    # Ajustar interpretação com base nos sentimentos
    if "frustração" in feelings:
        interpretation.append("A presença de sentimentos de frustração indica que...")
    elif "realização" in feelings:
        interpretation.append("Os sentimentos de realização sugerem que...")
    
    # Analisar os elementos do sonho como antes
    freudian_symbols = {
        "casa": "Representa o self e a mente.",
        "água": "Simboliza o inconsciente e emoções.",
        "voar": "Desejos de liberdade e transcendência.",
        "fama": "Desejo de reconhecimento e validação, associado ao ego.",
        "cantor": "Pode representar a expressão do self e criatividade.",
    }
    
    jungian_symbols = {
        "sombra": "Aspectos ocultos do self.",
        "anima": "Aspectos femininos na psique masculina.",
        "herói": "Busca por individuação e auto-realização.",
        "fama": "Busca de individuação e auto-realização.",
        "cantor": "Símbolo de auto-expressão e a busca de um caminho de vida autêntico.",
    }
    
    for word in dream_text.split():
        if word in freudian_symbols:
            interpretation.append(f"Freud: {freudian_symbols[word]}")
        if word in jungian_symbols:
            interpretation.append(f"Jung: {jungian_symbols[word]}")
    
    return " ".join(interpretation)

# Endpoint para interpretar sonho sem considerar sentimentos
@app.route('/interpret_dream', methods=['POST'])
def interpret_dream():
    data = request.get_json()
    dream_text = data.get('dream_text', '')
    
    # Chama a função de interpretação sem sentimentos
    interpretation = interpret_freud_and_jung(dream_text)
    
    return jsonify({'interpretation': interpretation})

# Endpoint para interpretar sonho considerando sentimentos
@app.route('/interpret_dream_with_feelings', methods=['POST'])
def interpret_dream_with_feelings():
    data = request.get_json()
    dream_text = data.get('dream_text', '')
    feelings = data.get('feelings', [])
    
    # Chama a função de interpretação com sentimentos
    interpretation = interpret_with_feelings(dream_text, feelings)
    
    return jsonify({'interpretation': interpretation})

if __name__ == '__main__':
    app.run(debug=True)
