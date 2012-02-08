import os, sys, subprocess

i = 0

def fail(test,s):
    print "...failed!"
    print s
    print "Total tests passed: "+ str(i) +" / " + str(len(tests))
    sys.exit()

print "Running tests...\n"

tests  = map(lambda s: ''.join(s.split('.')[0:-1]),filter(lambda s: s.split('.')[-1] =='in', os.listdir('./tests')))


for test in tests:
    if not os.path.exists("./tests/" + test + ".out"):
        fail(test, "No .out file for test '" + test + "'.")
    
    with open("./tests/" + test + ".out") as f:
        expected = str.strip(''.join(f.readlines()))
        actual = str.strip(subprocess.check_output("cat ./tests/"+test+".in | python scheme.py",shell=True))
        print str(i+1) + ". " + test,
        if expected != actual:
            fail(test,"Incorrect output. \nExpected output: \n" + expected + "\nActual output: \n"+actual)
        
        i += 1
        print "... good.\n(" + str(i) + "/" + str(len(tests)) + " tests passed)"

print "Congratulations! All " + str(len(tests)) + " tests passed successfully."