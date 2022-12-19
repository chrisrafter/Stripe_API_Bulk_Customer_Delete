
#Import the Stripe API Package
import stripe
# Paste your Stripe API Secret Key between the quotes below
stripe.api_key = ""

#Create list of Customer IDs you want to exclude from deletion, for example active subs, etc.
supp_cust_list = ["cus_KBqFO4CSOJHszp", "cus_HZbnx0PQV2sD4S"]

#Get the list of customers (API is limited to max of 100 per request)
r = 1
for r in range (1,50):
    print("Run #", r)
    customers = stripe.Customer.list(limit=100)
    r = r+1

    for x in range(0, 100):

#Check if customer ID is in suppress list, if yes, skip and go to next
        if (customers.data[x].id in supp_cust_list):
            print(customers.data[x].name, "was found and skipped.")
            #x=x+1
            continue
        print(customers.data[x].name, "will be deleted")
# Delete the customer
        stripe.Customer.delete(customers.data[x].id)





