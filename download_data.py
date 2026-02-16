import os
import subprocess
import zipfile

DATASET = "zynicide/wine-reviews"
DOWNLOAD_FOLDER = "downloads"
EXTRACT_FOLDER = "data"


def create_folders():
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(EXTRACT_FOLDER, exist_ok=True)


def download_dataset():
    print("Downloading dataset from Kaggle...")

    subprocess.run([
        "kaggle", "datasets", "download",
        "-d", DATASET,
        "-p", DOWNLOAD_FOLDER
    ], check=True)


def extract_zip():
    for file in os.listdir(DOWNLOAD_FOLDER):
        if file.endswith(".zip"):
            zip_path = os.path.join(DOWNLOAD_FOLDER, file)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(EXTRACT_FOLDER)

            print(f"Extracted: {file}")


def main():
    create_folders()
    download_dataset()
    extract_zip()
    print("Data pipeline completed!")


if __name__ == "__main__":
    main()
