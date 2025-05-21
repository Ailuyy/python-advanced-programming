import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    DATASET = 'piotrstefaskiue/poland-vehicle-license-plate-dataset'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        DATASET,
        path=data_dir,
        unzip=True
    )
    print('Data has been downloaded and extracted')

if __name__ == '__main__':
    download_dataset()