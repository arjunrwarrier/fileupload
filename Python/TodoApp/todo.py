
while True:
    user_action = input("Type add , show, edit, complete or exit: ")
    user_action = user_action.strip()


    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            #reading file and storing it in the list todos
            with open('todo.txt','r') as file:
                todos = file.readlines()


            todos.append(todo)

            #writing the newly entered values into the file
            with open('todo.txt','w') as file:
                file.writelines(todos)

        case 'show':
           
            with open('todo.txt','r') as file:
                todos = file.readlines()
            
            for index,item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index+1}.{item}")
             


        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number-1

            with open('todo.txt','r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open('todo.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the number of completed todo: "))

            with open('todo.txt','r') as file:
                todos = file.readlines()
            
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)


            todos.pop(number-1)    

            with open('todo.txt','w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the todolist."
            print(message)

        case 'exit':
            break 
        # case _:  can be used to check if not value in cases are entered.
        #     print("Enter a correct statement")


print("End!")        