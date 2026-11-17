import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  const [precios, setPrecios] = useState([]);

useEffect(() => {
    axios
      .get('https://west.albion-online-data.com/api/v2/stats/prices/T4_BAG.json?locations=Caerleon,Bridgewatch,Lymhurst')
      .then((response) => {
        console.log(response.data); // Aquí puedes inspeccionar todas las variables en consola
        setPrecios(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="p-4 md:p-8 min-h-screen bg-gray-50/50 text-gray-800">
      <section className="max-w-7xl mx-auto">
        <div className="mb-10">
          <h2 className="text-3xl md:text-4xl font-extrabold text-gray-900 tracking-tight">
            Tratamientos de Albion Online
          </h2>
          <p className="text-base md:text-lg text-gray-500 tracking-tight mt-1">
            Precios registrados para el ítem T4_BAG por ciudad.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 md:gap-8">
          {precios.map((item, index) => (
            <article
              key={`${item.city}-${item.quality}-${index}`}
              className="group relative overflow-hidden bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
            >
              <div className="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-orange-400 to-orange-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

              <div className="mb-5 flex items-center justify-between">
                <span className="inline-flex items-center justify-center px-3 py-1.5 rounded-xl bg-orange-50 text-orange-600 font-bold text-sm">
                  {item.item_id}
                </span>
                <span className="text-xs font-semibold text-gray-400">
                  Calidad {item.quality}
                </span>
              </div>

              <h3 className="text-lg font-bold text-gray-900 mb-3 group-hover:text-orange-600 transition-colors duration-300">
                {item.city}
              </h3>

              <div className="space-y-1 text-sm text-gray-500 mb-4">
                <p>Venta mín: <span className="font-semibold text-gray-800">{item.sell_price_min} silver</span></p>
                <p>Compra máx: <span className="font-semibold text-gray-800">{item.buy_price_max} silver</span></p>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Home;