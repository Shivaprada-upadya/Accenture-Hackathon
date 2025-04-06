

"""
from agents.customer_agent import get_customer_profile
from agents.product_agent import get_all_products
from ollama_integration.run_llm import query_llm

def recommend_products(customer_id):
    profile = get_customer_profile(customer_id)
    products = get_all_products()
    prompt = f"""
   # Based on this customer profile:
   # {profile}

   ### and these products:
   # {products.head(5).to_string()}

   # Recommend top 3 personalized products.
   # """
    #return query_llm(prompt)
    
from agents.product_agent import get_all_products
from ollama_integration.run_llm import query_llm

def get_recommendations(profile):
    products = get_all_products()

    prompt = f"""
    Based on this customer profile:
    {profile}

    and these products:
    {products.head(5).to_string()}

    Recommend top 3 personalized products.
    """
    return query_llm(prompt)

