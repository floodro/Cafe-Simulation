import time
import random

from datetime import datetime
from Coffee import Stack
from Customers import LinkedList

class cafe_simulation:
    customer_names  = ["Peter", "James", "Thomas", "Bartholomew", "John", "Judas" , "Andrew", "Philip", "Matthew"]
    customer_inline = LinkedList()
    cup_stack       = Stack()

    sleep_sec = .5

    max_customer    = 30   
    min_cups        = 5
    max_cups        = 20

    customer_ctr    = 0
    max_arrving     = 3
    
    duration        = 180
    seconds_pass    = 0
    min_time        = 2
    max_time        = 5
    max_prep_time   = 2
    
    def add_customers_to_line(self, timestamp):
        arriving_customers = random.randint(0,self.max_arrving)
        if(arriving_customers > 0):
            while arriving_customers > 0: 
                if(self.customer_inline.length < self.max_customer): 
                    name = self.customer_names[random.randint(0, len(self.customer_names)-1)]
                    self.customer_ctr = self.customer_ctr + 1;
                    self.customer_inline.append(name, timestamp, self.customer_ctr);
                    print("Customer added to line!")
                else:
                    print("The line is currently full!")
                arriving_customers -= 1
                
    def remove_customer_from_line(self, no):
            self.customer_inline.remove(no)

    def restack_cups(self, no_of_cups):
        while self.cup_stack.size < self.max_cups:
            self.cup_stack.push(no_of_cups)
    
    def check_cups(self):
        if self.cup_stack.size < self.min_cups:
            self.restack_cups(1)

    def make_coffee(self, amount, customer):
        print(customer.getVal(), "'s order of ", amount, "cups has been served.")
        self.cup_stack.pop();

    def run(self):

        next_cus_in = 0;
        prep_time = self.max_prep_time
        coffe_ctr = 0
        order_amt = 0
        while self.seconds_pass < self.duration:
            self.check_cups();
            print("\n\nTime:",str(self.seconds_pass // 60).rjust(2,'0') ,":", str(self.seconds_pass%60).rjust(2,'0'),"\n")

            if next_cus_in < 1:
                self.add_customers_to_line(self.seconds_pass)
                next_cus_in = random.randint(self.min_time,self.max_time)

            if(self.customer_inline.length > 0):
                current_customer = self.customer_inline.nodeAt(0)
                
                if prep_time==self.max_prep_time:
                    order_amt = random.randint(1,3)
                    print("Customer number: ",current_customer.getLineNo()," named ",current_customer.getVal()," ordered ",order_amt," cup of coffee.")
                elif prep_time < self.max_prep_time and prep_time > 0:
                    print("Preparing coffee of  customer number [",current_customer.getLineNo(),"] named ",current_customer.getVal(),".\n\n")
                else:
                    self.make_coffee(coffe_ctr+1,current_customer)
                    prep_time = 2
                    coffe_ctr += 1

                if coffe_ctr == order_amt:
                    coffe_ctr = 0
                    print("Done serving customer number [",current_customer.getLineNo(),"] named ",current_customer.getVal(), ".")
                    print("Customer has waited for ", self.seconds_pass - current_customer.getTime(),"second/s." )
                    self.remove_customer_from_line(0)
            
            next_cus_in -= 1
            prep_time -= 1

            self.seconds_pass +=1
            time.sleep(self.sleep_sec)

            print("\nCups left in stack: ", self.cup_stack.size)
            print("\n",self.customer_inline.length," Customers left inline: ")
            self.customer_inline.print()
 
random.seed(datetime.now())    
cafe = cafe_simulation()
cafe.run()
