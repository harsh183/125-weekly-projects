
  ## What is Pylint
      - Pylint is a tool that checks for errors in Python code. It is useful because it tries to enforce a coding standard. It displays some messages about warnings and errors found in the file and gives your code an overall score.
      - Pylint isn't the gospel and sometimes may warn you about things you purposely have done.
  ## How to use Pylint
      - First, make sure you have Pylint installed.
          - To check if you already have it installed:
              - ` pip list ` will give you a list of all of your installed Python libraries.
              - ` pip show pylint ` will show the details of your installed pylint package if you already have it installed.
      - If you do not have it installed, install it by running this.
            - ```python
              pip install pylint 
              ```
      - Pylint is meant to be called from the command line. The usage is
          - ```python
            pylint [options] modules_or_packages
            #example
            pylint potatoes.py
            ```
            - A module is just a file consisting of python code.
        - Then Pylint outputs a reports of errors like in the example below and gives you a code analysis score.
            - ```python
              ##example output 
              myModule.py:144:0: C0103: Function name "isPalindrome" doesn't conform to snake_case naming style (invalid-name)
              myModule.py:144:0: C0116: Missing function or method docstring (missing-function-docstring)
              myModule.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
              myModule.py:172:4: W0107: Unnecessary pass statement (unnecessary-pass)

              ------------------------------------------------------------------
              Your code has been rated at 4.51/10 
              ```
                - The message type can be:
                    - [I]nformational messages that Pylint emits (do not contribute to your analysis score)
                    - [R]efactor for a "good practice" metric violation
                    - [C]onvention for coding standard violation
                    - [W]arning for stylistic problems, or minor programming issues
                    - [E]rror for important programming issues (i.e. most probably bug)
                    - [F]atal for errors which prevented further processing
                    - Info: [ Pylint output — Pylint 2.8.3.dev49+g0978e091 documentation](http://pylint.pycqa.org/en/latest/user_guide/output.html#:~:text=the%20message%20type%20can%20be)
        - Lastly, fix your errors and rerun Pylint until you get a 10/10.
  ## Using Pylint Example
      - Example code:
          - ```python
            def characterCount(phrase):
                totalCount = 0
                for character in phrase:
                    totalCount +=1  #totalCount = totalCount+1
                print(totalCount)

            def main():
                characterCount(input("Enter a phrase to count the characters of: "))

            main()
            ```
      - Output
          - ```python
            ************* Module test
            test.py:10:0: C0304: Final newline missing (missing-final-newline)
            test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
            test.py:1:0: C0103: Function name "characterCount" doesn't conform to snake_case naming style (invalid-name)
            test.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
            test.py:2:4: C0103: Variable name "totalCount" doesn't conform to snake_case naming style (invalid-name)
            test.py:4:8: C0103: Variable name "totalCount" doesn't conform to snake_case naming style (invalid-name)
            test.py:3:8: W0612: Unused variable 'character' (unused-variable)
            test.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)

            ------------------------------------------------------------------
            Your code has been rated at 0.00/10
            ```
            - The author feels really sad that they have gotten a 0.00/10. Please fix the above code.
      - Tips for Pylint
          - Python uses snake_case (underscores) instead of camelCase (first letter of the first word is lower case, while the first letter of every subsequent word is uppercase).
          - Beware of too long lines and trailing whitespaces
          - Don't include unused variables
    - Disabling Pylint 
      - After we have fixed style issues from the above code, we have gotten:
        - ```python
          """This module contains some functions that we want to test."""

          def character_count(phrase):
              """This function counts the number of characters in a phrase"""
              total_count = 0
              for character in phrase:
                  total_count +=1  #totalCount = totalCount+1
              print(total_count)

          def main():
              """This module tests the above modules"""
              character_count(input("Enter a phrase to count the characters of: "))

          main()
          ```
       - However, we still get this error message (pertaining to the for loop that we use to count each character in the inputted phrase.)
          - ```python
            test.py:6:8: W0612: Unused variable 'character' (unused-variable)
            ```
        - I want to disable this error message.
            - Add this line to your python file.
                - ```python
                  # pylint: disable=W0612
                  ```
            - Or you can disable it while running it
                - ```python
                  pylint --disable=W0612 test.py
                  ```
    ## Sources
        - Pylint user guide: [http://pylint.pycqa.org/en/latest/user_guide/index.html](http://pylint.pycqa.org/en/latest/user_guide/index.html)
        - [ Check the version of Python package / library | note.nkmk.me](https://note.nkmk.me/en/python-package-version/)

