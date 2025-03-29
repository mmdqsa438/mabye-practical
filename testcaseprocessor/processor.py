
import sys 
import subprocess

def block_prosesor( i , p , o ):
    
    with open( i , 'r' ) as f :
        block = f.read()
    
    blocks = block.split('###')
    blocks = [ block.strip() for block in blocks if block.strip() ]
    
    with open( o , 'w' ) as f :
        
        for i,block in enumerate( blocks ,1) :
            
            f.write(f"{i}th TESTCASE OUTPUT$ >>>\n\n")
            try :
                res = subprocess.run( [p] , input= block , text=True , capture_output=True , shell=True )
                
                if res.stdout:
                    f.write(res.stdout + "\n")
                if res.stderr :
                    f.write("ERROR :\n"+res.stderr+"\n")
                    
            except Exception as e :
                f.write(F"ERROR processing block : {str(e)}\n")
            f.write("\n------------------------\n------------------------\n")

if __name__ == "__main__" :
    
    """if len(sys.argv) != 4 :
        print('There is many input file ! please enter in pattern : < input_text_file > < executed_program_file > < outpuut_text_file > ')
        sys.exit(1)
    """
    input = sys.argv[1]
    program = sys.argv[2]
    output = sys.argv[3]
    
    block_prosesor ( input , program , output )
    