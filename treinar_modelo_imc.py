"""
Script para treinar modelo de classificação de obesidade - Versão Corrigida
"""

import csv
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def criar_dados():
    dados = [
        [18.5, False], [22.0, False], [24.9, False],
        [25.5, False], [27.3, False], [28.7, False],
        [29.1, False], [30.0, True], [32.5, True],
        [35.8, True], [40.2, True], [45.0, True]
    ]
    
    with open('dados_imc.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['imc', 'obeso'])
        writer.writerows(dados)

def treinar_modelo():
    try:
        df = pd.read_csv('dados_imc.csv')
        X = df[['imc']]
        y = df['obeso']
        
        modelo = LogisticRegression()
        modelo.fit(X, y)
        
        acc = accuracy_score(y, modelo.predict(X))
        print(f"Modelo treinado com precisão de {acc:.1%}")
        
        joblib.dump(modelo, 'modelo_imc.pkl')
        print("Modelo salvo com sucesso!")
        
    except Exception as e:
        print(f"ERRO no treinamento: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("Criando dados de treinamento...")
    criar_dados()
    
    print("\nTreinando modelo...")
    if treinar_modelo():
        print("\nProcesso concluído com sucesso!")
    else:
        print("\nFalha no treinamento do modelo")