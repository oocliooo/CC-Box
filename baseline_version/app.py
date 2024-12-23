from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI

app = Flask(__name__)

client = AzureOpenAI(
    api_key="2b27fb0a4cfb4e398463ff91f2cd6ff3",
    api_version="2023-05-15",
    azure_endpoint="https://hkust.azure-api.net"
)

@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/generate-plan', methods=['POST'])
def generate_plan():
    user_input = request.json.get('prompt')

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        products = response.choices[0].message.content
        return jsonify({'products': products})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to fetch data from GPT API'}), 500
    
@app.route('/plan')
def plan():
    return render_template('plan.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

if __name__ == '__main__':
    app.run(debug=True)