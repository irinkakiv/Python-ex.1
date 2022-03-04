with open("text_4.txt","r",encoding='utf-8') as f_my:
    useful = [f'{line}.{count.strip()} - {len(count.split())} слов'
              for line,count in enumerate(f_my,1)]
    print(*useful,f"Всего строк - {len(useful)}.", sep="\n")