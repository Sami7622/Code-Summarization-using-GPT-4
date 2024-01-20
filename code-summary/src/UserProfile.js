import React, { useState, useEffect } from 'react';

const UserProfile = () => {
  const [user, setUser] = useState({ username: '', email: '' });

  useEffect(() => {
    // Fetch user data from backend and set it
    // Example: setUser(await fetchUserData());
  }, []);

  const handleSave = async () => {
    // Save the updated user data to the backend
    // Example: await updateUserProfile(user);
  };

  return (
    <div>
      <input
        type="text"
        value={user.username}
        onChange={e => setUser({ ...user, username: e.target.value })}
      />
      <input
        type="email"
        value={user.email}
        onChange={e => setUser({ ...user, email: e.target.value })}
      />
      <button onClick={handleSave}>Save Profile</button>
    </div>
  );
};

export default UserProfile;
