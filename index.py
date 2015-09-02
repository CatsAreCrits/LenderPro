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

	def nextID(self):
		self.getLoans()
		global ids
		ids = []
		for loan in loans:
			ids.append(loan[0])
		return max(ids) + 1

	# Gets ALL open or closed loans.
	# Example: l.getStatus(status="closed") = all closed loans, l.getStatus() = all open loans
	def getStatus(self, status="open"):
		self.getLoans()
		open = []
		closed = []
		for loan in loans:
			if loan[11] == "open":
				open.append(loan[0])
			elif loan[11] == "closed":
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

@route('/edit')
def edit():
	edit_status = request.forms.get('status')
	pass

# Route to get all loans from borrower
@route('/loans/id/<id>')
def viewLoan(id):
	# We use (int(id)) because it doesn't know it's an int, it thinks it's a string. So it won't work without making it an int.
	if l.getLoansID(int(id))[11] == "open":
		statusId = "open"
		color = "bad"
	elif l.getLoansID(int(id))[11] == "closed":
		statusId = "closed"
		color = "good"

	loan_data = {
		'id': l.getLoansID(int(id))[0],
		'borrower': l.getLoansID(int(id))[1],
		'given': l.getLoansID(int(id))[2],
		'interest': l.getLoansID(int(id))[3],
		'agreed_repay_date': l.getLoansID(int(id))[4],
		'repaid': l.getLoansID(int(id))[5],
		'unpaid': l.getLoansID(int(id))[6],
		'original_thread': l.getLoansID(int(id))[7],
		'given_date': l.getLoansID(int(id))[8],
		'paidback_date': l.getLoansID(int(id))[9],
		'info': l.getLoansID(int(id))[10],
		'status': l.getLoansID(int(id))[11],
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

@route('/loans/payments/<id>')
def viewPaymentsbyLoanID(id):
	payment_data = {
	'payment_data': l.getLoanPayments(int(id))
	}
	return template('loan_payments', **payment_data)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 2323))
	run(host='0.0.0.0', port=port, debug=True, server='cherrypy')
