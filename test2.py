list1 = ["GMAIL","YAHOO","OUTLOOK","HUBSPOT","AOL","YANDEX","GMX"]

print(sorted(list1, key = lambda s: sum(map(ord, s)), reverse=True))