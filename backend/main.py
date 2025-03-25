from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

df = pd.read_csv(
    '/home/malcolnlmr/git/teste-de-nivelamento/data_sample/Relatorio_cadop.csv',
    sep=';',
    encoding='utf-8'
    )

@app.get("/search")
async def search(q: str = Query(...)):
    query = q.lower()
   

    # Filtrar registros que contenham o texto na Razão Social ou Nome Fantasia
    results = df[
        df['Razao_Social'].str.lower().str.contains(query) |
        df['Nome_Fantasia'].str.lower().str.contains(query)
    ]

    results = results.fillna('')

    # Retornar os 10 primeiros resultados
    return results.head(10).to_dict(orient='records')
