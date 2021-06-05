# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 13:56:42 2020

CS330
PA 2 -- Implement Dijkstra's Algorithm
"""

import sys
import heapq


""" global variables """
infinity = 10**4
shortest_path = {}      #{node:[shortest distance, parent]}
adj_list = {}           #{node:[child, edge weight]}
queue = []

          
def main():

    lines = sys.stdin.read().splitlines()
    n,m,s = [int(i) for i in lines[0].split()]
    lines = lines[1:]
    
    #setting up the dictionaries
    for i in range(len(lines)):
        n1,n2,w = [int(x) for x in lines[i].split()]
        
        if n1 in adj_list:
            adj_list[n1]+=[[n2,w]]
        
        else:
            adj_list[n1] = [[n2,w]]
        
    
    heapq.heappush(queue, (0, [s,"start"]))
    #run Dijkstra and print to standard output
    Dijkstra(s)
    
    printOutput(s)
    
    
def Dijkstra(s):
    
    while(queue):
        temp = heapq.heappop(queue)
        dist = temp[0]
        parent = temp[1][0]
        prev = temp[1][1]
        
        if parent not in shortest_path:
            shortest_path[parent] = [dist, prev]
            
            if parent in adj_list:
            
                for edge in adj_list[parent]:
                    child = edge[0]
                    weight = edge[1]
                    #dist+=weight
                    new_dist = dist+weight
                    heapq.heappush(queue,(new_dist,[child,parent]))
      
    
def printOutput(s):
    #(node reachable from s, d from s, parent)
    pq = []
    
    for node in shortest_path:
        dist = str(shortest_path[node][0])
        prev = str(shortest_path[node][1])
        
        if node != s:
            heapq.heappush(pq,(node, str(node)+" "+dist+" "+prev))
            
    while(pq):
        sys.stdout.write(heapq.heappop(pq)[1] + "\n")
        
    
main()
