import socket
import threading

# Função para lidar com a conexão do cliente
def handle_client(client_socket):
    # Recebe os dados do cliente
    request = client_socket.recv(1024)
    
    # Imprime a solicitação HTTP recebida do cliente
    print("[*] Received request:")
    print(request)
    
    # Modifique a requisição conforme necessário (por exemplo, pode-se filtrar ou alterar URLs)
    
    # Estabelece uma conexão com o servidor de destino
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('www.google.com', 80))  # Altere para o host e porta do servidor de destino
    
    # Encaminha a solicitação para o servidor de destino
    server_socket.send(request)
    
    # Recebe a resposta do servidor de destino
    response = server_socket.recv(1024)
    
    # Imprime a resposta recebida do servidor de destino
    print("[*] Received response:")
    print(response)
    
    # Envia a resposta de volta para o cliente
    client_socket.send(response)
    
    # Fecha as conexões
    client_socket.close()
    server_socket.close()

# Função principal para iniciar o servidor proxy
def start_proxy_server():
    # Cria um socket TCP/IP
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket à porta local 8888
    proxy_socket.bind(('127.0.0.1', 8888))
    
    # Coloca o socket em modo de escuta
    proxy_socket.listen(5)
    
    print("[*] Proxy server is listening on port 8888")
    
    while True:
        # Aguarda por conexões dos clientes
        client_socket, addr = proxy_socket.accept()
        
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        
        # Cria uma thread para lidar com a conexão do cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Inicia o servidor proxy
if __name__ == "__main__":
    start_proxy_server()
