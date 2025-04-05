
from agents.recommendation_agent import recommend_products

def main():
    customer_id = input("Enter customer ID: ")
    
    recommendations = recommend_products(customer_id)
    
    print("\n🎯 Final Recommendations:\n")
    print(recommendations)

if __name__ == "__main__":
    main()  
 

"""
from agents.recommendation_agent import recommend_products
from utils.graph_insights import plot_top_products

def main():
    customer_id = input("Enter customer ID: ")
    recommendations = recommend_products(customer_id)
    
    print("\n🎯 Final Recommendations:\n")
    for idx, rec in enumerate(recommendations, start=1):
        print(f"{idx}. {rec}\n")

    # 🎁 Bonus: Ask user if they want to see insights
    see_graph = input("📊 Do you want to see top 5 products for your customer type? (y/n): ").lower()
    if see_graph == 'y':
        from utils.customer_utils import get_customer_type
        from database.load_data import load_customer_data, load_product_data

        customer_df = load_customer_data()
        product_df = load_product_data()
        customer_type = get_customer_type(customer_id, customer_df)
        plot_top_products(product_df, customer_type)

if __name__ == "__main__":
    main()
"""