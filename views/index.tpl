<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Meta -->
        <title>Cody's Hub</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Cody Morton">
        <meta name="robots" content="noindex, nofollow">
        <!-- CSS -->
        <link href="http://catsarecrits.com/hub1/assets/css/animate.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/bootstrap.min.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/flat-ui-pro.min.css" rel="stylesheet">
        <link href="http://catsarecrits.com/hub1/assets/css/style.css" rel="stylesheet">
        <link href="//cdnjs.cloudflare.com/ajax/libs/x-editable/1.5.0/bootstrap3-editable/css/bootstrap-editable.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="sidebar_top pull-left">
        </div>
        <div class="header">
            <nav class="navbar navbar-inverse" role="navigation">
                <div class="navbar-text navbar-right">
                    <span id="time"></span>
                    <span class="date">{{get('date')}}</span>
                    <span class="links"><a target="_new" href="https://www.google.com/search?q=weather">Weather</a></div>
                        </div>
                    </nav>
                </div>
                <div id="quicklinks">
                    <div id="wellBorder"></div>
                    <div class="well">
                        <div class="row text-center">
                            <!-- You can links here like this..
                            <div class="col-lg-2"><a class="button" href="http://www.twitter.com"><img src="http://catsarecrits.com/hub1/assets/img/thumbs/twitter.png"></a></div> -->

                        </div>
                    </div>
                    <div id="wellBorder"></div>
                </div>
            </div>
            <div class="sidebar_bottom pull-left">
            </div>
            <div class="loans_list">
                <div class="row">
                    <div class="col-lg-3"><h5><a id="add_loan" href="#">Add Loan</a></h5></div>
                    <div class="col-lg-6"><h3>Open Loans:</h3></div>
                    <div class="col-lg-3"><h4></h4></div>
                </div>
                <span id="status_open">
                    
                </span>
                <div class="row">
                    <div class="col-lg-3"><h5></h5></div>
                    <div class="col-lg-6"><h3>Closed Loans:</h3></div>
                    <div class="col-lg-3"><h4></h4></div>
                </div>
                <span id="status_closed">
                    
                </span>
                <div id="borrower_loans">
            </div>
            </div>
            <span id="loan_info">
                
            </span>
            <span id="loan_info2">
                
            </span>
        </body>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
        <script src="http://catsarecrits.com/hub1/assets/js/bootstrap.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/x-editable/1.5.0/bootstrap3-editable/js/bootstrap-editable.min.js"></script>
        <script src="http://catsarecrits.com/hub1/assets/js/js.js"></script>
<script>
$(function() {
      $("#add_loan").click( function()
           {
             $( "#loan_info" ).load( "http://localhost:8080/loans");
           }
      );
});
 </script>
        <script>$( "#status_open" ).load( "http://localhost:8080/loans/status/open" );</script>
        <script>$( "#status_closed" ).load( "http://localhost:8080/loans/status/closed" );</script>
    </html>