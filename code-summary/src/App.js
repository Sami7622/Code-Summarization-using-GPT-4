import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import RegistrationForm from './RegistrationForm';
import LoginForm from './LoginForm';
import UserProfile from './UserProfile';
import PasswordResetRequest from './PasswordResetRequest';
import Home from './Home';
import './App.css';


const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (loginStatus) => {
    setIsLoggedIn(loginStatus);
  };

  return (
    <Router>
      <div>
        <nav>
          <ul>
            {isLoggedIn ? (
              <>
                <li>
                  <Link to="/home">Home</Link>
                </li>
                <li>
                  <Link to="/profile">Profile</Link>
                </li>
                <li>
                  <Link onClick={() => {handleLogin(false)}} to='/'>Logout</Link>
                </li>
              </>
            ) : (
              <>
                <li>
                  <Link to="/register">Register</Link>
                </li>
                <li>
                  <Link to="/login">Login</Link>
                </li>
              </>
            )}
          </ul>
        </nav>

        <Routes>
          {isLoggedIn ? (
            <>
              <Route path="/profile" element={<UserProfile />} />
              <Route path="/home" element={<Home />} />
              <Route path="/" element={<Home />} />
            </>
          ) : (
            <>
              <Route path="/register" element={<RegistrationForm onLogin={handleLogin} />} />
              <Route path="/login" element={<LoginForm onLogin={handleLogin} />} />
              <Route path="/reset-password" element={<PasswordResetRequest />} />
              <Route path="/" element={<LoginForm />} />
            </>
          )}
        </Routes>
      </div>
    </Router>
  );  
};

export default App;
