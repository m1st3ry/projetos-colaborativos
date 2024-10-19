# Importa a biblioteca necessária para testar a velocidade da internet
import speedtest

# Função principal para testar a velocidade da internet
def testar_velocidade_internet():
    # Cria uma instância do Speedtest
    st = speedtest.Speedtest()

    # Seleciona o melhor servidor para realizar o teste
    print("Testando servidores...")
    st.get_best_server()

    # Testa a velocidade de download (em Mbps)
    print("Medindo velocidade de download...")
    download_speed = st.download() / 1_000_000  # Convertendo para Mbps

    # Testa a velocidade de upload (em Mbps)
    print("Medindo velocidade de upload...")
    upload_speed = st.upload() / 1_000_000  # Convertendo para Mbps

    # Testa o ping (em milissegundos)
    print("Medindo ping...")
    ping = st.results.ping

    # Exibe os resultados no console
    print(f"Velocidade de Download: {download_speed:.2f} Mbps")
    print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

# Verifica se o script está sendo executado diretamente para chamar a função
if __name__ == "__main__":
    testar_velocidade_internet()
