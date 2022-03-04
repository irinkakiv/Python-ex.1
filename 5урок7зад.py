import json


with open("my_ex7.json", "w", encoding="utf-8") as writemy_f:
    with open("text_7.txt", encoding="utf-8") as my_f:
        profit = {line.split()[0]: int(line.split()[2])- int(line.split()[3]) for line in my_f}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result,writemy_f, ensure_ascii=False, indent=4)