import praw
from flask import Flask
from flask import request
from flask import json  #importing json cause that’s what we’re going to be working with
import git,subprocess

#if self.git_is_installed():
#            g = Git(options['path'])
#            g.init()

app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello World!'

@app. route('/hooktest', methods=['POST'])  # ‘/hooktest’ specifies which link will it work on
def hook_root():
  #if request.headers['Content-Types'] == 'application/json':  # calling json objects
  #print(request.json)
  try: p.terminate()
  except: pass
  g = git.cmd.Git('https://github.com/ur8moms/first_repo')
  g.pull('https://github.com/ur8moms/first_repo')
  p = subprocess.Popen(['python', 'test.py'])
  return json.dumps(request.json)

if __name__ == '__main__':
  app.run(debug=True)
