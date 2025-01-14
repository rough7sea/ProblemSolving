from collections import defaultdict
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        if startGene == endGene:
            return 0

        graph = defaultdict(set)
        bank.insert(0, startGene)
        for i in range(len(bank)):
            for j in range(i, len(bank)):
                if self.closeMutation(bank[i], bank[j]):
                    graph[bank[i]].add(bank[j])
                    graph[bank[j]].add(bank[i])
        queue = [(startGene, 0)]
        visited = {startGene}

        while queue:
            gene, step = queue.pop(0)

            while graph[gene]:
                next_gene = graph[gene].pop()

                if next_gene in visited:
                    continue
                if next_gene == endGene:
                    return step + 1
                queue.append((next_gene, step + 1))
        return -1


    def closeMutation(self, gene_left: str, gene_right: str):
        count = 0
        for i in range(len(gene_right)):
            if gene_left[i] != gene_right[i]:
                if count > 0:
                    return False
                else:
                    count += 1
        return True


sol = Solution()
print(sol.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA",
                      bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]))