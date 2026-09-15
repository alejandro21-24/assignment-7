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
    """
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    """
    return len(product_tags.intersection(customer_tags))


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    """
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    """
    results = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        results.append({'name': product['name'], 'match_count': match_count})

    results.sort(key=lambda x: x['match_count'], reverse=True)
    return results


# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_tags)
print("Recommended Products:")
for recommendation in recommendations:
    print(f"- {recommendation['name']} ({recommendation['match_count']} match(es))")

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#  This program's primary features include loops, list appending, set conversion, and set intersection.
#  Until the user entered "N," I used a while loop to repeatedly collect customer preferences. I then
# used append() to store each response in a list. A list made logical in this case since adding to a list
# is simple and efficient, and the number and order of user inputs didn't yet matter. I collected the raw
# preferences and then converted the list into a set using set(). This automatically removed any duplicate
#  preferences the user may have entered twice because sets cannot contain repeated values. In the same manner,
#  I changed the tags for every product from a list to a set. Converting both lists to sets is done for
#  performance reasons: comparing two lists item by item is significantly slower than using.intersection() to
# check for overlap between two sets, especially when the amount of data increases. Sets employ hashing internally,
#  making membership tests and intersections nearly constant in time, whereas comparing lists requires comparing
# every element against every other element. Finally, I used sort() with a lambda key to rank the results by match
#  count, highest first, after using count_matches() on each product using a for loop inside recommend_products().


# 2. How might this code change if you had 1000+ products?
#  The current solution would still work well with more than 1,000 commodities since transforming tags
# to sets keeps each individual comparison speedy. However, cycling over every product on every request
# could get slow at a larger scale (tens of thousands of products or more). I could optimize this by
# making an index that links each tag to the list of things that contain it, rather than scanning the
# entire catalog. In this manner, I would only consider goods that have at least one tag in common with
# the customer. I might also consider limiting results early rather than sorting the complete list each time.

