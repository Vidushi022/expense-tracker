"""tracker.py - the data and calculations for the Expense Tracker.

This file has NO screen code. It only stores expenses and does maths on them.
gui.py imports the classes from here.
"""


# Tuple is used to keep categories fixed
#these are the categories available  expense tracker
CATEGORIES = ("Stationery", "Food", "Travel", "Snacks", "Books",
              "Necessities", "Online Shopping")


class Expense:       
   

    def __init__(self, title, amount, category, date):      #stores the problem entered by user 
                 self.title = title
                 self.amount = amount               
                 self.category = category              
                 self.date = date                     


class ExpenseTracker:                         #stores expenses and does calculation 

    def __init__(self):
        self.expenses = []                    # expenses are kept in this empty list while program is runnning 
        self.budget = 0                       # no budget is set till now by the user

        

    def add_expense(self, expense):
        self.expenses.append(expense)        # adds new expense in the list


        

    def delete_expense(self, index):          # Only delete if that position really exists in the list.
       
        if 0 <= index < len(self.expenses):   # index must be between 0 and length of the self expense list 
            self.expenses.pop(index)          # pop(index) removes the item at that index
            return True                       # delete the index if exists
        return False




    def total(self):
        total = 0                           
        for expense in self.expenses:
            total += expense.amount           # add this expense's amount to the running total

        return total              
                             
                                

    def totals_by_category(self,category):             # gives total expenses of selected category individually 
        totals = {}                           
        for expense in self.expenses:               
            totals[expense.category] = (totals.get(expense.category, 0) + expense.amount)
        return totals

    

    def search_by_category(self, category):      #search categories individually 
        if category == "All":                 
            return list(self.expenses)
        
        matches = []                           
        for expense in self.expenses:                
            if expense.category == category:         
                matches.append(expense)              
        return matches

    

    def highest_expense(self):              #gives the highest expense in the list 
        if len(self.expenses) == 0:           
            return None                       
        highest = self.expenses[0]         #assuming that first expense is highest for comparing purpose  
        for expense in self.expenses:              
            if expense.amount > highest.amount:     
                highest = expense                   
        return highest


    

    def set_budget(self, amount):          #sets a monthly budget for saving purpose
        self.budget = amount

        

    def month_total(self, month_year):      #gives how much we spend monthly
        total = 0                            
        for expense in self.expenses:               
            if expense.date[3:] == month_year:     #month year are in format MM-YYYY 
                total += expense.amount             
        return total

    

    def remaining_budget(self, month_year):    #calculates how much money is left in the budget set 
        return self.budget - self.month_total(month_year)

    

    def is_over_budget(self, month_year):    #checks if we have reached our budget or spend extra 
        return self.budget > 0 and self.month_total(month_year) > self.budget
