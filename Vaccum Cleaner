def vacuum_world():

    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter Location of Vacuum (A/B): ")  # user input for vacuum location
    status_input = input("Enter status of " + location_input + " (0 for Clean, 1 for Dirty): ")  # user input for status
    status_input_complement = input("Enter status of other room (0 for Clean, 1 for Dirty): ")

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1  # cost for moving right
                print("COST for moving RIGHT: " + str(cost))
 
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("COST for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action. Cost: " + str(cost))

        elif status_input == '0':
            print("Location A is already clean.")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to Location B.")
                cost += 1  # cost for moving right
                print("COST for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean. No action. Cost: " + str(cost))

    elif location_input == 'B':
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            cost += 1  # cost for suck
            print("COST for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # cost for moving left
                print("COST for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("COST for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action. Cost: " + str(cost))

        elif status_input == '0':
            print("Location B is already clean.")
            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to Location A.")
                cost += 1  # cost for moving left
                print("COST for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1  # cost for suck
                print("Cost for SUCK: " + str(cost))
                print("Location A has been Cleaned.")
            else:
                print("Location A is already clean. No action. Cost: " + str(cost))

    else:
        print("Invalid vacuum location entered.")

    print("GOAL STATE: ")
    print(goal_state)
    print("Performance Measurement (Total cost): " + str(cost))
