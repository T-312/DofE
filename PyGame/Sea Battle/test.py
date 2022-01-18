# def gen_squares():
#     all_sq = []
#     for x in range(60, 601):
#         current = []
#         for y in range(60, 601):
#             current.append((x,y))
#             if not sum(current[0]) % 60 and not sum(current[-1]) % 60:
#                 all_sq.append(current)

#     for i in all_sq:
#         print(i[0]+i[-1])

# print(gen_squares())

def gen_square(start, end):
    sq = []
    for x in range(start, end+1):
        for y in range(start, end+1):
            sq.append((x, y))

    return sq

for x in range(60, 601):
    for y in range(60, 601):
        if not x % 60 and not y % 60:
            print((x,y))