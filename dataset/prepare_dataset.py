import os
import random
import shutil

# Directorio de entrada (dataset original)
input_dir = 'dataset/UoM_SignatureHwNameDateLocation_169_augmented_doc'

# Directorio de salida
output_dir = 'dataset/UoM_SignatureHwNameDateLocation_169_augmented_doc_yolo'

# Porcentaje de datos para entrenamiento
train_percentage = 90

# Crear la estructura de directorios de salida
os.makedirs(os.path.join(output_dir, 'images', 'train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'images', 'valid'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'labels', 'train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'labels', 'valid'), exist_ok=True)

# Obtener la lista de archivos de entrada
input_files = os.listdir(input_dir)

# Filtrar los archivos de imágenes
image_files = [file for file in input_files if file.endswith('.jpg')]

# Asegurar que los datos estén equiespaciados
num_files = len(image_files)
split_index = int(num_files * train_percentage / 100)
step = num_files // split_index

# Ordenar la lista de archivos
image_files.sort()

# Generar una lista de índices equiespaciados
indices = list(range(0, num_files, step))

# Elegir índices equiespaciados para el conjunto de entrenamiento
train_indices = random.sample(indices, split_index)

# Construir listas de archivos para entrenamiento y validación
train_image_files = [image_files[i] for i in train_indices]
valid_image_files = [image_files[i] for i in range(num_files) if i not in train_indices]

# Copiar archivos de imágenes de entrenamiento y validación y sus respectivas etiquetas
for img_file in train_image_files:
    img_path = os.path.join(input_dir, img_file)
    label_file = img_file.replace('.jpg', '.txt')
    label_path = os.path.join(input_dir, label_file)

    shutil.copy(img_path, os.path.join(output_dir, 'images', 'train', img_file))
    shutil.copy(label_path, os.path.join(output_dir, 'labels', 'train', label_file))

for img_file in valid_image_files:
    img_path = os.path.join(input_dir, img_file)
    label_file = img_file.replace('.jpg', '.txt')
    label_path = os.path.join(input_dir, label_file)

    shutil.copy(img_path, os.path.join(output_dir, 'images', 'valid', img_file))
    shutil.copy(label_path, os.path.join(output_dir, 'labels', 'valid', label_file))

# Copiar el archivo clases.txt a la carpeta de etiquetas
shutil.copy(os.path.join(input_dir, 'classes.txt'), os.path.join(output_dir, 'labels', 'classes.txt'))

print("Proceso completado.")
