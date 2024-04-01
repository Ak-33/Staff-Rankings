import streamlit as st
import fortnite_api

# Initialize the Fortnite API client
api = fortnite_api.FortniteAPI(api_key='8eeca9b5-14ca-4afd-91d6-aed25f55d5b7')

def display_item_shop():
    try:
        # Fetch the latest item shop
        shop = api.shop.fetch()

        # Display the item shop information
        st.write("Item Shop Update:")
        
        if shop.featured:
            st.write("Featured Items:")
            display_shop_section(shop.featured)

        if shop.daily:
            st.write("Daily Items:")
            display_shop_section(shop.daily)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def display_shop_section(section):
    for entry in section.entries:
        name = entry.display_name if hasattr(entry, 'display_name') else "Name Unavailable"
        st.write(f"Name: {name}")
        st.write(f"Price: {entry.final_price} V-Bucks")
        # Attempt to construct image URL based on item name
        image_url = f"https://fortnite-api.com/images/cosmetics/br/{name.lower().replace(' ', '_')}/small.png"
        st.image(image_url, caption="Item Image", width=100)
        st.write("---")  # Add a separator between items

# Create the Streamlit app
def main():
    st.title("Fortnite Item Shop Update")
    display_item_shop()

if __name__ == "__main__":
    main()
