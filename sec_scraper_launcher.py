import subprocess
import webbrowser
import time
import os
import sys

# Get the absolute path to the script in the packaged temp folder
script_path = os.path.join(sys._MEIPASS, "SECscraper.py")

# Launch Streamlit app
process = subprocess.Popen(["streamlit", "run", script_path])

# Give Streamlit a moment to start
time.sleep(2)

# Open the browser
webbrowser.open("http://localhost:8501")

# Wait for Streamlit to exit
process.wait()
