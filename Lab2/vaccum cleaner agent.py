def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0
    
    location_input = input("Enter Location of Vacuum (A or B): ").strip().upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    status_input_complement = input(f"Enter status of {'B' if location_input == 'A' else 'A'} (0 for Clean, 1 for Dirty): ").strip()

    print("Initial Location Condition:", goal_state)

    if location_input == 'A':
        if status_input == '1':
            goal_state['A'] = '0'
            cost += 1
            print("Location A has been Cleaned. Cost for CLEANING A:", cost)

        if status_input_complement == '1':
            cost += 1
            goal_state['B'] = '0'
            cost += 1
            print("Location B has been Cleaned. Cost for SUCK:", cost)
        else:
            print("Location B is already clean. No action needed.")

    else:
        if status_input == '1':
            goal_state['B'] = '0'
            cost += 1
            print("Location B has been Cleaned. Cost for CLEANING B:", cost)

        if status_input_complement == '1':
            cost += 1
            goal_state['A'] = '0'
            cost += 1
            print("Location A has been Cleaned. Cost for SUCK:", cost)
        else:
            print("Location A is already clean. No action needed.")

    print("GOAL STATE:", goal_state)
    print("Total Performance Measurement (Cost):", cost)

vacuum_world()
