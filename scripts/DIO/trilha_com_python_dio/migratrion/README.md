# 🗄️ Gerador de Migration SQL com PowerShell

Script desenvolvido em **PowerShell** para reunir vários arquivos `.sql` em um único arquivo chamado `migration.sql`.

O projeto foi criado para facilitar a organização de cargas de dados em um banco de dados, mantendo os arquivos SQL separados e organizados e, posteriormente, juntando todos eles automaticamente em um único arquivo.

---

## 📁 Estrutura do projeto

A estrutura utilizada neste projeto é:

```text
GeradorDeMigrationSQLPowerShell/
│
├── .git/
├── README
│
└── migration/
    │
    ├── schema.sql
    │
    └── seeds/
        ├── migration.sql
        ├── seed1.sql
        ├── seed2.sql
        ├── seed3.sql
        └── to_migration.ps1
```

### 📄 Arquivos

| Arquivo | Descrição |
|---|---|
| `schema.sql` | Cria o banco de dados e as tabelas |
| `seed1.sql` | Insere 50 registros de blockchains |
| `seed2.sql` | Insere 50 registros de criptomoedas |
| `seed3.sql` | Insere 100 registros de tokens |
| `to_migration.ps1` | Script PowerShell responsável por juntar os arquivos SQL |
| `migration.sql` | Arquivo final gerado pelo script |
| `README` | Documentação do projeto |

---

## 🗃️ Estrutura do banco

O arquivo `schema.sql` é responsável por criar o banco de dados e as tabelas utilizadas no projeto.

As principais tabelas são:

```text
blockchain
     │
     ├───────────────┐
     │               │
     ▼               ▼
criptomoeda        token
```

A tabela `criptomoeda` possui relacionamento com `blockchain`.

A tabela `token` também possui relacionamento com `blockchain`.

---

# 🌱 Cargas de dados

As cargas de dados foram separadas em três arquivos para facilitar a organização.

### `seed1.sql`

Responsável por inserir **50 blockchains**:

```sql
INSERT INTO blockchain
    (nome, simbolo, algoritmo_consenso, rede_principal)
VALUES
    ('Bitcoin', 'BTC', 'Proof of Work', 'Mainnet'),
    ('Ethereum', 'ETH', 'Proof of Stake', 'Mainnet'),
    ('BNB Chain', 'BNB', 'Proof of Staked Authority', 'Mainnet');
```

O arquivo possui a carga completa das 50 blockchains.

---

### `seed2.sql`

Responsável por inserir **50 criptomoedas**:

```sql
INSERT INTO criptomoeda
    (blockchain_id, nome, simbolo, casas_decimais, fornecimento_maximo)
VALUES
    (1, 'Bitcoin', 'BTC', 8, 21000000),
    (2, 'Ether', 'ETH', 18, NULL),
    (3, 'BNB', 'BNB', 18, 200000000);
```

O campo `blockchain_id` relaciona cada criptomoeda com uma blockchain cadastrada anteriormente.

Por isso, esse arquivo deve ser executado depois do `seed1.sql`.

---

### `seed3.sql`

Responsável por inserir **100 tokens**:

```sql
INSERT INTO token
    (blockchain_id, nome, simbolo, endereco_contrato, padrao, casas_decimais, fornecimento_total)
VALUES
    (2, 'USD Coin', 'USDC', '0x0000000000000000000000000000000000000001', 'ERC-20', 6, 55000000000),
    (2, 'Tether USD', 'USDT', '0x0000000000000000000000000000000000000002', 'ERC-20', 6, 120000000000),
    (2, 'Chainlink', 'LINK', '0x0000000000000000000000000000000000000003', 'ERC-20', 18, 1000000000);
```

Assim como as criptomoedas, os tokens utilizam `blockchain_id`.

Por isso, também dependem dos registros inseridos anteriormente em `seed1.sql`.

---

# 🔢 Ordem dos arquivos

A junção dos arquivos é realizada em **ordem crescente pelo nome**.

Neste projeto:

```text
seed1.sql
seed2.sql
seed3.sql
```

serão processados nesta ordem:

```text
seed1.sql
    ↓
seed2.sql
    ↓
seed3.sql
```

Essa ordem é importante.

Primeiro são inseridas as **blockchains**:

```text
seed1.sql
    ↓
50 blockchains
```

Depois são inseridas as **criptomoedas**, que utilizam `blockchain_id`:

```text
seed2.sql
    ↓
50 criptomoedas
```

Por último são inseridos os **tokens**, que também utilizam `blockchain_id`:

```text
seed3.sql
    ↓
100 tokens
```

Portanto:

```text
50 Blockchains
       ↓
50 Criptomoedas
       ↓
100 Tokens
```

---

# ▶️ Como utilizar

## 1. Clone o projeto

Primeiro, clone este projeto para o seu computador.

Depois de clonar, abra o terminal na pasta onde o projeto foi clonado.

A estrutura deverá ser semelhante a:

```text
GeradorDeMigrationSQLPowerShell/
```

---

## 2. Entre na pasta `seeds`

Acesse a pasta:

```text
migration/seeds/
```

É nessa pasta que estão os arquivos que serão reunidos pelo PowerShell:

```text
seeds/
├── migration.sql
├── seed1.sql
├── seed2.sql
├── seed3.sql
└── to_migration.ps1
```

---

## 3. Organize os arquivos SQL

Coloque dentro da pasta `seeds` os arquivos `.sql` que deseja reunir.

Neste projeto, os arquivos são:

```text
seed1.sql
seed2.sql
seed3.sql
```

O script encontrará automaticamente os arquivos com extensão `.sql`.

A ordem será definida pelo nome dos arquivos.

```text
seed1.sql
seed2.sql
seed3.sql
```

