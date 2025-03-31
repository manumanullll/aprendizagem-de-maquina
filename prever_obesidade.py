"""
Script para prever obesidade baseada em IMC - Versão Corrigida
"""

import joblib
import pandas as pd
import sys

class ClassificadorIMC:
    def __init__(self):
        try:
            self.modelo = joblib.load('modelo_imc.pkl')
        except FileNotFoundError:
            print("ERRO: Modelo não encontrado. Execute primeiro 'treinar_modelo_imc.py'")
            sys.exit(1)
        except Exception as e:
            print(f"ERRO ao carregar modelo: {str(e)}")
            sys.exit(1)

    def prever(self, valor_imc):
        try:
            imc = float(valor_imc)
            if imc <= 0:
                return None, "ERRO: IMC deve ser positivo"
            
            dados = pd.DataFrame([[imc]], columns=['imc'])
            proba = self.modelo.predict_proba(dados)[0][1]
            predicao = self.modelo.predict(dados)[0]
            
            return predicao, proba
            
        except ValueError:
            return None, "ERRO: Digite um número válido"
        except Exception as e:
            return None, f"ERRO: {str(e)}"

def mostrar_resultado(imc, resultado):
    if resultado[0] is not None:
        status = "Obeso" if resultado[0] else "Não obeso"
        print(f"IMC {imc:.1f}: {status} (Probabilidade: {resultado[1]:.1%})")
    else:
        print(resultado[1])

if __name__ == "__main__":
    try:
        classificador = ClassificadorIMC()
        testes = [5.0, 10.5, 20.0, 32.0, 65.0, "abc", -2, 28.5]
        
        print("\nRESULTADOS DA CLASSIFICAÇÃO:\n")
        for valor in testes:
            resultado = classificador.prever(valor)
            mostrar_resultado(valor, resultado)
            
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"\nERRO CRÍTICO: {str(e)}")
        sys.exit(1)