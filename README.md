# 💰 Prada - Educadora Financeira Virtual

⚠️ **PROJETO DE TESTE E ESTUDO**

Este é um projeto desenvolvido para fins educacionais e de experimentação. Serve como prototipagem e teste de conceitos de IA aplicados à educação financeira. Não deve ser utilizado em ambientes de produção.

---

Uma aplicação inteligente de educação financeira que utiliza IA para ensinar conceitos de finanças pessoais de forma prática e acessível.

## 📋 Sobre o Projeto

**Prada** é uma educadora financeira virtual baseada em IA que fornece orientações personalizadas sobre educação financeira. A aplicação analisa o perfil financeiro do usuário (Ka) e oferece explicações didáticas sobre conceitos de finanças, mercado e gestão de recursos.

### Características Principais

- 🤖 **IA Conversacional**: Integração com Ollama (modelo Phi) para respostas naturais
- 👤 **Perfil Personalizado**: Análise de dados financeiros individuais (renda, patrimônio, objetivos)
- 💬 **Chat Interativo**: Interface amigável em Streamlit para perguntas e respostas
- 📊 **Contexto Inteligente**: Utiliza histórico de transações e atendimentos para personalizar respostas
- 🔒 **Educação Segura**: Foca em educação financeira, nunca recomenda investimentos específicos

## 🎯 Objetivo

Democratizar o acesso a conhecimento financeiro, ajudando usuários a:

- Compreender conceitos de economia pessoal
- Aprender sobre mercado financeiro
- Construir reserva de emergência
- Tomar decisões financeiras mais informadas

## 📦 Requisitos do Sistema

- Python 3.8+
- Ollama (para executar modelos de IA localmente)
- Conexão de internet (para primeira configuração)

### Dependências Python

```
streamlit>=1.0.0
pandas>=1.3.0
requests>=2.26.0
```

## 🚀 Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/projeto_ia_prada.git
cd projeto_ia_prada
```

### 2. Instale as Dependências Python

```bash
pip install -r requirements.txt
```

### 3. Instale e Configure o Ollama

- Baixe Ollama em: https://ollama.ai
- Instale seguindo as instruções do seu sistema operacional
- Cole o modelo Phi:

```bash
ollama pull phi
```

**Nota:** O modelo Phi ocupa ~1.6 GB de espaço em disco

### 4. Initialize o Servidor Ollama

Em um terminal separado:

```bash
ollama serve
```

O servidor rodará em `http://localhost:11434`

### 5. Execute a Aplicação

```bash
streamlit run src/app.py
```

A aplicação abrirá em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
projeto_ia_prada/
├── data/
│   ├── perfil_investidor.json          # Perfil financeiro do cliente
│   ├── transacoes.csv                  # Histórico de transações
│   ├── historico_atendimento.csv       # Registro de atendimentos anteriores
│   └── produtos_financeiros.json       # Produtos e serviços disponíveis
├── src/
│   └── app.py                          # Aplicação principal Streamlit
├── README.md                           # Este arquivo
├── requirements.txt                    # Dependências do projeto
└── .gitignore                          # Arquivos ignorados no Git
```

## ⚙️ Configuração

### Arquivos de Dados

#### `perfil_investidor.json`

Contém informações do cliente:

```json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [...]
}
```

#### `transacoes.csv`

Histórico de transações financeiras do cliente

#### `historico_atendimento.csv`

Registro de consultas e atendimentos anteriores

#### `produtos_financeiros.json`

Catálogo de produtos e serviços financeiros disponíveis

### Variáveis de Configuração (src/app.py)

```python
OLLAMA_URL = 'http://localhost:11434/api/generate'  # Endpoint do Ollama
MODELO = 'phi'                                       # Modelo de IA a usar
```

## 💬 Como Usar

1. **Inicie a aplicação** seguindo os passos de instalação
2. **Acesse** `http://localhost:8501` no navegador
3. **Digite sua pergunta** na caixa de chat
4. **Receba respostas personalizadas** baseadas no seu perfil financeiro

### Exemplos de Perguntas

- "Como construir uma reserva de emergência?"
- "Qual é a diferença entre ações e títulos?"
- "Como posso aumentar minha renda mensal?"
- "Qual é o impacto da inflação no meu patrimônio?"

## 🔧 Desenvolvimento

### Adicionar Novas Funcionalidades

1. **Modificar o Prompt**: Edite `SYSTEM_PROMPT` em `src/app.py`
2. **Adicionar Dados**: Inclua novos arquivos em `data/`
3. **Expandir a Interface**: Use componentes do Streamlit em `src/app.py`

### Trocar o Modelo de IA

Para usar um modelo diferente:

```bash
# Remover modelo atual
ollama rm phi

# Instalar novo modelo (exemplo: neural-chat)
ollama pull neural-chat

# Atualizar em src/app.py
MODELO = 'neural-chat'
```

**Modelos Recomendados:**

- `phi` (1.6 GB) - Rápido e leve
- `neural-chat` (4.1 GB) - Mais contextualizado
- `mistral` (5 GB) - Respostas mais sofisticadas

## 🛠️ Troubleshooting

### Erro: "Ollama não está rodando"

```bash
# Inicie o servidor Ollama
ollama serve
```

### Erro: "Modelo não encontrado"

```bash
# Liste modelos instalados
ollama list

# Se não estiver, instale
ollama pull phi
```

### Erro: "Não há memória suficiente"

- Use um modelo menor (phi é o mais leve)
- Feche outros aplicativos
- Aumente a RAM disponível

### Erro: "Porta 11434 já está em uso"

```bash
# Windows
netstat -ano | findstr :11434
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :11434
kill -9 <PID>
```

## 📊 Fluxo de Funcionamento

```
Usuário digita pergunta
         ↓
Streamlit captura input
         ↓
App carrega contexto (perfil + histórico)
         ↓
Prompt é enviado para Ollama (API)
         ↓
Modelo Phi processa e gera resposta
         ↓
Resposta é formatada e exibida
```

## 🔐 Privacidade e Segurança

- ✅ **Execução Local**: Todo processamento acontece localmente, sem enviar dados para servidores externos
- ✅ **Sem Recomendações Específicas**: A IA não recomenda investimentos específicos
- ✅ **Educação Focada**: Apenas ensina conceitos e teorias financeiras

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto de educação financeira com IA.

## 📞 Suporte

Para dúvidas, reportar bugs ou sugestões:

- Abra uma [Issue](https://github.com/seu-usuario/projeto_ia_prada/issues)
- Envie um email ou entre em contato

---

## ⚠️ Aviso Importante

**Este é um projeto de teste e estudo.** Desenvolvido para fins educacionais e experimentação com tecnologias de IA. Não é recomendado para uso em produção ou para fornecer aconselhamento financeiro real sem revisão e validação profissional.

### Limitações Conhecidas

- ❌ Não deve substituir orientação financeira profissional
- ❌ Respostas baseadas em modelos de IA podem conter imprecisões
- ❌ Contexto limitado ao perfil local do cliente
- ❌ Sem integração com dados de mercado em tempo real

---

**Desenvolvido com ❤️ para fins educacionais**
