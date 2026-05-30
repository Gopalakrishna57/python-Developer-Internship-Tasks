import os
import shutil

def clean_my_folder():
    print("--- File Automation Script ---")
    path = input("Enter the folder path to clean up: ")
    
    if not os.path.exists(path):
        print("Folder does not exist! Please check the path.")
        return

    # Read all files in the given directory
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        
        # Check if it is a file (not a folder)
        if os.path.isfile(file_path):
            # Get the file extension (e.g., pdf, jpg, txt)
            ext = file.split('.')[-1].lower() + "_Files"
            folder_path = os.path.join(path, ext)
            
            # Create a new folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            # Move the file into the respective folder
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"-> Moved: {file} to {ext}")

    print("\nAll files have been successfully organized!")

if __name__ == "__main__":
    clean_my_folder()