# =============================================================================
# BSB WEEKEND — Agregador de Eventos de Brasília (v6 — agente único)
# =============================================================================
#
#   DATAS → 1 Agente (web_search) → .md formatado → Telegram (opcional)
#
# FILOSOFIA v6:
#   Menos é mais. Um agente único com boas instruções é mais confiável
#   do que múltiplos agentes com ferramentas que bloqueiam bots (403).
#   A validação é feita por você em 2 minutos antes de publicar —
#   isso é mais seguro do que qualquer validação automática.
# =============================================================================

import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.websearch import WebSearchTools
from agno.tools.file import FileTools
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────────────────────────────────────
MODELO = "gpt-4o-mini"

output_dir = Path(__file__).parent / "output/fdsnodf_bot/"
output_dir.mkdir(parents=True, exist_ok=True)

file_tools = FileTools(
    base_dir=output_dir,
    enable_save_file=True,
    enable_read_file=True,
    enable_list_files=True,
)

web_tools = WebSearchTools(
    enable_search=True,
    enable_news=False,
    fixed_max_results=8,
    timelimit="w",
    region="br-pt",
    timeout=15,
)

# ─────────────────────────────────────────────────────────────────────────────
# AGENTE ÚNICO — Curador BSB Weekend
# ─────────────────────────────────────────────────────────────────────────────
agente_bsb = Agent(
    name="Curador BSB Weekend",
    model=OpenAIChat(id=MODELO, api_key=os.getenv("OPENAI_API_KEY")),
    instructions=[
        "Você é o curador do canal @BSBWeekend no Telegram.",
        "Sua missão: montar a agenda cultural de Brasília para o fim de semana.",
        "",
        "═══════════════════════════════════════",
        "PASSO 1 — BUSCA (faça buscas separadas)",
        "═══════════════════════════════════════",
        "Use web_search com estas queries, uma por vez:",
        "  1. 'shows Brasília junho 2026'",
        "  2. 'site:sympla.com.br Brasília'",
        "  3. 'site:ticketandgo.com.br Brasília'",
        "  4. 'festas juninas Brasília 2026'",
        "  5. 'site:cadebrasilia.com.br eventos'",
        "  6. 'teatro Brasília junho 2026'",
        "  7. 'feiras Brasília fim semana'",
        "  8. 'site:agitabrasilia.com eventos brasilia'",
        "",
        "Para cada resultado, extraia:",
        "  - Nome do evento",
        "  - Data e horário",
        "  - Local",
        "  - Preço",
        "  - URL (copie EXATAMENTE do resultado — nunca invente)",
        "",
        "REGRAS DE COLETA:",
        "• Use APENAS eventos que aparecem nos resultados de busca",
        "• NUNCA invente eventos, locais, preços ou URLs",
        "• Se não achar URL específica para um evento, não liste ele",
        "• 'Mais informações' ou 'Clique aqui' NÃO são URLs — descarte",
        "",
        "FILTRO DE DATAS — CRÍTICO:",
        "• Você recebeu as datas exatas do fim de semana na mensagem",
        "• SOMENTE inclua eventos cuja data bate com sexta, sábado ou domingo informados",
        "• Se o resultado de busca mostrar um evento mas a data for anterior → DESCARTE",
        "• Se a data do evento não estiver clara no resultado → DESCARTE",
        "• Exemplos de descarte:",
        "  ❌ Evento aconteceu semana passada",
        "  ❌ Evento é 'todo sábado' mas o site não confirma esse sábado específico",
        "  ❌ Data mencionada no resultado é diferente do fim de semana buscado",
        "• Exemplos de inclusão:",
        "  ✅ Resultado confirma explicitamente a data do fim de semana buscado",
        "  ✅ Evento de longa duração que INCLUI o fim de semana (ex: 'de 4 a 14 de junho')",
        "",
        "═══════════════════════════════════════",
        "PASSO 2 — FORMATAÇÃO TELEGRAM",
        "═══════════════════════════════════════",
        "Formate os eventos encontrados neste template EXATO:",
        "",
        "🗓️ FDS NO DF — [sexta DD], [sábado DD] e [domingo DD] de [mês]",
        "",
        "Boa semana, Brasília! Confira o que rola no fim de semana 👇",
        "",
        "——————————————————",
        "🌟 DESTAQUE DA SEMANA",
        "——————————————————",
        "**[Nome do evento mais relevante]**",
        "📅 [Dia] às [horário]",
        "📍 [Local]",
        "🎟️ [Preço]",
        "🔗 [URL completa]",
        "",
        "——————————————————",
        "🎵 SHOWS",
        "——————————————————",
        "• **[Nome]** — [Dia] às [horário]",
        "  📍 [Local] | 🎟️ [Preço]",
        "  🔗 [URL]",
        "",
        "——————————————————",
        "🎭 TEATRO & CULTURA",
        "——————————————————",
        "• **[Nome]** — [Dia] às [horário]",
        "  📍 [Local] | 🎟️ [Preço]",
        "  🔗 [URL]",
        "",
        "——————————————————",
        "🎉 FESTAS & FEIRAS",
        "——————————————————",
        "• **[Nome]** — [Dia] às [horário]",
        "  📍 [Local] | 🎟️ [Preço]",
        "  🔗 [URL]",
        "",
        "——————————————————",
        "📍 Todos os eventos em Brasília e entorno",
        "🔁 Compartilhe com quem precisa saber!",
        "",
        "REGRAS DE FORMATAÇÃO:",
        "• Inclua SOMENTE eventos com URL real encontrada na busca",
        "• Inclua SOMENTE eventos com data confirmada no fim de semana buscado",
        "• Antes de incluir cada evento, confirme mentalmente: 'essa data bate com o fim de semana?'",
        "• Se a data for de outra semana ou não estiver confirmada → OMITA o evento",
        "• Omita seções sem eventos (ex: sem shows = sem seção 🎵)",
        "• NUNCA use 'Clique aqui' — coloque a URL completa após 🔗",
        "• Use bullets (•), não listas numeradas",
        "• Se tiver poucos eventos (1-2): publique normalmente, qualidade > quantidade",
        "",
        "═══════════════════════════════════════",
        "PASSO 3 — FORMATO FINAL",
        "═══════════════════════════════════════",
        "Entregue a agenda SOMENTE dentro de um bloco ```markdown``` assim:",
        "```markdown",
        "🗓️ FDS NO DF — ...",
        "...",
        "```",
        "NÃO escreva nada fora do bloco markdown — nem 'o arquivo foi salvo', nem confirmações.",
        "O sistema salva o arquivo automaticamente a partir do bloco markdown.",
    ],
    tools=[web_tools, file_tools],
    add_datetime_to_context=True,
    markdown=True,
)

