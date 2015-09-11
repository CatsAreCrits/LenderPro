# LenderPro
For the lenders of /r/borrow.

This is LenderPro, a python web app made to help lenders manage all the loans they give out. It is very much NOT FINSIHED.
Whenever I make a post on /r/borrow it will be in a decently usable state. Keep in mind this is pretty much my first legit python app..
# Features (So Far)
* View, add, and edit all loans and payments.
* Easy to use HUB that shows all open and closed loans.
* View loans by borrower, view payments by loan.
* All stored in a very simple SQLite database.
* The data stored per loan: Loan ID, Borrower, amount given (initial payment), agreed interest, given data, repay date (added when they repay), unpaid? (if the loan is unpaid or overdue), original thread, info file/folder
* The data stored per payment: Payment ID, Payment Type (examples: initial loan, full repayment, full repayment + interest, and interest), Amount, Date, Transaction ID (for paypal, will look into other payment types soon).

# Features to Come
* Edit loans (easily)
* Search loans
* Make a not extremely terrible frontend. The current one looks pretty great but in reality, it's terrible.
* Add payments to loans
* Stats page (amount of interest made, amount of lenders, amount overdue, amount due, etc etc)
* Make it easy for the average /r/borrow user to use
* Much more..
