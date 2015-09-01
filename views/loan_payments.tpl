<h4>All payments for this loan:</h4>
<table class="table">
	<tr>
		<th>Payment ID</th>
		<th>Payment Type</th>
		<th>Amount</th>
		<th>Date</th>
		<th>Transaction ID</th>
	</tr>
%for item in payment_data:
<tr>
	<td>{{item[0]}}</td>
	<td>{{item[3]}}</td>
	<td>{{item[2]}}</td>
	<td>{{item[4]}}</td>
	<td>{{item[5]}}</td>
</tr>
%end
</table>
