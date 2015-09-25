<div class="loans_info">
    <h1>Adding Payment for Loan ID: {{id}}</h1>
    <form class="form-horizontal" method="post">
        <div class="form-group">
            <label for="inputPType" class="col-sm-2 control-label">Payment Type</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="inputPType" placeholder="Payment Type" name="ptype">
            </div>
        </div>
        <div class="form-group">
            <label for="inputAmount" class="col-sm-2 control-label">Amount</label>
            <div class="col-sm-10">
                <input type="number" class="form-control" id="inputAmount" placeholder="Amount" name="amount">
            </div>
        </div>
        <div class="form-group">
            <label for="inputDate" class="col-sm-2 control-label">Date</label>
            <div class="col-sm-10">
                <input type="date" class="form-control" id="inputDate" placeholder="Date" name="date">
            </div>
        </div>
        <div class="form-group">
            <label for="inputTrans" class="col-sm-2 control-label">Transaction ID</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="inputTrans" placeholder="Transaction ID" name="transactionID">
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-default">Add Payment</button>
            </div>
        </div>
    </form>
</div>