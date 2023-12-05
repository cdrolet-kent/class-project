<html>
<body>
<hr/>
<form action="/list/update" method="post">
  <input type="hidden" name="id" value="{{str(item['id'])}}"/>
  <p>Description:<input name="description" value="{{item['description']}}"/></p>
  <p>Approximated Price:<input name="price" value="{{item['price']}}"/></p>
  <p><button type="submit">Submit</button></p>
<form>
<hr/>
<body>
</html>