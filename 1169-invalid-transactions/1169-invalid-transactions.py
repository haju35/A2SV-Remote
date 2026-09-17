class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transaction = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            transaction.append((name, int(time), int(amount), city))
        groupByName = defaultdict(list)
        for i, (name, time, amount, city) in enumerate(transaction):
            groupByName[name].append(i)
        
        invalid = set()
        for i, (name, time, amount, city) in enumerate(transaction):

            if amount > 1000:
                invalid.add(i)
                continue
            for j in groupByName[name]:
                if j == i:
                    continue
                _, other_time, _, other_city = transaction[j]
                if other_city != city and abs(other_time - time) <= 60:
                    invalid.add(i)
                    break
        return[transactions[i] for i in invalid]
