import tabula, os

def extract_data(filename, file_folder="download_pdf", save_folder="extracted_data", auto_save=False):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)

    file = os.path.join(file_folder, os.path.basename(filename))

    df = tabula.read_pdf(file, pages='3-181', multiple_tables=False, output_format="dataframe")[0]

    df.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}, inplace=True)

    if auto_save:
        save_df_to_csv_compressed(df, "Teste_Malcoln_Lucas.csv.zip", save_folder)
    else:
        return df

def save_df_to_csv_compressed(df, filename, save_folder="extracted_data"):
    if not os.path.exists(save_folder) and not save_folder == ".":
        os.makedirs(save_folder)

    df.to_csv(os.path.join(save_folder, filename), index=False, compression="zip")

if __name__ == "__main__":
    extract_data("Anexo_I.pdf", auto_save=True)