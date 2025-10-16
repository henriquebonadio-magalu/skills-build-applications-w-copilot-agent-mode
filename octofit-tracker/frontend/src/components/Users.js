import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const items = data.results ? data.results : data;
        setUsers(items);
        console.log('Fetched users:', items);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Users</h2>
      <ul>
        {users.map((user, idx) => (
          <li key={idx}>{user.name} ({user.email})</li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
