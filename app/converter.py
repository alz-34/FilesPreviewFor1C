import subprocess

class Converter:

    def run_unoconv(self, *args, timeout=None):
        # return subprocess.run(["unoconv", *args], check=True)
        
        proc=None
        try:
            proc=subprocess.run(['py', './Scripts/unoconv', *args], timeout=timeout)
        except subprocess.TimeoutExpired:            
            if '--listener' not in args:
                raise            
            else:
                # listener doesn't release shell, so terminate process by timeout
                pass    
        return proc 

    def __init__(self):
        self.run_unoconv('--listener', timeout=2)            

    def convert(self, *args):
        return self.run_unoconv(*args)