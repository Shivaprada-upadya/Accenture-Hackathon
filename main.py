from agents.recommendation_agent import recommend_products

def main():
    customer_id = input("Enter customer ID: ")
    recommendations = recommend_products(customer_id)
    print("\n🎯 Final Recommendations:\n")
    print(recommendations)

if __name__ == "__main__":
    main()
