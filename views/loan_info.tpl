<div class="loans_info">
    <div class="row loans_header {{color}}">
        <div class="col-lg-6">
            <h4 class="borrower value"><a class="loans_header_text_{{color}}" href="https://www.reddit.com/user/{{borrower}}"><span class="slashu">/u/</span>{{borrower}}</a></h4>
        </div>
        <div class="col-lg-6">
            <h4 class="actions value loans_header_text_{{color}}">ID: {{id}} <span class="status value loans_header_text_{{color}}">Status: <a href="#" id="status" data-type="text" data-pk"{{id}}" data-url"/edit" data-title"Enter status">{{status}}</a></span></h4>
        </div>
    </div>
    <hr>
    <div class="row">
        <div class="col-lg-6">
            <p class="loan_balance value"><span class="loan_text">Balance: </span>{{balance}}</p>
            <p class="given value"><span class="loan_text">Given: </span>${{given}}</p>
            <p class="interest value"><span class="loan_text">Interest: </span>${{interest}}</p>
            <p class="repaid value"><span class="loan_text">Repaid: </span>${{repaid}}</p>
            <a href="{{original_thread}}"><p class="thread value">reddit Thread</p></a>
        </div>
        <div class="col-lg-6">
            <p class="repay_date value"><span class="loan_text">To be repaid on: </span>{{agreed_repay_date}}</p>
            <p class="given_date value"><span class="loan_text">Given on: </span>{{given_date}}</p>
            <p class="paidback_date value"><span class="loan_text">Paid back in: </span>N/A</p>
            <p class="paidback_date value"><span class="loan_text">Paid back on: </span>{{paidback_date}}</p>
        </div>
    </div>
    <div id="payment_table">
    </div>
    <script>$( "#payment_table" ).load( "/loans/payments/{{id}}" );
    $(document).ready(function() {
    $('#status').editable();
    });</script>