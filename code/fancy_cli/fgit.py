from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls, git

from PyInquirer import prompt

def print_banner(text):
    print(Figlet(font='slant').renderText(text))

def get_files():
    ls_output = ls().strip()
    files = ls_output.split("\n")
    return files

def generate_questions(files):
    questions = [{
        'type': 'checkbox',
        'name': 'files',
        'message': 'What would you like to commit',
        'choices': [{'name': file.strip()} for file in files],   
    }]
    return questions

class FancyGitAdd(cli.Application):
    VERSION = "1.3"
    commit = cli.Flag(['c', 'commit'], help="Commits the added files as well")

    def main(self):
        print_banner("Git fancy add")
        files = get_files()

        questions = generate_questions(files)
        answers = prompt(questions)
        git('add', answers['files'])
        if (self.commit):
            git('commit', '-m', 'add files')

if __name__ == "__main__":
    FancyGitAdd()

### TESTS

def test_get_files():
    files = get_files()
    assert len(files) == 5

def test_generate_questions():
    files = ["best.rb", "good.kt", "small.py"]
    questions = generate_questions(files)
    assert len(questions) == 1 # one question

    question = questions[0]
    assert question['type'] == 'checkbox' # has to be a checkbox
    assert len(question['choices']) == len(files) # same size as files


# fancy_ascii("Fancy Git Add")
# files = get_files()
# print("All files:")
# print(files)

# questions = [
#     {
#         'type': 'checkbox',
#         'name': 'files',
#         'message': 'What would you like to commit',
#         'choices': [{'name': file} for file in files],
#     }
# ]
# questions.append({
#     'type': 'confirm',
#     'message': 'Do you want to commit?',
#     'name': 'commit',
#     'default': False,
# })

# answers = prompt(questions)
# # pprint(answers)

# git('add', answers['files'])

# if answers['commit']:
#     git('commit', '-m', 'add files')