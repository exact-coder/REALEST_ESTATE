import PropTypes from 'prop-types';
import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import { connect } from 'react-redux';
import { Link, Navigate } from 'react-router-dom';
import { login } from '../actions/auth';

const Login = ({login,isAuthenticated}) => {
  const [formData, setFormData] = useState(
    {email: '',
    password: ''
  });

  const {email,password} = formData;

  const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

  const onSubmit = e => {
    e.preventDefault();
    login(email,password);
  }

  if(isAuthenticated){
    return <Navigate to={'/'}/>
  }

  return (
    <div className="auth">
      <Helmet>
        <title>Realest State - Login</title>
        <meta name='description' content='login page'/>
      </Helmet>
      <h1 className="auth__title">Sign In</h1>
      <p className="auth__lead">Sign into Your Account</p>
      <form action="post" className='auth__form' onSubmit={e => onSubmit(e)} >
        <div className="auth__form__group">
          <input type="email" className="auth__form__input" placeholder='Email' name='email' value={email} onChange={(e) => onChange(e)} required />
        </div>
        <div className="auth__form__group">
          <input type="password" className="auth__form__input" placeholder='Password' name='password' value={password} onChange={(e) => onChange(e)} minLength="4" />
        </div>
        <button className="auth__form__button">LogIn</button>
      </form>
      <p className="auth__authtext">
        Don't have an account? <Link className="auth__authtext__link" to={'/signup'} >Sign Up</Link>
      </p>
    </div>
  )
}

Login.propTypes = {
  login: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, {login})(Login);