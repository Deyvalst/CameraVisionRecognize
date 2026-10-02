import socket
import datetime
# import io

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
# server_socket.bind(("100.115.41.45", 2222))
server_socket.bind(("192.168.88.248", 36273))

print(f"server launched")

while True:
    try:
        data, addr = server_socket.recvfrom(65536)

        print("recieved:",str(data),", from ",str(addr));

        response = str(datetime.datetime.now()).encode('utf-8')
        
        # Отправляем результат обратно клиенту по UDP
        print(server_socket.sendto(response, addr))
    except Exception as e:
        # Если пакет пришел битым или неполным, просто пропускаем его
        print(f"Ошибка обработки пакета: {e}")





# import socket
# import io
# import torch
# import torchvision.transforms as transforms
# from PIL import Image
# from torchvision.models import resnet18, ResNet18_Weights

# # 1. Настройка сокета
# UDP_IP = "0.0.0.0"
# UDP_PORT = 5005

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # Увеличиваем размер системного буфера, чтобы операционная система не теряла пакеты
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65536)
# server_socket.bind((UDP_IP, UDP_PORT))

# print(f"UDP CV сервер запущен на {UDP_IP}:{UDP_PORT}...")

# # 2. Инициализация модели CV
# weights = ResNet18_Weights.DEFAULT
# model = resnet18(weights=weights).eval()
# categories = weights.meta["categories"]

# transform = transforms.Compose([
#     transforms.Resize(256),
#     transforms.CenterCrop(224),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# ])

# # 3. Бесконечный цикл обработки входящих кадров
# while True:
#     try:
#         # Получаем данные (максимальный размер UDP пакета)
#         data, addr = server_socket.recvfrom(65536)
        
#         # Декодируем JPEG из байт-потока в PIL Image
#         image = Image.open(io.BytesIO(data)).convert("RGB")
        
#         # Подготовка тензора
#         tensor = transform(image).unsqueeze(0)
        
#         # Инференс
#         with torch.no_grad():
#             outputs = model(tensor)
#             probabilities = torch.nn.functional.softmax(outputs, dim=0)
            
#         conf, class_id = torch.max(probabilities, dim=0)
#         label = categories[class_id.item()]
        
#         # Формируем компактный текстовый ответ
#         response = f"{label}:{conf.item():.4f}".encode('utf-8')
        
#         # Отправляем результат обратно клиенту по UDP
#         server_socket.sendto(response, addr)
        
#     except Exception as e:
#         # Если пакет пришел битым или неполным, просто пропускаем его
#         print(f"Ошибка обработки пакета: {e}")
