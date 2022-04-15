import praw
from flask import Flask
from flask import request
from flask import json  #importing json cause that’s what we’re going to be working with
import git,subprocess
import traceback

#if self.git_is_installed():
#            g = Git(options['path'])
#            g.init()

app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello World!'

@app. route('/hooktest', methods=['POST'])  # ‘/hooktest’ specifies which link will it work on
def hook_root():
  global p_arr
  #if request.headers['Content-Types'] == 'application/json':  # calling json objects
  #print(request.json)
  try: p_arr[-1].kill()
  except: 
    traceback.print_exc()
  g = git.cmd.Git('https://github.com/ur8moms/first_repo')
  g.pull('https://github.com/ur8moms/first_repo')
  p = subprocess.Popen(['python', 'first.py'])
  return json.dumps(request.json)

if __name__ == '__main__':
  #hook_root()
  p_arr=[]
  app.run(debug=True)
