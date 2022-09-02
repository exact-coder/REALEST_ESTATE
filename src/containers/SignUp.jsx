import PropTypes from 'prop-types';
import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import { connect } from 'react-redux';
import { Link, Navigate } from 'react-router-dom';
import { setAlert } from '../actions/alert';
import { signup } from '../actions/auth';


const SignUp = ({setAlert,signup,isAuthenticated}) => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    password2: ''
  });

  const {name,email,password,password2} = formData;

  const onChange = e => setFormData({...formData, [e.target.name]: e.target.value});

  const onSubmit = e => {
    e.preventDefault();
    
    if (password !== password2) {
      setAlert("Password do not match", 'error');
    }else {
      signup({name,email,password,password2});
    }
  }

  if(isAuthenticated){
    return <Navigate to={'/'}/>
  };

  return (
    <div className="auth">
      <Helmet>
        <title>Realest State - SignUp</title>
        <meta name='description' content='Signup page'/>
      </Helmet>
      <h1 className="auth__title">Sign Up</h1>
      <p className="auth__lead">Create Your Account</p>
      <form method="post" action='post' className='auth__form' onSubmit={e => onSubmit(e)} >
        <div className="auth__form__group">
          <input type="text" className="auth__form__input" placeholder='Name' name='name' value={name} onChange={(e) => onChange(e)} required />
        </div>
        <div className="auth__form__group">
          <input type="email" className="auth__form__input" placeholder='Email' name='email' value={email} onChange={(e) => onChange(e)} required />
        </div>
        <div className="auth__form__group">
          <input type="password" className="auth__form__input" placeholder='Password' name='password' value={password} onChange={(e) => onChange(e)} minLength="4" />
        </div>
        <div className="auth__form__group">
          <input type="password" className="auth__form__input" placeholder='Confirm Password' name='password2' value={password2} onChange={(e) => onChange(e)} minLength="4" />
        </div>
        <button className="auth__form__button">Register</button>
      </form>
      <p className="auth__authtext">
        Already have an account? <Link className="auth__authtext__link" to={'/login'} >SignIn</Link>
      </p>
    </div>
  )
}

SignUp.propTypes = {
  setAlert: PropTypes.func.isRequired,
  signup: PropTypes.func.isRequired,
  isAuthenticated: PropTypes.bool
};

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, {setAlert,signup})(SignUp);