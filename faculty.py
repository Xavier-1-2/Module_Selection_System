def education_module_selection(year, semester):
    print("Module selection for the Faculty of Education and Liberal Studies")

    schools = {
        1: "School of Humanities & Social Sciences",
        2: "School of Technical & Vocational Education"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Choose from the options above.")


    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"EDU101": 150, "LIB102": 150, "EDU103": 150},
        (1, 2): {"EDU201": 150, "LIB202": 150, "EDU203": 150},
        (2, 1): {"EDU301": 150, "LIB302": 150, "EDU303": 150},
        (2, 2): {"EDU401": 150, "LIB402": 150, "EDU403": 150},
        (3, 1): {"EDU501": 150, "LIB502": 150, "EDU503": 150},
        (3, 2): {"EDU601": 150, "LIB602": 150, "EDU603": 150},
        (4, 1): {"EDU701": 150, "LIB702": 150, "EDU703": 150},
        (4, 2): {"EDU801": 150, "LIB802": 150, "EDU803": 150}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

        while True:
         select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")

def engine_module_selection(year, semester):
    print("Module selection for the Faculty of Engineering and Computing")

    schools = {
        1: "School of Engineering",
        2: "School of Computing & Information Technology"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")


    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"ENG101": 100, "CMP102": 120, "MAT103": 100},
        (1, 2): {"ENG201": 100, "CMP202": 120, "ELE203": 100},
        (2, 1): {"ENG301": 100, "CMP302": 120, "SYS303": 100},
        (2, 2): {"ENG401": 100, "CMP402": 120, "NET403": 100},
        (3, 1): {"ENG501": 100, "CMP502": 120, "ELE503": 100},
        (3, 2): {"ENG601": 100, "CMP602": 120, "SYS603": 100},
        (4, 1): {"ENG701": 100, "CMP702": 120, "NET703": 100},
        (4, 2): {"ENG801": 100, "CMP802": 120, "ELE803": 100}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")


def built_envi_module_selection(year, semester):
    print("Module selection for the Faculty of The Built Environment")

    schools = {
        1: "School of Building & Land Management",
        2: "Caribbean School of Architecture"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")


    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"ARC101": 80, "CIV102": 80, "BTE103": 80},
        (1, 2): {"ARC201": 80, "CIV202": 80, "BTE203": 80},
        (2, 1): {"ARC301": 80, "CIV302": 80, "BTE303": 80},
        (2, 2): {"ARC401": 80, "CIV402": 80, "BTE403": 80},
        (3, 1): {"ARC501": 80, "CIV502": 80, "BTE503": 80},
        (3, 2): {"ARC601": 80, "CIV602": 80, "BTE603": 80},
        (4, 1): {"ARC701": 80, "CIV702": 80, "BTE703": 80},
        (4, 2): {"ARC801": 80, "CIV802": 80, "BTE803": 80}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")
    
def cobam_module_selection(year, semester):
    print("Module selection for the College of Business and Management Sciences")

    schools = {
        1: "School of Business Administration",
        2: "School of Hospitality & Tourism Management",
        3: "Joan Duncan School of Entrepreneurship, Ethics and Leadership",
        4: "School of Advanced Management"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")

    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"BUS101": 200, "ACC102": 200, "MKT103": 200},
        (1, 2): {"BUS201": 200, "ACC202": 200, "FIN203": 200},
        (2, 1): {"BUS301": 200, "MKT302": 200, "FIN303": 200},
        (2, 2): {"BUS401": 200, "ACC402": 200, "MGT403": 200},
        (3, 1): {"BUS501": 200, "ACC502": 200, "FIN503": 200},
        (3, 2): {"BUS601": 200, "ACC602": 200, "MGT603": 200},
        (4, 1): {"BUS701": 200, "ACC702": 200, "FIN703": 200},
        (4, 2): {"BUS801": 200, "ACC802": 200, "MGT803": 200}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")

