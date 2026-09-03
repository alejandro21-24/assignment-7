from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  
print(customer_preferences)
# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)



# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    product['tags'] = set(product['tags'])
    converted_products.append(product)




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    return len(product_tags.intersection(customer_tags))
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    results = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        results.append({'name': product['name'], 'match_count': match_count})
    results.sort(key=lambda x: x['match_count'], reverse=True)
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    return results



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_tags)
print("Recommended products:")
for recommendation in recommendations:
    print(f"- {recommendation['name']} ({recommendation['match_count']} matches)")



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#   Loops, list appending, set conversion, and set intersection are the main functions of 
# this program. Until the user typed "N," I repeatedly gathered consumer preferences using a 
# while loop. I then stored each response in a list using append(). Since adding to a list is easy
# and effective and the order and quantity of user inputs didn't yet matter, a list made sense in 
# this situation. After gathering the raw preferences, I used set() to turn the list into a set. 
# Since sets cannot include repeated values, this automatically eliminated any duplicate preferences 
# the user might have input twice. I converted each product's tags from a list to a set in the 
# same way.Performance is the reason for converting both to sets: comparing two lists item by 
# item is much slower than using.intersection() to check for overlap between two sets, especially
#  when the amount of data increases. While comparing lists necessitates comparing each element 
# against every other element, sets use hashing internally, making membership tests and intersections 
# almost constant in time. Lastly, I used count_matches() on each product using a for loop inside 
# recommend_products(), and then I used sort() with a lambda key to rank the results by match 
# count, highest first.

# 2. How might this code change if you had 1000+ products?
#  Since #converting tags to sets keeps each individual comparison quick, the present method 
# would still function properly with more than 1,000 goods. However, at a higher scale 
# (tens of thousands of products or more), looping through each and every product on each request
#  could become slow. Instead of scanning the full catalog, I could optimize this by creating an
#  index # that maps each tag to the list of items that include it. This way, I would only look 
# at # products that share at least one tag with the client. Instead of sorting the entire list 
# each time, I might also think about limiting results early (e.g., only tracking # the top 10 
# matches).