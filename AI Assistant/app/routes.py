from flask import Blueprint, render_template, request, jsonify
import google.generativeai as genai
import time

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/ask', methods=['POST'])
def ask_gemini():
    data = request.json
    prompt = data['prompt']
    model_name = data.get('model', 'gemini-pro')
    
    start_time = time.time()
    
    try:
        # Initialize the generative model
        model = genai.GenerativeModel(model_name)
        
        # Generate content
        response = model.generate_content(prompt)
        
        end_time = time.time()
        
        return jsonify({
            'success': True,
            'response': response.text,
            'time_taken': round(end_time - start_time, 2),
            'model_used': model_name
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
