import cv2
from deepface import DeepFace
import os 

path = os.listdir()

for file in path:
    if 'jpg' in file:
        # ler a nossa imagem
        image = cv2.imread(file)

        # passa r a imagem para a deepfacce 
        result = DeepFace.analyze(image, actions=('emotion', 'gender'))

        # ver resultado 
        print('-'*10)
        print(f'emotion: {result[0]["dominant_emotion"]} \ngender: { result[0]["dominant_gender"]}')
