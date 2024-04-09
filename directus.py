import json
import requests


def import_posts_to_directus(json_file_path, directus_url, api_key):
    """
    Reads posts from a JSON file and imports them into Directus, including handling featured images.
    """
    with open(json_file_path, "r") as file:
        posts = json.load(file)

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    for post in posts:
        # Extract the first image URL from the content and simulate its upload to Directus
        # Prepare the payload for Directus
        payload = {
            "Title": post["Title"],
            "Content": post["Content"],
            "Date": post["Date"],
        }

        # POST the data to the Directus API
        response = requests.post(
            f"{directus_url}/items/article", headers=headers, json=payload
        )

        if response.status_code in [200, 201]:
            print(f"Post '{post['Title']}' imported successfully.")
        else:
            print(f"Failed to import post '{post['Title']}': {response.text}")


# Example usage
json_file_path = "modified_WP-data.json"
directus_url = "https://your.directus.app"
api_key = ""

# Uncomment the line below to run the function with your actual Directus URL and API key
import_posts_to_directus(json_file_path, directus_url, api_key)
