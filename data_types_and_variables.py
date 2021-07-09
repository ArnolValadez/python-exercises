# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
# (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?
little_mermaid = 3
brother_bear = 5
hercules = 1
price_per_day = 3
total_price = price_per_day * (little_mermaid + brother_bear + hercules)
total_price

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they 
# pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for 
# Google and 4 hours for Amazon.
google_rate = 400
amazon_rate = 380
facebook_rate = 350
google_time = 6
amazon_time = 4
facebook_time = 10
total_pay = google_rate * google_time + facebook_rate * facebook_time + amazon_rate * amazon_time
total_pay

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does 
# not conflict with her current schedule.
class_is_full = False
schedule_conflict = False
enrollable_status = not (class_is_full or schedule_conflict)
enrollable_status

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not 
# expired. Premium members do not need to buy a specific amount of products.
more_than_two_items = True
offer_not_expired = True
premium_membership = False
discount_eligibility = offer_not_expired and (more_than_two_items or premium_membership)
discount_eligibility

# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
password_length = len(password) >= 5
user_length = len(username) < 21
password_not_username = username != password
user_no_white_space = not (username.startswith(' ') or username[-1] == ' ')
password_no_white_space = not (password.startswith(' ') or password[-1] == ' ')
user_and_password_valid = password_length and user_length and password_not_username and user_no_white_space and password_no_white_space
user_and_password_valid

# could also use
.strip to remove leading and trailing whitespace

# could also use ... for white spaces
password_no_whitespace_ends = password[0] != ' ' and password[-1] != ' '