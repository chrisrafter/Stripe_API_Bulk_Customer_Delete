
#Import the Stripe API Package
import stripe
import time
stripe.api_key = ""
cust_list = ["cus_KBqFO4CSOJHszp", "cus_HZbnx0PQV2sD4S", "cus_JZE6VNNTJQS4ej", "cus_JuGmXJAWdOYDj2", "cus_KBpoqSis1TtI4a",
"cus_KBpWCRYCMv0piL", "cus_KBpvZPl6MR8Z1O", "cus_L1YvLgkBSU340w"]

#Get the list of customers (API is limited to max of 100 per request)
r = 1
for r in range (1,50):
    print("Run #", r)
    #time.sleep(2)
    customers = stripe.Customer.list(limit=100)
    r = r+1

    for x in range(0, 100):
        if (customers.data[x].id in cust_list):
            print(customers.data[x].name, "was found and skipped.")
            #x=x+1
            continue
        print(customers.data[x].name, "will be deleted")
        stripe.Customer.delete(customers.data[x].id)

    #DELETE THE CUSTOMER




