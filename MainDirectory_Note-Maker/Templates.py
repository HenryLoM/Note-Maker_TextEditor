import tkinter as tk

# - - - - - - - templates - - - - - - -

todolist = '''Todo list:

1. Wake up
2. Survive
3. Fall asleep
----------------------------------------
-) *Usual task or remind*
-) *Usual task or remind*'''

email = '''EMAIL
----------------------------------------
From: *user*
To: *recipient*
Topic: *topic*
----------------------------------------
Greetings, *recipient*, My name is *user*. I decided to text to you to talk about *...*

*other email*

I do hope you will have a nice day. Thank you for reading.
----------------------------------------
With a good wishes: *user*'''

readmefile = '''# *PROJECTS NAME*

*DESCRIPTION*

## Features

- *feature #1*
- *feature #2*
- *feature #3*

## Prerequisites

- *used thing #1*
- *used thing #2*
- *used thing #3*

## Installation

1. Clone the repository
2. Set Up Your Environment
3. Install the required dependencies
4. Run the code

You can copy this to do all steps avoid:

```bash
git clone https://github.com/*your github username*/*project's name*.git
cd *name of the directory*
pip install -r requirements.txt
*programing language* *file*
```

## Contribution Guidelines

We welcome contributions from the community. To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: git checkout -b feature-name.
3. Implement your feature and commit your changes: git commit -m "Description of changes.".
4. Push to your fork: git push origin feature-name.
5. Submit a pull request.

## License

This project is licensed under the *Type of the license* - see the LICENSE file for details.
'''

# - - - - - - - function - - - - - - -

def call_template(text, topic):
    if topic == "Todo list":
        text.delete(1.0, tk.END)
        text.insert(tk.END, todolist)
    elif topic == "Email":
        text.delete(1.0, tk.END)
        text.insert(tk.END, email)
    elif topic == "README file":
        text.delete(1.0, tk.END)
        text.insert(tk.END, readmefile)
    else:
        text.delete(1.0, tk.END)