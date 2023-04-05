from translate import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translator = Translator(to_lang="en", from_lang="fr")
result = {}
for word in french_words:
    result[word] = translator.translate(word)

print(result)
