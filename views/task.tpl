<html>
<body>
<h2>List of Tasks</h2>
<hr/>
<table>
% for item in task_list:
  <tr>
  <td>{{str(item['description'])}}</td>
  <td><a href="/task/update/{{str(item['id'])}}">update</a></td>
  <td><a href="/task/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/task/add">Add a new item</a>
<hr/>
<a href="/home">Return to Home Page</a>
<hr/>
</body>
</html>
