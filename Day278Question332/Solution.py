from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstruct the itinerary starting from 'JFK' using all the tickets exactly once.

        Args:
        tickets (List[List[str]]): List of tickets where each ticket is [from, to].

        Returns:
        List[str]: The reconstructed itinerary in the smallest lexical order.
        """
        # Step 1: Build the graph
        graph = defaultdict(list)
        for from_airport, to_airport in sorted(tickets, reverse=True):
            graph[from_airport].append(to_airport)
        
        # Step 2: Initialize an empty itinerary list
        itinerary = []

        # Step 3: Define DFS function
        def dfs(airport):
            """
            Perform DFS to visit all destinations from the current airport.
            Append the airport to the itinerary after visiting all destinations.
            """
            while graph[airport]:
                next_airport = graph[airport].pop()  # Visit next smallest lexical airport
                dfs(next_airport)
            itinerary.append(airport)  # Add to itinerary in post-order

        # Step 4: Start DFS from 'JFK'
        dfs("JFK")

        # Step 5: Reverse the itinerary to get the correct order
        return itinerary[::-1]
