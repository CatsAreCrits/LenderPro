# Loan Tracker
# By Cody Morton
import praw
import datetime
from datetime import date
import sqlite3 as lite
import sys

# Loan Tracker
# By Cody Morton

# Misc
today = datetime.date.today()

class LoanTracker:
	def __init__(self):
		self.getLoans()

	def getLoans(self):
		conn = lite.connect('db.db')
		c = conn.cursor()
		with conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM Loans")
			rows = cur.fetchall()
			global loans
			# Loans is globally the list of ALL LOANS
			loans = rows

	def getPayments(self):
		conn = lite.connect('db.db')
		c = conn.cursor()
		with conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM payments")
			rows = cur.fetchall()
			global payments
			# Payments is globally the list of ALL PAYMENTS
			payments = rows

	def getTypes(self):
		conn = lite.connect('db.db')
		c = conn.cursor()
		with conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM types")
			rows = cur.fetchall()
			global types
			# Types is globally the list of ALL TYPES
			types = rows

	def nextID(self, type="Loans"):
		self.getLoans()
		self.getPayments() 
		ids = []
		if type == "Loans":
			for loan in loans:
				ids.append(loan[0])
			return max(ids) + 1
		elif type == "Payments":
			for payment in payments:
				ids.append(payment[0])
			return max(ids) + 1

	# Gets ALL open or closed loans.
	# Example: l.getStatus(status="closed") = all closed loans, l.getStatus() = all open loans
	def getStatus(self, status="open"):
		self.getLoans()
		open = []
		closed = []
		for loan in loans:
			if loan[12] == "open":
				open.append(loan[0])
			elif loan[12] == "closed":
				closed.append(loan[0])
		if status == "open":
			if open == []:
				return None
			else:
				return open
		elif status == "closed":
			if closed == []:
				return None
			else:
				return closed
	# Get all loans for a specific borrower.
	# Example: l.getBorrowerLoans("Cody") = gets all loans to Cody
	def getBorrowerLoans(self, borrower):
		self.getLoans()
		borrower_loans = []
		for loan in loans:
			if loan[1] == borrower:
				borrower_loans.append(loan[0])
		if borrower_loans == []:
			return None
		else:
			return borrower_loans

	# Gets loan based off ID provided
	def getLoansID(self, id):
		self.getLoans()
		for loan in loans:
			if loan[0] == id:
				return loan
	# Gets all payments based off ID provided
	def getLoanPayments(self, id):
		self.getLoans()
		self.getPayments()
		# Payment List
		pl = []
		for payment in payments:
			if payment[1] == id:
				pl.append(payment)
		return pl

	# Gets all loan payments and calculates balance
	def makeLoanBalance(self, id):
		self.getLoans()
		self.getPayments()
		# Payment List for Amounts
		pla = []
		for payment in payments:
			if payment[1] == id:
				pla.append(payment[2])
		balance = sum(pla)
		a = [balance, id]
		# SQLLite
		conn = lite.connect('db.db')
		c = conn.cursor()
		c.execute('UPDATE Loans SET balance = ? WHERE id = ?', a)
		conn.commit()
		conn.close()


l = LoanTracker()
l.getTypes()
l.getPayments()

l.makeLoanBalance(7)