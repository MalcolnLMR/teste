import csv
import os, requests, zipfile, pandas as pd

def download_data():
    for i in range(1, 5):
        download_resource(f"https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2023/{i}T2023.zip", "download_data", f"{i}T2023.zip")
        with zipfile.ZipFile(f"download_data/{i}T2023.zip", 'r') as zip_ref:
            zip_ref.extractall("download_data")
        os.remove(f"download_data/{i}T2023.zip")

        download_resource(f"https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2024/{i}T2024.zip", "download_data", f"{i}T2024.zip")
        with zipfile.ZipFile(f"download_data/{i}T2024.zip", 'r') as zip_ref:
            zip_ref.extractall("download_data")
        os.remove(f"download_data/{i}T2024.zip")
    
    download_resource("https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv", "download_data", "Relatorio_cadop.csv")
    
    os.rename("download_data/2t2023.csv", "download_data/2T2023.csv")

def download_resource(url, save_folder=".", filename="downloaded_file"):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)

    response = requests.get(url)
    if response.status_code == 200:

        file = os.path.join(save_folder, os.path.basename(filename))

        if os.path.isdir(file):
            file = os.path.join(file, "downloaded_file")

        with open(file, 'wb') as file:            
            file.write(response.content)

    else:
        return None

def merge_data(save_folder="data_sample"):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)

    data_dir = os.path.join(os.path.abspath(''), "download_data")
    
    file_list = os.listdir(data_dir)
    file_list.sort()        

    data_frames = []
    for file in file_list[:-1:]:
        df = pd.read_csv(os.path.join(data_dir, file), sep=";", decimal=",", parse_dates=True)
        
        if 'DATA' in df.columns and file == "4T2023.csv": 
            df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True, errors='coerce')
        
        data_frames.append(df)

    
    merged_df = pd.concat(data_frames, ignore_index=True)
    
    merged_df.to_csv(os.path.join(save_folder, "merged_data.csv"), index=False, sep=";", encoding="utf-8", quoting=csv.QUOTE_NONNUMERIC)

if __name__ == "__main__":
    #download_data()
    merge_data()
    