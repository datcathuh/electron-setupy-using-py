import os
import subprocess
import sys

NODE_PATH = r'C:\Program Files\nodejs\node.exe'
NPM_PATH = r'C:\Program Files\nodejs\npm.cmd'

def check_node_npm():
    print("Checking for Node.js and npm installation...")
    try:
        subprocess.check_call([NODE_PATH, '--version'])
        print("Node.js is installed successfully.")
        subprocess.check_call([NPM_PATH, '--version'])
        print("npm is installed successfully.")
    except subprocess.CalledProcessError:
        print("Node.js or npm is missing. Please install them first.")
        sys.exit(1)

def install_electron():
    print("Checking if Electron is installed globally...")
    try:
        subprocess.check_call([NPM_PATH, 'list', '-g', 'electron'])
        print("Electron is already installed globally.")
    except subprocess.CalledProcessError:
        print("Electron is not installed. Installing Electron globally...")
        subprocess.check_call([NPM_PATH, 'install', '-g', 'electron'])
        print("Electron has been installed globally.")

def setup_electron_project():
    print("Setting up Electron project...")
    project_path = os.path.join(os.getcwd(), "my_electron_app")
    
    if not os.path.exists(project_path):
        os.makedirs(project_path)
        print(f"Created project directory at {project_path}")
    else:
        print("Project directory already exists. Continuing...")

    package_json = '''{
  "name": "my-electron-app",
  "version": "1.0.0",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "devDependencies": {
    "electron": "^24.0.0"
  }
}
'''
    with open(os.path.join(project_path, 'package.json'), 'w') as f:
        f.write(package_json)
        print("package.json has been created.")

    main_js = '''const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;

app.on('ready', () => {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'renderer.js'),
    }
  });

  mainWindow.loadFile('index.html');
});
'''
    with open(os.path.join(project_path, 'main.js'), 'w') as f:
        f.write(main_js)
        print("main.js has been created.")

    index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Electron App</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Hello, this is my Electron app!</h1>
</body>
</html>
'''
    with open(os.path.join(project_path, 'index.html'), 'w') as f:
        f.write(index_html)
        print("index.html has been created.")

    renderer_js = '''// You can add additional JS logic here if needed.
'''
    with open(os.path.join(project_path, 'renderer.js'), 'w') as f:
        f.write(renderer_js)
        print("renderer.js has been created.")

    print(f"Electron project has been successfully set up at {project_path}.")
    return project_path

def install_dependencies(project_path):
    print("Navigating to project directory to install dependencies...")
    os.chdir(project_path)
    print("Installing project dependencies...")
    subprocess.check_call([NPM_PATH, 'install'])
    print("Project dependencies have been installed successfully.")

def run_electron_app(project_path):
    print("Launching the Electron app...")
    os.chdir(project_path)
    subprocess.run([NPM_PATH, 'start'])
    print("Electron app is now running.")

if __name__ == "__main__":
    print("Starting Electron app setup...")
    check_node_npm()
    install_electron()
    project_path = setup_electron_project()
    install_dependencies(project_path)
    run_electron_app(project_path)
    print("Setup complete. Enjoy your Electron app!")
