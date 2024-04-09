import json
import requests
import os

# Replace with the path to your JSON file
json_file_path = "WP-data.json"


# Simulated function to upload an image to Directus and return the new image URL
def upload_to_directus(image_url):
    # This is where you'd upload the image to Directus using its API.
    # Below is a simulated Directus URL for demonstration purposes.

    print(image_url)
    image_content = requests.get(image_url).content
    temp_image_path = "temp_image.jpg"  # Temporary file path for the downloaded image
    with open(temp_image_path, "wb") as file:
        file.write(image_content)

    headers = {"Authorization": "Bearer bqqTDS73DBsxPDUC9c0m5-xULZPAqeL3"}

    files = {
        "file": open(
            temp_image_path, "rb"
        )  # Open the temporary file to include in the request
    }
    directus_upload_url = "https://mvhd-blog.directus.app/files"

    print(f"Uploading image to Directus: {directus_upload_url}")
    response = requests.post(directus_upload_url, files=files, headers=headers)
    response_str = response.json()
    directus_image_id = response_str["data"]["id"]
    # Cleanup: remove the temporary image file
    os.remove(temp_image_path)

    # Construct the Directus image URL from the response

    directus_image_url = f"https://mvhd-blog.directus.app/assets/{directus_image_id}"

    print(f"Directus Image URL: {directus_image_url}")

    return directus_image_url


# Load JSON data from the file
with open(json_file_path, "r") as file:
    data = json.load(file)

# Iterate through each post in the JSON data
for post in data:
    content = post["Content"]

    # Check if there is an image in the content
    if '<img src="' in content:
        # Extract the image URL
        start_index = content.index('<img src="') + 10
        end_index = content.index('"', start_index)
        image_url = content[start_index:end_index]

        # Upload the image to Directus and get the new URL
        new_image_url = upload_to_directus(image_url)
        print(new_image_url)

        # Replace the old image URL with the new one in the content
        post["Content"] = content.replace(image_url, new_image_url)

# Output the modified JSON data to a new file or print it out
output_file_path = "modified_WP-data.json"
with open(output_file_path, "w") as file:
    json.dump(data, file, indent=4)

# Print a message to indicate completion
print("The JSON data has been updated with Directus image URLs.")
