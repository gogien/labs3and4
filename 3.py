import csv
import pickle


class TableOperations:

    def __init__(self, table):
        for row in table:
            for i in range(len(row)):
                row[i] = None if row[i] == '' else row[i]
        self.table = table

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if stop is None:
            stop = start
        if copy_table:
            new_table = [row.copy() for row in self.table[start-1:stop]]
            return new_table
        else:
            return self.table[start-1:stop]

    def get_rows_by_index(self, *values, copy_table=False):
        if copy_table:
            new_table = [row.copy() for row in self.table if row[0] in values]
            return new_table
        else:
            return [row for row in self.table if row[0] in values]

    def get_column_types(self, by_number=True):
        column_types = {}

        for col_index in range(len(self.table[0])):
            if by_number:
                column_types[col_index] = self.get_column_type(col_index)
            else:
                column_types[' '.join(row[col_index] for row in self.table)] = self.get_column_type(col_index)

        return column_types

    def get_column_type(self, column):
        types = set()
        for row in self.table[1:]:
            value = row[column]
            if isinstance(value, int):
                types.add(int)
            elif isinstance(value, float):
                types.add(float)
            elif isinstance(value, bool):
                types.add(bool)
            elif value is None:
                pass
            else:
                types.add(str)

        return types.pop() if len(types) == 1 else str

    def set_column_types(self, types_dict, by_number=True):
        columns = {}
        for index in range(len(self.table[0])):
            columns[' '.join(row[index] for row in self.table)] = index
        for col_index, col_type in types_dict.items():
            if by_number:
                self.set_column_type(col_index, col_type)
            else:
                self.set_column_type(columns[col_index], col_type)

    def set_column_type(self, column, new_type):
        for row in self.table:
            value = row[column]
            if value is not None:
                if new_type == int:
                    row[column] = int(value)
                elif new_type == float:
                    row[column] = float(value)
                elif new_type == bool:
                    row[column] = bool(value)
                else:
                    row[column] = str(value)

    def get_values(self, column=0):
        result_column = []
        column_type = self.get_column_type(column)

        for row in self.table:
            value = row[column]
            result_column.append(column_type(value))

        return result_column

    def get_value(self, column=0):
        row = self.table[0]
        column_type = self.get_column_type(column)
        value = row[column]
        return column_type(value)

    def set_values(self, values, column=0):
        if column > max(len(row) for row in self.table)-1:
            for i in range(column - max([len(row) for row in self.table])+1):
                for row in self.table:
                    row.append(None)
            self.set_values(values, column)
        else:
            column_type = self.get_column_type(column)
            typed_values = []
            for value in values:
                if value is not None and value != '':
                    typed_values.append(column_type(value))
                else:
                    typed_values.append(None)
            if len(typed_values) == len(self.table):
                for i in range(len(self.table)):
                    self.table[i][column] = typed_values[i]
            elif len(typed_values) > len(self.table):
                for i in range(len(self.table)):
                    self.table[i][column] = typed_values[i]
                typed_values = typed_values[len(self.table):]
                for i in range(len(typed_values)):
                    child = [None]*max(len(row) for row in self.table)
                    child[0] = typed_values[i]
                    self.table.append(child)
            elif len(typed_values) < len(self.table):
                for i in range(len(typed_values)):
                    self.table[i][column] = typed_values[i]
                for i in range(len(typed_values), len(self.table)):
                    self.table[i][column] = None

    def set_value(self, value, column=0):
        column_type = self.get_column_type(column)
        typed_value = column_type(value)
        self.table[0][column] = typed_value

    def check_nones_rows(self):
        flag = True
        for item in self.table[-1]:
            if item is not None:
                flag = False
                break
        return flag

    def add(self, *columns):
        if all([self.get_column_type(column) in [int, float, bool] for column in columns]):
            temp = columns[0]
            columns = columns[1:]
            print(columns)
            for column in columns:
                for j in range(len(self.table)):
                    try:
                        self.table[j][temp] += self.table[j][column]
                    except TypeError:
                        self.table[j][temp] = self.table[j][column] if self.table[j][temp] is None else self.table[j][temp]
                    self.table[j][column] = '123'
            for row in range(len(self.table)):
                self.table[row] = list(filter(lambda x: x != '123', self.table[row]))
        else:
            raise TypeError('Нельзя выполнить сложение этих столбцов')

    def sub(self, *columns):
        if all([self.get_column_type(column) in [int, float, bool] for column in columns]):
            temp = columns[0]
            columns = columns[1:]
            for column in columns:
                for j in range(len(self.table)):
                    try:
                        self.table[j][temp] -= self.table[j][column]
                    except TypeError:
                        self.table[j][temp] = -self.table[j][column] if self.table[j][temp] is None else self.table[j][temp]
                    self.table[j][column] = '123'
            for row in range(len(self.table)):
                self.table[row] = list(filter(lambda x: x != '123', self.table[row]))
        else:
            raise TypeError('Нельзя выполнить вычитание этих столбцов')

    def mul(self, *columns):
        if all([self.get_column_type(column) in [int, float, bool] for column in columns]):
            temp = columns[0]
            columns = columns[1:]
            for column in columns:
                for j in range(len(self.table)):
                    try:
                        self.table[j][temp] *= self.table[j][column]
                    except TypeError:
                        self.table[j][temp] = 0
                    self.table[j][column] = '123'
            for row in range(len(self.table)):
                self.table[row] = list(filter(lambda x: x != '123', self.table[row]))
        else:
            raise TypeError('Нельзя выполнить умножение этих столбцов')

    def div(self, *columns):
        if all([self.get_column_type(column) in [int, float, bool] for column in columns]):
            temp = columns[0]
            columns = columns[1:]
            for column in columns:
                for j in range(len(self.table)):
                    try:
                        self.table[j][temp] /= self.table[j][column]
                        self.table[j][column] = '123'
                    except TypeError:
                        if self.table[j][temp] is None:
                            self.table[j][temp] = 0
                            self.table[j][column] = '123'
                        else:
                            raise 'Делить на None нельзя'
            for row in range(len(self.table)):
                self.table[row] = list(filter(lambda x: x != '123', self.table[row]))
        else:
            raise TypeError('Нельзя выполнить деление этих столбцов')

    def print_table(self):
        for i in range(len(self.table)):
            if i == len(self.table)-1 and self.check_nones_rows():
                pass
            else:
                if all([row[-1] is None for row in self.table]):
                    print('|'.join(list(map(str, self.table[i][:-1]))))
                else:
                    print('|'.join(list(map(str, self.table[i]))))


class TableCsv(TableOperations):

    def __init__(self, table):
        super().__init__(table)

    @staticmethod
    def save_table(table, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table)

    @staticmethod
    def load_table(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            table = [row for row in reader]
        return table


class TablePickle(TableOperations):

    def __init__(self, table):
        super().__init__(table)

    @staticmethod
    def load_table(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    @staticmethod
    def save_table(table, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(table, file)


class TxtTable(TableOperations):

    def __init__(self, table):
        super().__init__(table)

    @staticmethod
    def save_table(table, file_path):
        with open(file_path, 'w') as file:
            for row in table:
                file.write('|'.join(row)+'\n')


data = TableCsv(TableCsv.load_table('test1.csv'))
data.set_column_type(0, int)
data.set_column_type(1, int)
data.set_column_type(2, int)
data.set_column_type(3, int)
data.print_table()
print()
print(data.get_column_types())
data.mul(0, 1, 2, 3)
data.print_table()
TableCsv.save_table(data.table, 'test2.csv')