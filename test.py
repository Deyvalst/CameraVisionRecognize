import socket
import sys
import ctypes
UDP_IP = input()
UDP_PORT = 36273

if UDP_IP == "host":
    UDP_IP = "100.115.41.45"
if UDP_IP == "user":
    UDP_IP = "172.31.112.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Устанавливаем таймаут, чтобы клиент не завис навсегда, если пакет потеряется
client_socket.settimeout(5.0) 
handle = client_socket.fileno()
if True:
    # Константы для Windows API
    SIO_UDP_CONNRESET = 0x9800000C
    dwBytesReturned = ctypes.c_ulong()
    bNewBehavior = ctypes.c_bool(False)
    
    # Вызываем WSAIoctl напрямую из системной библиотеки WS2_32.dll
    windll = ctypes.windll.ws2_32
    result = windll.WSAIoctl(
        handle, 
        SIO_UDP_CONNRESET, 
        ctypes.byref(bNewBehavior), 
        ctypes.sizeof(bNewBehavior), 
        None, 
        0, 
        ctypes.byref(dwBytesReturned), 
        None, 
        None
    )

# Читаем локальное изображение (или кадр с веб-камеры)
# image = cv2.imread("test_image.jpg")

# ВАЖНО: сжимаем изображение в JPEG, чтобы оно уместилось в один UDP пакет (<65 КБ)
# Для нейросети 224x224 этого качества (80%) хватит с запасом
# encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
# result, encoded_img = cv2.imencode('.jpg', image, encode_param)
result = True
if result:
    # Превращаем в байты и отправляем
    # byte_data = encoded_img.tobytes()
    # print(f"Отправка кадра размером {len(byte_data)} байт...")
    
    client_socket.sendto("hello world".encode('utf-8'), (UDP_IP, UDP_PORT))
    
    try:
        # Ждем ответ от сервера
        response, server = client_socket.recvfrom(1024)
        print(f"Ответ сервера: {response.decode('utf-8')}")
    except socket.timeout:
        print("Превышено время ожидания ответа (пакет потерялся)")
