# Moving from WordPress to Directus
These Python scripts enable you to export JSON files gotten from WordPress to Directus. 

## Reasons for Migrating to Directus
Migrating to Directus usually stems from the need for:
- Greater Flexibility: Directus allows for a more flexible content structure and presentation—headless CMS standard.
- Improved Performance: By decoupling the backend from the frontend, Directus can offer performance benefits, especially for content-heavy sites.
- Don't need to worry about databases or the backend in general.
- Enhanced Control over Content Delivery: Directus provides easier control over how and where content is delivered.
- Easily deliver content across various platforms and devices using their API or SDK

## How to use
If you already have Python installed you only need to install dotenv which we will use to get the environment variables.
```
pip install python-dotenv
```
After installations create the environment variables in `.env` file and populate them with your Directus details.
```
# .env
DIRECTRUS_URL=https://your.directus.app
ACCESS_KEY=your_access_key
```
Run the following to replace the current images with the images with the images saved in Directus: 
```bash
python extract-image.py
```
Run the following to post the JSON data to your Directus field:

```bash
python directus.py
```
