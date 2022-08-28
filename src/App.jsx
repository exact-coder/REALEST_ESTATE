import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NotFound from './components/NotFound';
import About from './containers/About';
import Contact from './containers/Contact';
import Home from './containers/Home';
import ListingDetail from './containers/ListingDetail';
import Listings from './containers/Listings';
import Login from './containers/Login';
import SingUp from './containers/SignUp';
import Layout from './hocs/Layout';

const App = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path='/' element={<Home/>} />
          <Route path='/about' element={<About/>} />
          <Route path='/contact' element={<Contact/>} />
          <Route path='/listings' element={<Listings/>} />
          <Route path='/listings/:id' element={<ListingDetail/>} />
          <Route path='/signup' element={<SingUp/>} />
          <Route path='/login' element={<Login/>} />
          <Route path='*' element={<NotFound/>}/>
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}

export default App;
