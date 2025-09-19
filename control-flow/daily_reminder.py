tasks = input("Enter a tasks description:").lower()
priority = input("Priority high, medium, low:").lower()
time_bound = input("Is it time-bound? yes or no:").lower()
match priority:
    case "high" | "medium" | "low":
        if time_bound == 'yes':
            print(f"{tasks} is a {priority} priority task that requires immediate attention today!")
        elif time_bound =="no":
            print(f"{tasks} is a {priority} priority task. Consider completing it when you have free time.!")
        else:
            print(f"please indicate if {tasks} is time based with yes/no")
    case _:
            print("Invalid priority level! Please enter either high, medium, or low,")