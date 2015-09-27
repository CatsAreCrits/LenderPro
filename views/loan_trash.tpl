<h1>Are you sure you want to trash Loan ID: {{id}}?</h1>
<p>It will be moved to trash where it will be deleted in two weeks.</p>
<form class="form-horizontal" method="post">
	<div class="form-group">
		<label for="id" class="col-sm-2 control-label">Trash ID</label>
		<div class="col-sm-10">
			<input type="number" class="form-control" id="inputID" value="{{id}}" name="id">
		</div>
	</div>
	<div class="form-group">
		<div class="col-sm-offset-2 col-sm-10">
			<button type="submit" class="btn btn-default">Trash Loan</button>
		</div>
	</div>
</form>