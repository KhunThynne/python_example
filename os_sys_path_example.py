import os
import sys

# Get the current working directory
current_working_directory = os.getcwd()
# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Check if the current working directory is not the script directory
if current_working_directory != script_directory:
    # Create a path to the 'services' directory within the current working directory
    # services_path = os.path.join(current_working_directory, 'services')
    
    sys.path.append(os.path.abspath('services'))