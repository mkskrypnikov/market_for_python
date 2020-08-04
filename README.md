## Получение данных из яндекс маркет

указать ID приложения, api ключ, id магазинов и их названия

```python
at = 'xxx'
cid = 'xxx'
mag = [xxx, xxx, xxx, xxx]
magname = ['xxx', 'xxx', 'xxx', 'xxx']
```

формирование дат отчета 

произвольные даты:
```python
start_datesg = '2020-02-01'
end_datesg = '2020-02-13'
start_dates = '01-02-2020'
end_dates = '13-02-2020'
```

последние 3 дня для автоматического запуска:
```python
start_dates = lastday20
end_dates = lastday0
start_datesg = lastday22
end_datesg = lastdayx
```

очистка актуализируемых данных и перезапись новых
```python
x1 = pd.read_csv('market_cost_offer_t.csv', sep=';', encoding='cp1251', header=0)
x2 = pd.read_csv('market_cost_offer.csv', sep=';', encoding='cp1251', header=0)

x2 = x2[x2.дата.str.contains(lastdayx)==False]
x2 = x2[x2.дата.str.contains(lastday11)==False]
x2 = x2[x2.дата.str.contains(lastday22)==False]


x2 = x2.append(x1, ignore_index=False)
x2.to_csv('market_cost_offer.csv', index=False, header=True, sep=';', encoding='cp1251')
```