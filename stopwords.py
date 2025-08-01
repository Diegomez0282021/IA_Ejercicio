import nltk 

# Desde NLTK, importamos las stopwords que son las palabras comunes en un idioma
from nltk.corpus import stopwords

# Descargamos la lista de palabras vacías stopwords sino está disponible en nuestra computadora
nltk.download('stopwords')

# Guardar en una variable la lista de stopwords en español
lista_de_stopwords = stopwords.words('spanish')

# Imprimir la lista de stopwords
print(lista_de_stopwords)