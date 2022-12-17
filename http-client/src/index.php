<html>

<head>
    <title>HTML Service</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Jost">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <style>
        body {
            font-family: "Jost", sans-serif;
            color: white;
            background: no-repeat;
            background-size: 100%;
            background-image: url('https://img1.akspic.ru/crops/2/5/9/4/44952/44952-rastitelnost-tuman-el-elovo_pihtovye_lesa-pustynya-1920x1080.jpg');
        }

        .navbar-inverse {
            background: black;
            border: none;
        }

        .navbar-inverse .navbar-brand {
            color: #fff;
        }

        .navbar-inverse .navbar-right .form-control {
            font-size: 13px;
        }

        .table {
            background-color: black;
        }

        .btn {
            margin-top: 8px;
        }

        .table th {
            cursor: pointer;
        }

        .table .th-sort-asc::after {
            content: "\25be";
        }

        .table .th-sort-desc::after {
            content: "\25b4";
        }

        .table .th-sort-asc::after,
        .table .th-sort-desc::after {
            margin-left: 5px;
        }

        .table .th-sort-asc,
        .table .th-sort-desc {
            background: rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body>
    <div class="container form">

        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <div class="navbar-header">
                    <b class="navbar-brand">Animals</b>
                </div>
                <div class="navbar-form navbar-right">
                    <input id="searchButton" type="text" class="form-control search-input" placeholder="Search" data-table="table">
                </div>
                <form action="index.php" method="post" class="form">
                    <input type="hidden" name="create" id="create" value=1>
                    <button type="submit" class="btn btn-info">Create</button>
                </form>
            </div>
        </nav>
        <table class="table" id="table">

            <?php
            if (isset($_POST['create'])) {
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/api/',
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                echo '<thead>
                <th onclick="sortTable(0)">CSVId</th>
                <th onclick="sortTable(1)">Id</th>
                <th onclick="sortTable(2)">Name</th>
                <th onclick="sortTable(3)">Type</th>
                <th onclick="sortTable(4)">Colour</th>
                <th onclick="sortTable(5)">Size</th>
                </thead>
                <tbody>';
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                $json = json_decode($response, true);
                for ($i = 0; $i < count($json['Name']); $i++) {
                    echo "<tr>";
                    foreach ($json as $key => $value) {

                        echo "<td>" .  $value[$i] . "</td>";
                    }
                    echo "</tr>";
                }
            }
            ?>
            </tbody>
        </table>
    </div>
    <script src="script.js"></script>
</body>

</html>