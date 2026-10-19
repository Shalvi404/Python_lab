text=input(f"Введите текст текст:").strip().lower().split()
def transformation(words):
    if not words:
        print(f"Пустой текст")
        return
    unique_text=set(words)
    count=0
    max_len=0
    freq_word=''
    longest_word=words[0]
    smallest_word=words[0]
    for word in unique_text:
        print(f"Слово {word} встречается: {words.count(word)}")
        if len(word)>max_len:
            max_len=len(word)
            longest_word=word
        if len(word)<len(smallest_word):
            smallest_word=word
        if words.count(word)>count:
            count=words.count(word)
            freq_word=word
    print(f"Самое часто встречающееся слово: {freq_word}, которое встретилось {count} раз")
    print(f"Самое длинное слово:{longest_word}")
    print(f"Самое короткое слово:{smallest_word}")
transformation(text)
text=[word for word in text if len(word)>2]
transformation(text)