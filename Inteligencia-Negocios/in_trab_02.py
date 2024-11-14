# -*- coding: utf-8 -*-
"""IN_TRAB_02

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V3A9e0-d5X72fsp97lJmOjQ3-nsKxjb5
"""

!pip install graphviz

"""####@Imports"""

import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics


import graphviz
import pydot

"""####@Estabelecendo conexão com a Base de Dados"""

dermatologyDb = pd.read_csv('dermatology.data');
#dermatologyDb

"""####**@Pré Processamento**"""

#Informação do dataset
dermatologyDb.info()

dermatologyDb

#Removendo Idade fora do range e removendo strings da Idade.
dbAux = dermatologyDb[dermatologyDb["age"]!= "?"]
dbAux.fillna(method='bfill')
dermatologyDb.age.replace({"?":int(dbAux.age.median())},inplace = True)

#Removendo Idade fora do range e removendo strings da Idade.

#Verificação de Propriedades
dermatologyDb.describe()

#Removendo todos nulos
dermatologyDb.dropna()

"""####@Aplicação da Ávore de decisão"""

x_train, x_test, y_train, y_test = train_test_split (dermatologyDb.drop('family history', axis = 1), dermatologyDb['family history'], test_size  = 0.3)

x_train.shape, x_test.shape

y_test.shape, y_test.shape

modeloClassificador = DecisionTreeClassifier(max_depth = None,
                                  max_features = None,
                                  criterion = 'entropy',
                                  min_samples_leaf = 1,
                                  min_samples_split = 2
                                  )

modeloClassificador_2 = DecisionTreeClassifier(max_depth = None,
                                  max_features = None,
                                  criterion = 'gini',
                                  min_samples_leaf = 1,
                                  min_samples_split = 2
                                  )

"""--Treinando o modelo"""

test_model_1 = modeloClassificador.fit(x_train, y_train)

test_model_2 = modeloClassificador_2.fit(x_train, y_train)

"""--Resultado do teinamento"""

resultado = test_model_1.predict(x_test)

resultado

resultado_2 = test_model_2.predict(x_test)

resultado_2

print (metrics.classification_report(y_test, resultado))

print (metrics.classification_report(y_test, resultado_2))

"""--Exibindo árvore"""

dot_data = export_graphviz(
    test_model_1,
    out_file = None,
    feature_names = dermatologyDb.drop('family history', axis = 1).columns,
    class_names = ['0', '1'],
    filled = True,
    rounded = True,
    proportion = True,
    node_ids = True,
    rotate = True,
    label = 'all',
    special_characters = True)

graph = graphviz.Source(dot_data)

graph