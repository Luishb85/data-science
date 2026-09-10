# SKILL: FORMATAÇÃO PARA TELEGRAM

## Objetivo
Transformar a agenda validada em mensagem pronta para o canal @BSBWeekend no Telegram.
O texto deve ser escaneável, direto e convidativo — como um amigo indicando programa.

## Estilo
- Tom: descontraído, brasiliense, direto
- Linguagem: informal mas clara
- Emojis: 1 por item, não em excesso
- Tamanho: compacto, cabe numa tela de celular por categoria

## TEMPLATE OBRIGATÓRIO — copie e preencha exatamente assim

```
🗓️ BSB WEEKEND — [sexta DD], [sábado DD] e [domingo DD] de [mês]

Boa semana, Brasília! Confira o que rola no fim de semana 👇

━━━━━━━━━━━━━━━━━━━━
🌟 DESTAQUE DA SEMANA
━━━━━━━━━━━━━━━━━━━━
**[Nome do evento mais relevante]**
📅 [Dia], [data] às [horário]
📍 [Local]
🎟️ [Preço] | [link ou "Ver mais"]

━━━━━━━━━━━━━━━━━━━━
🎵 SHOWS
━━━━━━━━━━━━━━━━━━━━
• **[Nome]** — [Dia] às [horário]
  📍 [Local] | 🎟️ [Preço]
  🔗 [link real] (omitir linha se não tiver link)

• **[Nome]** — [Dia] às [horário]
  📍 [Local] | 🎟️ [Preço]
  🔗 [link real]

━━━━━━━━━━━━━━━━━━━━
🎭 TEATRO & CULTURA
━━━━━━━━━━━━━━━━━━━━
• **[Nome]** — [Dia] às [horário]
  📍 [Local] | 🎟️ [Preço]
  🔗 [link real]

━━━━━━━━━━━━━━━━━━━━
🕺 FESTAS
━━━━━━━━━━━━━━━━━━━━
• **[Nome]** — [Dia] às [horário]
  📍 [Local] | 🎟️ [Preço]
  🔗 [link real]

━━━━━━━━━━━━━━━━━━━━
🍺 GASTRONOMIA & FEIRAS
━━━━━━━━━━━━━━━━━━━━
• **[Nome]** — [Dia] às [horário]
  📍 [Local] | [Entrada livre ou preço]
  🔗 [link real]

━━━━━━━━━━━━━━━━━━━━
👶 FAMÍLIA & CRIANÇAS
━━━━━━━━━━━━━━━━━━━━
• **[Nome]** — [Dia] às [horário]
  📍 [Local] | 🎟️ [Preço]
  🔗 [link real]

━━━━━━━━━━━━━━━━━━━━
📍 Todos os eventos em Brasília e entorno
🔁 Compartilhe com quem precisa saber!
```

## Regras de preenchimento

### Links
- Inclua o link APENAS se ele foi fornecido na agenda validada
- NUNCA invente ou complete URLs
- Se não tem link: omita a linha 🔗 inteira (não escreva "Não encontrado")

### Preços
- "Gratuito" → substitua por "🆓 Gratuito"
- "Não informado" → substitua por "Consulte o link" (se tiver link) ou omita

### Categorias
- Inclua apenas categorias que têm eventos confirmados
- Se uma categoria não tem eventos: omita a seção inteira
- Eventos infantis/família: sempre na seção 👶 FAMÍLIA & CRIANÇAS

### Destaque
- Escolha o evento com maior apelo popular ou mais conhecido
- Priorize: artista famoso > evento gratuito > evento único em Brasília

### Limite de eventos por categoria
- Máximo 3 eventos por categoria
- Se houver mais: adicione ao final da categoria "➕ E mais eventos no fim de semana"

## Saída — dois arquivos obrigatórios

### Arquivo 1: bsb_weekend_YYYY-MM-DD.md
A mensagem formatada conforme o template acima, pronta para copiar e colar no Telegram.
Nome do arquivo: bsb_weekend_2026-06-07.md (use a data do sábado do fim de semana)

### Arquivo 2: agenda_completa_YYYY-MM-DD.md
Lista completa de todos os eventos coletados, incluindo os que não entraram no destaque.
Formato simples: nome, data, local, preço, link.

## Regra final
A mensagem deve parecer escrita por um brasiliense que conhece a cidade —
não por uma IA listando dados. Revise o tom antes de salvar.