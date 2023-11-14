import streamlit as st

def generate_imdb_urls(base_url, increment, results_per_page, total_results):
    num_links = total_results // results_per_page
    urls = []

    for i in range(increment + 1, num_links * increment + 1, increment):
        url = f"{base_url}&start={i}&ref_=adv_nxt"
        urls.append(url)

    return urls

def main():
    st.title("IMDb Search URL Generator")

    # Get user input for base URL
    base_url = st.text_input("Enter IMDb base URL:")

    # Get user input for increment, results per page, and total results
    increment = st.slider("Select Increment", min_value=1, max_value=100, value=50)
    results_per_page = st.slider("Select Results Per Page", min_value=1, max_value=100, value=50)
    total_results = st.number_input("Enter Total Results", value=10000)

    # Generate URLs
    if st.button("Generate URLs"):
        if base_url:
            urls = generate_imdb_urls(base_url, increment, results_per_page, total_results)
            st.success("URLs generated successfully!")
            st.write("Generated URLs:")
            for url in urls:
                st.write(url)
        else:
            st.warning("Please enter a valid base URL.")

if __name__ == "__main__":
    main()
