import os
import time
import shutil

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def move_file(source_path, destination_directory):
    try:
        # Move the file to the destination directory
        shutil.move(source_path, destination_directory)
        print(f"File moved successfully to {destination_directory}")
    except Exception as e:
        print(f"Error moving file: {e}")

def detect_changes(directory, move_directory):
    # Get the initial list of files in the directory
    files_before = list_files(directory)
    audio_extensions = ['mp3', 'mp4', 'wav']
    image_extensions = ['jpeg', 'png', 'jpg', 'arw']
    pdf_extensions = ['pdf']
    word_extensions = ['doc']
    excel_extensions = ['xlsx']

    while True:
        # Get the current list of files in the directory
        files_after = list_files(directory)

        # Find the differences between the two lists
        added_files = set(files_after) - set(files_before)
        deleted_files = set(files_before) - set(files_after)

        # Check if any changes occurred
        if added_files or deleted_files:
            print("Changes detected:")
            if added_files:
                print("Added files:", added_files)
                for file in added_files:
                  file_extension  = file.split(".")[-1].lower()
                  if file_extension in audio_extensions:
                      move_file(file, move_directory + "/Audio")
                  elif file_extension.lower() in image_extensions:
                      move_file(file, move_directory + "/Images")
                  elif file_extension.lower() in pdf_extensions:
                      move_file(file, move_directory + "/Pdf")
                  elif file_extension.lower() in word_extensions:
                      move_file(file, move_directory + "/Word")
                  elif file_extension.lower() in excel_extensions:
                      move_file(file, move_directory + "/Excell")
                  elif file_extension.lower() == "excalidraw":
                      move_file(file, move_directory + "/Notebook")
                  else:
                      pass
  
            if deleted_files:
                print("Deleted files:", deleted_files)
            # Update the list of files for the next iteration
            files_before = files_after

        # Sleep for a specific interval (e.g., 1 second)
        time.sleep(1)


    
