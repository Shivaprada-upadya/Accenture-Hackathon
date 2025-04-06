"""
from agents.recommendation_agent import recommend_products

def main():
    customer_id = input("Enter customer ID: ")
    
    recommendations = recommend_products(customer_id)
    
    print("\n🎯 Final Recommendations:\n")
    print(recommendations)

if __name__ == "__main__":
    main()  
 
    """
    
    
from flask import Flask, request, jsonify
from flask_cors import CORS
from agents.customer_agent import get_customer_profile
from agents.recommendation_agent import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    customer_id = data.get('customer_id')

    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    try:
        customer_profile = get_customer_profile(customer_id)
        final_recommendation_text = get_recommendations(customer_profile)

        return jsonify({"recommendations_text": final_recommendation_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



