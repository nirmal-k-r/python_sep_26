import os, subprocess

#run hello.py as subprocess in background

subprocess.Popen(['python', 'hello.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#threading -> ThreadPoolExecutor


# def run_hello():
#     subprocess.Popen(['python', 'hello.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# with ThreadPoolExecutor(max_workers=1) as executor:
#     executor.submit(run_hello)