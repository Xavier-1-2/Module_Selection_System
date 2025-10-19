from kafka import KafkaProducer
import json
from faculty import (
    education_module_selection,
    engine_module_selection,
    built_envi_module_selection,
    cobam_module_selection,
    cohs_module_selection,
    joint_comohvs_module_selection,
    law_module_selection,
    foss_module_selection
)

# Map faculty numbers to names
faculty_names = {
    1: "Faculty of Education and Liberal Studies",
    2: "Faculty of Engineering and Computing",
    3: "Faculty of The Built Environment",
    4: "College of Business and Management Sciences",
    5: "College of Health Sciences",
    6: "Joint College of Medicine, Oral Health & Veterinary Sciences",
    7: "Faculty of Law",
    8: "Faculty of Science and Sport"
}

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

faculty_mapping = {
    1: education_module_selection,
    2: engine_module_selection,
    3: built_envi_module_selection,
    4: cobam_module_selection,
    5: cohs_module_selection,
    6: joint_comohvs_module_selection,
    7: law_module_selection,
    8: foss_module_selection
}

#Allows program to run multiple times
while True:
    print("\nWelcome to the Revised Module Selection System!")
    year = int(input("Enter year of study to matriculate into: "))
    while year < 1 or year > 5:
        print("Invalid year selection.")
        year = int(input(f"Please enter a year between 0 and 5."))
    print(f"Year Selected: {year}")

    semester = int(input("Enter semester of study to matriculate into (1 or 2): "))
    while semester not in [1, 2]:
        print("Invalid semester selection. Please enter 1 or 2.")
        semester = int(input("Enter semester of study to matriculate into (1 or 2): "))
    
    print("Faculties:")
    for num, name in faculty_names.items():
        print(f"{num}. {name}")
    
    faculty = int(input("Select the faculty to which you belong: "))
    while faculty not in range(1, 9):
        print("Invalid faculty selection. Choose from the list of options above.")
        faculty =int(input("Select the faculty to which you belong: "))
    faculty_name = faculty_names.get(faculty, "Unknown Faculty")
    
    if faculty in faculty_mapping:
        result = faculty_mapping[faculty](year, semester)
        
        if result:
            selected_module, school_name = result  # Expect the function to return both
            message = {
                "year": year,
                "semester": semester,
                "faculty": faculty_name,
                "school": school_name,
                "module": selected_module
            }
            producer.send("module_selection_topic", message)
            producer.flush()
            print(f"Module selection sent to Kafka: {message}")
        else:
            print("No module selected. Nothing sent to Kafka.")
    
    
    # Ask if user wants to continue
    cont = input("Do you want to select another module? (y/n): ").strip().lower()
    if cont != "y":
        print("Exiting Module Selection System.")
        break
