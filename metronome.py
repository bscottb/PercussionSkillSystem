import time

#Start_time = time.time() - 1 

def main(bpm = 120, bpb = 4):
    sleep = 60.0 / bpm
    counter = 0
    Start_time = time.time() - 1
    while True:
        counter += 1
        
        if counter % bpb:
            print ('Elapsed time: ' + str(round(time.time() - Start_time)))
            print ('tick')
            
        else:
            print ('Elapsed time: ' + str(round(time.time() - Start_time)))
            print ('TICK')
            Start_time = time.time() 
        
        time.sleep(sleep)

main()
                
