# Importa as bibliotecas necessárias
from sklearn.datasets import load_iris  # Conjunto de dados das flores
from sklearn.model_selection import train_test_split  # Para separar treino e teste
from sklearn.neighbors import KNeighborsClassifier  # O algoritmo KNN

# 1. Carrega os dados das flores Iris
iris = load_iris()
X = iris.data  # As medidas das flores
y = iris.target  # O tipo de cada flor (como número)

#Divide os dados em treino e teste (não obrigatório para este exercício, mas é uma boa prática)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Cria o modelo KNN com 3 vizinhos
modelo_knn = KNeighborsClassifier(n_neighbors=3)

#Treina o modelo com os dados de treino
modelo_knn.fit(X_train, y_train)

#Recebe as 4 medidas do usuário
print("Digite as 4 medidas da flor (separadas por espaço):")
entrada = input().split()
entrada = [float(x) for x in entrada]  # Converte para números

#Faz a previsão usando o modelo treinado
predicao = modelo_knn.predict([entrada])[0]

#Mostra o nome da flor correspondente
nome_flor = iris.target_names[predicao]
print(f"O nome da flor é: {nome_flor}")


