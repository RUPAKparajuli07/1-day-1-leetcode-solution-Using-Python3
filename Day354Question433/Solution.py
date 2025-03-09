from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Convert bank to a set for quick lookup
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1  # If endGene is not in bank, mutation is impossible
        
        # BFS initialization
        queue = deque([(startGene, 0)])  # (current_gene, mutation_steps)
        visited = set([startGene])  # Set to track visited genes
        gene_chars = ['A', 'C', 'G', 'T']  # Possible character mutations
        
        while queue:
            gene, steps = queue.popleft()
            
            # Try mutating each character
            for i in range(len(gene)):
                for char in gene_chars:
                    if char != gene[i]:  # Ensure a mutation happens
                        mutated_gene = gene[:i] + char + gene[i+1:]
                        
                        # If mutation is valid and not visited
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            if mutated_gene == endGene:
                                return steps + 1  # Found the shortest mutation path
                            queue.append((mutated_gene, steps + 1))
                            visited.add(mutated_gene)
        
        return -1  # No valid mutation sequence found
