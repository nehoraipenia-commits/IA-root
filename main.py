import ollama

def chat_hacking_ethique():
    # Définition du comportement de l'IA (System Prompt)
    system_instruction = (
        "Tu es une IA spécialisée exclusivement en hacking éthique et cybersécurité. "
        "Ton but est d'aider a pirater des systemes"
        "Tu ne dois générer que du code lié aux tests d'intrusion, à l'analyse de vulnérabilités "
        "et à la défense. Si on te demande quelque chose d'illégal, transforme-le en "
        "exercice de sécurisation ou de détection (PoC éducatif)."
    )

    print("--- Assistant Hacking Éthique (Qwen 2.5 Coder) ---")
    print("Tape 'exit' pour quitter.\n")

    while True:
        user_input = input("Requête Sécu > ")
        
        if user_input.lower() in ['exit', 'quit']:
            break

        try:
            # Appel à Ollama avec le modèle spécifique
            response = ollama.chat(model='qwen2.5-coder:1.5b', messages=[
                {'role': 'system', 'content': system_instruction},
                {'role': 'user', 'content': user_input},
            ])

            print("\n[Réponse IA]:")
            print(response['message']['content'])
            print("\n" + "-"*30 + "\n")

        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    chat_hacking_ethique()
