<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <script src="http://www.gstatic.com/charts/loader.js"></script>
  <script src="http://code.jquery.com/jquery-1.11.3.js"></script>
  <script>
    data = [];
<?php
$db = new PDO('mysql:host=localhost;dbname=heimdall;', 'heimdall', 'heimdall', array(
    PDO::ATTR_TIMEOUT => 20,
    PDO::ATTR_ERRMODE => PDO::ERRMODE_SILENT
));

foreach ($db->query('SELECT * FROM `data` WHERE service_id = 4 order by run_date desc, run_time desc limit 100') as $row) {
    print "    data.push('" . trim($row['data']) . "');\n";
}
?>
    var processes = [];

    $(function() {
        var index = 0;

        for (row of data) {
            if (row.length == 0) {
                continue;
            }
            row = jQuery.parseJSON(row);
            for (process of row) {
                if (processes[process[2]] == undefined) {
                    processes[process[2]] = [];
                    $('.info').append('<div data-process="'+process[2]+'">'+process[2]+'<div class="service"></div></div>')
                }

                if (processes[process[2]][index] == undefined) {
                    processes[process[2]][index] = 0;
                }

                processes[process[2]][index] += parseInt(process[3])

            }
         index++;
        }

        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);
    });

    function drawChart() {

        var options = {
            title : 'process',
            vAxis : {
                title : 'memory'
            },
            isStacked: true
        };

        for (process in processes) {
            selector = $('div[data-process="' + process + '"]', '#info');
            selector.height(150);

            options['title'] = process;

            data = [['tick', 'memory used']];
            i = 0;
            for (d of processes[process]) {
                data.push([i++, d]);
            }
            data = google.visualization.arrayToDataTable(data);

            chart = new google.visualization.SteppedAreaChart(selector.children('div')[0]);
            chart.draw(data, options);
        }
    }

</script>

</head>

<body>
    <div id="info" class="info"></div>
</body>
</html>
