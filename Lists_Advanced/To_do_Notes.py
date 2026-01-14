def to_do_notes():
    notes = []

    while True:
        note = input()
        if note == 'End':
            break
        notes.append(note)
    sorted_notes = sorted(notes, key=lambda x: int(x.split('-')[0]))
    sorted_text = [note.split('-')[1] for note in sorted_notes]
    return sorted_text

result = to_do_notes()
print(result)
