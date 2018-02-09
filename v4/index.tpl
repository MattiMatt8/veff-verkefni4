<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Verkefni 4</title>
	<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<h1>Verkefni 4</h1>
<table>
  <tr>
    <th>Kennitala</th>
    <th>Nafn</th>
    <th>Braut</th>
  </tr>
  %for nemandi in bekkur['nemendur']:
	  <tr>
	    <td><a href="nemandi/{{nemandi['kt']}}">{{nemandi['kt']}}</a></td>
	    <td>{{nemandi['nafn']}}</td>
	    <td>{{nemandi['braut']}}</td>
	  </tr>
  %end
</table>
</body>
</html>