# ─────────────────────────────────────────────────────────────────────────────
# TELEGRAM
# ─────────────────────────────────────────────────────────────────────────────
async def publicar_no_telegram(mensagem: str) -> bool:
    try:
        from telegram import Bot
    except ImportError:
        print("  Execute: uv add python-telegram-bot")
        return False

    token   = os.getenv("TELEGRAM_BOT_TOKEN")
    channel = os.getenv("TELEGRAM_CHANNEL_ID")
    if not token or not channel:
        return False

    try:
        bot = Bot(token=token)
        LIMITE = 4096
        partes = [mensagem[i:i+LIMITE] for i in range(0, len(mensagem), LIMITE)]
        for i, parte in enumerate(partes, 1):
            await bot.send_message(chat_id=channel, text=parte, parse_mode="Markdown")
            if len(partes) > 1:
                print(f"   📤 Parte {i}/{len(partes)}")
        print(f"[OK] Publicado em {channel}")
        return True
    except Exception as e:
        print(f" Erro: {e}")
        return False


def ler_md_gerado() -> str:
    arquivos = sorted(output_dir.glob("fdsnodf_*.md"), reverse=True)
    if not arquivos:
        return ""
    print(f"   {arquivos[0].name}")
    return arquivos[0].read_text(encoding="utf-8")

