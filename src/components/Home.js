import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  const [variablec, setconsumo] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/conmedicos')
      .then(response => {
        setconsumo(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

return (
  <div className="p-4 md:p-8 min-h-screen bg-gray-50/50 text-gray-800">
    <section className="max-w-7xl mx-auto">
      
      {/* Encabezado */}
      <div className="mb-10">
        <h2 className="text-3xl md:text-4xl font-extrabold text-gray-900 tracking-tight">
          Medicos
        </h2>
        <p className="text-1xl md:text-1xl  text-gray-500 tracking-tight">
          Listado de los protocolos actualmente en curso. Explora los detalles de cada tratamiento en las tarjetas a continuación.
        </p>
      </div>

      {/* Grid de Cartas */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8">
        {variablec.map((vrc) => (
          <article 
            key={vrc.idMed}
            className="group relative bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col overflow-hidden"
          >
            {/* Línea superior decorativa que aparece al hacer hover */}
            <div className="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-orange-400 to-orange-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            
            {/* Insignia (Badge) del ID */}
            <div className="mb-5">
              <span className="inline-flex items-center justify-center w-10 h-10 rounded-xl bg-orange-50 text-orange-600 font-bold text-sm border border-orange-100 group-hover:bg-orange-500 group-hover:text-white transition-colors duration-300">
                #{vrc.idMed}
              </span>
            </div>

            {/* Título de la tarjeta */}
            <h3 className="text-lg font-bold text-gray-900 mb-3 capitalize line-clamp-2 group-hover:text-orange-600 transition-colors duration-300">
              {vrc.nombresMed}
            </h3>

            {/* Cuerpo/Descripción */}
            <p className="text-gray-500 text-sm leading-relaxed line-clamp-4 mb-4">
              {vrc.apellidosMed}
            </p>

            {/* Botón fantasma al final (opcional, para dar sensación de interactividad) */}
            <div className="mt-auto pt-4 border-t border-gray-50">
              <button className="text-orange-500 text-sm font-semibold flex items-center gap-1 group-hover:gap-2 transition-all duration-300">
                Ver detalles 
                <span className="text-lg leading-none"></span>
              </button>
            </div>
          </article>
        ))}
      </div>
      
    </section>
  </div>
);
};

export default Home;