def objective_function(x):
    return -(x  ** 2) + 10


def hill_climbing(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)

    for i in range(max_iterations):
        left = current - step_size
        right = current + step_size

        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:

            break

    return current, current_value



start = float(input("Enter the starting value: "))
step_size = float(input("Enter the step size: "))
max_iterations = int(input("Enter the maximum number of iterations: "))


best_position, best_value = hill_climbing(start, step_size, max_iterations)


print("\nBest position=", best_position)
print("Maximum value=", best_value)



#output


"""Enter the starting value: 5
Enter the step size: 4
Enter the maximum number of iterations: 60

Best position= 1.0
Maximum value= 9.0"""