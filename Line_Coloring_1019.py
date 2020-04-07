
sections = []
values = {0, 1000000000}


class Section:
    def __init__(self, begin, end, color):
        self.begin = begin
        self.end = end
        self.color = True if color or color == 'w' else False

    def __len__(self):
        return self.end - self.begin

    def __repr__(self):
        color = 'white' if self.color else 'black'
        return repr((self.begin, self.end, color))


for _ in range(int(input())):
    a, b, c = input().split()
    a, b, = map(int, (a, b))
    if c == 'w':
        sections.append(Section(a, b, 1))
    else:
        sections.append(Section(a, b, 0))
    values.add(a)
    values.add(b)


values = list(sorted(values))

all_sections = [(values[i], values[i+1]) for i in range(len(values)-1)]
all_colors = [1 for i in range(len(values)-1)]
indexes_start_dict = {}
indexes_end_dict = {}

for i, elem in enumerate(all_sections):
    indexes_start_dict[elem[0]] = i
    indexes_end_dict[elem[1]] = i+1

del values

for section in sections:
    start = indexes_start_dict[section.begin]
    end = indexes_end_dict[section.end]
    all_colors[start:end] = [1]*(end-start) if section.color else [0]*(end-start)


all_sections = {all_sections[i]: all_colors[i] for i in range(len(all_colors))}
prev = 0
for elem in all_sections.keys():
    if all_sections[elem]:
        all_sections[elem] = prev + elem[1]-elem[0]
        prev = all_sections[elem]
    else:
        prev = 0
        all_sections[elem] = 0


maxima = max(all_sections.values())
for key in all_sections.keys():
    if all_sections[key] == maxima:
        a, b = key[1]-maxima, key[1]
        if b > a:
            print(a, b)
        break
