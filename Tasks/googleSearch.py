try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# Enter your query
query = input("Enter the query: ")

# Search the query
results = search(query, tld="co.in", num=5, stop=5, pause=2)
 
# Display the results 
for result in results:
    print(result)