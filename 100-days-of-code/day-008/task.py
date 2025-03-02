def life_in_weeks(age):
    total_lifespan = 90
    weeks_in_a_year = 52
    weeks_left = (total_lifespan - age) * weeks_in_a_year
    print(f"You have {weeks_left} weeks left.")


life_in_weeks(56)
