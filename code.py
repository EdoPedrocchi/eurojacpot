import pandas as pd

def crea_dataset_eurojackpot():
    data = {
        "Data": [
            "4 marzo 2025", "28 febbraio 2025", "25 febbraio 2025", "21 febbraio 2025",
            "18 febbraio 2025", "14 febbraio 2025", "11 febbraio 2025", "7 febbraio 2025",
            "4 febbraio 2025", "31 gennaio 2025", "28 gennaio 2025", "24 gennaio 2025",
            "21 gennaio 2025", "17 gennaio 2025", "14 gennaio 2025", "10 gennaio 2025",
            "7 gennaio 2025", "3 gennaio 2025", "31 dicembre 2024", "27 dicembre 2024", "24 dicembre 2024", 
            "20 dicembre 2024", "17 dicembre 2024", "13 dicembre 2024", "10 dicembre 2024", "6 dicembre 2024", 
            "3 dicembre 2024", "29 novembre 2024", "26 novembre 2024", "22 novembre 2024", "19 novembre 2024", 
            "15 novembre 2024", "12 novembre 2024", "15 ottobre 2024", "11 ottobre 2024", "8 ottobre 2024", 
            "4 ottobre 2024", "1 ottobre 2024", "27 settembre 2024", "24 settembre 2024", "20 settembre 2024", 
            "17 settembre 2024", "13 settembre 2024", "10 settembre 2024", "6 settembre 2024", "3 settembre 2024"
        ],
        "Primo numero": [4, 3, 7, 1, 6, 2, 8, 5, 3, 10, 1, 2, 7, 2, 9, 17, 3, 5, 2, 1, 9, 1, 11, 1, 17, 8, 7, 10, 20, 6, 4, 27, 2, 9, 8, 13, 4, 17, 6, 3, 9, 1, 2, 7, 7, 5],
        "Secondo numero": [12, 4, 14, 11, 13, 9, 16, 14, 12, 20, 15, 9, 14, 16, 11, 34, 4, 12, 21, 9, 15, 3, 14, 4, 23, 14, 20, 19, 21, 10, 7, 31, 3, 20, 11, 29, 16, 37, 15, 13, 17, 3, 3, 10, 11, 17],
        "Terzo numero": [35, 13, 22, 21, 25, 17, 24, 23, 22, 30, 27, 16, 22, 23, 25, 38, 13, 22, 26, 25, 28, 10, 18, 19, 30, 45, 23, 24, 28, 30, 19, 35, 34, 38, 23, 42, 27, 42, 25, 34, 19, 13, 17, 31, 27, 23],
        "Quarto numero": [37, 20, 29, 31, 36, 28, 33, 32, 28, 40, 35, 46, 33, 40, 32, 42, 20, 28, 34, 27, 36, 32, 35, 35, 41, 47, 24, 25, 32, 34, 26, 46, 38, 44, 44, 44, 34, 45, 29, 41, 26, 24, 40, 41, 42, 36],
        "Quinto numero": [48, 21, 35, 41, 44, 35, 42, 41, 47, 50, 44, 47, 45, 50, 44, 48, 21, 47, 49, 37, 39, 44, 42, 42, 43, 50, 37, 40, 37, 41, 27, 50, 49, 45, 45, 48, 44, 50, 41, 43, 39, 44, 44, 46, 45, 37],
        "Primo Euronumero": [4, 8, 5, 2, 4, 3, 7, 6, 1, 5, 4, 3, 6, 3, 5, 2, 8, 1, 7, 6, 6, 1, 4, 1, 4, 2, 4, 5, 1, 7, 4, 3, 10, 4, 10, 2, 4, 6, 1, 1, 4, 11, 4, 1, 3, 5],
        "Secondo Euronumero": [10, 12, 11, 8, 9, 10, 12, 11, 12, 10, 7, 9, 11, 9, 10, 11, 12, 12, 12, 8, 7, 8, 11, 3, 11, 12, 10, 9, 5, 10, 5, 10, 11, 12, 12, 8, 7, 7, 3, 5, 10, 12, 8, 5, 10, 9]
    }
    
    df = pd.DataFrame(data)
    file_path = "eurojackpot_2024_2025.xlsx"
    df.to_excel(file_path, index=False)
    print(f"File salvato: {file_path}")

if __name__ == "__main__":
    crea_dataset_eurojackpot()
