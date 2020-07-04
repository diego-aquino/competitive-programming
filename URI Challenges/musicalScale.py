def main():
    notes = getNotes()
    print(scale(notes))

databank = [
    "do", "do#", "re", "re#", "mi", "fa", "fa#",
    "sol", "sol#", "la", "la#", "si"
]

def getNotes():
    n = int(input())

    notes = []
    for i in range(n):
        noteId = (int(input()) % 12) - 1
        notes.append(databank[noteId])

    return notes

def scale(notes):
    scales = [
        {'do': 1, 're': 1, 'mi': 1, 'fa': 1, 'sol': 1, 'la': 1, 'si': 1},
        {'do#': 1, 're#': 1, 'fa': 1, 'fa#': 1, 'sol#': 1, 'la#': 1, 'do': 1},
        {'re': 1, 'mi': 1, 'fa#': 1, 'sol': 1, 'la': 1, 'si': 1, 'do#': 1},
        {'re#': 1, 'fa': 1, 'sol': 1, 'sol#': 1, 'la#': 1, 'do': 1, 're': 1},
        {'mi': 1, 'fa#': 1, 'sol#': 1, 'la': 1, 'si': 1, 'do#': 1, 're#': 1},
        {'fa': 1, 'sol': 1, 'la': 1, 'la#': 1, 'do': 1, 're': 1, 'mi': 1},
        {'fa#': 1, 'sol#': 1, 'la#': 1, 'si': 1, 'do#': 1, 're#': 1, 'fa': 1},
        {'sol': 1, 'la': 1, 'si': 1, 'do': 1, 're': 1, 'mi': 1, 'fa#': 1},
        {'sol#': 1, 'la#': 1, 'do': 1, 'do#': 1, 're#': 1, 'fa': 1, 'sol': 1},
        {'la': 1, 'si': 1, 'do#': 1, 're': 1, 'mi': 1, 'fa#': 1, 'sol#': 1},
        {'la#': 1, 'do': 1, 're': 1, 're#': 1, 'fa': 1, 'sol': 1, 'la': 1},
        {'si': 1, 'do#': 1, 're#': 1, 'mi': 1, 'fa#': 1, 'sol#': 1, 'la#': 1}
    ]

    for note in notes:
        i = 0
        while i < len(scales):
            if note in scales[i]:
                i += 1
            else:
                scales.pop(i)
                databank.pop(i)

    if len(databank) > 0:
        return databank[0]
    else:
        return "desafinado"

main()