---

## 4. Abra o terminal na pasta `seeds`

No terminal, navegue até a pasta:

```text
migration/seeds/
```

Exemplo:

```powershell
cd "C:\caminho\do\projeto\migration\seeds"
```

Você pode utilizar:

```powershell
dir
```

para verificar os arquivos existentes.

O terminal deverá mostrar algo semelhante a:

```text
migration.sql
seed1.sql
seed2.sql
seed3.sql
to_migration.ps1
```

---

## 5. Execute o PowerShell

Com o terminal aberto dentro da pasta `seeds`, execute:

```powershell
.\to_migration.ps1
```

O `.\` indica ao PowerShell que o arquivo que será executado está localizado na **pasta atual**.

---

# ⚙️ O que o script faz?

O arquivo:

```text
to_migration.ps1
```

realiza automaticamente as seguintes etapas:

```text
📂 Localiza a pasta onde o script está
        ↓
📄 Define o migration.sql como arquivo de saída
        ↓
🔎 Verifica se migration.sql já existe
        ↓
🗑️ Remove o migration.sql anterior
        ↓
🔎 Localiza todos os arquivos .sql
        ↓
🔤 Ordena os arquivos pelo nome
        ↓
📖 Lê cada arquivo SQL
        ↓
➕ Adiciona o conteúdo ao migration.sql
        ↓
🔗 Adiciona GO
        ↓
✅ Finaliza a execução
```

---

# 🗄️ Resultado

Depois de executar:

```powershell
.\to_migration.ps1
```

um novo arquivo será criado:

```text
migration.sql
```

A estrutura ficará:

```text
seeds/
├── migration.sql
├── seed1.sql
├── seed2.sql
├── seed3.sql
└── to_migration.ps1
```

O arquivo `migration.sql` terá a junção dos arquivos:

```text
seed1.sql
    +
seed2.sql
    +
seed3.sql
```

---

# 🔄 Exemplo do resultado

Os arquivos originais possuem responsabilidades diferentes:

```text
seed1.sql
    ↓
50 blockchains

seed2.sql
    ↓
50 criptomoedas

seed3.sql
    ↓
100 tokens
```

Depois da execução:

```text
             ┌─────────────────┐
             │    seed1.sql    │
             │ 50 blockchains  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    seed2.sql    │
             │ 50 criptomoedas │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │    seed3.sql    │
             │   100 tokens    │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  migration.sql  │
             │ Arquivo final   │
             └─────────────────┘
```

---

# 🧹 O que acontece se `migration.sql` já existir?

Antes de gerar o novo arquivo, o script verifica:

```powershell
if (Test-Path $outputFile)
```

Se o arquivo existir, ele será removido:

```powershell
Remove-Item $outputFile
```

Depois disso, um novo `migration.sql` será criado.

Isso evita que os dados da execução anterior sejam adicionados novamente.

---

# ➕ O que significa `-Append`?

O parâmetro:

```powershell
-Append
```

faz com que o conteúdo seja adicionado ao final do arquivo.

Por exemplo:

```text
seed1.sql
    ↓
migration.sql

seed2.sql
    ↓
adiciona ao final

seed3.sql
    ↓
adiciona ao final
```

Dessa forma, o conteúdo dos arquivos é reunido em um único arquivo.

---

# 🔗 Separação com `GO`

Após cada arquivo SQL, o script adiciona:

```text
GO
```

Assim, o `migration.sql` possui uma separação entre os conteúdos dos arquivos.

O resultado segue aproximadamente esta estrutura:

```sql
-- Conteúdo do seed1.sql

INSERT INTO blockchain (...);

GO

-- Conteúdo do seed2.sql

INSERT INTO criptomoeda (...);

GO

-- Conteúdo do seed3.sql

INSERT INTO token (...);

GO
```

> ⚠️ **Observação:** `GO` não é um comando SQL nativo do MariaDB. Ele é utilizado como separador de lotes principalmente em ferramentas relacionadas ao SQL Server. Caso o arquivo `migration.sql` seja executado diretamente no MariaDB, é necessário verificar se a ferramenta utilizada aceita esse separador.

---

# 🎯 Objetivo do projeto

O objetivo deste projeto é automatizar a criação de um arquivo único de carga SQL.

Em vez de manter todos os `INSERTs` em um único arquivo grande, os dados são separados:

```text
seed1.sql
→ Blockchains

seed2.sql
→ Criptomoedas

seed3.sql
→ Tokens
```

Depois, o PowerShell reúne tudo:

```text
seed1.sql
      +
seed2.sql
      +
seed3.sql
      ↓
migration.sql
```

Dessa forma, os arquivos permanecem organizados e o processo de criação da migration é automatizado.

---

# 🧠 Conceitos utilizados

Este projeto utiliza conceitos de:

### PowerShell

- Variáveis
- `if`
- `foreach`
- `Get-ChildItem`
- `Get-Content`
- `Out-File`
- `Test-Path`
- `Remove-Item`
- `Join-Path`
- `Sort-Object`
- `Write-Host`
- `-Append`

### Banco de dados

- SQL
- `INSERT`
- Chaves primárias
- Chaves estrangeiras
- Relacionamentos
- Carga de dados
- Organização de migrations

---

# 🚀 Resumo

Para utilizar o projeto:

```powershell
cd "caminho\do\projeto\migration\seeds"
```

Depois:

```powershell
.\to_migration.ps1
```

O resultado será:

```text
seed1.sql
    ↓
50 blockchains

seed2.sql
    ↓
50 criptomoedas

seed3.sql
    ↓
100 tokens

        ↓

migration.sql
```

Assim, o PowerShell automatiza a união das cargas SQL em um único arquivo.