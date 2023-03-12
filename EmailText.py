import json

class EmailText():
    def input(self):
        file_name = 'Input.json'
        with open(file_name, 'r', encoding='utf-8') as f:
            my_data = json.load(f)
        return my_data

    def build_email_text(self):
        my_data = self.input()
        text = f'''Vacation Type: {my_data['type_of_leave']}
Vacation starts on: {my_data['start']}
Vacantion ends on: {my_data['end']}
        '''
        return text