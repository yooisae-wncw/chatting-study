import socket # socket을 사용하기 때문에 socket 패키지 import
from threading import Thread # socket accept하는 것과 메시지를 받는 것을 동시에 하기 위해서 thread 사용

class ChatServer:
    # server 초기 설정
    def __init__(self, port) -> None:
        # 서버의 ip주소와 port번호
        self.host = "0.0.0.0"
        self.port = port

        # 클라이언트 소켓을 저장할 리스트
        # 채팅방에 들어와있는 클라이언트 목록
        self.client_sockets = []

        self.s = socket.socket()
        # 재사용 가능한 주소로 설정
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.s.bind((self.host, self.port))
        self.s.listen()
        print(f'[*] {self.host}:{self.port} 주소에서 통신 대기중...')

    def communication_with_client(self, cs):
        while True:
            try:
                message = cs.recv(1024).decode()
            except Exception as e:
                print(f"[!] 에러발생: {e}")
                break
            else:
                for client_socket in self.client_sockets:
                    if cs != client_socket:
                        client_socket.send(message.encode())

    def serve(self):
        while True:
            client_socket, client_address = self.s.accept()
            print(f'[*] 연결완료: {client_address}')
            self.client_sockets.append(client_socket)
            t = Thread(target=self.communication_with_client, args=[client_socket], daemon=True)
            t.start()

        for cs in client_sockets:
            cs.close()

        s.close()
