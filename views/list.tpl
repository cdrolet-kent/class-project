<html>
<body>
<h2>Christmas List</h2>
<hr/>
<table>
  <tr>
    <th>Item Wished For:</th>
    <th>Approximated Price:</th>
  </tr>
% for item in xmas_list:
  <tr>
  <td>{{str(item['description'])}}</td>
  <td>{{str(item['price'])}}</td>
  <td><a href="/list/update/{{str(item['id'])}}">update</a></td>
  <td><a href="/list/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/list/add">Add a new item</a>
<hr/>
<a href="/list/search">Search for an item</a>
<hr/>
<a href="/home">Return to Home Page</a>
<hr/>
</body>
</html>