words_list = ['merdeka', 'hello', 'hellos', 'sohib', 'kari ayam']
user_input = 'he'
def search_words(x):
    if user_input in x:
        return x
search_result = list(filter(search_words, words_list))
print(search_result)