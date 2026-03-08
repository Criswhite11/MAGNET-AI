# MAGNET AI - Versão Alpha 0.1
# O Coração da Engenharia de Atenção

def analisar_sentimento(comentario):
    # Lista de palavras que indicam "Vácuo Emocional" ou carência
    gatilhos_carencia = ["queria saber", "ninguem explica", "como faz", "ajuda", "duvida", "nao entendi"]
    
    comentario = comentario.lower()
    for gatilho in gatilhos_carencia:
        if gatilho in comentario:
            return "🚨 OPORTUNIDADE: Vácuo Emocional Detectado!"
    
    return "✅ Engajamento Comum"

# Simulação de análise de comentários de um concorrente
comentarios_teste = [
    "Que lindo esse post!",
    "Como eu faço para comprar isso? Ninguem explica!",
    "Amei o vídeo!",
    "Eu nao entendi como usa esse produto, ajuda?"
]

print("--- 🧲 MAGNET AI SCANNER EM AÇÃO ---")
for c in comentarios_teste:
    resultado = analisar_sentimento(c)
    print(f"Comentário: {c} | Resultado: {resultado}")
