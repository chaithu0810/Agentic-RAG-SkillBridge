from src.policy_search import search_policy

question = "What are the attendance requirements?"

results = search_policy(question)

print("\nSEARCH RESULTS")

for result in results:

    print("\nSource:", result["source"])

    print("Content:")

    print(result["content"])

    print("-" * 50)