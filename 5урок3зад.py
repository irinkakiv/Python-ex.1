with open("text_3.txt","r",encoding='utf-8') as f_my:
    employer_dict= {line.split()[0]: float(line.split()[1]) for line in f_my}
    print(f'Avr salary = {round(sum(employer_dict.values()) / len(employer_dict), 3)}\n'
          f'Employer with salary <20k {[k[0] for k in employer_dict.items() if k[1] < 20000]}')