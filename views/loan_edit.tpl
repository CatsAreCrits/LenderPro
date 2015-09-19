<div class="loans_info">
    <h1>Editing Loan ID: {{id}}</h1>
    <form class="form-horizontal" method="post">
        <div class="form-group">
            <label for="inputBorrower" class="col-sm-2 control-label">Borrower</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="inputEmail3" value="{{borrower}}" name="borrower">
            </div>
        </div>
        <div class="form-group">
            <label for="inputGiven" class="col-sm-2 control-label">Given</label>
            <div class="col-sm-10">
                <input type="number" class="form-control" id="inputGiven" value="{{given}}" name="given">
            </div>
        </div>
        <div class="form-group">
            <label for="inputInterest" class="col-sm-2 control-label">Interest</label>
            <div class="col-sm-10">
                <input type="number" class="form-control" id="inputInterest" value="{{interest}}" name="interest">
            </div>
        </div>
        <div class="form-group">
            <label for="inputGiven_date" class="col-sm-2 control-label">Given Date</label>
            <div class="col-sm-10">
                <input type="date" class="form-control" id="inputGiven_date" value="{{given_date}}" name="given_date">
            </div>
        </div>
        <div class="form-group">
            <label for="inputRepay_date" class="col-sm-2 control-label">Repay Date</label>
            <div class="col-sm-10">
                <input type="date" class="form-control" id="inputRepay_date" value="{{agreed_repay_date}}" name="repay_date">
            </div>
        </div>
        <div class="form-group">
            <label for="inputRepaid" class="col-sm-2 control-label">Repaid</label>
            <div class="col-sm-10">
                <input type="number" class="form-control" id="inputRepaid" value="{{repaid}}" name="repaid">
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <div class="checkbox">
                    <label>
                        <input type="checkbox" name="unpaid" value="{{unpaid}}"> Unpaid
                    </label>
                </div>
            </div>
        </div>
        <div class="form-group">
            <label for="inputOriginal_thread" class="col-sm-2 control-label">Original Thread</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="inputOriginal_thread" value="{{original_thread}}" name="original_thread">
            </div>
        </div>
        <div class="form-group">
            <label for="inputInfo" class="col-sm-2 control-label">Info file</label>
            <div class="col-sm-10">
                <input type="text" class="form-control" id="inputInfo" value="{{info}}" name="info">
            </div>
        </div>
        <div class="form-group">
            <label for="inputPaidback" class="col-sm-2 control-label">Paidback Date</label>
            <div class="col-sm-10">
                <input type="date" class="form-control" id="inputPaidback" value="{{paidback_date}}" name="paidback_date">
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-10">
                <select name="status">
                    <option class="current" value="{{status}}">{{status}}</option>
                    <option value="closed">Open</option>
                    <option value="closed">Closed</option>
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <button type="submit" class="btn btn-default">Edit Loan</button>
            </div>
        </div>
    </form>
</div>