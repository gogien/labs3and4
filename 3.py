import csv

# загрузка таблицы
def load_table(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        table = [row for row in reader]
    return table

# сохранение таблицы
def save_table(table, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)


class TableOperations:
    def __init__(self, table):
        self.table = table

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        if not isinstance(start, int) or (stop is not None and not isinstance(stop, int)):
            raise ValueError("Invalid input: start and stop should be integers.")
        
        if stop is not None and start > stop:
            raise ValueError("Invalid input: start should be less than or equal to stop.")
        
        if copy_table:
            new_table = [row.copy() for row in self.table[start:stop]]
            return new_table
        else:
            return self.table[start:stop]

    def get_rows_by_index(self, *values, copy_table=False):
        if not values:
            raise ValueError("Invalid input: at least one value should be provided.")
        
        if copy_table:
            new_table = [row.copy() for row in self.table if row[0] in values]
            return new_table
        else:
            return [row for row in self.table if row[0] in values]

    def get_column_types(self, by_number=True):
        column_types = {}

        if by_number:
            for col_index in range(len(self.table[0])):
                column_types[col_index] = self._get_column_type(col_index)
        else:
            for col_name in self.table[0]:
                column_types[col_name] = self._get_column_type(col_name)

        return column_types

    def _get_column_type(self, column):
        # Внутренняя функция для определения типа значений в столбце
        types = set()
        for row in self.table[1:]:
            value = row[column]
            if isinstance(value, int):
                types.add(int)
            elif isinstance(value, float):
                types.add(float)
            elif isinstance(value, bool):
                types.add(bool)
            else:
                types.add(str)

        # Если встретились разные типы, вернем str
        return types.pop() if len(types) == 1 else str

    def set_column_types(self, types_dict, by_number=True):
        if by_number:
            for col_index, col_type in types_dict.items():
                self._set_column_type(col_index, col_type)
        else:
            for col_name, col_type in types_dict.items():
                self._set_column_type(col_name, col_type)

    def _set_column_type(self, column, new_type):
        # Внутренняя функция для установки нового типа значений в столбце
        for row in self.table:
            value = row[column]
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
        column_type = self._get_column_type(column)

        for row in self.table:
            value = row[column]
            result_column.append(column_type(value))

        return result_column

    def get_value(self, column=0):
        row = self.table[0]
        column_type = self._get_column_type(column)
        value = row[column]
        return column_type(value)

    def set_values(self, values, column=0):
        column_type = self._get_column_type(column)
        typed_values = [column_type(value) for value in values]

        for i, row in enumerate(self.table):
            row[column] = typed_values[i]

    def set_value(self, value, column=0):
        column_type = self._get_column_type(column)
        typed_value = column_type(value)
        self.table[column] = typed_value

    def print_table(self):
        for row in self.table:
            print(row)