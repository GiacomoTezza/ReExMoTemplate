# Script to initialize a React-Express-Mongo Docker Compose project

import os
import random
import string

def replace_in_file(file, to_replace):
    with open(file, "r+") as f:
        content = f.read()
        for key in to_replace:
            content = content.replace(key, to_replace[key])
        f.seek(0)
        f.write(content)
        f.truncate()

if __name__ == "__main__":
    # Ask user for project name
    project_name = input("Enter project name: ")

    # Ask user for project directory to where the project will be created
    project_dir = input("Enter project directory: ")

    # Generate random passwords and secrets
    to_replace = {
        "#[projectname]": project_name,
        "#[mongo-root-password]": ''.join(random.choice(string.ascii_letters + string.digits + "?!") for i in range(20)),
        "#[mongo-password]": ''.join(random.choice(string.ascii_letters + string.digits + "?!") for i in range(20)),
        "#[jwt-secret]": ''.join(random.choice(string.ascii_letters + string.digits + "!@#%^&*()") for i in range(32)),
        }

    # Create project directory, project_dir/project_name
    os.mkdir(os.path.join(project_dir, project_name))

    # Copy ./docker-compose.yml to project_dir/project_name
    os.system("cp ./docker-compose.yml " + os.path.join(project_dir, project_name))
    replace_in_file(os.path.join(project_dir, project_name, "docker-compose.yml"), to_replace)
    
    # Copy ./mongo-init.js to project_dir/project_name
    os.system("cp ./mongo-init.js " + os.path.join(project_dir, project_name))
    replace_in_file(os.path.join(project_dir, project_name, "mongo-init.js"), to_replace)

    # Copy ./mongod.conf to project_dir/project_name
    os.system("cp ./mongod.conf " + os.path.join(project_dir, project_name))

    # Copy ./backend and all its contents to project_dir/project_name/backend
    os.system("cp -r ./backend " + os.path.join(project_dir, project_name))

    # Copy ./frontend and all its contents to project_dir/project_name/frontend
    os.system("cp -r ./frontend " + os.path.join(project_dir, project_name))

    # Go to project_dir/project_name/backend and update dependencies in package.json
    os.chdir(os.path.join(project_dir, project_name, "backend"))
    os.system("npm update")

    # Go to project_dir/project_name/frontend and update dependencies in package.json
    os.chdir(os.path.join("../frontend"))
    os.system("npm update")

    # Print success message
    print("#" * len("Successfully created project " + project_name + " in " + project_dir + ".") )
    print("Successfully created project " + project_name + " in " + project_dir + ".")
    print("To start the project, go to the project directory and run 'docker-compose up --build'.")
    print("#" * len("Successfully created project " + project_name + " in " + project_dir + ".") )
