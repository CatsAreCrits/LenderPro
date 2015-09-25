#!/usr/bin/python
# -*- coding: utf-8 -*-

# INDEX.PY - Created 5/21/2015
# Includes code made for the WEBSITE ONLY, test things in loan.py

import json
import time
import threading
import os
import datetime
import sqlite3 as lite
import sys
from bottle import route, run, template, request, static_file

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

# Run the site
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='/root/lenderpro/files')

@route('/')
def index():
	return template('index')

@route('/loans')
def loanForm():
    return template('loan_add')

@route('/loans', method='POST')
def enterLoan():
	form_borrower = request.forms.get('borrower')
	form_given = request.forms.get('given')
	form_interest = request.forms.get('interest')
	form_repay_date = request.forms.get('repay_date')
	form_repaid = request.forms.get('repaid')
	form_unpaid = request.forms.get('unpaid')
	form_original_thread = request.forms.get('original_thread')
	form_given_date = request.forms.get('given_date')
	form_paidback_date = request.forms.get('paidback_date')
	form_info = request.forms.get('info')
	id = l.nextID()
	# SQLLite
	conn = lite.connect('db.db')
	c = conn.cursor()

	formloan = [id, form_borrower, form_given, form_interest, form_repay_date,
		form_repaid, form_unpaid, form_original_thread, form_given_date, form_paidback_date, form_info, "open"]

	c.execute('INSERT INTO Loans VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', formloan)

	conn.commit()
	conn.close()
	return template("<p>Data entered successfully:{{id}} {{form_borrower}}, {{form_given}}, {{form_interest}}, {{form_repay_date}}, {{form_repaid}}, {{form_unpaid}}, {{form_original_thread}}, {{form_given_date}}, {{form_paidback_date}}, {{form_info}}</p>",id = id, form_borrower = form_borrower, form_given = form_given, form_interest = form_interest, form_repay_date = form_repay_date, form_repaid = form_repaid, form_unpaid = form_unpaid, form_original_thread = form_original_thread, form_given_date = form_given_date, form_paidback_date = form_paidback_date, form_info = form_info)

@route('/loans/edit/<id:int>')
def editForm(id):
	loan_data = {
		'id': l.getLoansID(id)[0],
		'borrower': l.getLoansID(id)[1],
		'given': l.getLoansID(id)[3],
		'interest': l.getLoansID(id)[4],
		'agreed_repay_date': l.getLoansID(id)[5],
		'repaid': l.getLoansID(id)[6],
		'unpaid': l.getLoansID(id)[7],
		'original_thread': l.getLoansID(id)[8],
		'given_date': l.getLoansID(id)[9],
		'paidback_date': l.getLoansID(id)[10],
		'info': l.getLoansID(id)[11],
		'status': l.getLoansID(id)[12],
		
		}
	return template('loan_edit', **loan_data)

@route('/loans/edit/<id:int>', method='POST')
def edit(id):
	edit_borrower = request.forms.get('borrower')
	edit_given = request.forms.get('given')
	edit_interest = request.forms.get('interest')
	edit_repay_date = request.forms.get('repay_date')
	edit_repaid = request.forms.get('repaid')
	edit_unpaid = request.forms.get('unpaid')
	edit_original_thread = request.forms.get('original_thread')
	edit_given_date = request.forms.get('given_date')
	edit_paidback_date = request.forms.get('paidback_date')
	edit_info = request.forms.get('info')
	edit_status = request.forms.get('status')
	id = id
	# SQLLite
	conn = lite.connect('db.db')
	c = conn.cursor()

	formedit = [edit_borrower, edit_given, edit_interest, edit_repay_date, edit_repaid, edit_unpaid, edit_original_thread, edit_given_date, edit_paidback_date, edit_info, edit_status, id]

	c.execute('UPDATE Loans SET borrower = ?, given = ?, interest = ?, agreed_repay_date = ?, repaid = ?, unpaid = ?, original_thread = ?, given_date = ?, paidback_date = ?, info = ?, status = ? WHERE id = ?', formedit)
	conn.commit()
	conn.close()
	return template("<meta http-equiv='refresh' content='0';URL='/'/>")

# Route to get all loans from borrower
@route('/loans/id/<id:int>')
def viewLoan(id):
	if l.getLoansID(id)[12] == "open":
		statusId = "open"
		color = "bad"
	elif l.getLoansID(id)[12] == "closed":
		statusId = "closed"
		color = "good"

	loan_data = {
		'id': l.getLoansID(id)[0],
		'borrower': l.getLoansID(id)[1],
		'balance':l.getLoansID(id)[2],
		'given': l.getLoansID(id)[3],
		'interest': l.getLoansID(id)[4],
		'agreed_repay_date': l.getLoansID(id)[5],
		'repaid': l.getLoansID(id)[6],
		'unpaid': l.getLoansID(id)[7],
		'original_thread': l.getLoansID(id)[8],
		'given_date': l.getLoansID(id)[9],
		'paidback_date': l.getLoansID(id)[10],
		'info': l.getLoansID(id)[11],
		'status': l.getLoansID(id)[12],
		'color': color
		}
	return template('loan_info', **loan_data)

@route('/loans/status/<status>')
def viewLoansbyStatus(status):
	ids = l.getStatus(status)
	status_loans = []
	for id in ids:
		status_loans.append(l.getLoansID(id))
	status_data = {
	'status_loans_data': status_loans
	}
	return template('loan_status', **status_data)

@route('/loans/borrower/<borrower>')
def viewLoansbyBorrower(borrower):
	ids = l.getBorrowerLoans(borrower)
	borrower_loans = []
	for id in ids:
		borrower_loans.append(l.getLoansID(id))
	borrower_data = {
	'borrower_loans_data': borrower_loans
	}
	return template('loan_borrower', **borrower_data)

@route('/loans/payments/<id:int>/add')
def addPaymentForm(id):
	LoanInfo = {
	'id': l.getLoansID(id)[0]
	}
	return template('loan_payments_add', **LoanInfo)

@route('/loans/payments/<id:int>/add', method='POST')
def addPayment(id):
	form_amount = request.forms.get('amount')
	form_ptype = request.forms.get('ptype')
	form_date = request.forms.get('date')
	form_transID = request.forms.get('transactionID')
	pID = l.nextID(type="Payments")
	# SQLLite
	conn = lite.connect('db.db')
	c = conn.cursor()

	formpayments = [pID, id, form_amount, form_ptype, form_date, form_transID]

	c.execute('INSERT INTO Payments VALUES(?, ?, ?, ?, ?, ?)', formpayments)

	conn.commit()
	conn.close()
	l.makeLoanBalance(id)

@route('/loans/payments/<id:int>')
def viewPaymentsbyLoanID(id):
	payment_data = {
	'payment_data': l.getLoanPayments(id)
	}
	return template('loan_payments', **payment_data)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 2323))
	run(host='0.0.0.0', port=port, debug=True, server='cherrypy')