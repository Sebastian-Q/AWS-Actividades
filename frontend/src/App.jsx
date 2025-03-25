import { useState, useEffect } from 'react'
import './App.css'
import { AnimatePresence } from 'framer-motion';
import {BrowserRouter as Router, Routes, Route, useLocation} from 'react-router-dom';
import axios from 'axios';

import "bootstrap/dist/css/bootstrap.min.css"
//import PrivateRoute from './components/PrivateRoute';
import Login from './components/Login';
import Navbar from './components/Navbar';
import AboutUs from './pages/AboutUs';
import NotFound from './pages/404';
import CustomUserForm from './components/NewUser';

const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode= "wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/login" element={<Login/>}></Route>

        {/* Home 
        <Route path="/" element={<PrivateRoute><Home /></PrivateRoute>}/> */}
        <Route path="/" element={<Home />}/>
        
        {/* 404 */}
        <Route path="*" element={<NotFound />}/>

        
        {/* About us */}
        <Route path="/about" element={<AboutUs />}/>
        
        {/* El formulario de registro de usuario */}
        <Route path="/register" element={<CustomUserForm/>}/>
      </Routes>
    </AnimatePresence>
  );
}

function Home() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [Loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError("Error al obtener los datos: " + error);
        setLoading(false);
      });
  }, []);

  if (Loading) {
    return <div>Cargando...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Datos de la API de usuarios (Desde Django)</h1>
      <h3>{localStorage.getItem('access_token')}</h3>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Navbar />
      <div className='container mt-4'>
        <div className='row'>
          <div className='col'> 
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App
