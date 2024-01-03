import time
from pathlib import Path

# Try to import requests, if it fails, exit the program
try :
    import requests
except ImportError:
    print("Error: requests is not installed")
    exit()

def create_filename(base_path, prefix, index, extension=".jpg"):
    """
    Create a filename that doesn't exist in a directory
    If a same file already exists, it will increment the index until it finds a unique filename
    :param base_path: The directory where the file will be saved
    :param prefix: The prefix of the filename
    :param index: The index of the filename
    :param extension: The file extension, default is .jpg
    :return: The path to the new and unique file
    """
    # Add a dot to the extension if it doesn't have one
    if extension[0] != ".":
        extension = "." + extension

    # Create the path
    file_path = base_path / (prefix + str(index) + extension)

    # If the file already exists, increment the index until it finds a unique filename
    while file_path.exists():
        index += 1
        file_path = base_path / (prefix + str(index) + extension)

    return file_path

def get_image(session, url):
    """
    Get an image from a url
    If requests successfully gets the image, it will return the image content
    If not, it will return None
    :param session (requests.Session): The session to use
    :param url: The url of the image
    :return: The image content if it was successful, None if not
    """
    try :
        response = session.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.ConnectionError as er:
        print(f"Error in get_image: {er}")
        return None

def save_image(image, path):
    """
    Save an image to a path
    If it was successful, it will return True
    If not, it will print an error message and return False
    :param image: The image content
    :param path: The path to save the image
    :return: True if it was successful, False if not
    """
    try :
        with open(path, "wb") as file:
            file.write(image)
        return True
    except IOError as er:
        print(f"Error in save_image: {er}")
        return False


def get_faces(session, url, nb_faces=1, timing=0.30, save_between=False, path_to_save="faces/", prefix="face_"):
    """
    Retrieve a number of faces from a url and save them to a directory
    Each face is retrieved every timing seconds (to avoid spamming the server)
    If save_between is True, each face will be saved immediately after it is retrieved (avoid problems)
    :param session: The session to use
    :param url: The url of the image
    :param nb_faces: The number of faces to retrieve (default is 1)
    :param timing: The time between each face retrieval (default is 0.30 seconds, don't go too low or you might get double images)
    :param save_between: If True, each face will be saved immediately after it is retrieved (default is False)
    :param path_to_save: The path to save the faces (default is "faces/")
    :param prefix: The prefix of the filename (default is "face_")
    :return:
    """
    # Create path and make sure it exists
    path_to_save = Path(path_to_save)
    path_to_save.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

    faces = []

    # Get the faces
    for i in range(nb_faces):
        # start the timer
        timer = time.time()

        # Get the image
        image = get_image(session, url)

        # If the image is None, it means that there was an error
        # So we skip to the next one
        if not image:
            print("Image not found, skipping...")
            continue # Skip to the next iteration

        # Process the image
        faces.append(image)
        if save_between:
            file_path = create_filename(path_to_save, prefix, i)
            save_image(image, file_path)
            print(f"Image saved : {file_path}")


        # Wait until the timer is done
        while time.time() - timer < timing:
            pass

    return faces

