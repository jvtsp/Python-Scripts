# Hoster Toaster

Script em Python para gerenciar arquivos de hosts locais.

## Descrição
O `hoster-toaster.py` é uma ferramenta para atualizar ou sobrescrever entradas em arquivos de hosts. Foi desenvolvido para facilitar a gestão de resoluções de nomes locais.

## Funcionalidades
- **Modo Sobrescrever**: Substitui todo o conteúdo do arquivo de hosts alvo pelo conteúdo de um arquivo fornecido.
- **Modo Atualizar (-s)**: Lê um arquivo de entrada formatado e atualiza ou insere entradas específicas (IP e Hostname).

## Como Usar

### Pré-requisitos
- Python 3 instalado.

### Execução

O script opera sobre o arquivo definido na variável `hosts_file` (padrão: `hosts_test`).

#### 1. Adicionar ou Atualizar entradas
Para processar um arquivo com lista de IPs e Hostnames:

```bash
python hoster-toaster.py <arquivo_entrada> -s
```

**Formato do arquivo de entrada:**
O arquivo deve conter linhas no formato `IP:HOSTNAME`.

Exemplo:
```text
1.1.1.1:exemplo.com
127.0.0.1:meulocalhost.test
```

#### 2. Sobrescrever arquivo
Para substituir o conteúdo do arquivo de hosts pelo conteúdo de outro arquivo:

```bash
python hoster-toaster.py <arquivo_origem>
```

## Estrutura do Projeto
- `hoster-toaster.py`: Script principal.
- `hosts_test`: Arquivo alvo de modificação (usado para testes).
- `dns.txt`, `dns_novo`: Exemplos de arquivos de entrada.

## Autor
- **Renata Dos Santos**
- Data: 08/01/2022
