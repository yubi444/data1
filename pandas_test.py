import pandas as pd

df = pd.read_csv('fastfood.csv')


print(df.to_string())


# Finding max and min
p = df['calories'].max()
q = df['calories'].min()

# Print max and min values
print("Maximum calories: ", p)
print("Minimum calories: ", q)

# Accessing a specific value|The value that I picked was the last in the mcdonalds menu
calories_at_first_row_iat = df.iat[56, df.columns.get_loc('calories')]
calories_at_first_row_at = df.at[0, 'calories']

# Get the index of the min and max in the fastfood.csv
index_max_calorie = df['calories'].idxmax()

index_min_calorie = df['calories'].idxmin()

# Get the name of the food item with max calories
restaurant_with_max_calorie = df.at[index_max_calorie, 'restaurant']
restaurant_with_min_calorie = df.at[index_min_calorie, 'restaurant']

item_with_max_calorie = df.at[index_max_calorie, 'item']
item_with_min_calorie = df.at[index_min_calorie, 'item']
# This Prints the highest and lowest calorie item
print("---------------Highest Calorie---------------------")
print("The food item with the highest calories is:", item_with_max_calorie)
print("The Restaurant with the highest calorie item is", restaurant_with_max_calorie)
print("It has", df.at[index_max_calorie, 'calories'], "calories.")
print("---------------Lowest Calorie---------------------")
print("The food item with the lowest calories is:", item_with_min_calorie)
print("The Restaurant with the lowest calorie item is", restaurant_with_min_calorie)
print("It has", df.at[index_min_calorie, 'calories'], "calories")

def get_max_min_calorie_items(restaurant_name):
    # Filter the dataframe for the given restaurant
    df_filtered = df[df['restaurant'] == restaurant_name]

    # If the filtered DataFrame is empty, return None
    if df_filtered.empty:
        return None

    # Get the indices of the max and min calorie items
    index_max_calorie = df_filtered['calories'].idxmax()
    index_min_calorie = df_filtered['calories'].idxmin()

    # Get the names of the max and min calorie items
    item_with_max_calorie = df_filtered.at[index_max_calorie, 'item']
    item_with_min_calorie = df_filtered.at[index_min_calorie, 'item']

    # Get the max and min calorie values
    max_calories = df_filtered.at[index_max_calorie, 'calories']
    min_calories = df_filtered.at[index_min_calorie, 'calories']

    return item_with_max_calorie, max_calories, item_with_min_calorie, min_calories


restaurant_name = input("Please enter the name of a restaurant (From The List): ")

result = get_max_min_calorie_items(restaurant_name)

if result is None:
    print(f"No data available for the restaurant: {restaurant_name}.")
else:
    item_with_max_calorie, max_calories, item_with_min_calorie, min_calories = result

    print("---------------Highest Calorie Item at", restaurant_name, "---------------------")
    print("The food item with the highest calories is:", item_with_max_calorie)
    print("It has", max_calories, "calories.")
    print("---------------Lowest Calorie Item at", restaurant_name, "---------------------")
    print("The food item with the lowest calories is:", item_with_min_calorie)
    print("It has", min_calories, "calories.")



def search_food_item(item_name):
    # Search for the given item name in the DataFrame
    df_searched = df[df['item'].str.contains(item_name, case=False, na=False)]

    # If no matching items are found, return None
    if df_searched.empty:
        return None

    # Return the matched rows
    return df_searched


# Get the item name from the user
item_name = input("Please enter the name of a food item to search: ")

# Get the search results
search_results = search_food_item(item_name)

# Display the search results
if search_results is None:
    print(f"No food items found with the name {item_name}.")
else:
    print("Search Results:")
    print(search_results[['restaurant', 'item', 'calories']].to_string())

