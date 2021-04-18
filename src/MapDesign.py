g_design1 = {1: {2: 0, 3: 0},  # 节点1指向节点2,3,损耗都是0
             2: {1: 0, 3: 0, 4: 0},
             3: {1: 0, 2: 0, 4: 0},
             4: {2: 0, 3: 0}}
# 先姑且写损耗为0

# 这是地图的设计


g_design2 = {

    1: {2: 0, 4: 0, 5: 0, },
    2: {1: 0, 3: 0, 5: 0, 6: 0, },
    3: {2: 0, 6: 0, 7: 0, },
    4: {1: 0, 5: 0, 8: 0, 9: 0, },
    5: {1: 0, 2: 0, 4: 0, 6: 0, 9: 0, 10: 0, },
    6: {2: 0, 3: 0, 5: 0, 7: 0, 10: 0, 11: 0},
    7: {3: 0, 6: 0, 11: 0, 12: 0},
    8: {4: 0, 9: 0, 13: 0, },
    9: {4: 0, 5: 0, 8: 0, 10: 0, 13: 0, 14: 0},
    10: {5: 0, 6: 0, 9: 0, 11: 0, 14: 0, 15: 0, },
    11: {6: 0, 7: 0, 10: 0, 12: 0, 15: 0, 16: 0, },
    12: {7: 0, 11: 0, 16: 0, },
    13: {8: 0, 9: 0, 14: 0, 17: 0, },
    14: {9: 0, 10: 0, 13: 0, 15: 0, 17: 0, 18: 0, },
    15: {10: 0, 11: 0, 14: 0, 16: 0, 18: 0, 19: 0, },
    16: {11: 0, 12: 0, 15: 0, 19: 0},
    17: {13: 0, 14: 0, 18: 0, },
    18: {14: 0, 15: 0, 17: 0, 19: 0},
    19: {15: 0, 16: 0, 18: 0, }

}
g_map_xy2 = {
    1: (-2, 1),
    2: (-2, 0),
    3: (-2, -1),
    4: (-1, 1.5),
    5: (-1, 0.5),
    6: (-1, -0.5),
    7: (-1, -1.5),
    8: (0, 2),
    9: (0, 1),
    10: (0, 0),
    11: (0, -1),
    12: (0, -2),
    13: (1, 1.5),
    14: (1, 0.5),
    15: (1, -0.5),
    16: (1, -1.5),
    17: (2, 1),
    18: (2, 0),
    19: (2, -1)
}

g_design3 = {
    1: {2: 0}, 2: {1: 0}
}

g_design = g_design2
g_map_xy = g_map_xy2
