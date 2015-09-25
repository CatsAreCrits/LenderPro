<table class="table">
	<tr>
		<th>ID</th>
		<th>Given</th>
		<th>Borrower</th>
		<th>Action</th>
	</tr>
%for item in status_loans_data:
<tr>
	<td>{{item[0]}}</td>
	<td>${{item[3]}}</td>
	<td>/u/{{item[1]}}</td>
	<td><a href="#" id="{{item[0]}}">View</a> / <a href="/loans/edit/{{item[0]}}" id="">Edit</a></td>
</tr>
%end
<script>
%for item in status_loans_data:
$(function() {
      $("#{{item[0]}}").click( function()
           {
             $( "#loan_info" ).load( "/loans/id/{{item[0]}}");
             $( "#borrower_loans" ).load( "/loans/borrower/{{item[1]}}");
           }
      );
});
%end
 </script>
</table>
