import heapq
import snowfall
from cost import get_crashes, get_cost, get_heuristic

graph = {
    'Colorado State University': { 'neighbors': {'I-25mm_10'}},
    'I-25mm_10' : {'neighbors': {'I-25mm_20'}},
    'I-25mm_20' : {'neighbors': {'I-25mm_10', 'I-25mm_30'}},
    'I-25mm_30' : {'neighbors': {'I-25mm_20', 'I-25mm_40'}},
    'I-25mm_40' : {'neighbors': {'I-25mm_30', 'Eldora', 'I-25mm_50'}},
    'Eldora' : {'neighbors': {'I-25mm_40', 'I-25mm_50'}},
    'I-25mm_50' : {'neighbors': {'I-25mm_40', 'Eldora', 'I-25mm_60'}},
    'I-25mm_60' : {'neighbors': {'I-25mm_50', 'I-70mm_10'}},
    'I-70mm_10' : {'neighbors': {'I-25mm_60', 'I-70mm_20'}},
    'I-70mm_20' : {'neighbors': {'I-70mm_10', 'I-70mm_30'}},
    'I-70mm_30' : {'neighbors': {'I-70mm_20', 'Winter Park', 'I-70mm_40'}},
    'Winter Park' : {'neighbors': {'I-70mm_30', 'I-70mm_40'}},
    'I-70mm_40' : {'neighbors': {'I-70mm_30', 'Winter Park', 'I-70mm_50'}},
    'I-70mm_50' : {'neighbors': {'I-70mm_40', 'Loveland', 'Arapahoe Basin', 'I-70mm_60'}},
    'Loveland' : {'neighbors': {'I-70mm_50', 'I-70mm_60'}},
    'Arapahoe Basin': {'neighbors': {'I-70mm_50', 'I-70mm_60'}},
    'I-70mm_60' : {'neighbors': {'I-70mm_50', 'Loveland', 'Arapahoe Basin', 'Keystone', 'I-70mm_70'}},
    'Keystone' : {'neighbors': {'I-70mm_60', 'I-70mm_70'}},
    'I-70mm_70' : {'neighbors': {'I-70mm_60', 'Keystone', 'Breckenridge', 'Copper Mountain', 'I-70mm_80'}},
    'Breckenridge' : {'neighbors': {'I-70mm_70', 'I-70mm_80'}},
    'Copper Mountain' : {'neighbors': {'I-70mm_70', 'I-70mm_80'}},
    'I-70mm_80' : {'neighbors': {'I-70mm_70', 'Breckenridge', 'Copper Mountain', 'I-70mm_90'}},
    'I-70mm_90' : {'neighbors': {'I-70mm_80', 'Vail', 'I-70mm_100'}},
    'Vail' : {'neighbors': {'I-70mm_90', 'I-70mm_100'}},
    'I-70mm_100' : {'neighbors': {'I-70mm_90', 'Vail', 'Beaver Creek', 'I-70mm_110'}},
    'Beaver Creek' : {'neighbors': {'I-70mm_100', 'I-70mm_110'}},
    'I-70mm_110' : {'neighbors': {'I-70mm_100', 'Beaver Creek', 'I-70mm_120'}},
    'I-70mm_120' : {'neighbors': {'I-70mm_110'}},
}

resorts = snowfall.march_resorts_list

def crash_reroute(current, goal, total_cost):
    print(f'crash at {current} re-evaluating goal resort...')       
    best_neighbor = None
    best_priority = float('inf')
    for neighbor in graph[current]['neighbors']:
        if neighbor in resorts:
            if neighbor != current:
                priority = total_cost[current] + heuristic(goal, current, neighbor)
                if priority < best_priority:
                    best_neighbor = neighbor
                    best_priority = priority
    return best_neighbor

def heuristic(goal, current, neighbor):
    current_cost = get_cost(current)
    neighbor_cost = get_cost(neighbor)
    if neighbor_cost < current_cost:
        return (goal == neighbor) * (current_cost - neighbor_cost)
    return get_heuristic(goal, neighbor)

def a_star_search(start, goal, frontier, visited, total_cost):
    if not frontier: frontier = [(0, start)]
    if not visited: 
        visited = {}
        visited[start] = None
    if not total_cost:
        total_cost = {}
        total_cost[start] = 0

    suggested_goal = None

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            path = [goal]
            current = goal
            while current != start:
                current = visited[current]
                path.append(current)
            path.reverse()
            return "done", path, total_cost, goal, None

        for neighbor in graph[current]['neighbors']:
            if neighbor != current:
                new_cost = total_cost[current] + get_cost(current)
                if neighbor not in total_cost or new_cost < total_cost[neighbor]:
                    total_cost[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, current, neighbor)
                    heapq.heappush(frontier, (priority, neighbor))
                    visited[neighbor] = current

        if current in get_crashes():
            suggested_goal = crash_reroute(current, goal, total_cost)
            if suggested_goal: return "reroute", suggested_goal, frontier, visited, total_cost

    return "done", visited, total_cost, goal, None

def test_a_star_search(start, goal):
    status, val1, val2, val3, val4 = a_star_search(start, goal, None, None, None)
    while status == "reroute":
        suggested_goal = val1
        frontier = val2
        visited = val3
        total_cost = val4
        ans = input(f"Re-evaluating trip to {goal}, Accept new goal: {suggested_goal} (y/n)")
        if ans == 'y':
            goal = suggested_goal
            print(f'Accepted new goal resort: {goal}')
        elif ans == 'n':
            print(f"Denied new goal: {suggested_goal}, Continuing to {goal}")
        status, val1, val2, val3, val4 = a_star_search(start, goal, frontier, visited, total_cost)
    path = val1
    total_cost = val2
    new_goal = val3

    return path, total_cost, new_goal
