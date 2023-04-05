"""
models.py
by Valentin Piombo
urMelody
April 2023
"""


class Note:
    label: str
    label_solfege: str
    chromatic_before: object
    chromatic_after: object
    conversion_solfege = {
        "C": "Do",
        "C#": "Do#",
        "D": "Re",
        "D#": "Re#",
        "E": "Mi",
        "F": "Fa",
        "F#": "Fa#",
        "G": "Sol",
        "G#": "Sol#",
        "A": "La",
        "A#": "La#",
        "B": "Si",
    }

    def __int__(self, label, chromatic_before, chromatic_after):
        self.label = label
        self.label_solfege = self.conversion_solfege[label]
        self.chromatic_before = chromatic_before
        self.chromatic_after = chromatic_after


class Scale:
    label: str
    sequence: list[str]
    notes: list[object]
    type: str

    def __str__(self):
        return f"{self.type.title()} scale of {self.label}"

    def notes_builder(self):
        self.notes = [self.label]
        for step in self.sequence:
            # if step == "w"
            pass

class ChromaticScale(Scale):
    sequence = ["h"] * 12
    type = "chromatic"


class MajorScale(Scale):
    sequence = ["w", "w", "h", "w", "w", "w", "h"]
    type = "major"


class NaturalMinorScale(Scale):
    sequence = ["w", "h", "w", "w", "h", "w", "w"]
    type = "natural minor"


class HarmonicMinorScale(Scale):
    sequence = ["w", "h", "w", "w", "h", "a2", "h"]
    type = "harmonic minor"


class MelodicMinorScale(Scale):
    sequence = ["w", "h", "w", "w", "W", "w", "h"]
    type = "melodic scale"


if __name__ == '__main__':
    # DEBUG ZONE
    c_major = Scale()
    c_major.label = "C Major"
    print(c_major)
