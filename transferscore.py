from music21 import converter, instrument, note, chord

# 用musescore导出musicxml文件，加载 MusicXML 文件
score = converter.parse("demo.musicxml")

parts = score.parts
if len(parts) > 0:
    part = parts[0]
else:
    print("乐谱中没有找到任何声部")
    exit()

key_signature = score.analyze("key")
print(f"Detected key: {key_signature}")


def extract_notes_by_measure(part):
    measures = part.getElementsByClass("Measure")
    notes_by_measure = []

    for measure in measures:
        measure_notes = []
        for element in measure.notesAndRests:  # 只获取音符和休止符
            if isinstance(element, note.Note):
                # 如果是单个音符，获取其音名和时值
                measure_notes.append((str(element.pitch), element.quarterLength))
            elif isinstance(element, chord.Chord):
                # 如果是和弦，获取其所有音名和时值
                measure_notes.append(
                    (".".join(str(p) for p in element.pitches), element.quarterLength)
                )
            elif isinstance(element, note.Rest):
                # 如果是休止符，用 'r' 表示，并附上时值
                measure_notes.append(("r", element.quarterLength))
            # 可以根据需要添加对其他元素（如记号、动态标记等）的处理

        notes_by_measure.append(measure_notes)

    return notes_by_measure


def to_jianpu(note_info, offset):
    pitch_to_jianpu = [
        "C",
        "D",
        "E",
        "F",
        "G",
        "A",
        "B",
    ]

    jianpu_notes = []
    for pitch, duration in note_info:
        # print(pitch[0],duration)
        if "." in pitch:
            continue
        if(pitch[0] != "r"):
            jianpu_pitch = str((pitch_to_jianpu.index(pitch[0])+offset) % 7)

            if "#" in pitch:
                jianpu_pitch += "#"
            if "-" in pitch:
                jianpu_pitch += "$"
            if "2" in pitch:
                jianpu_pitch += ","
            if "4" in pitch:
                jianpu_pitch += "'"
        else:
            jianpu_pitch = "0"
        if duration == 4:
            jianpu_note = f"{jianpu_pitch}---"
        elif duration == 4.0:
            jianpu_note = f"{jianpu_pitch}---"
        elif duration == 3:
            jianpu_note = f"{jianpu_pitch}--"
        elif duration == 2:
            jianpu_note = f"{jianpu_pitch}-"
        elif duration == 1.5:
            jianpu_note = f"{jianpu_pitch}."
        elif duration == 1:
            jianpu_note = f"{jianpu_pitch}"
        elif duration == 0.5:
            jianpu_note = f"{jianpu_pitch}/"
        elif duration == 0.25:
            jianpu_note = f"{jianpu_pitch}//"
        else:
            jianpu_note = f"{jianpu_pitch}({duration})"

        jianpu_notes.append(jianpu_note)

    return " ".join(jianpu_notes)


notes_by_measure = extract_notes_by_measure(part)

# 生成番茄简谱的脚本，http://zhipu.lezhi99.com/Zhipu-index.html
jianpu_groups = []
group_size = 4  # 控制每行几个小节
offset = 4 # 控制转调
for i, measure_notes in enumerate(notes_by_measure, start=1):
    jianpu_result = to_jianpu(measure_notes, offset)
    if (i - 1) % group_size == 0:
        jianpu_groups.append([])
    jianpu_groups[-1].append(jianpu_result)
    if i % group_size == 0 or i == len(notes_by_measure):
        print("Q:", " | ".join(jianpu_groups[-1]))
