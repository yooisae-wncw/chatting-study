import socket
from threading import Thread

class ChatClient:
    def __init__(self, host, port, name='익명') -> None:
        # 연결 할 server의 주소와 port를 지정
        self.host = host
        self.port = port
        self.name = name

        # 통신을 위해서 socket을 생성
        self.s = socket.socket()
        print(f'[*] {host}:{port} 로 연결시도중...')

        # 서버와 연결을 시도
        self.s.connect((host, port))
        print('[+] 연결 완료')

    def communication_with_server(self):
        while True:
            message = self.s.recv(1024).decode()
            print(message)

    def connect(self):
        t = Thread(target=self.communication_with_server, daemon=True)
        t.start()  

        while True:
            message = input()
            message = f"{self.name}: {message}"
            # 내가 입력한 message를 encoding해서 서버에게 전송
            self.s.send(message.encode())

        self.s.close()
