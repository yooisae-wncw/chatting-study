from .client import ChatClient
from .server import ChatServer
import sys

HELP_MESSAGE = """사용법: __main__.py COMMAND

COMMANDs:
    serve   특정 포트로 채팅 서버를 엽니다. 사용법: __main__.py serve [PORT] 로 실행하세요.
        PORT:   서버에서 사용 할 port 입니다.
    connect 채팅 서버로 연결합니다. __main__.py connect [IP] [PORT] [NAME] 으로 실행하세요.
        IP:     연결 할 서버의 IP입니다.
        PORT:   연결 할 서버의 port입니다.
        NAME:   채팅에서 사용 할 이름입니다.
    help    이 메시지를 출력합니다.
"""

def main():
    if len(sys.argv) < 2:
        sys.stderr.write(HELP_MESSAGE)
        return
    
    if sys.argv[1] == 'serve':
        if len(sys.argv) == 3:
            port = int(sys.argv[2])
            server = ChatServer(port)
            server.serve()
        else:
            sys.stderr.write("사용법: __main__.py serve [PORT]\n")

    elif sys.argv[1] == 'connect':
        if len(sys.argv) == 5 or len(sys.argv) == 4:
            ip = sys.argv[2]
            port = int(sys.argv[3])
            # 채팅 아이디를 정하지 않았을 경우
            if len(sys.argv) == 4:
                client = ChatClient(ip, port)
            # 채팅 아이디를 입력했을 경우
            elif len(sys.argv) == 5:
                name = sys.argv[4]
                client = ChatClient(ip, port, name)
            client.connect()

        else:
            sys.stderr.write("사용법: __main__.py connect [IP] [PORT] [NAME]\n")

    elif sys.argv[1] == 'help':
        sys.stderr.write(HELP_MESSAGE)

    else: 
        sys.stderr.write("사용법: __main__.py [COMMAND]\n")
        sys.stderr.write("COMMAND: serve, connect, help\n")

if __name__ == '__main__':
    main()