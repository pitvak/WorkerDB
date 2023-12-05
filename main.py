import csv
import unittest


def id_generator(start=1):
    current_id = start
    while True:
        yield current_id
        current_id += 1


id_gen = id_generator()


class Worker:
    def __init__(self, name, surname, department, salary, _id):
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary
        self._id = next(id_gen)

    def get_id(self):
        return self._id

    def set_id(self, new_id):

        self._id = new_id

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

    def edit(self, worker_id, new_worker):
        for index, worker in enumerate(self.workers):
            if worker.get_id() == worker_id:
                self.workers[index] = new_worker

    def delete(self, worker_id):
        for worker in self.workers:
            if worker.get_id() == worker_id:
                self.workers.remove(worker)
                return True

    def load_from_csv(self, filename):
        while True:
            try:
                #file_input = input("Enter the filename: ")
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
                        id_gen = id_generator(start=int(row["ID"]) + 1)
                        self.workers.append(worker)
                break
            except FileNotFoundError:
                print("File not found.")

    def dec_sort(func):
        def wrapper(self, *args):
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
                    result = func(self, name)
                    return result

        return wrapper

    @dec_search
    def search_by_name(self, name):
        result = []
        for worker in self.workers:
            if worker.get_name() == name:
                result.append(worker)
        return result


class TestCollection(unittest.TestCase):
    def setUp(self):
        self.worker_db = WorkerDB()

    def test_add(self):
        worker = Worker("GGGg", "Dhhh", "IhhT", "8999", "4")
        self.worker_db.add(worker)
        self.assertEqual(len(self.worker_db.workers), 4)

    def test_delete(self):
        self.worker_db.delete(1)
        self.assertEqual(len(self.worker_db.workers), 3)

    #def test_edit(self):

        #self.worker_db.edit(1, "olga")
        #self.assertEqual(len(self.worker_db.workers.name), "olga")

    def test_sort(self):
        self.worker_db.sorted_by_name("name")
        first_worker_name = self.worker_db.workers[0].get_name()
        self.assertEqual(first_worker_name, "John")

    def test_search(self):
        #self.assertEqual(len(self.worker_db.workers.search_by_name("Jonh")), 1)
        search_result = self.worker_db.search_by_name("John")
        self.assertEqual(len(search_result), 1)

if __name__ == '__main__':
    unittest.main()
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
            #salary = float(input("Enter worker's salary: "))
            while True:
                try:
                    salary = float(input("Enter worker's salary: "))
                    break
                except ValueError:
                    print("Invalid value.")
            worker = Worker(name, surname, department, salary)
            worker_db.add(worker)

        elif choice == '2':
            worker_id = int(input("Enter the ID of the worker to edit: "))
            new_name = input("Enter the new name: ")
            new_surname = input("Enter the new surname: ")
            new_department = input("Enter the new department: ")
            #new_salary = float(input("Enter the new salary: "))
            while True:
                try:
                    new_salary = float(input("Enter new worker's salary: "))
                    break
                except ValueError:
                    print("Invalid value.")

            new_worker = Worker(new_name, new_surname, new_department, new_salary)

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

