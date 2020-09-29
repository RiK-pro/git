import json

result = []
with open("file_7.json", "w", encoding="utf-8") as write:
    with open("text_7.txt", encoding="utf-8") as f_obj:
        profit = {}
        for line in f_obj:
            profit[line.split(" ")[0]] = int(line.split(" ")[2]) - int(line.split(" ")[3])
        average = sum([int(i) for i in profit.values() if int(i)>0])/len([int(i) for i in profit.values() if int(i)>0])
        result.append(profit)
        result.append({"Average_profit": round(average)})
    json.dump(result, write)