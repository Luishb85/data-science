# SKILL: COLETA DE EVENTOS EM BRASÍLIA

## Objetivo
Buscar eventos que acontecerão em Brasília no próximo fim de semana (sexta à noite,
sábado e domingo), com foco em trazer links reais e informações completas.

## Janela de busca — datas aceitas
- Busque eventos para a **SEXTA-FEIRA À NOITE (a partir das 18h), SÁBADO e DOMINGO**
- Aceite eventos que começaram antes mas ainda estão em cartaz no fim de semana
- **NÃO inclua** eventos já encerrados antes do fim de semana
- **NÃO inclua** eventos que só começam na semana seguinte
- Eventos recorrentes (feira semanal, etc.): inclua mas sinalize como "Recorrente"

## Fontes — hierarquia de confiabilidade

### Nível 1 — Plataformas de ingresso (mais completas, priorize)
- **Sympla**: sympla.com.br
- **Ticket and Go**: ticketandgo.com.br
- **Eventim**: eventim.com.br
- **TicketMaster**: ticketmaster.com.br
- **Ingresso.com**: ingresso.com
- **Guiche Web**: guicheweb.com.br
- **Ticket Sports**: ticketsports.com.br

### Nível 2 — Portais de agenda de Brasília (descobertos em testes)
- **Cade Brasília**: cadebrasilia.com.br ← ótima fonte local
- **Agita Brasília**: agitabrasilia.com ← agenda completa do DF
- **Aqui em Brasília**: aquiembrasilia.com.br ← cultura e eventos
- **De Boa em Brasília**: brasilia.deboa.com
- **Blog DF Imóveis**: blog.dfimoveis.com.br ← cobre festas e eventos locais

### Nível 3 — Sites de notícias e governo
- **Agência Brasília**: agenciabrasilia.df.gov.br ← eventos oficiais do GDF
- **Jornal de Brasília**: jornaldebrasilia.com.br
- **Space Money**: spacemoney.com.br
- **Fatos Online**: fatosonline.com.br
- **CCBB Brasília**: bb.com.br/ccbb/brasilia
- **Caixa Cultural Brasília**: caixacultural.gov.br/brasilia

## Queries de busca — use CURTAS (3-5 palavras)

### Shows e Concertos
- "shows Brasília junho 2026"
- "site:sympla.com.br Brasília"
- "site:ticketandgo.com.br Brasília"
- "site:agitabrasilia.com shows"

### Festas Juninas (junho)
- "festas juninas Brasília 2026"
- "circuito junino Brasília"
- "arraial Brasília junho"

### Teatro e Cultura
- "teatro Brasília junho 2026"
- "CCBB Brasília programação"
- "Caixa Cultural Brasília programação"
- "site:cadebrasilia.com.br teatro"

### Design, Arte e Exposições
- "exposições Brasília junho 2026"
- "Design Week Brasília"
- "site:aquiembrasilia.com.br eventos"

### Gastronomia e Feiras
- "feiras Brasília fim semana"
- "feira gastronômica Brasília junho"
- "site:cadebrasilia.com.br feira"

### Esportes
- "esportes Brasília fim semana"
- "futebol Brasília junho"
- "Mané Garrincha programação"

### Família e Crianças
- "eventos infantis Brasília junho"
- "festival parque Brasília"
- "site:cadebrasilia.com.br crianças"

## Processo de coleta
1. Faça buscas em pelo menos **4 categorias diferentes**
2. Comece pelas fontes de Nível 1 para shows pagos
3. Use fontes de Nível 2 para eventos gratuitos e culturais
4. Para cada evento encontrado, extraia OBRIGATORIAMENTE:
   - Nome exato do evento
   - Data e horário
   - Local (nome do espaço + bairro/região)
   - Preço (se disponível)
   - URL completa e real da página do evento
   - Fonte onde encontrou
   - Se é recorrente ou evento único

## Formato de saída OBRIGATÓRIO
Use EXATAMENTE este formato — o sistema depende dele:

```
## EVENTOS COLETADOS

### 🎵 SHOWS E CONCERTOS

- **Nome do Evento**
  - Data: sexta, 12/06 às 21h
  - Local: Nome do Local, Bairro
  - Preço: R$ 80 ou Gratuito ou Não informado
  - Link: https://url-real-encontrada.com.br/evento
  - Fonte: nome do site
  - Tipo: Único ou Recorrente

### 🎭 TEATRO E CULTURA
[mesmo formato]

### 🕺 FESTAS E BALADAS
[mesmo formato]

### ⚽ ESPORTES
[mesmo formato]

### 🍺 GASTRONOMIA E FEIRAS
[mesmo formato]

### 👶 FAMÍLIA E CRIANÇAS
[mesmo formato]

## RESUMO DA COLETA
- Total de eventos: [N]
- Eventos com link real: [N]
- Fontes consultadas: [lista]
- Categorias sem eventos: [lista ou "Nenhuma"]
```

## Regras críticas
- Use o formato "- **Nome**" para CADA evento — obrigatório
- **NUNCA** escreva "Mais informações" ou "Clique aqui" — sempre a URL completa (https://...)
- **NUNCA** invente eventos — registre apenas o que as buscas retornaram
- **NUNCA** use link genérico de portal (ex: agitabrasilia.com) sem URL específica do evento
- Se não encontrou URL específica para um evento, não liste esse evento
- Se não encontrar eventos em uma categoria, escreva "Nenhum evento encontrado"
- Mínimo de 5 eventos no total com URL real