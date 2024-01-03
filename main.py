import FacesGenerator

# Main execution
if __name__ == "__main__":
    # 1. Informations
    url = "https://thispersondoesnotexist.com"
    path_to_save = "faces/"
    prefix = "face_"

    # 2. Get the number of faces to generate
    try :
        nb_faces = int(input("How many faces do you want to generate? "))
        if nb_faces < 1:
            raise ValueError("The number of faces must be greater than 0")
    except ValueError as er:
        print(f"Error: {er}")
        exit()

    # 3. Create a Session and get the faces
    with FacesGenerator.requests.Session() as session:
        FacesGenerator.get_faces(session, url, nb_faces, timing=0.3,save_between=True, path_to_save=path_to_save)