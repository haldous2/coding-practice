import time
import threading
  
"""
Avoid deadlocks with dining philosophers
"""
class Philosopher(object):

    def __init__(self, id):
        self.id = id
        self.prev = None            ## Philosopher on the right
        self.eaten = 0
        self.hungry = True          ## False after eating 10 times
        self.chopstick = threading.Lock()
        self.go_left_first = True   ## Breaks tie to prevent deadlocks

    def go_right_first(self):
        self.go_left_first = False
              
    def set_prev(self, philosopher):
        self.prev = philosopher

    def is_hungry(self):
        return self.hungry

    def eat_food(self):
        self.eaten += 1
        if self.eaten < 10:
            print "Philosopher", self.id, "done eating - burp"
        else:
            print "Philosopher", self.id, "is full"
            self.hungry = False

    ## Try to eat - dig in, if not just sit and think
    def eat(self):

        print "Philosopher", self.id, "thinking - hmmmm, I'm hungry"

        # In order to break a tie in grabbing the left chopstick first
        #    set a philosopher to grab right first
        if self.go_left_first:
            chopstick_1 = self.chopstick        # left
            chopstick_2 = self.prev.chopstick   # right
        else:
            chopstick_1 = self.prev.chopstick   # right
            chopstick_2 = self.chopstick        # left

        # acquire is blocking, so Philosopher might have to wait to get chopsticks
        #   that's why I thought they might be thinking they are hungry
        if chopstick_1.acquire():
            # first acquired
            if chopstick_2.acquire():
                # second acquired
                print "Philosopher", self.id, "eating - nom nom nom"
                chopstick_1.release()
                chopstick_2.release()
                self.eat_food()
                # takes a break
                # time.sleep(random.randint(10,100)*.01)
            else:
                # second not acquired - drop first
                chopstick_1.release()

    def run(self):
        # time.sleep(random.randint(10,100)*.001)
        self.eat()
        
if __name__ == '__main__':
  
  def worker(philosopher):
      while philosopher.is_hungry():
          philosopher.run()

  # Setup philosophers in a circular table
  philosopher1 = Philosopher(1)
  philosopher1.go_right_first()
  philosopher2 = Philosopher(2)
  philosopher3 = Philosopher(3)
  philosopher4 = Philosopher(4)
  philosopher5 = Philosopher(5)
  philosopher1.set_prev(philosopher5)
  philosopher2.set_prev(philosopher1)
  philosopher3.set_prev(philosopher2)
  philosopher4.set_prev(philosopher3)
  philosopher5.set_prev(philosopher4)

  threads = []

  t = threading.Thread(target=worker, args=(philosopher1,))
  threads.append(t)
  t = threading.Thread(target=worker, args=(philosopher2,))
  threads.append(t)
  t = threading.Thread(target=worker, args=(philosopher3,))
  threads.append(t)
  t = threading.Thread(target=worker, args=(philosopher4,))
  threads.append(t)
  t = threading.Thread(target=worker, args=(philosopher5,))
  threads.append(t)

  for thread in threads:
      thread.start()

  for thread in threads:
      thread.join()

  print "done!"
