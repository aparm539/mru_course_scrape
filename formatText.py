import re
class Course:
    def __init__(self, code, name, credits,lecture_hours,lab_hours,tutorial_hours, other_hours, lecture_schedule_type, other_hours_schedule_type, description, prerequisites, notes):
        self.code = code
        self.name = name
        self.credits = credits
        self.lecture_hours = lecture_hours
        self.lab_hours = lab_hours
        self.tutorial_hours = tutorial_hours
        self.other_hours = other_hours
        self.other_hours_schedule_type = other_hours_schedule_type
        self.lecture_schedule_type = lecture_schedule_type
        self.description = description
        self.prerequisites = prerequisites
        self.notes = notes

    def __repr__(self):
        return f"{self.code} - {self.name}\nCredits: {self.credits}\n"\
               f"Lecture Hours: {self.lecture_hours}\nLab Hours: {self.lab_hours}\nTutorial Hours: {self.tutorial_hours}\n"\
               f"Other Hours: {self.other_hours}\nLecture Type: {self.lecture_schedule_type}\nOther Hours Type: {self.other_hours_schedule_type}\n" \
               f"Description: {self.description}\nPrerequisites: {self.prerequisites}\nNotes: {self.notes}"

with open('courseDescriptions.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split text into course descriptions
course_texts = text.split('---')


# List to store Course objects
courses = []

# Regex patterns
course_pattern = re.compile(r'Description: (\w+ \d+) - (.+)')
credit_pattern = re.compile(r'Credit\(s\): (\d+(\.\d+)?)')
lab_hours_pattern = re.compile(r'Lab Hour\(s\): (\d+)')
lecture_hours_pattern = re.compile(r'Lecture Hour\(s\): (\d+)')
tutorial_hours_pattern = re.compile(r'Tutorial Hour\(s\): (\d+)')
other_hours_pattern = re.compile(r'Other Hour\(s\): (\d+)')
lecture_schedule_type_pattern = re.compile(r'(?<=Lecture Hours Schedule Type: ).*')
other_hours_schedule_type_pattern = re.compile(r'Other Hours Schedule Type: ([\w\s,]+)')
prerequisite_pattern = re.compile(r'(?<=Prerequisite\(s\): ).*')
note_pattern = re.compile(r'Note: (.+)')
lecture_schedule_type_remove_pattern = re.compile(r'Lecture Hours Schedule Type: .*')
prerequisite_remove_pattern = re.compile(r'Prerequisite\(s\): .*')

# Parse each course text and create Course object
for course_text in course_texts:
    course_match = course_pattern.search(course_text)
    if not course_match:
        continue

    code = course_match.group(1)
    name = course_match.group(2)

    # Remove matched course pattern from course_text
    course_text = re.sub(course_pattern, '', course_text)

    credit_match = credit_pattern.search(course_text)
    credits = credit_match.group(1) if credit_match else None

    # Remove matched credit pattern from course_text
    course_text = re.sub(credit_pattern, '', course_text) if credit_match else course_text

    lab_hours_match = lab_hours_pattern.search(course_text)
    lab_hours = int(lab_hours_match.group(1)) if lab_hours_match else None

    # Remove matched lab_hours pattern from course_text
    course_text = re.sub(lab_hours_pattern, '', course_text) if lab_hours_match else course_text

    lecture_hours_match = lecture_hours_pattern.search(course_text)
    lecture_hours = int(lecture_hours_match.group(1)) if lecture_hours_match else None

    # Remove matched lecture_hours pattern from course_text
    course_text = re.sub(lecture_hours_pattern, '', course_text) if lecture_hours_match else course_text

    tutorial_hours_match = tutorial_hours_pattern.search(course_text)
    tutorial_hours = int(tutorial_hours_match.group(1)) if tutorial_hours_match else None

    # Remove matched tutorial_hours pattern from course_text
    course_text = re.sub(tutorial_hours_pattern, '', course_text) if tutorial_hours_match else course_text

    other_hours_match = other_hours_pattern.search(course_text)
    other_hours = int(other_hours_match.group(1)) if other_hours_match else None

    # Remove matched other_hours pattern from course_text
    course_text = re.sub(other_hours_pattern, '', course_text) if other_hours_match else course_text
    
    lecture_schedule_type_match = lecture_schedule_type_pattern.search(course_text)
    lecture_schedule_type = lecture_schedule_type_match.group(0) if lecture_schedule_type_match else None
    lecture_schedule_type = lecture_schedule_type.replace(",","") if lecture_schedule_type else None
    

    # Remove matched schedule_type pattern from course_text
    course_text = re.sub(lecture_schedule_type_pattern, '', course_text) if lecture_schedule_type_match else course_text
    course_text = re.sub(lecture_schedule_type_remove_pattern, '', course_text)
    
    other_hours_schedule_type_match = other_hours_schedule_type_pattern.search(course_text)
    other_hours_schedule_type = other_hours_schedule_type_match.group(1) if other_hours_schedule_type_match else None
    other_hours_schedule_type = other_hours_schedule_type.replace(",","") if other_hours_schedule_type else None

    # Remove matched schedule_type pattern from course_text
    course_text = re.sub(other_hours_schedule_type_pattern, '', course_text) if other_hours_schedule_type_match else course_text

    prerequisite_match = prerequisite_pattern.search(course_text)
    prerequisites = prerequisite_match.group(0) if prerequisite_match else None

    # Remove matched prerequisite pattern from course_text
    course_text = re.sub(prerequisite_pattern, '', course_text) if prerequisite_match else course_text
    course_text = re.sub(prerequisite_remove_pattern, '', course_text)
    
    note_match = note_pattern.search(course_text)
    notes = note_match.group(1) if note_match else None

    # Remove matched note pattern from course_text
    course_text = re.sub(note_pattern, '', course_text) if note_match else course_text
    
    description = course_text.strip()


    # Create and store Course object
    courses.append(Course(code, name, credits, lecture_hours, lab_hours, tutorial_hours, other_hours, lecture_schedule_type, other_hours_schedule_type, description, prerequisites, notes))

# Print out Course objects
with open('courseList.txt', 'w', encoding='utf-8') as f:    
    for course in courses:
        f.write(f'{course}\n')
        f.write('---\n')
