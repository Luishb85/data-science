# SKILL: CURADORIA DE EVENTOS

## Objetivo
Receber a lista bruta de eventos coletados, remover duplicatas, organizar por
categoria e selecionar os mais relevantes para o público de Brasília.

## Quando usar
- Após a coleta de eventos (skill coleta_eventos)
- Antes da validação e formatação final

## Processo de curadoria

### Passo 1 — Deduplicação
Identifique e remova eventos duplicados usando estes critérios:
- Mesmo nome de evento em fontes diferentes → manter apenas 1 (priorize a fonte com mais informações)
- Mesmo local + mesmo horário → provavelmente o mesmo evento, mesclar informações
- Nomes muito similares (ex: "Feira Gastronômica" e "Feira de Gastronomia") → verificar se são o mesmo

### Passo 2 — Validação de datas
- Confirme que o evento é realmente no próximo sábado ou domingo
- Remova eventos com datas passadas ou sem data confirmada
- Marque como ⚠️ eventos com data incerta

### Passo 3 — Enriquecimento
Para eventos com informações incompletas, tente buscar:
- Preço (se "Não informado")
- Horário (se ausente)
- Link oficial (se ausente)
Use queries curtas: "[nome do evento] Brasília ingresso" ou "[nome do evento] Brasília horário"

### Passo 4 — Classificação por relevância
Para cada categoria, ordene os eventos por:
1. Artista/evento de maior nome ou audiência esperada
2. Eventos gratuitos (acessibilidade)
3. Eventos únicos ou raros em Brasília
4. Novidades e estreias

### Passo 5 — Seleção final
- Selecione até 3 eventos por categoria para o destaque principal
- Mantenha uma lista completa separada
- Marque 1 evento como "DESTAQUE DA SEMANA" (o mais relevante de todos)

## Formato de saída

```
## DESTAQUE DA SEMANA 🌟
- **[Nome do Evento]**
  - Por que é destaque: [justificativa em 1 frase]
  - Data: [data e horário]
  - Local: [local]
  - Preço: [preço]
  - Link: [URL]

## AGENDA CURADA — FIM DE SEMANA EM BRASÍLIA

### 🎵 SHOWS E CONCERTOS ([N] eventos)
[lista dos melhores, formato padrão]

### 🎭 TEATRO E CULTURA ([N] eventos)
[lista]

### 🕺 FESTAS E BALADAS ([N] eventos)
[lista]

### ⚽ ESPORTES ([N] eventos)
[lista]

### 🍺 GASTRONOMIA E FEIRAS ([N] eventos)
[lista]

## EVENTOS REMOVIDOS
- [Nome] — Motivo: [duplicata/data passada/sem confirmação]

## MÉTRICAS DA CURADORIA
- Eventos recebidos: [N]
- Eventos removidos: [N]
- Eventos na agenda final: [N]
- Categorias com 3+ eventos: [lista]
- Categorias com menos de 3 eventos: [lista] ⚠️
```

## Regras
- Mínimo de 5 eventos no total para considerar a curadoria bem-sucedida
- Se uma categoria tiver 0 eventos, sinalize claramente como ⚠️ SEM EVENTOS
- Nunca invente informações — se não encontrou preço, mantenha "Não informado"
- Priorize eventos com link funcional e informações completas