def cohs_module_selection(year, semester):
    print("Module selection for the College of Health Sciences")

    schools = {
        1: "Caribbean School of Nursing",
        2: "School of Allied Health & Wellness",
        3: "School of Pharmacy"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")

    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"BIO101": 120, "CHE102": 120, "HSC103": 120},
        (1, 2): {"BIO201": 120, "CHE202": 120, "HSC203": 120},
        (2, 1): {"BIO301": 120, "HSC302": 120, "NUR303": 120},
        (2, 2): {"BIO401": 120, "HSC402": 120, "NUR403": 120},
        (3, 1): {"BIO501": 120, "CHE502": 120, "HSC503": 120},
        (3, 2): {"BIO601": 120, "CHE602": 120, "NUR603": 120},
        (4, 1): {"BIO701": 120, "HSC702": 120, "NUR703": 120},
        (4, 2): {"BIO801": 120, "CHE802": 120, "NUR803": 120}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")

def joint_comohvs_module_selection(year, semester):
    print("Module selection for the Joint College of Medicine, Oral Health & Veterinary Sciences")

    schools = {
        1: "School of Public Health & Health Technology",
        2: "College of Oral Health Sciences"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")


    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"MED101": 60, "DEN102": 60, "VET103": 60},
        (1, 2): {"MED201": 60, "DEN202": 60, "VET203": 60},
        (2, 1): {"MED301": 60, "DEN302": 60, "VET303": 60},
        (2, 2): {"MED401": 60, "DEN402": 60, "VET403": 60},
        (3, 1): {"MED501": 60, "DEN502": 60, "VET503": 60},
        (3, 2): {"MED601": 60, "DEN602": 60, "VET603": 60},
        (4, 1): {"MED701": 60, "DEN702": 60, "VET703": 60},
        (4, 2): {"MED801": 60, "DEN802": 60, "VET803": 60}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")
   
def law_module_selection(year, semester):
    print("Module selection for the Faculty of Law")

    # Law has no school
    school_name = "N/A"

    module_catalog = {
        (1, 1): {"LAW101": 90, "LAW102": 90, "LAW103": 90},
        (1, 2): {"LAW201": 90, "LAW202": 90, "LAW203": 90},
        (2, 1): {"LAW301": 90, "LAW302": 90, "LAW303": 90},
        (2, 2): {"LAW401": 90, "LAW402": 90, "LAW403": 90},
        (3, 1): {"LAW501": 90, "LAW502": 90, "LAW503": 90},
        (3, 2): {"LAW601": 90, "LAW602": 90, "LAW603": 90},
        (4, 1): {"LAW701": 90, "LAW702": 90, "LAW703": 90},
        (4, 2): {"LAW801": 90, "LAW802": 90, "LAW803": 90}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")


def foss_module_selection(year, semester):
    print("Module selection for the Faculty of Science and Sport")

    schools = {
        1: "School of Mathematics & Statistics",
        2: "School of Natural & Applied Sciences",
        3: "Caribbean School of Sports Sciences"
    }

    print("Schools:")
    for key, value in schools.items():
        print(f"{key}. {value}")

    while True:
        school_choice = int(input("Select your school: "))
        if school_choice in schools:
            break  # valid, exit loop
        else:
            print("Invalid school selection. Try again.")

    school_name = schools[school_choice]
    print(f"Selected school: {school_name}")

    module_catalog = {
        (1, 1): {"SCI101": 180, "PHY102": 180, "SPT103": 180},
        (1, 2): {"SCI201": 180, "PHY202": 180, "SPT203": 180},
        (2, 1): {"SCI301": 180, "PHY302": 180, "SPT303": 180},
        (2, 2): {"SCI401": 180, "PHY402": 180, "SPT403": 180},
        (3, 1): {"SCI501": 180, "PHY502": 180, "SPT503": 180},
        (3, 2): {"SCI601": 180, "PHY602": 180, "SPT603": 180},
        (4, 1): {"SCI701": 180, "PHY702": 180, "SPT703": 180},
        (4, 2): {"SCI801": 180, "PHY802": 180, "SPT803": 180}
    }

    if (year, semester) in module_catalog:
        modules = module_catalog[(year, semester)]
        print("Available modules:", ", ".join(modules.keys()))

    while True:
        select_mod = input("Select module of choice: ").strip().upper()
        if select_mod in modules:
            if modules[select_mod] > 0:
                modules[select_mod] -= 1
                print(f"{select_mod} was successfully selected.")
                return select_mod, school_name
            else:
                print(f"{select_mod} is at maximum capacity.")
        else:
            print("Invalid module code entered. Try again.")
