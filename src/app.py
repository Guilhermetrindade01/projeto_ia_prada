import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÕES
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'phi'

# CARREGAR DADOS
perfil = json.load(open('data/perfil_investidor.json'))
transacoes = pd.read_csv('data/transacoes.csv')
historico = pd.read_csv('data/historico_atendimento.csv')
produtos = json.load(open('data/produtos_financeiros.json'))

# MONTAR CONTEXTO (resumido para evitar timeout)
contexto = f"""
CLIENTE: Ka ({perfil['nome']}), {perfil['idade']} anos
PROFISSÃO: {perfil['profissao']}
PERFIL INVESTIDOR: {perfil['perfil_investidor']}
RENDA MENSAL: R$ {perfil['renda_mensal']}
PATRIMÔNIO TOTAL: R$ {perfil['patrimonio_total']}
RESERVA DE EMERGÊNCIA: R$ {perfil['reserva_emergencia_atual']}
OBJETIVO PRINCIPAL: {perfil['objetivo_principal']}
"""
# SYSTEM PROMPT
SYSTEM_PROMPT = """Você é Prada, uma educadora financeira experiente e profissional baseada em Lisboa. Sua missão é ensinar Ka sobre educação financeira de forma clara, acessível e prática.

VOCÊ DEVE:
- Explicar conceitos financeiros com simplicidade, como se estivesse conversando com um amigo;
- Usar exemplos concretos baseados na situação real de Ka;
- Nunca recomendar investimentos específicos - apenas educar sobre como funcionam;
- Ser encorajador e positivo;
- Fazer perguntas para garantir compreensão;
- Respostas concisas: máximo 2 parágrafos;

SUA ABORDAGEM:
1. Entender o contexto financeiro de Ka
2. Identificar áreas de melhoria
3. Educar sobre economia pessoal e mercado
4. Sugerir práticas seguras de gestão de recursos"""


def perguntar(msg: str) -> str:
    prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""
    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False},
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        return data.get("response", "")
    except requests.exceptions.HTTPError as e:
        return f"❌ Erro ao conectar com Ollama: {e.response.status_code}. Verifique se o Ollama está rodando e se o modelo '{MODELO}' está instalado."
    except Exception as e:
        return f"❌ Erro: {str(e)}"
    # /api/generate retorna o texto em "response" quando stream=False [web:25]


# INTERFACE
st.set_page_config(
    page_title="Prada | Educadora Financeira", layout="centered")
st.title("💰 Prada - Sua Educadora Financeira")
st.markdown(
    "Bem-vindo Ka! Aqui você aprende sobre finanças pessoais de forma prática e segura.")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
