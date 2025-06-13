import json


FILENAME = "data.json"


def load_blog_posts():
    """
    Load blog posts from a JSON file.
    :param: None
    :return: List of blog posts.
    """
    try:
        with open(FILENAME, "r") as file:
            blog_posts = json.load(file)
        return blog_posts
    except FileNotFoundError:
        print(f"Error: The file {FILENAME} does not exist.")
        return []   # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print(f"Error: The file {FILENAME} is not a valid JSON.")
        return []   # Return an empty list if the JSON is invalid


def save_blog_posts(blog_posts):
    """
    Save blog posts to a JSON file.
    :param blog_posts: List of blog posts to save.
    :return: None
    """
    try:
        with open(FILENAME, "w") as file:
            json.dump(blog_posts, file, indent=4)
    except IOError as e:
        print(f"Error: Could not write to file {FILENAME}. {e}")    # Handle file write errors



