# from __future__ import print_function, unicode_literals

from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls
# from plumbum.cmd import ls, git
# from PyInquirer import prompt, print_json
#from pprint import pprint

def print_banner(text):
    print(Figlet(font='slant').renderText(text)) 

# def get_files():
#     ls_output = ls() # todo: add strip in red green refactor
#     files = ls_output.split("\n")
#     return files

# def generate_questions(files, commit_flag):

class FancyGitAdd(cli.Application):
    VERSION = "1.3"
    # commit = cli.Flag(['c', 'commit'], help="Commits the added files as well")

    def main(self):
        print_banner("Git fancy add")
        # if (self.commit):
            # print("I see you also want to commit")

if __name__ == "__main__":
    FancyGitAdd()


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