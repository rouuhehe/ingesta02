import boto3

ficheroUpload = "data.csv"
nombreBucket = "yarii123-storage-s2"

"""
# Conectando a la bd
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123",
    database="prueba"
)

cursor = conn.cursor()

# Leyendo datos de la bd 

query = "SELECT * FROM abogados"
cursor.execute(query)
result = cursor.fetchall()

# convirtiendo a dataframe en csv
df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])
df.to_csv(ficheroUpload, index=False)

# guardando en local
print(f"Fichero {ficheroUpload} creado correctamente")
"""

s3 = boto3.client('s3')
s3.upload_file(ficheroUpload, nombreBucket, f'ingesta2/{ficheroUpload}')


print("Ingesta completada")