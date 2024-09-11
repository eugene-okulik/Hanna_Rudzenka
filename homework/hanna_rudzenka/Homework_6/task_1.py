text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,"
    " dignissim vitae libero"
)
new_text = []
text = text.split(' ')
for word in text:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1] + 'ing' + word[-1:]
    new_text.append(word)
print(' '.join(new_text))