# ─────────────────────────────────────────────────────────────────────────────
# DIAGNÓSTICO
# ─────────────────────────────────────────────────────────────────────────────
def verificar_configuracao():
    chave = os.getenv("OPENAI_API_KEY")
    if not chave or not chave.startswith("sk-"):
        print("  OPENAI_API_KEY não encontrada no .env")
        return False
    print(f"[OK] OpenAI           : {chave[:12]}...{chave[-4:]}")
    print(f"[OK] Modelo           : {MODELO}")
    print(f"[OK] Arquitetura      : 1 agente (simples e rápido)")
    print(f"[OK] Validação        : você revisa o .md antes de publicar")

    token   = os.getenv("TELEGRAM_BOT_TOKEN")
    channel = os.getenv("TELEGRAM_CHANNEL_ID")
    auto    = os.getenv("TELEGRAM_AUTO", "false").lower() == "true"
    if token and channel:
        print(f"[OK] Telegram         : {channel} ({'AUTO' if auto else 'MANUAL'})")
    else:
        print(f"  Telegram         : não configurado (modo arquivo apenas)")
    return True

# ─────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from datetime import date, timedelta

    hoje  = date.today()
    dias_ate_sexta = (4 - hoje.weekday()) % 7
    if dias_ate_sexta == 0:
        dias_ate_sexta = 7
    sexta   = hoje + timedelta(days=dias_ate_sexta)
    sabado  = sexta + timedelta(days=1)
    domingo = sexta + timedelta(days=2)

    MESES_PT = {
        1:"janeiro",2:"fevereiro",3:"março",4:"abril",5:"maio",6:"junho",
        7:"julho",8:"agosto",9:"setembro",10:"outubro",11:"novembro",12:"dezembro"
    }

    sexta_str   = f"{sexta.day:02d}/{sexta.month:02d}/{sexta.year}"
    sabado_str  = f"{sabado.day:02d}/{sabado.month:02d}/{sabado.year}"
    domingo_str = f"{domingo.day:02d}/{domingo.month:02d}/{domingo.year}"
    mes_str     = MESES_PT[sexta.month]

    print("\n [INFO] Verificando configuração...")
    if not verificar_configuracao():
        exit(1)

    print(f" Período          : sexta {sexta_str}, sábado {sabado_str} e domingo {domingo_str}")

    print("\n [INFO] Gerando agenda BSB Weekend...\n")
    print("-" * 60)

    mensagem = (
        f"Monte a agenda BSB Weekend para o fim de semana: "
        f"sexta {sexta_str}, sábado {sabado_str} e domingo {domingo_str} "
        f"de {mes_str} de {sexta.year}. "
        f"Siga os 3 passos das instruções."
    )
    print(">>> ANTES DO AGENTE")
    resultado = agente_bsb.run(mensagem)
    print(">>> DEPOIS DO AGENTE")

    print("\n" + "-" * 60)
    print(" AGENDA GERADA\n")

    conteudo = resultado.content or ""
    if conteudo:
        print(conteudo)

        # Salva o arquivo diretamente no código — não depende do agente chamar a tool
        from datetime import date, timedelta
        hoje2 = date.today()
        dias = (5 - hoje2.weekday()) % 7
        if dias == 0:
            dias = 7
        sabado2 = hoje2 + timedelta(days=dias)
        nome_arquivo = f"fdsnodf_{sabado2.strftime('%Y-%m-%d')}.md"
        caminho = output_dir / nome_arquivo

        # Extrai só o conteúdo markdown (remove ```markdown se existir)
        import re
        md_match = re.search(r"```markdown\s*(.+?)```", conteudo, re.DOTALL)
        conteudo_md = md_match.group(1).strip() if md_match else conteudo

        caminho.write_text(conteudo_md, encoding="utf-8")
        print(f"\n Arquivo salvo: {nome_arquivo}")
    else:
        print("  Resposta vazia — tente rodar novamente.")

    # ── Telegram ──────────────────────────────────────────────────────────────
    auto    = os.getenv("TELEGRAM_AUTO", "false").lower() == "true"
    token   = os.getenv("TELEGRAM_BOT_TOKEN")
    channel = os.getenv("TELEGRAM_CHANNEL_ID")

    if token and channel:
        conteudo = ler_md_gerado()
        if conteudo:
            if auto:
                print("\n [INFO]  Publicando no Telegram...")
                asyncio.run(publicar_no_telegram(conteudo))
            else:
                print("\n" + "-" * 60)
                print(" MODO MANUAL — revise o .md e publique com:")
                print("   uv run publicar_telegram.py")
    else:
        print("\n Arquivo salvo em output/BSB/")
        print("   Configure Telegram no .env para publicar automaticamente.")