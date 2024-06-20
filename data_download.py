import pandas as pd
import requests
import os
import re

def download_video(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            # optmize for quality and speed
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"Failed to download {url}")

def download_videos(csv_path, folder='./data'):
    """
    Reads a CSV file containing video URLs and downloads each video into the specified folder
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    df = pd.read_csv(csv_path, header=None)
    for index, row in df.iterrows():
        # assume that the URL is the only column and in valid format
        url = row[0]
        match = re.search(r'[^/]+(?=\.\w+$)', url)
        if match:
            filename = match.group(0)
        else:
            filename = "annonymous"
        filename = os.path.join(folder, f"{filename}.mp4")
        
        # download the video
        print(f"Downloading video from {url} to {filename}")
        download_video(url, filename)

if __name__ == "__main__":
    csv_path = 'group_videos.csv'
    download_videos(csv_path)
