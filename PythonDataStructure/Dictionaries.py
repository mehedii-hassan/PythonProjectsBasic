#creating dictionaries----------
studentId={
    "101":"Mehedi Hassan",
    "102": "Mou",
    "103": "Moon",
    "104": "Mayan",
    "105": "Emu",
    "106": "Tonu",
    3:"dhagh"
}
print(studentId)
print(studentId["104"])
print(studentId.get("105"))
print(studentId.get(3))
print(studentId.get(6))
print(studentId.get(5,"not a valid key"))
