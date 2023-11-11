import csv


class Worker:
    def __init__(self, name, surname, department, salary, worker__id):
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
        self.__id = worker__id

    def get_id(self):
        return self.__id

    def set_id(self, new_id):

        self.__id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_department(self):
        return self.department

    def set_department(self, new_department):
        self.department = new_department

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary


class WorkerDB:
    def __init__(self):
        self.workers = []
        self.load_from_csv("workers.csv")

    def read(self):
        return self.workers

    def add(self, worker):
        self.workers.append(worker)

    def edit(self, worker__id, new_worker):
        for index, worker in enumerate(self.workers):
            if worker.get_id() == worker__id:
                self.workers[index] = new_worker

    def delete(self, worker_id):
        for worker in self.workers:
            if worker.get_id() == worker_id:
                self.workers.remove(worker)
                return True

    def load_from_csv(self, filename):
        self.workers = []
        with open(filename, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                worker = Worker(
                    row["Name"],
                    row["Surname"],
                    row["Department"],
                    float(row["Salary"]),
                    int(row["ID"])
                )
                self.workers.append(worker)


    def dec_sort(func):
        def wrapper(self):
            sorted_workers = sorted(self.workers, key=lambda worker: worker.get_name())
            func(self, sorted_workers)
        return wrapper

    @dec_sort
    def sorted_by_name(self, sorted_workers):
        for worker in sorted_workers:
            print(
                f"ID: {worker.get_id()}, Name: {worker.get_name()}"
                f", Department: {worker.get_department()}, Salary: {worker.get_salary()}")

    def dec_search(func):
        def wrapper(self, name):
            for worker in self.workers:
                if worker.get_name() == name:
                    print(
                        f"ID: {worker.get_id()}, Name: {worker.get_name()}"
                        f", Department: {worker.get_department()}, Salary: {worker.get_salary()}")
                    func(self, name)
        return wrapper

    @dec_search
    def search_by_name(self, name):
        pass




if __name__ == '__main__':
    worker_db = WorkerDB()

    while True:
        print("1. Add Worker")
        print("2. Edit Worker")
        print("3. Delete Worker")
        print("4. Print Workers")
        print("5.Sorted list")
        print("6.Search")
        print("7. Exit")


        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter worker's name: ")
            surname = input("Enter worker's surname: ")
            department = input("Enter worker's department: ")
            salary = float(input("Enter worker's salary: "))
            worker__id = int(input("Enter worker's ID: "))
            worker = Worker(name, surname, department, salary, worker__id)
            worker_db.add(worker)

        elif choice == '2':
            worker_id = int(input("Enter the ID of the worker to edit: "))
            new_name = input("Enter the new name: ")
            new_surname = input("Enter the new surname: ")
            new_department = input("Enter the new department: ")
            new_salary = float(input("Enter the new salary: "))
            new_worker = Worker(new_name, new_surname, new_department, new_salary, worker_id)
            worker_db.edit(worker_id, new_worker)

        elif choice == '3':
            worker_id = int(input("Enter the ID of the worker to delete: "))
            worker_db.delete(worker_id)

        elif choice == '4':
            for worker in worker_db.read():
                print(f"ID: {worker.get_id()}, Name: {worker.get_name()}, Department: {worker.get_department()}"
                      f", Salary: {worker.get_salary()}")

        elif choice == '5':
            worker_db.sorted_by_name()

        elif choice == '6':
            name = input("Enter the name: ")
            worker_db.search_by_name(name)

        elif choice == '7':
            break
        else:
            print("Invalid choice. Please select a valid option.")



