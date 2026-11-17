import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink, Navigate } from 'react-router-dom';
import Home from './components/Home';
import Tratamientos from './components/Tratamientos';
import Acerca from './components/Acerca';

function App() {
  const estiloBoton = ({ isActive }) =>
    `px-5 py-2.5 rounded-xl font-semibold text-sm transition-all duration-200 ${
      isActive
        ? 'bg-orange-500 text-white shadow-md shadow-orange-500/20'
        : 'text-gray-600 hover:bg-orange-50 hover:text-orange-600'
    }`;

  return (
    <Router>
      <div className="min-h-screen bg-gray-50/50">
        {/* Barra de navegación superior */}
        <header className="sticky top-0 z-10 bg-white/90 backdrop-blur-md border-b border-gray-100 shadow-sm">
          <nav className="max-w-7xl mx-auto px-4 md:px-8 h-16 flex items-center justify-between">
            {/* Marca a la izquierda */}
            <div className="flex items-center gap-2.5">
              <span className="w-3 h-3 rounded-full bg-orange-500"></span>
              <span className="font-extrabold text-gray-900 tracking-tight text-lg">
                Panel Médico
              </span>
            </div>

            {/* Botones de navegación */}
            <div className="flex items-center gap-2">
              <NavLink to="/inicio" className={estiloBoton}>
                Home
              </NavLink>
              <NavLink to="/tratamientos" className={estiloBoton}>
                Tratamientos
              </NavLink>
              <NavLink to="/acerca" className={estiloBoton}>
                Acerca
              </NavLink>
            </div>
          </nav>
        </header>

        {/* Contenido de las vistas */}
        <main className="App">
          <Routes>
            <Route path="/" element={<Navigate to="/inicio" replace />} />
            <Route path="/inicio" element={<Home />} />
            <Route path="/tratamientos" element={<Tratamientos />} />
            <Route path="/acerca" element={<Acerca />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;